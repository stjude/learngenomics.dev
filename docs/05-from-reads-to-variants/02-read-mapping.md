---
title: Read Mapping
track: From Reads to Variants
---

Sequencing leaves you with something like a box of puzzle pieces dumped out on a table.
Each read is one piece, and nothing on it says where it belongs. Putting each piece back
in its place is called **read mapping**, or alignment. As with any puzzle, it helps to
have the picture on the front of the box, and in genomics that picture is the [reference
genome](../03-genomic-variation/01-baselines-for-variation.md). The picture isn't a
perfect match, though. Your genome differs from the reference in millions of places, and
those differences are what this chapter is looking for. And some parts of the picture,
like a stretch of clear sky, look the same in many places, so a piece from there could
fit in more than one spot.

## Choosing a Reference

Before mapping, you decide which reference to use. Here it's chromosome 20 of GRCh38,
which you downloaded on [Setting Up](01-setting-up.md). Every step after this one
depends on that choice. The same position has different coordinates in different
versions of the reference, so results from two versions can't be compared directly (see
[Baselines for Variation](../03-genomic-variation/01-baselines-for-variation.md)).
Moving an analysis to a new version means mapping every sample again, so a project
usually stays on the version it started with. GRCh38 was the first update to change
coordinates since GRCh37, released in 2009 ([Schneider et al.,
2017](https://doi.org/10.1101/gr.213611.116)), and both are still in use. Genome in a
Bottle, for example, publishes its newest truth set for GRCh37 as well as GRCh38.

## How an Aligner Works

The software that does the mapping is called a mapper or **aligner**. It starts by
building an **index** of the reference, a lookup table of short sequences and where each
one occurs. For every read, it looks up short exact matches, called seeds, to find the
places the read might belong. It then lines up the whole read at each of those places,
allowing for mismatches, insertions and deletions, and keeps the best ([Li,
2018](https://doi.org/10.1093/bioinformatics/bty191)). For paired reads, it maps both
reads of a pair together and expects them to land a fragment's length apart, facing each
other (see [Paired-End
Reads](../04-next-generation-sequencing/03-short-read-sequencing.md#paired-end-reads)).
Aligners have many settings that can be tuned to the kind of data.

[BWA](https://github.com/lh3/bwa) ([Li and Durbin,
2009](https://doi.org/10.1093/bioinformatics/btp324)) has long been a standard choice
for short DNA reads. This chapter uses [minimap2](https://github.com/lh3/minimap2), from
the same author, which is three to four times as fast as the usual short-read aligners
at comparable accuracy and also handles long reads ([Li,
2018](https://doi.org/10.1093/bioinformatics/bty191)). RNA needs a different kind of
aligner. A read from a spliced mRNA can span two exons that sit far apart in the genome
(see [Transcription](../01-biological-foundations/03-transcription.md)), so
[RNA-Seq](../04-next-generation-sequencing/05-types-of-sequencing/03-rna-seq.md) reads
are mapped with a splice-aware aligner such as [STAR](https://github.com/alexdobin/STAR)
([Dobin et al., 2013](https://doi.org/10.1093/bioinformatics/bts635)).

## What the Aligner Records

The aligner writes its results in **SAM** (Sequence Alignment/Map) format: plain text,
with one line per read and the details in tab-separated columns ([SAM
specification](https://samtools.github.io/hts-specs/SAMv1.pdf)). Text is simple for any
program to write and read, which is why aligners produce it, but it takes up a lot of
space. Pipelines therefore usually store alignments as **BAM**, the same records
compressed into a binary form (see [SAM/BAM/CRAM
Files](../06-genomic-file-formats/03-BAM-files.md)). A BAM file is several times
smaller, and once it is sorted it can be indexed, so tools can jump straight to one
region instead of reading the whole file. Nearly every analysis after this point starts
from a BAM file.

For each read, the aligner records where the read landed, how it lines up there and how
sure the aligner is. Where it lines up is written as a **CIGAR** string, a short code
that counts bases in runs. `148M` means all 148 bases are aligned to the reference,
matching or not; `I` marks bases inserted relative to the reference, `D` bases deleted
from it and `S` bases left out of the alignment ([SAM
specification](https://samtools.github.io/hts-specs/SAMv1.pdf)).

![Three examples, each showing a row of reference bases with a read's bases lined up underneath. First, Fits one place, MAPQ 60: a ten-base read matches the reference except for one base, which is highlighted. Second, Fits two places equally well, MAPQ 0: the reference contains the sequence ACGTA twice, labeled copy 1 and copy 2. The read ACGTA sits under copy 1, with "or?" and a dashed outline of the same read under copy 2. Third, End doesn't fit, MAPQ 60: the first eight bases of a read match the reference, and the last four, which don't match, are drawn as dashed outlines and labeled soft-clipped.](../images/5.2-read-mapping.svg "Read mapping. A read that fits only one place gets a high mapping quality, even if one of its bases differs from the reference. A read that matches both copies of a repeat gets mapping quality 0, because the aligner can't tell which copy it came from. When the end of a read doesn't match, the aligner soft-clips it: the bases stay in the file but are left out of the alignment.")

How sure the aligner is goes in the **mapping quality**, or MAPQ. Like a base quality
score (see [Quality
Scores](../04-next-generation-sequencing/03-short-read-sequencing.md#quality-scores)),
it is on the Phred scale: MAPQ is −10 log<sub>10</sub> of the chance that the position
is wrong, so 60 means about a one in a million chance ([SAM
specification](https://samtools.github.io/hts-specs/SAMv1.pdf)). It is the aligner's own
estimate, and each aligner works it out differently. minimap2 reports values from 0 to
60. A read that fits two or more places equally well, such as a read from inside a
repeat, gets a MAPQ of 0. The aligner still reports one of the places, but it has no way
of knowing which is right. A read pair can sometimes settle it, because a mate in unique
sequence nearby shows which copy the pair came from.

Variant callers give reads with low mapping quality little or no weight, so variants in
repeated sequence are easy to miss. One study of standard short-read data found
stretches of 748 genes, inside protein-coding exons, that either had too few reads that
mapped or had reads that couldn't be placed with confidence ([Ebbert et al.,
2019](https://doi.org/10.1186/s13059-019-1707-2)). Long reads, which can span a repeat,
resolved most of them.

Sometimes the end of a read doesn't fit anywhere near where the rest of it lines up. It
might be leftover adapter, or the read might cross the breakpoint of a [structural
variant](../03-genomic-variation/04-structural-variation.md#breakpoints-and-junctions).
Rather than force a poor alignment, the aligner **soft-clips** the end: the bases stay
in the file, but they're left out of the alignment. minimap2 can then map the clipped
part on its own, somewhere else, as a supplementary alignment ([Li,
2018](https://doi.org/10.1093/bioinformatics/bty191)).

## Try It

This step needs `chr20.fa`, `reads_1.fq.gz` and `reads_2.fq.gz` from [Setting
Up](01-setting-up.md). Run it from the same folder, with the `reads-to-variants`
environment active:

```bash
# Map each read pair to chromosome 20, then save the alignments as a BAM file
minimap2 -ax sr -t 4 chr20.fa reads_1.fq.gz reads_2.fq.gz \
  | samtools view -b -o hg002.mapped.bam -
```

`-x sr` loads minimap2's settings for short reads, `-a` asks for full alignments in SAM
format and `-t 4` uses four processor cores. minimap2 builds its index of `chr20.fa`
first, which for one chromosome takes a few seconds. It then writes SAM text, and the
`|` (a pipe) passes that text straight to `samtools view -b`, which compresses it into
`hg002.mapped.bam`. The SAM text is never saved to disk. As SAM, these alignments would
take about 190 MB; as BAM, they take 57 MB. On our computer, the whole step took about
four seconds and less than 1 GB of memory.

Then ask `samtools` for a summary:

```bash
# Count how the reads mapped
samtools flagstat hg002.mapped.bam
```

Among its output are these lines:

```text
415831 + 0 in total (QC-passed reads + QC-failed reads)
235 + 0 supplementary
412743 + 0 mapped (99.26% : N/A)
387086 + 0 properly paired (93.14% : N/A)
3084 + 0 singletons (0.74% : N/A)
```

The file holds 415,831 alignments: one for each of the 415,596 reads, plus 235
supplementary alignments for clipped parts mapped somewhere else. Over 99% of the reads
mapped. 93% are properly paired, meaning both reads mapped facing each other at a
distance that fits the library. Most of the rest mapped too, but sit 800 to 1,000 bases
apart, farther than minimap2 expected from the typical pair here. The 3,084 singletons
are reads that mapped while their mate didn't.

Next, look at the alignments themselves. `samtools view` prints a BAM file's records as
SAM text, and `cut -f 1-6` keeps the first six columns:

```bash
# Show the first five alignments, keeping only the first six columns
samtools view hg002.mapped.bam | head -n 5 | cut -f 1-6
```

Each line is one alignment. Here is a made-up example of what one looks like:

```text
read_1	99	chr20	10250312	60	140M8S
```

From left to right, the columns are ([SAM
specification](https://samtools.github.io/hts-specs/SAMv1.pdf)):

- `read_1`: the read's name, the same as in the FASTQ file.
- `99`: the **flag**, a number that packs several yes-or-no facts together. Each fact
  has its own value, and the flag is their sum. Here 99 is 1 + 2 + 32 + 64: the read is
  paired, the pair is properly paired, the mate is on the reverse strand and this is
  Read 1.
- `chr20` and `10250312`: the chromosome and the position of the first aligned base.
- `60`: the mapping quality.
- `140M8S`: the CIGAR string. The first 140 bases are aligned and the last 8 are
  soft-clipped.

Compare the example with your own output. Then count the reads that got a mapping
quality of 0:

```bash
# Keep the mapped reads with a mapping quality of 0, then count them
samtools view -F 0x904 hg002.mapped.bam | awk '$5 == 0' | wc -l
```

`-F 0x904` skips unmapped reads and extra alignments, so each read is counted once, and
the mapping quality is the fifth column. The answer is 99, out of 412,508 mapped reads.
That's very few, partly because the reference here is a single chromosome, so a read
whose other copies lie on other chromosomes has only one place to go (see [Check What
You Have](01-setting-up.md#check-what-you-have)). Across the whole genome, the share
would be higher.

Next, get the alignments ready for variant calling: [Preparing
Alignments](03-preparing-alignments.md).
