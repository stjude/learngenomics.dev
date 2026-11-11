---
title: Conclusion
---

You have now followed one sample from raw reads to a checked list of variants. Each step
turned one kind of file into the next:

- [Read Mapping](02-read-mapping.md) placed each read from the FASTQ files on the
  reference genome.
- [Preparing Alignments](03-preparing-alignments.md) sorted the alignments by position,
  flagged duplicates and indexed the BAM file.
- [Calling Variants](04-calling-variants.md) weighed the reads at each position, decided
  the genotype and wrote the calls to a VCF.
- [Filtering and Checking Calls](05-filtering-and-checking-calls.md) labeled the calls
  most likely to be wrong, then measured how accurate the rest were against HG002's
  truth set.

The calls matched most of HG002's known variants in the region you used, and most of the
errors were indels in runs of one repeated base or in short repeated patterns.

## Going Further

The pipeline in this chapter is deliberately simple. A real analysis follows the same
steps but differs in a few ways:

- **More data.** The same commands work on a whole genome, but take far more disk space
  and time than one region of one chromosome.
- **Other callers.** [Calling Variants](04-calling-variants.md) described callers with
  more detailed models, such as `HaplotypeCaller` and DeepVariant, and joint calling for
  groups of samples.
- **Other kinds of variants.** [Structural
  variants](../03-genomic-variation/04-structural-variation.md), [copy number
  variants](../03-genomic-variation/05-copy-number-variation.md) and the [somatic
  variants](../03-genomic-variation/01-baselines-for-variation.md#a-second-baseline-the-persons-own-dna)
  found in tumors each need their own tools and methods.
- **No truth set.** Your own samples won't have a list of known variants to check
  against. Running a pipeline on a reference sample such as HG002 first tells you how
  far to trust its calls on samples you can't check.

The next chapter covers the file formats used here in full: [Genomic File
Formats](../06-genomic-file-formats/00-introduction.md).
