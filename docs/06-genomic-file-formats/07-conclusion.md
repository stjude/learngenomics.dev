---
title: Conclusion
---

You can now read the formats that carry most genomic data, and you've worked with each
of them yourself. Together they follow an analysis from start to finish:

- [FASTQ Files](02-FASTQ-files.md) hold the reads as they come off the sequencer.
- [SAM/BAM/CRAM Files](03-BAM-files.md) place those reads on the reference genome.
- [VCF/BCF Files](04-VCF-files.md) list the variants called from them.
- [BED Files](05-BED-files.md) mark regions of the genome, such as the ones an analysis
  should cover.
- [GTF/GFF3 Files](06-GTF-GFF3-files.md) describe where the genes are and how each one
  is built.

[Compression and BGZF](01-compression-and-BGZF.md) runs underneath almost all of them. A
file that is sorted, compressed with BGZF and indexed lets a tool jump straight to one
region, however large the file.

## Keep Practicing

[Sandbox.bio](https://sandbox.bio/tutorials) runs real bioinformatics tools in your
browser, and its tutorials pick up where this chapter leaves off.

For FASTQ files, [Wrangle FASTA and FASTQ with
SeqKit](https://sandbox.bio/tutorials/seqkit-intro) summarizes, subsamples, filters and
searches reads with `seqkit`. [DNA Sequencing
QC](https://sandbox.bio/tutorials/fastp-intro) checks the quality of a paired-end run,
then trims and filters the reads, with `fastp`.

For SAM and BAM files, [BAM Parsing with
samtools](https://sandbox.bio/tutorials/samtools-intro) converts SAM to BAM, sorts and
indexes it, reads the header and uses the FLAG to pick out alignments.

For VCF files, [Sequence Alignment with
bowtie2](https://sandbox.bio/tutorials/bowtie2-intro) maps reads and, in its last step,
calls variants with `bcftools mpileup` and `bcftools call`. The [IGV
tutorial](https://sandbox.bio/tutorials/igv-intro) loads read alignments into the IGV
genome browser and shows how to tell real variants from artifacts.

For BED files, the [bedtools tutorial](https://sandbox.bio/tutorials/bedtools-intro)
uses `bedtools` on real BED files to find overlaps, merge nearby regions, find the gaps
between regions and measure coverage.

## What's Next

That's the end of the main text. Congratulations on making it this far! You started with
what a cell is, and you can now take a sample's reads all the way to its variants and
read every file along the way.

If you'd like to keep going, Advanced Topics gathers standalone pages on subjects such
as [alternative splicing](../07-advanced-topics/alternative-splicing.md), [epigenetic
modifications](../07-advanced-topics/epigenetic-modifications.md) and [the structure of
DNA](../07-advanced-topics/dna-structure.md). Read them in any order, whenever one
interests you.

Thanks for reading!
