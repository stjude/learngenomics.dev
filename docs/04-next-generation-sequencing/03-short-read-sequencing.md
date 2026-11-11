---
title: Short-Read Sequencing
description: "How Illumina short-read sequencing works: sequencing by synthesis, base quality scores, paired-end reads, common errors, and the files it produces."
---

import YouTube from '@site/src/components/YouTube';

The most widely used sequencers are made by [Illumina][illumina]. They read a few
hundred bases from each fragment, which is why their data is called short-read
sequencing, and they make up for the short reads with sheer numbers: a single run of a
large instrument reads billions of fragments at once.

## Sequencing by Synthesis

Illumina instruments use a method called sequencing by synthesis. Rather than reading a
strand of DNA directly, they watch it being copied one base at a time. Illumina's own
animation walks through the whole process in about five minutes. It shows the original
version of the chemistry, with four dye colors. Newer instruments use fewer dyes, but
the steps are the same.

<YouTube
  id="fCd6B5HRaZ8"
  title="Overview of Illumina Sequencing by Synthesis Workflow"
  provider="Illumina"
  duration="5:13"
>
  Illumina's animation of sequencing by synthesis, from library to aligned reads.
</YouTube>

In outline:

1. **Loading.** The library is washed over a **flow cell**, a glass slide with narrow
   channels whose inner surface is coated with short DNA strands that match the
   adapters. Fragments stick where their adapters meet a matching strand.
2. **Clustering.** Each fragment is copied in place, over and over, into a tight
   **cluster** of identical copies about one micron across ([Bentley et al.,
   2008][bentley]). A single molecule is too faint to see, but a cluster of copies glows
   brightly enough for a camera.
3. **Cycling.** In each cycle, the instrument adds all four nucleotides, each carrying a
   fluorescent dye and a removable cap that stops the copying after one base. Every
   cluster adds exactly one base, the camera records the color at each cluster, and the
   dye and cap are washed off before the next cycle. Cycle 1 reads the first base of
   every fragment, cycle 2 the second, and so on, so 150 cycles give 150-base reads.

![Three panels. a, a DNA fragment with an adapter at each end attaches to one of many short matching strands on a flow cell surface. b, the same spot now holds a cluster of identical copies. c, one strand in the cluster: a new copy grows along the template, and its newest base, C, carries a dye and a cap. A loop reads: add one base, image, remove dye and cap, repeat. Below, the camera records one colored square per cycle for cycles 1 to 4, which reads T G A C.](../images/4.1-sequencing-by-synthesis.svg "Sequencing by synthesis. a, a library fragment attaches to a matching strand on the flow cell. b, the fragment is copied in place into a cluster of identical copies. c, in each cycle, every strand in the cluster adds one dye-labeled base with a cap that stops further copying. The camera records the color, then the dye and cap are removed. Reading the colors cycle by cycle gives the sequence. Colors here are schematic; current instruments use fewer dyes.")

Software turns the images into bases, a step called **base calling**, and gives each
base a score for how sure it is.

## Quality Scores

Every base comes with a **quality score**, written on the Phred scale ([Ewing and Green,
1998][phred]). The score Q stands for the estimated chance that the base is wrong, P,
through Q = −10 × log₁₀(P). Each step of 10 is a tenfold change:

| Quality score | Chance the base is wrong | Accuracy |
| ------------- | ------------------------ | -------- |
| Q10           | 1 in 10                  | 90%      |
| Q20           | 1 in 100                 | 99%      |
| Q30           | 1 in 1,000               | 99.9%    |
| Q40           | 1 in 10,000              | 99.99%   |

Q30 is the usual yardstick: instrument specifications and run reports quote the share of
bases at Q30 or above. The scores are stored next to the bases in [FASTQ
files](../06-genomic-file-formats/02-FASTQ-files.md), and later steps use them to decide
how much to trust each base.

Quality falls along the read. In every cycle, a few molecules in a cluster fail to add a
base, or add two, and fall out of step with the rest. The errors add up, so by later
cycles each cluster's signal is a blur of neighboring positions. This is the main reason
short reads stay short.

## Paired-End Reads

Most runs read each fragment from both ends. The instrument first reads a set number of
bases from one end, called **Read 1**. It then copies the fragment so the other strand
faces up and reads the same number of bases from the opposite end, called **Read 2**.
Together they make a **read pair**. A common setup reads 150 bases from each end,
written 2 × 150. The reads stay the same length, but the fragments don't. On a long
fragment, the two reads leave an unread gap in the middle. On a shorter one, they
overlap. And when the fragment is shorter than a read, each read runs off the end of the
sample's DNA and into the adapter on the far side. Those adapter bases aren't part of
the sample, so trimming tools remove them ([Chen et al., 2018][fastp]).

![A key shows Read 1 as a teal arrow, Read 2 as a purple arrow, adapters in orange and the insert in grey. A dashed vertical line marks 150 bases from the start of Read 1 and runs through three fragments drawn to scale. Long fragment, 500-base insert: Read 1 and Read 2 each cover 150 bases from opposite ends, leaving an unread gap in the middle. Medium fragment, 250-base insert: the two reads overlap in the middle, shaded green. Short fragment, 100-base insert: each read runs past the end of the insert into the adapter on the far side, shown hatched.](../images/4.2-paired-end-reads.svg "The reads stay the same length; the fragments don't. With 150-base reads, a long insert leaves an unread gap between Read 1 and Read 2, a medium insert makes them overlap, and an insert shorter than a read makes both reads run into the adapter.")

The two reads in a pair come from the same fragment, so they lie a known distance apart
and face each other. The length of the fragment between the adapters is the **insert
size**, and the unread stretch between the two reads is the inner distance.

![One fragment drawn larger: an orange Read 1 adapter on the left, a grey insert, and an orange Read 2 adapter on the right, with 5′ and 3′ marking the ends of both strands. Read 1, a teal arrow, starts at the left end of the insert and points right. Read 2, a purple arrow below, starts at the right end of the insert and points left. Brackets below mark the inner distance between the inner ends of the two reads, the insert size between the adapters, and the fragment length including the adapters.](../images/4.3-paired-end-read-zoomed.svg "One fragment up close. Read 1 and Read 2 start at opposite ends of the insert and read toward each other. The inner distance is the unread stretch between them, the insert size spans the DNA between the adapters, and the fragment length includes the adapters.")

That known spacing is useful. If one read of a pair falls in a repeat that appears in
many places, its partner, in unique sequence nearby, shows which copy it came from. And
when the two reads land much farther apart than the insert size allows, on different
chromosomes, or facing the wrong way, they point to a rearrangement, one of the main
signals in [Finding Structural
Variants](../03-genomic-variation/04-structural-variation.md#finding-structural-variants).

## Errors to Know About

Illumina reads are accurate, with roughly one error per thousand bases in a modern run
([Wenger et al., 2019][wenger]), but the errors aren't random, and each kind leaves its
own mark:

- **Mostly substitutions.** Errors are almost always one base read as another.
  Insertions and deletions are rare.
- **Worse toward the end.** Error rates climb along the read, as described above, and
  Read 2 is usually a little worse than Read 1.
- **GC bias.** Regions very rich or very poor in G and C get fewer reads, partly from
  PCR in [library preparation](02-library-preparation.md#making-copies).
- **Poly-G tails.** Two-color instruments, such as the [NextSeq][nextseq] and
  [NovaSeq][novaseq], record G as the absence of light. When a cluster's signal fades
  near the end of a read, the instrument sees darkness and calls a run of Gs that isn't
  there ([Chen et al., 2018][fastp]). Trimming tools remove them.
- **Index hopping.** On some instruments, a small share of reads carry another sample's
  index, as described in [Adding Adapters and
  Indexes](02-library-preparation.md#adding-adapters-and-indexes).

## From Images to Files

During a run, the instrument writes its base calls to BCL files, one set per cycle. When
the run ends, software converts them into FASTQ files, sorting reads into samples by
their index on the way. A paired-end run gives each sample two FASTQ files, one for Read
1 and one for Read 2, with the reads in the same order in both. Those FASTQ files are
usually where a computational team's work begins.

## Other Short-Read Instruments

Illumina isn't the only maker, and the market has grown more crowded. Most of these
instruments also read by synthesis, each with its own chemistry, and their output looks
much the same: short reads, quality scores, FASTQ files. This list is not complete, and
it changes quickly. Each company's site has more on its instruments.

| Company | Instruments | How it differs |
| --- | --- | --- |
| Element Biosciences | [AVITI][aviti] | Reads with a different chemistry, called avidity sequencing |
| MGI and Complete Genomics | [DNBSEQ][dnbseq] | Copies each fragment into a ball of DNA, a DNA nanoball, instead of a cluster |
| Ultima Genomics | [UG 100][ug100], [UG 200][ug200] | Spreads fragments on a spinning silicon wafer to lower cost |
| Thermo Fisher (Ion Torrent) | [Ion GeneStudio, Genexus][iontorrent] | Detects the tiny change in acidity as each base is added, instead of light |

[bentley]: https://doi.org/10.1038/nature07517
[phred]: https://doi.org/10.1101/gr.8.3.186
[wenger]: https://doi.org/10.1038/s41587-019-0217-9
[fastp]: https://doi.org/10.1093/bioinformatics/bty560
[illumina]: https://www.illumina.com/systems/sequencing-platforms.html
[nextseq]: https://www.illumina.com/systems/sequencing-platforms/nextseq-1000-2000.html
[novaseq]: https://www.illumina.com/systems/sequencing-platforms/novaseq-x-plus.html
[aviti]: https://www.elementbiosciences.com/products/aviti
[dnbseq]: https://www.completegenomics.com/
[ug100]: https://www.ultimagenomics.com/products/ug-100-sequencing-platform
[ug200]: https://www.ultimagenomics.com/products/ug200-series
[iontorrent]: https://www.thermofisher.com/us/en/home/brands/ion-torrent.html
