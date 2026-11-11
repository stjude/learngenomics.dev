---
title: Introduction
---

[Next Generation Sequencing](../04-next-generation-sequencing/00-introduction.md) ended
with FASTQ files: millions of reads, each with a quality score for every base. On their
own, those reads tell you very little. Nothing in a read says where in the genome it
came from, and the few reads that differ from the reference are buried among millions
that match it. FASTQ files are usually where the sequencing lab hands off and
computational analysis picks up, and this chapter follows that analysis from reads to a
list of variants.

Throughout, we use real reads from HG002, a person whose genome the [Genome in a Bottle
Consortium](https://www.nist.gov/programs-projects/genome-bottle) has studied in great
detail, so you can check your results against a known answer.

Here, we focus on building a simple pipeline for germline [single nucleotide
variants](../03-genomic-variation/02-single-nucleotide-variation.md) and [small
insertions and deletions](../03-genomic-variation/03-insertions-and-deletions.md). A
typical genome differs from the reference at about four to five million sites, and more
than 99.9% of those variants are SNVs or short indels ([1000 Genomes Project Consortium,
2015](https://doi.org/10.1038/nature15393)). Other kinds of variants, such as somatic,
structural and copy number variants, would each need a chapter of their own, which we
don't have space for here.

Getting from reads to variants takes four steps:

1. Map each read to the place in the reference genome it most likely came from.
2. Prepare the alignments: sort them by position, flag reads that are copies of the same
   original fragment, and build an index so tools can jump straight to any region.
3. Call variants: at each position, weigh the evidence in the reads and decide the
   genotype.
4. Filter and check: set aside calls that are probably wrong, then measure how accurate
   the rest are by comparing them with a truth set, a list of variants already known for
   the same sample.

![Three stages from top to bottom, joined by arrows. Top, labeled FASTQ: nine short read bars scattered in no order, a few with a marked base. An arrow reads Map to the reference, then sort and mark duplicates. Middle, labeled BAM: a reference sequence of 27 bases with a C at position 1,042 highlighted. Below it, eight reads are stacked in place. Four of the seven ordinary reads have a marked base at position 1,042, meaning it differs from the reference, and the eighth read, drawn dashed, is labeled Duplicate. An arrow reads Call variants, then filter. Bottom, labeled VCF: a table of four variant calls with columns Position, Ref, Alt, Genotype and Filter. 1,027, G to A, 1/1, PASS. 1,042, C to T, 0/1, PASS, highlighted. 1,115, ATGCA to A, 1/1, PASS. 1,180, A to C, 0/1, LowQual, in lighter text.](../images/5.1-reads-to-variants.svg "An example of going from reads to variants. The reads start in no particular order. Mapping places each one on the reference, and sorting stacks them by position. At position 1,042, about half the reads have T where the reference has C, so the sample carries one copy of each. The genotype column lists the allele on each of the sample's two copies, where 0 is the reference allele and 1 is the alternate allele: 0/1 means heterozygous, and 1/1 means both copies carry the alternate allele. A read marked as a duplicate of another is not counted twice. The calls are written to a VCF, and a call that fails a filter is labeled rather than deleted.")

Along the way the data moves through three file formats: FASTQ for reads, BAM for reads
placed on the reference, and VCF for variant calls. These pages explain just enough of
each to follow along, and [Genomic File
Formats](../06-genomic-file-formats/00-introduction.md) covers them in full.

## Try It Yourself

Each step ends with a Try It section that runs it on HG002's reads. Because the exercise
uses a small piece of one chromosome, it needs only a terminal on macOS or Linux (on
Windows, use the [Windows Subsystem for
Linux](https://learn.microsoft.com/windows/wsl/install)), about 500 MB of disk space and
a few minutes.

## In This Chapter

- [Setting Up](01-setting-up.md): installing the tools and downloading the data for the
  Try It sections.
- [Read Mapping](02-read-mapping.md): finding where in the genome each read came from.
- [Preparing Alignments](03-preparing-alignments.md): sorting, marking duplicates and
  indexing.
- [Calling Variants](04-calling-variants.md): deciding the genotype at each position
  from the reads that cover it.
- [Filtering and Checking Calls](05-filtering-and-checking-calls.md): setting aside
  likely errors, and measuring how well the calls match a truth set.
- [Conclusion](06-conclusion.md): what the pipeline did, and how real analyses go
  further.
