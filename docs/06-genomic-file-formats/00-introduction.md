---
title: Introduction
description: "An overview of the file formats for reads, alignments, variants, regions and genes, and the compression most of them share."
---

[From Reads to Variants](../05-from-reads-to-variants/00-introduction.md) moved data
through three file formats, FASTQ for reads, BAM for reads placed on the reference and
VCF for variant calls, and explained just enough of each to follow along. This chapter
covers them in full, along with the formats that list regions and describe genes, and
the compression that most of them share.

Genomic file formats are simpler than they first look. Most are plain text. SAM, VCF,
BED and GTF/GFF3 put one record on each line, with its fields separated by tabs, and
FASTQ spends four lines on each read. BAM, CRAM and BCF store the same records in a
compressed, binary form, and tools such as `samtools` and `bcftools` turn them back into
text. So you can look inside nearly any genomic file, and do a lot of work with it,
using ordinary command-line tools such as `grep`, `cut`, `sort` and `awk`.

[Sandbox.bio](https://sandbox.bio/tutorials) has some great tutorials to teach you these
things. [Terminal Basics](https://sandbox.bio/tutorials/terminal-basics) covers `grep`
and pipes, [Terminal Exercises](https://sandbox.bio/tutorials/carpentries-shell-novice)
practices `cut` and `sort`, and [Data Exploration with
awk](https://sandbox.bio/tutorials/awk-intro) covers `awk`.

## Try It Yourself

Each page ends with a Try It section that runs real commands on real or simulated data.
Like [From Reads to
Variants](../05-from-reads-to-variants/00-introduction.md#try-it-yourself), the
exercises need only a terminal on macOS or Linux.

## In This Chapter

- [Compression and BGZF](01-compression-and-BGZF.md): how genomic files are compressed,
  and how an index lets tools jump straight to one region.
- [FASTQ Files](02-FASTQ-files.md): reads and their quality scores, as they come off the
  sequencer.
- [SAM/BAM/CRAM Files](03-BAM-files.md): reads placed on the reference, stored as text,
  as compressed binary, or as differences from the reference.
- [VCF/BCF Files](04-VCF-files.md): variant calls, and each sample's genotype at every
  one.
- [BED Files](05-BED-files.md): lists of regions, and the two ways of counting
  positions.
- [GTF/GFF3 Files](06-GTF-GFF3-files.md): where the genes are, and how each one is
  built.
- [Conclusion](07-conclusion.md): how the formats fit together, and tutorials for more
  practice.
