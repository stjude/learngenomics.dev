---
title: Library Preparation
description: "How DNA is made into a sequencing library: breaking it into fragments, choosing what to keep, adding adapters and indexes, and making copies."
---

Freshly extracted DNA needs some preparation before it can be sequenced. It is first
made into a **library**: a collection of DNA fragments, each a suitable length and each
carrying short synthetic sequences at both ends that the instrument knows how to grab
and read from. Building one is called library preparation, and it happens in the wet lab
before the sample ever reaches a sequencer.

RNA needs one extra step first. Most sequencers read only DNA, so RNA is copied into
**complementary DNA** (cDNA) by reverse transcriptase, the enzyme retroviruses such as
HIV use to copy their RNA genomes into DNA. From there, the cDNA is prepared like any
other DNA. Nanopore instruments are the exception, since they can also read RNA directly
([Garalde et al., 2018][garalde]).

The recipe changes with the instrument and with what you want to read, but most
libraries go through some version of four steps, roughly in the order below. Those steps
grew up around short-read sequencing, and they don't all apply equally to long reads.
[Short-read](03-short-read-sequencing.md) and [long-read](04-long-read-sequencing.md)
sequencing each get their own page next. For now, the table below shows which steps
apply to which, and each section below splits into short reads and long reads.

| Step | Short reads | Long reads |
| --- | --- | --- |
| [Breaking the DNA](#breaking-the-dna) | Into pieces a few hundred bases long | Gently, keeping pieces many thousands of bases long |
| [Choosing what to keep](#choosing-what-to-keep) | Common | Possible, with methods of its own |
| [Adding adapters and indexes](#adding-adapters-and-indexes) | Always | Always, with adapters built for the instrument |
| [Making copies](#making-copies) | Usually, though often skipped for whole genomes | Usually skipped |

## Breaking the DNA

The first step is breaking the DNA, and here short and long reads want opposite things.

#### Short Reads

Extracted DNA comes in pieces tens of thousands of bases long, while a short-read
instrument reads a few hundred bases at most. So the DNA is broken on purpose into
fragments of a few hundred bases. There are three popular ways to do it:

- **Shearing** breaks DNA with physical force. Long DNA strands are fragile and snap
  when shaken or squeezed hard enough. The usual tool is sonication, which shakes the
  DNA with focused sound waves. An older method, nebulization, sprays it through a tiny
  opening.
- **Enzymatic fragmentation** uses a mix of enzymes that cut DNA at scattered spots. It
  needs no special instrument.
- **Tagmentation** uses an enzyme called a transposase, which cuts the DNA and attaches
  the adapters [described below](#adding-adapters-and-indexes) in a single step ([Adey
  et al., 2010][adey]). The same enzyme is the heart of
  [ATAC-seq](05-types-of-sequencing/06-atac-seq.md).

The choice often comes down to a lab's equipment and workflow. In one comparison,
sonication, nebulization, and enzymes all made good libraries, with only small
differences between them ([Knierim et al., 2011][knierim]).

Whichever method is used, each copy of the genome in a sample breaks in different
places, so the fragments overlap one another, which is what later lets software piece
the reads back together. The breaks are close to random but not perfectly so. Even
shearing breaks some sequences more easily than others, which can leave coverage uneven
([Poptsova et al., 2014][poptsova]).

Along the way, a size-selection step keeps only fragments in a narrow range, often
around 200 to 500 bases.

#### Long Reads

For long reads, the goal is to handle the DNA gently and keep the molecules as long as
possible. PacBio libraries are still broken, but into pieces many thousands of bases
long. For nanopore, read length depends mostly on how intact the extracted DNA is
([Logsdon et al., 2020][logsdon]).

## Choosing What to Keep

Many kinds of sequencing also keep only some of the material. This step is called
**library selection** or **enrichment**. Public archives such as the [European
Nucleotide Archive][ena] ask for it with every sequencing run submitted, using values
like "PolyA" or "Hybrid Selection". Unlike the other steps, it has no fixed place in the
order.

#### Short Reads

The best-known examples are short-read assays, which keep the parts from exons
([whole-exome sequencing](05-types-of-sequencing/02-whole-exome-sequencing.md)), RNA
with a poly-A tail or all RNA except ribosomal RNA
([RNA-seq](05-types-of-sequencing/03-rna-seq.md)), or DNA bound to a particular protein
([ChIP-seq](05-types-of-sequencing/05-chip-seq.md)). RNA-seq and ChIP-seq pull out what
they want before library preparation starts, while exome sequencing fishes the exons out
of a finished library. This step is what makes an exome an exome, and each page under
[Common Types of Sequencing](05-types-of-sequencing/00-introduction.md) explains its own.

#### Long Reads

Long reads can be targeted too, mostly with methods of their own. This guide doesn't
cover them in depth, but a 2024 review describes each in detail ([Iyer et al.,
2024][iyer]). It groups them into four kinds:

- **Long-range PCR** uses primers that stick just outside each target, then copies the
  stretch between them. What's left is a pool of copies of only the targets, each up to
  about 10 kb, with up to roughly 1,000 targets at once. The copies lose their
  methylation marks, because PCR builds each new strand from plain, unmarked bases, and
  the original molecules end up a tiny fraction of the pool.
- **Hybrid capture** breaks the DNA into pieces around 10 kb long and mixes them with
  baits, short strands matching the targets that magnetic beads can grab. The beads pull
  out the pieces stuck to baits, and everything else is washed away. The captured pieces
  are then copied by PCR, so methylation marks are lost.
- **Cas9**, the DNA-cutting enzyme behind CRISPR, is guided to cut on both sides of each
  target after the DNA's own ends are blocked. Adapters then favor the targets' fresh
  ends, so the original target molecules, often tens of kb long, are read with
  methylation intact. Targets get deep coverage, though stray molecules still make up
  most reads ([Gilpatrick et al., 2020][gilpatrick]).
- **Adaptive sampling** happens during the run, on nanopore instruments only, using an
  ordinary whole-genome library. Software reads the first few hundred bases of each
  molecule as it enters the pore, and if it isn't a target, the instrument reverses the
  voltage to eject it ([Payne et al., 2021][payne]). Targets are read in full with
  methylation intact, while everything else leaves only a short stub.

## Adding Adapters and Indexes

Next, short known sequences called **adapters** are joined to both ends of every
fragment. They are what the instrument grabs and reads from, and they can carry an
**index**, a short barcode sequence unique to each sample. Indexes let a lab pool dozens
or hundreds of libraries and run them together, called **multiplexing**. Afterward,
software sorts the reads back into samples by their index, called **demultiplexing**.

#### Short Reads

Short-read adapters do three jobs: (1) they let the fragment stick to the sequencer's
flow cell, (2) they give the sequencing reaction a known place to start reading, and (3)
they carry the index. [Figure 4.1](03-short-read-sequencing.md#figure-4-1) shows a
fragment's adapters attaching to a flow cell.

Sorting by index isn't perfect: on some Illumina instruments, a small share of reads
pick up another sample's index, a problem called index hopping. One large study measured
swap rates of 0.2 to 6% of reads ([Costello et al., 2018][costello]). Giving each sample
a unique pair of indexes, one on each adapter, lets software throw away any read whose
pair doesn't match.

#### Long Reads

Long-read adapters are built for how each instrument works. PacBio's hairpin adapters
close each fragment into a loop ([Figure 4.4](04-long-read-sequencing.md#figure-4-4)),
and nanopore adapters carry the motor protein that feeds DNA through the pore ([Figure
4.5](04-long-read-sequencing.md#figure-4-5); [Logsdon et al., 2020][logsdon]). Both can
be multiplexed. PacBio can build indexes into its hairpin adapters ([Ardui et al.,
2018][ardui]), and nanopore kits attach an index to both ends of each molecule ([Wick et
al., 2018][wick]).

## Making Copies

The last step is optionally amplifying the library with **PCR** (polymerase chain
reaction), which copies every fragment many times. There are two reasons to do it.
First, there may not be enough DNA: libraries made without PCR need a fairly large
amount of starting DNA, which many samples can't supply. Second, PCR copies only
fragments with adapters on both ends, so it enriches the library for pieces that can
actually be sequenced ([Aird et al., 2011][aird]).

The cost is that copies aren't perfect stand-ins for the original molecules:

- **Duplicates.** Copies of the same original fragment get sequenced more than once.
  They look like independent evidence for whatever they carry, including errors, but
  they aren't. Software later marks reads that start and end at exactly the same
  positions as duplicates and counts them once.
- **Bias.** Regions very rich or very poor in G and C copy less efficiently, so they end
  up with fewer reads ([Aird et al., 2011][aird]).
- **Copying errors.** A mistake made in an early PCR cycle is copied into every later
  copy of that fragment.
- **Lost marks.** Copies are built from plain, unmarked bases, so chemical marks on the
  original DNA, such as methylation, aren't carried over.

Once amplification is done, or skipped, the lab measures the library's concentration and
fragment sizes, pools it with others, and loads it onto a sequencer.

#### Short Reads

Whether a short-read library is amplified depends on the assay. Capture-based libraries,
such as exomes and panels, need PCR after capture ([Gnirke et al., 2009][gnirke]), and
many tagmentation kits use PCR to finish the adapters and add the indexes ([Head et al.,
2014][head]). Whole genomes can skip it when there is enough DNA. The 1000 Genomes
Project's high-coverage set of 3,202 genomes, for example, was made with PCR-free
libraries from 1 µg of DNA each ([Byrska-Bishop et al., 2022][byrska-bishop]). When
there isn't enough DNA, short random tags called **unique molecular identifiers** (UMIs)
can be attached to each fragment before amplification, so every copy of the same
original molecule carries the same tag and can be recognized ([Kivioja et al.,
2011][kivioja]).

#### Long Reads

Long-read libraries usually skip PCR altogether. PCR copies long molecules poorly,
rarely beyond about 10 kb ([Iyer et al., 2024][iyer]), and reading the original
molecules keeps methylation marks, which both PacBio and nanopore instruments can detect
([Logsdon et al., 2020][logsdon]). The main exception is long-range PCR, used to target
specific regions as described above.

[costello]: https://doi.org/10.1186/s12864-018-4703-0
[adey]: https://doi.org/10.1186/gb-2010-11-12-r119
[knierim]: https://doi.org/10.1371/journal.pone.0028240
[poptsova]: https://doi.org/10.1038/srep04532
[logsdon]: https://doi.org/10.1038/s41576-020-0236-x
[gnirke]: https://doi.org/10.1038/nbt.1523
[iyer]: https://doi.org/10.1101/gr.279168.124
[ena]: https://ena-docs.readthedocs.io/en/latest/submit/reads/webin-cli.html
[gilpatrick]: https://doi.org/10.1038/s41587-020-0407-5
[payne]: https://doi.org/10.1038/s41587-020-00746-x
[ardui]: https://doi.org/10.1093/nar/gky066
[wick]: https://doi.org/10.1371/journal.pcbi.1006583
[garalde]: https://doi.org/10.1038/nmeth.4577
[aird]: https://doi.org/10.1186/gb-2011-12-2-r18
[head]: https://doi.org/10.2144/000114133
[byrska-bishop]: https://doi.org/10.1016/j.cell.2022.08.004
[kivioja]: https://doi.org/10.1038/nmeth.1778
