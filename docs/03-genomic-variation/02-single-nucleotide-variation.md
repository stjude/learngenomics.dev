---
title: Single Nucleotide Variation
track: Genomic Variation
---

import ProteinPaint from '@site/src/components/ProteinPaint';

A **single nucleotide variant** (**SNV**) is the smallest change a genome can carry: one
base swapped for another at a single position. Most of the four to five million
differences in a typical genome (see the [Introduction](00-introduction.md)) are SNVs.

![A reference row and a sample row; at one position the reference has A and the sample has C.](../images/3.3-snv.svg "A single nucleotide variant: at one position, the sample has C where the reference genome has A.")

One change like this can have a large effect. In many melanomas, the tumor has a T at
`chr7:140,753,336` (GRCh38) where the reference has an A. That single change, known as
*BRAF* V600E, swaps one amino acid in the BRAF protein and leaves it permanently
switched on, pushing the cell to keep dividing.

## SNVs and SNPs

A **single nucleotide polymorphism** (**SNP**, pronounced "snip") is an SNV that is
common in a population, usually defined as carried by more than 1% of people, though
there is no agreed cutoff. Every SNP is an SNV, but not every SNV is a SNP. In practice
the line blurs: people say "snips" for any SNV, since "SNV" has no easy pronunciation,
and the [dbSNP](https://www.ncbi.nlm.nih.gov/snp/) catalog, despite its name, includes
rare variants and even small insertions and deletions.

In cancer, the more useful split is germline versus somatic. A variant that is common in
the population is almost always inherited, which is why tumor-only analyses use
[frequency databases](01-baselines-for-variation.md#how-common-is-a-variant) to set
common variants aside. Common SNPs can still be important: some raise or lower cancer
risk, and others change how the body handles drugs.

## What an SNV Can Do

The effect of an SNV depends on where it lands. Most fall outside genes, or in parts of
genes that don't encode protein, and have little or no effect. Inside a coding sequence,
the [codon
table](../01-biological-foundations/04-translation.md#decoding-the-transcript) predicts
the result:

- **Synonymous.** The new codon encodes the same amino acid, so the protein is
  unchanged.
- **Missense.** The new codon encodes a different amino acid, as in *BRAF* V600E. A
  **missense variant** can be harmless or severe, depending on which amino acid changes
  and where it sits in the [folded
  protein](../01-biological-foundations/05-protein-folding-and-modification.md).
- **Nonsense.** The new codon is a stop codon, cutting the protein short. A **nonsense
  variant** is what G542X is in *CFTR*.

SNVs outside the coding sequence can also have effects. One at a splice site can make
the cell skip an exon or keep an intron, and one in a regulatory region can change how
much of a gene is made.

## Where Somatic SNVs Come From

Where a somatic SNV lands is largely a matter of chance, but which change it makes often
isn't. Every cell picks up a slow, steady trickle of SNVs from copying errors and
ordinary chemical wear, such as the gradual decay that turns some Cs into Ts, so these
build up with age. Outside sources of damage add their own: ultraviolet light mostly
turns C into T, often two neighboring Cs at once (CC to TT), and tobacco smoke favors C
to A. The mix of SNVs in a tumor therefore records what caused them. These patterns are
called **mutational signatures**, and the [COSMIC signature
catalog](https://cancer.sanger.ac.uk/signatures/) helps analysts match a tumor's pattern
to its likely causes.

:::info Reading a Tumor's History

Because each process leaves its own pattern, software can now work backward from a tumor
to its history. Tools such as
[SigProfiler](https://github.com/AlexandrovLab/SigProfilerExtractor) and
[deconstructSigs](https://doi.org/10.1186/s13059-016-0893-4) sort a tumor's SNVs into 96
categories (six kinds of base change, each split by the bases on either side) and
estimate how much each known signature contributed. The answer can point outside the
body, to sunlight or smoking, or to problems inside the cell. A tumor that can't repair
its DNA properly, for example because of an inherited *BRCA1* variant, leaves a
recognizable signature. Some chemotherapy drugs leave a mark too, which shows up in
tumors that return after treatment. These are statistical estimates, though, and they
need plenty of mutations to work with; a tumor with only a few dozen SNVs gives them
little to go on.

:::

## Linking SNVs to Disease

A tumor can carry anywhere from a handful to hundreds of thousands of somatic SNVs, and
a germline genome carries millions. Each one tells you something, as mutational
signatures show, but in cancer the pressing question is which few actually raise the
risk of the disease or drive its growth.

One approach is statistical. A **genome-wide association study** (**GWAS**) compares
people with a disease (cases) to people without it (controls), looking for variants,
usually common SNPs, that turn up in cases more often than chance would explain. A hit
rarely pinpoints the cause on its own. Nearby variants are inherited together on the
same
[haplotype](../01-biological-foundations/06-genotype-phenotype-haplotype.md#haplotype),
so the SNP that stands out may only mark a region, and the variant that actually causes
the effect may be one of its neighbors. Most common diseases also involve many variants,
each with a small effect. Because GWAS needs thousands of samples, rare diseases are
harder to study this way, but not impossible: in 2009, [two][trevino]
[studies][papaemmanuil] found inherited variants in *ARID5B* and *IKZF1* that raise the
risk of childhood acute lymphoblastic leukemia.

For the somatic SNVs in a single tumor, analysts lean on biology instead. They look
closely at SNVs that change a protein, especially in genes already known to be involved
in cancer, and check every candidate against databases such as
[COSMIC](https://cancer.sanger.ac.uk/cosmic), which catalogs somatic variants found in
tumors. The strongest clue is recurrence: a variant that turns up at the same position
in many tumors, as *BRAF* V600E does, is likely a **driver** that helps the cancer grow.
Most of the rest are **passengers**, changes that came along for the ride.

Recurrence counts outside genes too. In [about 70% of melanomas][huang], and in several
other cancers, one of two SNVs sits in the
[promoter](../01-biological-foundations/03-transcription.md) of *TERT*. Each creates a
new binding site for transcription factors and turns up production of telomerase, an
enzyme that lets cells keep dividing indefinitely. The more common one, at
`chr5:1,295,113` in GRCh38, is known as C228T after its GRCh37 position,
`chr5:1,295,228`, a reminder that coordinates depend on the version. Drivers like these
are easy to miss: exome sequencing and many gene panels read only the coding parts of
genes, so finding them takes whole-genome sequencing or a panel designed to include
them.

Figure 3.4 shows what recurrence looks like in real data. It plots the somatic *BRAF*
variants found in tumors sequenced for the NCI Genomic Data Commons along the length of
the protein.

<ProteinPaint
  number="3.4"
  gene="BRAF"
  dslabel="GDC"
  description="A lollipop plot of the BRAF protein, about 770 amino acids long, drawn as a bar with its domains shaded. Somatic variants from tumors stand above it as circles on stems, sized by how many tumors carry each one. Small circles are scattered along the whole protein, smaller clusters sit at positions 466, 469, 581 and 594, and one circle at position 600, V600E, is far larger than all the others: it is found in several hundred tumors."
>
  Somatic variants in <em>BRAF</em> from tumors in the NCI Genomic Data Commons. Each circle is
  one protein change, sized by the number of tumors that carry it, and its color shows the
  kind of change (blue for missense). V600E dwarfs everything else. Drawn with{" "}
  <a href="https://proteinpaint.stjude.org">ProteinPaint</a> (<a href="https://doi.org/10.1038/ng.3466">Zhou et al., 2016</a>), which
  loads current data, so the counts grow as new tumors are added.
</ProteinPaint>

[trevino]: https://doi.org/10.1038/ng.432
[papaemmanuil]: https://doi.org/10.1038/ng.430
[huang]: https://doi.org/10.1126/science.1229259
