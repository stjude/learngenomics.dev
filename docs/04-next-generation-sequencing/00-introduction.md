---
title: Introduction
---

Everything in [Genomic Variation](../03-genomic-variation/00-introduction.md) assumed
you could read a person's DNA. This chapter is about how that happens: how a piece of
tissue or a tube of blood becomes a file of text that a computer can work with.

No instrument reads a genome from one end to the other. DNA comes out of cells already
broken into pieces, and even the best sequencers read somewhere between a few hundred
and a few hundred thousand bases of a molecule at a time. So sequencing works the other
way round. The DNA is broken into many pieces, millions or billions of them are read at
once, and software puts the picture back together afterward. The sequence of one piece,
as the instrument reports it, is called a **read**.

Getting from a sample to reads takes three steps:

1. Collect a sample and extract its DNA or RNA.
2. Build a library: break the DNA into fragments and attach the short synthetic
   sequences a sequencer needs to hold and read them.
3. Sequence the library. The instrument reads each fragment and writes the reads, with a
   quality score for every base, to files.

The pages in this chapter follow those steps, then turn to the choice that shapes
everything else, which part of the sample to read:

- [Samples and Extraction](01-samples-and-extraction.md): where the DNA comes from, and
  what can go wrong before sequencing starts.
- [Library Preparation](02-library-preparation.md): turning DNA into something a
  sequencer can read.
- [Short-Read Sequencing](03-short-read-sequencing.md): how Illumina instruments read
  billions of short fragments at once, and the errors they make.
- [Long-Read Sequencing](04-long-read-sequencing.md): how PacBio and Oxford Nanopore
  instruments read single molecules thousands of bases long.
- [Common Types of Sequencing](05-types-of-sequencing/00-introduction.md): choosing what to read,
  from whole genomes to single cells, with a page for each kind.

Unless a page says otherwise, the examples use paired-end Illumina reads, the most
widely used kind. What happens to the reads afterward, placing them on the reference and
finding variants, is the subject of [From Reads to
Variants](../05-from-reads-to-variants/00-introduction.md).
