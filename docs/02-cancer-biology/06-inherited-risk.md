---
title: Inherited Risk
description: "How inherited germline variants raise cancer risk, well-known predisposition syndromes, predisposition in childhood cancer, and how to find it in data."
---

Most of the mutations behind a cancer arise during a person's lifetime, in the cells
that become the tumor. Some people, though, start life with a germline variant that
raises their risk of cancer. A variant passed down in an egg or sperm is in every cell
of the body. One that arises after fertilization is passed only to the cells that
descend from the cell where it arose. Having cells with different genomes in one body is
called **mosaicism**, and it can start in the first days of development or later
([National Human Genome Research
Institute](https://www.genome.gov/genetics-glossary/Mosaicism)). About 5–10% of all
cancers are thought to be caused by harmful variants inherited from a parent ([National
Cancer
Institute](https://www.cancer.gov/about-cancer/causes-prevention/genetics/genetic-testing-fact-sheet)).

Such a variant creates a **predisposition** to cancer. It raises the odds, and some
carriers never develop cancer at all. How likely a carrier is to develop the disease is
the variant's **penetrance**, and it differs widely from gene to gene.

## The Second Hit

Most of the genes behind inherited risk are tumor suppressors. As [Two
Hits](03-oncogenes-and-tumor-suppressors.md#two-hits) explained, many tumor suppressors
stop holding a cell back only when both copies are lost. A person who inherits one
broken copy starts with every cell one step along, and a tumor often begins when one of
those cells loses the working copy. In tumors from 10,389 adults with 33 kinds of
cancer, 8% of patients carried a germline variant that predisposed them to cancer. In
tumor suppressors, 43% of these variants showed signs of a second hit in the tumor,
usually loss of the working copy. A smaller number were in oncogenes such as *MET* and
*RET*, and these genes tended to be more highly expressed ([Huang et al.,
2018](https://doi.org/10.1016/j.cell.2018.03.039)).

The second hit leaves a mark in sequencing data. In a normal sample from a carrier, each
cell has two copies of the gene, one with the variant and one that works. Reads come
from both copies about equally, so roughly half of the reads at that position show the
variant. The share wobbles a little above or below 50% by chance, and it can be well
below 50% when the variant is mosaic. One way a tumor loses the working copy is
[copy-neutral loss of
heterozygosity](../03-genomic-variation/05-copy-number-variation.md#allele-fractions),
which replaces it with a second copy of the broken one. Every read from a tumor cell
then shows the variant, and in a sample that is 60% tumor, about 80% of all reads do
(Figure 2.10).

![Two rows of ten cells, each cell holding two copies of a gene. In the normal sample, every cell has one working copy and one copy with an inherited variant, and a bar below shows 10 of 20 copies, or about 50% of reads, carrying the variant. In the tumor sample, six of the ten cells are tumor cells with two copies of the variant and no working copy, and four are normal cells like those above. The bar below shows 16 of 20 copies, or about 80% of reads, carrying the variant.](../images/2.10-germline-second-hit.svg "An inherited variant in normal and tumor samples. Every cell in the body carries the variant on one copy, so about half of the reads from a normal sample show it. Here the tumor cells have lost the working copy and copied the one with the variant in its place. In a sample that is 60% tumor, about 80% of the reads show the variant. The data are made up.")

## Well-Known Syndromes

A predisposition that runs in families and follows a recognizable pattern is called a
hereditary cancer syndrome. A few are especially well studied. In most of them, a person
is born with one broken copy of a gene in every cell, and the other copy still works.
Constitutional mismatch repair deficiency is the exception, because it starts with two
broken copies.

- **Li-Fraumeni syndrome** (*TP53*). Carriers develop many kinds of cancer, often young,
  including breast cancer, sarcomas and brain tumors. In 286 carriers, half of the women
  had developed cancer by age 31 and half of the men by 46, and nearly all by age 70.
  About half of those who had one cancer went on to develop another ([Mai et al.,
  2016](https://doi.org/10.1002/cncr.30248)).
- **Hereditary breast and ovarian cancer** (*BRCA1* and *BRCA2*). Among nearly 10,000
  women who carried a variant in one of these genes, the risk of breast cancer by age 80
  was 72% for *BRCA1* and 69% for *BRCA2*. The risk of ovarian cancer was 44% and 17%
  ([Kuchenbaecker et al., 2017](https://doi.org/10.1001/jama.2017.7112)).
- **Lynch syndrome** (*MLH1*, *MSH2*, *MSH6* and *PMS2*). These are [mismatch
  repair](03-oncogenes-and-tumor-suppressors.md#genes-that-guard-the-genome) genes, and
  about 1 in 279 people carries a harmful variant in one of them ([Win et al.,
  2017](https://doi.org/10.1158/1055-9965.EPI-16-0693)). The risk depends on the gene.
  Carriers of *MLH1* and *MSH2* variants have high risks of colorectal, endometrial and
  ovarian cancer, *MSH6* variants mainly raise the risk of endometrial cancer, and a
  large study found no clear rise in risk for *PMS2* ([Dominguez-Valentin et al.,
  2020](https://doi.org/10.1038/s41436-019-0596-9)).
- **Constitutional mismatch repair deficiency.** A child who inherits a broken copy of
  the same mismatch repair gene from both parents has no working copy in any cell.
  Cancers start in childhood, mainly in the blood, the brain and the intestines ([Wimmer
  et al., 2014](https://doi.org/10.1136/jmedgenet-2014-102284)).
- **Heritable retinoblastoma** (*RB1*). This is the case that led to the [two-hit
  model](03-oncogenes-and-tumor-suppressors.md#two-hits). About 25–30% of
  retinoblastomas are heritable, but only about a quarter of these children have a
  parent who had the disease. In the rest, the *RB1* variant arose new, in a sperm or
  egg cell or early in development ([National Cancer
  Institute](https://www.cancer.gov/types/retinoblastoma/hp/retinoblastoma-treatment-pdq)).
  Because every cell carries the broken copy, the risk doesn't end with the eye. Among
  1,128 survivors of heritable retinoblastoma, 33.1% had developed another cancer within
  50 years, with especially high risks of sarcomas and raised risks of melanoma and
  breast cancer. Survivors of the nonheritable form showed no rise in risk ([Schonfeld
  et al., 2021](https://doi.org/10.1038/s41416-020-01248-y)). In one study of survivors
  of the heritable form, those who'd had radiation treatment for the eye tumor had about
  three times the risk of these later cancers ([Kleinerman et al.,
  2005](https://doi.org/10.1200/JCO.2005.05.054)).

## Predisposition in Childhood Cancer

In children with cancer, these variants are more common than once thought. When the
genomes or exomes of 1,120 children and adolescents with cancer were sequenced, 8.5%
carried a germline variant judged harmful in a predisposition gene, compared with 1.1%
of people without known cancer. *TP53* was by far the most common, in 50 patients,
followed by *APC*, *BRCA2*, *NF1*, *PMS2*, *RB1* and *RUNX1*. Of the 58 carriers whose
family history was known, only 23 (40%) had relatives with cancer ([Zhang et al.,
2015](https://doi.org/10.1056/NEJMoa1508054)). A later study found more. In 309 children
sequenced at diagnosis or relapse, 18% carried a variant that predisposed them to
cancer, and the tumor data suggested a role in the tumor for 55% of the harmful germline
variants ([Newman et al., 2021](https://doi.org/10.1158/2159-8290.CD-20-1631)).

Why would most of these children have no relatives with cancer? The variant's penetrance
may be low, or the variant may be new. Among 336 people with Li-Fraumeni syndrome, at
least 14% of the *TP53* variants had arisen new in the person, and the authors estimate
that about a fifth of these arose during embryonic development, leaving a mosaic variant
carried by only some of the body's cells ([Renaux-Petel et al.,
2018](https://doi.org/10.1136/jmedgenet-2017-104976)).

## Common Variants, Small Effects

The variants above are rare, and many of them raise risk sharply. Inherited risk also
comes from many common variants that each raise it a little. These are found by
[genome-wide association
studies](../03-genomic-variation/02-single-nucleotide-variation.md#linking-snvs-to-disease),
and their small effects can be added up into a **polygenic risk score**. A score built
from 313 variants, using data from women of European ancestry, gave the 1% of women with
the highest scores an estimated lifetime risk of breast cancer of 32.6% ([Mavaddat et
al., 2019](https://doi.org/10.1016/j.ajhg.2018.11.002)).

## Finding Them in the Data

An inherited variant shows up in a tumor's data, where it can look like a change that
arose in the tumor. The clearest way to tell the two apart is to sequence a [matched
normal](../03-genomic-variation/01-baselines-for-variation.md#a-second-baseline-the-persons-own-dna)
alongside the tumor. In 815 patients with 15 kinds of cancer, the matched normal
revealed germline variants in predisposition genes in 3% of patients whose cancers
showed no sign of being inherited. Without it, the analysis couldn't tell for certain
which changes in these genes were inherited, and it added false findings that made up
31% of the changes in a targeted panel and 65% in exomes ([Jones et al.,
2015](https://doi.org/10.1126/scitranslmed.aaa7161)).

An inherited variant can be relevant to a patient's cancer, and their relatives may
carry it too. Studies have compared testing every patient with testing only those whose
cancer or family history points to an inherited cause. Among 2,984 adults with cancer
who were all tested, whatever their cancer type, age or family history, 13.3% carried a
harmful germline variant. In 6.4%, the variant wouldn't have been found under the usual
criteria for deciding who to test ([Samadder et al.,
2021](https://doi.org/10.1001/jamaoncol.2020.6252)).

Researchers have also followed carriers over time. In a study of 89 carriers from
families with Li-Fraumeni syndrome, 59 had regular scans and tests at some point, which
found 40 tumors in 19 of them before the tumors caused symptoms ([Villani et al.,
2016](https://doi.org/10.1016/S1470-2045(16)30249-2)).

## Up Next

This chapter followed cancer from the genes that drive it to the ways a tumor changes as
it grows. The rest of this guide is about finding those changes in data. [Genomic
Variation](../03-genomic-variation/00-introduction.md) starts with the kinds of variants
you'll find and the baselines they're measured against.
