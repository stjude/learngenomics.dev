---
title: Introduction
---

The same sequencer can answer very different questions depending on which molecules go
into the library. Sequence all of a person's DNA and you can look for variants anywhere.
Sequence only the exons and you get the protein-coding parts for a fraction of the cost.
Sequence RNA and you learn which genes are switched on. Sequence only the DNA a protein
was holding, or only the DNA left open, and you learn how the genome is being used.

Each of these is a separate **assay**, a laboratory method for measuring one thing, and
each has its own way of selecting molecules during [library
preparation](../02-library-preparation.md#choosing-what-to-keep). Choosing one is a
tradeoff between how much of the genome you read, how deeply you read it, and how much
you can spend. Unless a page says otherwise, the assays here use [short
reads](../03-short-read-sequencing.md).

## Coverage and Depth

Two words come up on every assay page. **Depth** is how many reads cover a given base.
**Coverage** usually means the average depth across the region being sequenced, written
with an "x": a genome sequenced to 30x has, on average, 30 reads over each base.
Coverage is also used for breadth, the share of the region covered by at least some
minimum number of reads, so a report might say "30x mean coverage, with 95% of bases at
20x or more".

Depth matters because no single read can be trusted on its own. With enough reads at a
position, a real variant shows up again and again, while a sequencing error shows up in
one or two reads and can be set aside.

![A grey reference bar, with short teal reads stacked below it at scattered positions. A highlighted column crosses seven reads and is labeled 'Depth = 7 at this base'. At one position, most reads carry an orange mark, labeled 'Real variant: seen in many reads'. Elsewhere a single read has a purple mark, labeled 'Error: seen in one read'. One stretch has no reads. Below, a depth plot rises and falls with the number of reads, drops to zero at the stretch with no reads, and has a dashed line for a mean coverage of 5x.](../../images/4.6-coverage-and-depth.svg "Coverage and depth. The number of reads over each base, its depth, rises and falls along the genome, and some stretches get no reads at all. Here the mean coverage is 5x. A real variant shows up in many reads at the same position, while a sequencing error usually appears in just one.")

Since reads fall at random, some bases get more than the average and some get fewer, and
a few may get none. If reads landed perfectly at random, the share of bases left with no
reads would be about e<sup>−c</sup>, where c is the coverage ([Lander and Waterman,
1988][lander]). At 1x, that's about 37% of the genome unread; at 5x, under 1%. Real data
is less even than that, because some regions are harder to read than others, so labs
sequence deeper than the arithmetic alone suggests.

How deep is deep enough depends on what you're looking for. A germline variant inherited
from one parent should be in about half the reads, so a modest depth finds it. A
[somatic](../../03-genomic-variation/00-introduction.md) variant in a tumor may be in
only a small share of the reads. Normal cells mixed into the sample dilute it, and so do
differences among the tumor cells themselves. A tumor usually starts from a single cell,
and its descendants keep picking up new variants as they divide ([Nowell,
1976][nowell]). A group of cells descended from one ancestor, and sharing its variants,
is a **clone**. A variant that arose later, in one branch of the tumor, is carried only
by that **subclone**, so it shows up in fewer reads. At 30x, a variant in 10% of the
reads is expected in only three of them, too few to tell from an error. Finding variants
like that takes much more depth.

## The Main Assays

| Assay | What goes into the library | What it's used for |
| --- | --- | --- |
| [Whole-genome sequencing](01-whole-genome-sequencing.md) (WGS) | All of the DNA | Every kind of variant, anywhere in the genome |
| [Whole-exome sequencing](02-whole-exome-sequencing.md) (WES) | DNA from exons only | Variants that change proteins, at lower cost |
| [RNA-seq](03-rna-seq.md) | RNA, copied into cDNA | Which genes are on and how much; fusions; splicing |
| [Targeted sequencing](04-targeted-sequencing.md) | DNA from a chosen set of regions | Very deep reads of known genes, often in clinical tests |
| [ChIP-seq](05-chip-seq.md) | DNA held by one protein | Where a protein binds, or where a histone mark sits |
| [ATAC-seq](06-atac-seq.md) | DNA left open, not wrapped in chromatin | Which regions are open and could be active |
| [Hi-C](07-hi-c.md) | Pieces of DNA that touch in the nucleus | How the genome is folded in three dimensions |
| [Single-cell sequencing](08-single-cell-sequencing.md) | Molecules from each cell, kept apart by barcodes | What differs from one cell to the next |

The first four look at the sequence itself: what the DNA says, and what RNA is made from
it. ChIP-seq, ATAC-seq and Hi-C look at how the genome is packaged and used, so where
the reads land tells you more than their sequence does. Single-cell sequencing is a way
of doing other assays, most often RNA-seq, one cell at a time.

[nowell]: https://doi.org/10.1126/science.959840
[lander]: https://doi.org/10.1016/0888-7543(88)90007-9
