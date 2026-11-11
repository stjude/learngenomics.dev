---
title: Assay for Transposase-Accessible Chromatin Using Sequencing (ATAC-seq)
---

**ATAC-seq** (assay for transposase-accessible chromatin using sequencing) finds the
parts of the genome that are open. Most DNA in the nucleus is wrapped tightly around
histones, out of reach of the proteins that read genes. The stretches left open include
the promoters and enhancers a cell is using, so a map of open DNA is a map of where the
genome could be active.

## What It Measures

ATAC-seq measures accessibility. DNA wraps around histones in units called
**nucleosomes**, each holding about 150 bases, and the DNA between nucleosomes is easier
to reach. Where [chromatin is loosely
packed](../../01-biological-foundations/01-cells-genomes-dna-chromosomes.md#how-dna-is-packaged),
there are wider gaps, and those gaps are where transcription factors bind.

Unlike ChIP-seq, ATAC-seq doesn't target a particular protein. It shows every open
region at once.

## How the Library Is Made

ATAC-seq uses the same enzyme as
[tagmentation](../02-library-preparation.md#adding-adapters-and-indexes): a transposase,
Tn5, loaded with sequencing adapters. The enzyme is added to intact nuclei, where it
cuts DNA and attaches adapters in the same step, but only where it can reach. Open DNA
gets cut often; DNA wrapped in nucleosomes rarely does. The tagged fragments are
amplified and sequenced.

The original method took two steps and as few as 500 to 50,000 cells ([Buenrostro et
al., 2013][buenrostro]), much less than earlier ways of mapping open chromatin. One
problem is that the DNA in mitochondria isn't packed into nucleosomes, so the enzyme
cuts it freely, and many reads can be wasted on it. An improved protocol, Omni-ATAC, cut
the number of reads from mitochondrial DNA 13-fold ([Corces et al., 2017][corces]).

## Depth and Read Setup

Reads are mapped, and regions where they pile up are called peaks, just as in ChIP-seq.
ATAC-seq is read paired-end, because the two reads of a pair give each fragment's exact
length, and fragment length shows what lay between the two cuts. The enzyme can't cut
DNA that is wrapped around a nucleosome, only the DNA on either side of it:

- **Under about 100 bases.** Both cuts landed in the same stretch of open DNA, with no
  nucleosome between them.
- **About 200 bases.** The cuts landed on either side of one nucleosome, so the fragment
  holds that nucleosome's DNA plus a little open DNA at each end.
- **About 400 or 600 bases.** The fragment spans two or three nucleosomes in a row.

Sorting fragments by length this way shows where individual nucleosomes sit inside an
open region, not just that the region is open ([Buenrostro et al., 2013][buenrostro]).

![Top: a stretch of chromatin with three nucleosomes on the left, an open region in the middle with one bound protein, and three more nucleosomes on the right. Small teal markers show where Tn5 cut: in the gaps between nucleosomes on the left, and several times inside the open region, on either side of the bound protein. Middle: the fragments that result, drawn under where they came from, with orange adapters on each end and dashed circles where nucleosomes were. Two short fragments from the open region are labeled no nucleosome, under 100 bases. A longer one is labeled one nucleosome, about 200 bases, and the longest two nucleosomes, about 400 bases. Bottom: read depth along about 1,600 bases of the reference genome is low across the nucleosomes and rises into a broad peak over the open region.](../../images/4.12-atac-seq.svg "ATAC-seq. Top: Tn5 cuts the DNA where it can reach, in the open region and in the short gaps between nucleosomes. Middle: once the proteins are removed, a fragment's length shows how many nucleosomes lay between its two cuts. Bottom: mapped reads pile up over the open region, giving a peak.")

## Tradeoffs

#### Pros

- **The whole genome at once.** ATAC-seq finds open regions across the genome.
- **Fewer cells, less work.** It needs fewer cells and less work than other methods.
- **Footprints.** Where a protein is bound inside an open region, it shields the DNA
  beneath it from the enzyme, leaving a small gap in the cuts called a footprint.
  Footprints at the binding sequence of a protein called CTCF were visible in the
  original study.

#### Cons

What it can't show is which protein is bound, or whether an open region is actually
doing anything. Open isn't the same as active. ATAC-seq is often paired with RNA-seq or
ChIP-seq to connect open regions to the genes they control.

## Example: A Blood Sample in an Afternoon

The first ATAC-seq paper showed how quick the method could be. Starting from a blood
sample, the authors had a finished sequencing library in 275 minutes ([Buenrostro et
al., 2013][buenrostro]). They mapped open chromatin in one person's T cells, a kind of
immune cell, on consecutive days, showing that a person's chromatin could be profiled
within a day. Since then, ATAC-seq has become one of the most widely used ways to map
open chromatin, including in [single cells](08-single-cell-sequencing.md).

[buenrostro]: https://doi.org/10.1038/nmeth.2688
[corces]: https://doi.org/10.1038/nmeth.4396
