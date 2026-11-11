---
title: Variant Equivalence
description: "Why the same variant can be written in several correct ways, why that breaks comparisons, and how normalization makes descriptions match."
track: Genomic Variation
---

A variant records how a sample differs from the reference, and there's often more than
one correct way to write it. Say the reference reads TCGGTC and the sample reads
TCGAAATC. That could be a G changed to A, followed by an AA insertion. It could be the G
deleted and AAA inserted. Or it could be a single replacement of G with AAA, written in
a [VCF file](../06-genomic-file-formats/04-VCF-files.md) as REF `G`, ALT `AAA`. All
three describe the same physical reality, and two tools can easily pick different ones.

![A reference, T C G G T C, aligned with a sample, T C G A A A T C. Below, the same difference is described three ways, each with the changed bases boxed. In a, the second G becomes A, then two A's are inserted. In b, the G is deleted, then three A's are inserted. In c, the G is replaced by A A A, written as REF G, ALT AAA. A note says the sample sequence is the same every time.](../images/3.11-variant-equivalence.svg "Variant equivalence. The same sample sequence can be described in more than one way. a, a G-to-A substitution followed by an insertion of AA. b, a deletion of G followed by an insertion of AAA. c, a single replacement of G with AAA. All three are correct, and each produces the same sample sequence from the reference.")

## Many Ways to Write One Change

Three situations account for most of the differences:

- **Position in a repeat.** As the
  [Indels](03-insertions-and-deletions.md#describing-and-finding-indels) page showed,
  deleting one CA from TCACACAG gives the same result whichever CA you remove. [VCF
  tools][bcftools-norm] left-align, placing the deletion at the first CA, positions 2–3.
  Variant names written in [HGVS](https://hgvs-nomenclature.org/) nomenclature, widely
  used in clinical reports and papers, do the opposite, assigning the change to [the
  most 3′ position possible][hgvs], here the last CA at positions 6–7. The same deletion
  can sit at two positions in a VCF file and in an HGVS name.
- **Split or merged.** Changes close together can be written as one event or several.
  Inside a codon, that changes the meaning. TTT codes for phenylalanine. Change the
  first base and you get CTT, leucine; change the second and you get TAT, tyrosine.
  Change both on the same copy and you get CAT, histidine, which neither change predicts
  alone. Across gnomAD, [18,756 nearby pairs of variants had a combined effect on the
  protein][mnv] that differed from reading them one at a time. HGVS writes changes less
  than two bases apart as a single replacement, called a delins, while many variant
  callers report them separately.
- **Structural variants.** Breakpoints from short reads are often uncertain by a few
  bases or more, and a deletion can be written out base by base or with a placeholder
  such as `<DEL>` plus an end position. Two calls of the same SV rarely match exactly,
  so they're compared by position, size and sequence within a tolerance. Too loose a
  tolerance merges different SVs; one study found that [over-merging made SVs look up to
  2.2 times as common][truvari] as they were.

![Four codons, each with the amino acid it codes for. The reference T T T codes for Phe. With only the first change, C T T codes for Leu. With only the second change, T A T codes for Tyr. These two rows are bracketed with the note 'Read one at a time'. With both changes on the same copy, C A T codes for His. This last row is emphasized and labeled 'Read together'.](../images/3.12-codon-mnv.svg "Two changes in one codon. On their own, changing the first base of TTT (Phe) gives CTT (Leu), and changing the second gives TAT (Tyr). On the same copy, the two changes make CAT, which codes for His, a result that neither change predicts when read alone.")

## Why It Matters

Differences in how variants are written rarely change the biology, but they break
comparisons:

- **Comparing call sets.** When two callers find the same variant but write it
  differently, a naive comparison counts one false positive and one false negative
  instead of a match. That makes callers look worse than they are and benchmarks
  unreliable.
- **Looking variants up.** Searching [gnomAD or
  ClinVar](01-baselines-for-variation.md#how-common-is-a-variant) with a different
  description of a known variant can come back empty, and a variant already reported as
  harmful can be missed.
- **Combining samples.** The same variant written two ways becomes two rows.
  [Inconsistent representation][tan] magnifies the differences between tools and
  complicates filtering and removing duplicates.

## Making Descriptions Match

No single fix covers every case, so analyses combine a few:

- **Normalization.** Rewrite every record the same way: left-align it, trim bases the
  reference and sample share, and split records listing several alternative alleles into
  one per allele. [Tan and colleagues][tan] defined a normalized variant as one that's
  left-aligned and as short as possible, and tools such as [`bcftools
  norm`][bcftools-norm] and `vt normalize` do this. Normalization fixes the repeat
  problem, but it doesn't merge separate records, so the three descriptions of TCGAAATC
  above still won't match.
- **Comparing sequences.** Benchmarking tools such as `hap.py` and `vcfeval` apply each
  set of variants to the reference and compare the sequences that result. If both
  produce TCGAAATC, they match, however they were written. The [Global Alliance for
  Genomics and Health (GA4GH)][krusche] recommends this approach for benchmarking small
  variants.
- **Computed identifiers.** GA4GH's [Variation Representation Specification][vrs] (VRS)
  gives each variant an identifier computed from the variant itself, so the same variant
  gets the same identifier wherever it's described. To deal with repeats, VRS doesn't
  pick a left or right end. It [expands the variant over the entire region of
  ambiguity][vrsnorm], so the CA deletion above becomes a change to the whole CACACA
  stretch.

## Up Next

Every method in this chapter starts from reads, short stretches of a sample's DNA read
by a sequencer and placed on the reference. [Next-Generation
Sequencing](../04-next-generation-sequencing/00-introduction.md) covers where reads come
from, from collecting a sample to choosing what to sequence and how.

[hgvs]: https://hgvs-nomenclature.org/stable/recommendations/general/
[mnv]: https://doi.org/10.1038/s41467-019-12438-5
[truvari]: https://doi.org/10.1186/s13059-022-02840-6
[bcftools-norm]: https://samtools.github.io/bcftools/bcftools.html#norm
[tan]: https://doi.org/10.1093/bioinformatics/btv112
[krusche]: https://doi.org/10.1038/s41587-019-0054-x
[vrs]: https://doi.org/10.1016/j.xgen.2021.100027
[vrsnorm]: https://vrs.ga4gh.org/en/stable/conventions/normalization.html
