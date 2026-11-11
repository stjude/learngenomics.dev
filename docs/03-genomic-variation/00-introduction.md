---
title: Introduction
---

Every time a cell divides, it copies all of its DNA, about six billion bases. The
copying is remarkably accurate, and repair machinery fixes most of the mistakes that
slip through, but not all of them. The outside world adds more: ultraviolet light and
the chemicals in tobacco smoke can both damage DNA. Any difference in a DNA sequence is
called a **variant**. You have already met two. F508del deletes three bases from *CFTR*,
and G542X changes a single base, turning a codon into a stop.

Where a variant arises decides who inherits it. A variant present in an egg or sperm
cell is passed on to the child and ends up in every cell of their body. These are
**germline** variants, and they are the ones that run in families. A variant that arises
later, in a single cell of the body, is passed only to that cell's descendants and never
to the person's children. These are **somatic** variants. Most cancers are driven by
somatic variants, like the second hit in retinoblastoma we discussed in [Oncogenes and
Tumor Suppressors](../02-cancer-biology/03-oncogenes-and-tumor-suppressors.md#two-hits).

Variants are everywhere. A typical person's genome differs from the standard human
reference (which we define on the next page) at roughly four to five million positions.
Most of these differences have little or no effect. A few are harmful, and fewer still
are helpful. Over many generations, natural selection tends to keep the helpful ones and
weed out the harmful ones, which is how species evolve.

For anyone working with genomic data, finding variants is one of the central jobs.
Comparing a sequenced sample against a reference and listing the differences is called
**variant calling**, and much of the rest of this guide builds toward it. This chapter
covers the kinds of variants you will be looking for:

- [Baselines for Variation](01-baselines-for-variation.md): what a variant is measured
  against.
- [Single Nucleotide Variation](02-single-nucleotide-variation.md): one base swapped for
  another.
- [Insertions and Deletions](03-insertions-and-deletions.md): bases added or removed.
- [Structural Variation](04-structural-variation.md): larger rearrangements, from about
  50 bases up.
- [Copy Number Variation](05-copy-number-variation.md): stretches of DNA, up to whole
  chromosomes, gained or lost.
- [Variant Equivalence](06-variant-equivalence.md): the same change written down in
  different ways.
