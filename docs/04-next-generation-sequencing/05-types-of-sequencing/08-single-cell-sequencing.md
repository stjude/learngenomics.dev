---
title: Single-Cell Sequencing
description: "Single-cell sequencing: measuring DNA or RNA one cell at a time to find rare cell types, with library prep, depth, tradeoffs and an example."
---

Every assay so far starts with DNA or RNA pooled from many thousands of cells, so the
result is an average. A tumor sample's RNA-seq shows the average of tumor cells, immune
cells and normal tissue together. A rare cell type disappears into the average, and two
groups of cells doing opposite things can look like one group doing nothing.
**Single-cell sequencing** keeps each cell's molecules labeled, so the data can be
pulled apart one cell at a time.

## What It Measures

Single-cell sequencing runs other assays on one cell at a time. Single-cell RNA-seq is
by far the most common, and measures which genes each cell is expressing. There are
single-cell versions of ATAC-seq and DNA sequencing too, and methods that measure more
than one thing in the same cell.

## How the Library Is Made

First, the tissue is broken apart into single cells, floating free in liquid. In the
most widely used approach, the cells then flow through a tiny channel where each is
sealed into an oil droplet together with a bead ([Zheng et al., 2017][zheng]). Every
bead is coated with short DNA strands carrying:

- a **cell barcode**, the same on every strand on that bead and different from every
  other bead,
- a UMI, different on every strand, to mark each [original
  molecule](../02-library-preparation.md#making-copies), and
- a run of T's, called **poly-T**, that catches the [poly-A
  tail](../../01-biological-foundations/03-transcription.md) at the end of each mRNA.

Inside the droplet, the cell breaks open, its mRNA sticks to the bead by the poly-A
tail, and each mRNA is copied into cDNA that carries the barcode and UMI of the strand
that caught it. Then the droplets are broken and everything is pooled into one library.
After sequencing, software sorts reads into cells by their barcode, much as indexes sort
reads into samples, and counts each gene's molecules in each cell using the UMIs.

![Three parts. Top: two channels, one carrying cells and one carrying barcoded beads, merge into one channel. Oil flows in from above and below, and droplets leave to the right, each holding one cell and one bead, with a teal, an orange and a purple bead. Middle: a zoom into the purple bead shows one of its strands. From the bead outward, a purple cell barcode, labeled same on the whole bead; a UMI, GGCT, labeled different on every strand; and a poly-T, TTTTTT, labeled catches the poly-A tail. An mRNA's AAAAAA tail is paired to the poly-T, and a dashed cDNA, copied from the mRNA, extends the strand. Bottom: six reads listed by barcode color, UMI and gene. The first two are both teal, GATC, Gene 1, bracketed as same UMI, counted once. Beside them, a table with one column for each cell, Cell 1 teal, Cell 2 orange and Cell 3 purple, and one row for each gene. Cell 1 has 1 for Gene 1 and 1 for Gene 3; Cell 2 has 2 for Gene 2; Cell 3 has 1 for Gene 1; the rest are 0.](../../images/4.15-single-cell.svg "Droplet single-cell RNA-seq. Top: each cell is sealed into an oil droplet with one bead. Middle: every strand on a bead carries the bead's cell barcode, its own UMI, and a poly-T that catches an mRNA by its poly-A tail; the mRNA is then copied into cDNA on the end of the strand. Bottom: after sequencing, reads are sorted into cells by barcode, and reads with the same UMI count as one molecule, giving a table of counts for each gene in each cell. Real experiments have thousands of cells and genes, and most of the table is zeros.")

One run can capture thousands to tens of thousands of cells. Not every cell is captured,
and a small share of droplets catch two cells at once, called doublets, which software
tries to find and remove.

## Depth and Read Setup

Depth is counted per cell, and it's low: a typical experiment reads far fewer molecules
from each cell than bulk RNA-seq reads from a whole sample. Most methods sequence only
one end of each mRNA, enough to tell which gene it came from and count it, but not to
see its whole sequence. One read of each pair carries the barcode and UMI, and the other
carries the gene sequence.

## Tradeoffs

#### Pros

- **Cell types.** Single-cell RNA-seq finds the kinds of cells in a sample, including
  rare ones, by grouping cells with similar expression.
- **Changes along a path.** It can show how cells change along a path, such as a stem
  cell maturing.
- **Where a gene is expressed.** It shows which cell types express a gene of interest.
- **Tumor and normal cells.** In cancer, it can separate tumor cells from the normal
  cells around them.

#### Cons

- **Each cell gives little data.** Only a fraction of each cell's mRNA is captured, so
  many genes have zero reads in a given cell. Most of those zeros reflect how few
  molecules were sampled, not a gene that's truly off ([Svensson, 2020][svensson]).
- **Breaking apart the tissue changes it.** Separating cells can stress them, which
  switches on stress genes before the cells are captured ([van den Brink et al.,
  2017][brink]). It also loses where each cell was in the tissue. Sequencing single
  nuclei instead of whole cells avoids some of these problems and works on frozen tissue
  ([Habib et al., 2017][habib]).
- **Cost per cell.** Thousands of cells per sample add up, so experiments often include
  fewer samples than bulk studies.

## Example: A New Cell Type for Cystic Fibrosis

In 2018, two groups used single-cell RNA-seq to map the cells lining the airways of mice
and people ([Montoro et al., 2018][montoro]; [Plasschaert et al., 2018][plasschaert]).
Both found a rare cell type no one had described before, which they called the
**pulmonary ionocyte**. Ionocytes make up only about 1% of the cells in the airway
lining, but they express
[*CFTR*](../../01-biological-foundations/06-genotype-phenotype-haplotype.md), the gene
behind cystic fibrosis, at much higher levels than the cells around them. In mice, they
were the source of most of the airway's *CFTR* RNA.

Bulk RNA-seq averages *CFTR* expression across all the airway's cells, so there was no
way to see that so much of it came from one rare cell type. Seeing each cell separately
changed which cells researchers study to understand the disease.

## Up Next

This chapter followed a sample from collection to a set of reads, and showed how the
choice of assay decides what those reads can tell you. The next chapter, [From Reads to
Variants](../../05-from-reads-to-variants/00-introduction.md), follows the reads from
there, starting with mapping them to the reference.

[zheng]: https://doi.org/10.1038/ncomms14049
[svensson]: https://doi.org/10.1038/s41587-019-0379-5
[brink]: https://doi.org/10.1038/nmeth.4437
[habib]: https://doi.org/10.1038/nmeth.4407
[montoro]: https://doi.org/10.1038/s41586-018-0393-7
[plasschaert]: https://doi.org/10.1038/s41586-018-0394-6
