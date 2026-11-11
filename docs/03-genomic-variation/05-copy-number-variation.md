---
title: Copy Number Variation
description: "Copy number variation: gains and losses of DNA in health, disease and cancer, and how copy number changes are found in sequencing data."
track: Genomic Variation
---

Most of the genome comes in two copies, one from each parent, so the usual **copy
number** is two. The exceptions are X and Y in males, which are present once each.
**Copy number variants** (CNVs) are stretches of DNA present in more or fewer copies
than that. They're the unbalanced [structural variants](04-structural-variation.md),
deletions and duplications, counted by how many copies are left, and they range from
part of a gene to a whole chromosome.

## Copy Number in Health and Disease

Everyone carries CNVs. Compared with the reference, a typical genome has [about 1,000
large deletions and 160 other copy number variants][1000g], and most do no harm. Some
are even useful. *AMY1* makes amylase, the enzyme in saliva that starts breaking down
starch, and the number of copies varies from person to person. People with more copies
make more amylase, and [people from populations with high-starch diets carry more copies
on average][perry].

Other CNVs cause disease. The largest are gains or losses of a whole chromosome or
chromosome arm, called **aneuploidy**. In Down syndrome, people carry three copies of
chromosome 21 instead of two. Smaller CNVs can have effects just as large. The 22q11.2
deletion removes [about 3 million bases][mcdonald] from one copy of chromosome 22. It
turns up in about 1 in 3,000 to 1 in 6,000 births, and its effects range from heart
defects and a weak immune system to learning difficulties and psychiatric illness.

## Copy Number in Cancer

Cancer cells gain and lose DNA far more than normal cells. In more than 10,000 tumors,
[88% had at least one whole-chromosome or arm-level change][taylor], and in [37% of
tumors][zack] the entire genome had been doubled. Smaller, focused changes pick out
particular genes:

- **Amplification.** A region holding an
  [oncogene](../02-cancer-biology/03-oncogenes-and-tumor-suppressors.md), a gene that
  pushes cells to grow, is copied many times over. In breast cancer, *ERBB2* (also
  called *HER2*) can be amplified [from twice to more than 20 times its usual copy
  number][slamon1987], and tumors that carry the amplification tend to come back sooner.
  It also became a target for drug development: in a trial, patients whose tumors made
  too much HER2 [lived longer][slamon2001] when an antibody that binds the HER2 protein
  was added to chemotherapy. In neuroblastoma, a childhood cancer of developing nerve
  cells, *MYCN* amplification [goes with more advanced disease][brodeur].
- **Homozygous deletion.** Both copies of a gene are lost, so none of its protein is
  made. It's one way to switch off a [tumor
  suppressor](../02-cancer-biology/03-oncogenes-and-tumor-suppressors.md#two-hits), a
  gene that holds cell growth in check. *CDKN2A*, which makes a brake on cell division,
  is [often lost this way][zack], in [many kinds of cancer][kamb].

## Finding Copy Number Changes

### Read Depth

The main signal is read depth. A region present in three copies instead of two gives
about 1.5 times as many reads, and a region with one copy gives about half as many.
Turning that into copy number takes a few steps:

1. **Count.** Split the genome into bins, often thousands of bases long, and count the
   reads in each. The depth at a single base is too noisy to use on its own.
2. **Correct.** Remove known biases. Regions unusually rich or poor in G and C are
   sequenced less evenly, reads from repeats can't be placed confidently, and duplicate
   reads from the same DNA fragment inflate the counts.
3. **Compare.** Divide each bin by a baseline: the [matched
   normal](01-baselines-for-variation.md#a-second-baseline-the-persons-own-dna) for a
   tumor, or a panel of normal samples sequenced the same way. This cancels the biases
   the corrections missed. Exome and targeted sequencing, which cover the genome
   unevenly, rely on this step most.
4. **Segment.** Join neighboring bins with similar ratios into segments, each with a
   single copy number.

![A reference of six segments, A to F, above a sample's two copies: copy 1 reads A B B C D E F and copy 2 reads A B C D F. Below, short reads are stacked over the reference positions; the stack is taller over B, marked 1.5 times, and shorter over E, marked half. At the bottom, a log2 ratio plot shows bins as dots and segments as lines: at 0, two copies, for A, C, D and F; at about +0.58, three copies, in red over B; and at −1, one copy, in blue over E.](../images/3.9-copy-number-variation.svg "Copy number variation. Top: a sample's two copies of a stretch of DNA. Copy 1 has an extra B and copy 2 has lost E, so B is present three times, E once and everything else twice. Middle: reads from both copies map back to the reference, so the stack of reads is about 1.5 times as tall over B and half as tall over E. Bottom: each bin's log2 ratio against the baseline, with segments at 0 for two copies, about +0.58 for three and −1 for one.")

Ratios are usually reported on a log2 scale, so a bin matching the baseline scores 0.
One copy where two are expected scores −1, three copies about 0.58 and four copies 1.

Depth gives a CNV's size and copy number, but its edges are only as sharp as the bins.
Split reads and discordant read pairs ([Finding Structural
Variants](04-structural-variation.md#finding-structural-variants)) pin down the exact
breakpoints and show where the extra copies went.

### Allele Fractions

The second signal comes from
[heterozygous](../01-biological-foundations/06-genotype-phenotype-haplotype.md#genotype)
sites, where the two copies carry different bases. The share of reads showing one of
them is its **allele fraction**, and normally it's about half. If one copy is
duplicated, there are three copies, two of one base and one of the other, so the
fractions shift to about two-thirds and one-third. If one copy is lost, every read shows
the base that's left.

Allele fractions also catch a change depth can't see. In **copy-neutral loss of
heterozygosity** (LOH), a cell loses one copy of a region and copies the other, so it
still has two copies, but they're identical. Depth looks normal, yet every heterozygous
site in the region now reads as homozygous. In cancer, this is a common way to lose the
last working copy of a tumor suppressor, the second of the [two
hits](../02-cancer-biology/03-oncogenes-and-tumor-suppressors.md#two-hits).

![Two plots share four regions of a chromosome: normal (genotype A/B), gain (A/A/B), loss (A with the other copy missing) and copy-neutral LOH (A/A). In the depth plot, the log2 ratio is 0 in the normal region, about +0.58 in the gain, −1 in the loss and back to 0 in the copy-neutral LOH region. In the allele fraction plot, heterozygous sites cluster at 0.5 in the normal region, form two bands near one-third and two-thirds in the gain, and sit at 0 and 1 in both the loss and the copy-neutral LOH regions. The copy-neutral LOH region is highlighted with a note: depth normal, allele fractions split.](../images/3.10-copy-number-signals.svg "Copy number signals. Four regions of a chromosome, each with the genotype at one site that is heterozygous (A/B) in normal cells. Top: depth, as a log2 ratio, is 0 for two copies, about +0.58 for a gain and −1 for a loss. Bottom: allele fractions at heterozygous sites sit near 0.5 with two different copies, split to about one-third and two-thirds with a gain, and move to 0 and 1 with a loss. In copy-neutral LOH, depth stays normal but allele fractions move to 0 and 1, so only allele fractions reveal it.")

### Tumors Complicate Things

A tumor sample is never pure. Normal cells mixed in pull every signal toward normal: in
a sample that's half tumor, losing one copy lowers depth to 75%, not 50%. The share of
tumor cells in the sample is its **purity**. Whole-genome doubling shifts the baseline,
too. A doubled tumor has about four copies of most regions, so its most common depth
stands for four copies, not two. The tumor's average copy number is its **ploidy**. Copy
number tools estimate purity and ploidy together, using depth and allele fractions at
once.

[1000g]: https://doi.org/10.1038/nature15393
[perry]: https://doi.org/10.1038/ng2123
[mcdonald]: https://doi.org/10.1038/nrdp.2015.71
[taylor]: https://doi.org/10.1016/j.ccell.2018.03.007
[zack]: https://doi.org/10.1038/ng.2760
[slamon1987]: https://doi.org/10.1126/science.3798106
[slamon2001]: https://doi.org/10.1056/NEJM200103153441101
[brodeur]: https://doi.org/10.1126/science.6719137
[kamb]: https://doi.org/10.1126/science.8153634
