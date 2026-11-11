---
title: Oncogenes and Tumor Suppressors
description: "How oncogenes act like a stuck accelerator and tumor suppressors like failed brakes, plus the two-hit model and driver versus passenger mutations."
---

import ProteinPaint from '@site/src/components/ProteinPaint';

The hallmarks come from changes in genes. Many genes help decide when a cell grows and
divides, and a car is a helpful way to picture how they work together. A driver keeps a
car under control with two pedals, pressing the accelerator to speed up and the brake to
slow down. A cell controls its growth in a similar way. Some genes act like the
accelerator, pushing the cell to grow and divide, and others act like the brakes,
holding it back. Cancer can start when the accelerator sticks to the floor or when the
brakes fail. A third group of genes is more like the mechanic who keeps the car in good
shape: losing them doesn't make the car go faster, but faults build up more quickly,
including faults in the accelerator and the brakes.

These three groups are called proto-oncogenes, tumor suppressor genes and DNA repair
genes. The genetic changes that drive cancer tend to affect them ([National Cancer
Institute](https://www.cancer.gov/about-cancer/understanding/what-is-cancer#types-of-genes-that-cause-cancer)).
This page covers each kind of gene, the two-hit model that explains how tumor
suppressors are lost and how researchers tell the changes that drive a tumor from the
ones that only come along for the ride.

## Oncogenes

**Proto-oncogenes** are the accelerator, normal genes that help cells grow and divide.
When one is changed so that its protein is more active than normal, or the cell makes
too much of it, it becomes an **oncogene**, and the cell can grow and survive when it
shouldn't ([National Cancer
Institute](https://www.cancer.gov/about-cancer/understanding/what-is-cancer#types-of-genes-that-cause-cancer)).
The idea came from a virus that causes cancer in birds. Its cancer-causing gene, *src*,
turned out to be a changed copy of a normal gene that the virus had picked up from a
cell it infected ([Berger et al., 2011](https://doi.org/10.1038/nature10275)).

Proto-oncogenes become oncogenes in three main ways ([Berger et al.,
2011](https://doi.org/10.1038/nature10275); [Vogelstein et al.,
2013](https://doi.org/10.1126/science.1235122)). The [Genomic
Variation](../03-genomic-variation/00-introduction.md) chapter shows an example of each.

- **A point mutation** changes the protein so that it stays switched on. *BRAF* V600E,
  in [Single Nucleotide
  Variation](../03-genomic-variation/02-single-nucleotide-variation.md), works this way.
- **Amplification** gives the cell many extra copies of the gene, often 10 to 100, so it
  makes far more of the protein. *ERBB2* in breast cancer is an example, in [Copy Number
  Variation](../03-genomic-variation/05-copy-number-variation.md#copy-number-in-cancer).
- **A chromosome rearrangement** can join part of the gene to part of another gene,
  making a new fusion protein, or move the gene next to DNA that switches it on too
  strongly. In
  [*BCR-ABL1*](../03-genomic-variation/04-structural-variation.md#bcr-abl1), a fusion
  keeps a kinase permanently switched on.

Because the changed protein pushes the cell to grow whatever the other copy of the gene
is doing, a change in one of the two copies is usually enough. Oncogenes are said to act
**dominantly**, and the change is a **gain of function** ([Lee and Muller,
2010](https://doi.org/10.1101/cshperspect.a003236)).

## Tumor Suppressors

**Tumor suppressor genes** are the brakes. Like proto-oncogenes, they help control cell
growth and division ([National Cancer
Institute](https://www.cancer.gov/about-cancer/understanding/what-is-cancer#types-of-genes-that-cause-cancer)),
but they hold it back. A tumor gains from them when they stop working, so the changes
that help a tumor cause a **loss of function**. For most tumor suppressors, one working
copy is enough to do the job, so a cell has to lose both copies before it escapes their
control. Inside the cell, tumor suppressors act **recessively** ([Carbone and Minna,
1993](https://doi.org/10.1146/annurev.me.44.020193.002315)).

There are many ways to lose a copy ([Berger et al.,
2011](https://doi.org/10.1038/nature10275)):

- a
  [nonsense](../03-genomic-variation/02-single-nucleotide-variation.md#what-an-snv-can-do)
  or
  [frameshift](../03-genomic-variation/03-insertions-and-deletions.md#indels-in-genes)
  mutation that cuts the protein short;
- a deletion of the gene, as when a tumor loses both copies of *CDKN2A* ([Copy Number
  Variation](../03-genomic-variation/05-copy-number-variation.md#copy-number-in-cancer));
- copy-neutral [loss of
  heterozygosity](../03-genomic-variation/05-copy-number-variation.md#allele-fractions),
  where the cell loses its working copy and duplicates the broken one;
- chemical marks on the gene's promoter that switch it off without changing its
  sequence. In most colorectal cancers with microsatellite instability that were not
  inherited, the DNA repair gene *MLH1* is switched off this way ([Herman et al.,
  1998](https://doi.org/10.1073/pnas.95.12.6870)).

Not every tumor suppressor follows the two-copy rule. For some, such as *TP53* and
*PTEN*, losing one copy, or even making a little less of the protein, can be enough to
help a tumor ([Berger et al., 2011](https://doi.org/10.1038/nature10275)).

## Two Hits

The need to lose both copies solved a puzzle about inherited cancer. In families that
carry a broken copy of a tumor suppressor, the risk of cancer is passed down as a
dominant trait. Inside the cell, though, the gene acts recessively ([Berger et al.,
2011](https://doi.org/10.1038/nature10275)).

In 1971, Alfred Knudson worked out why by studying retinoblastoma, an eye cancer of
young children. He proposed that the tumor needs two hits ([Knudson,
1971](https://doi.org/10.1073/pnas.68.4.820)). In the heritable form, a child is born
with the first hit in every cell, so one more hit in any cell of the developing retina
is enough. In the nonheritable form, both hits have to happen in the same cell (Figure
2.3). A second hit somewhere in the retina is so likely that almost every child born
with the first hit develops retinoblastoma ([Berger et al.,
2011](https://doi.org/10.1038/nature10275)). These children have an average of three
tumors, which explains why some have tumors in both eyes or several in one eye
([Knudson, 1971](https://doi.org/10.1073/pnas.68.4.820)). They are also diagnosed at a
younger age ([Berger et al., 2011](https://doi.org/10.1038/nature10275)). A tumor in
both eyes, or several in one eye, suggests the heritable form ([National Cancer
Institute](https://www.cancer.gov/types/retinoblastoma/hp/retinoblastoma-treatment-pdq#_sm_CDR0000779398_6)).

![Two panels, each showing a row of ten cells at birth and again later. Each cell holds two copies of a gene, drawn as bars, and a broken copy has a gap. In the nonheritable panel, every cell starts with two working copies; later, two cells have one broken copy and a single cell has two, which can start a tumor. In the heritable panel, every cell starts with one broken copy; later, three cells have a second broken copy, and each can start a tumor.](../images/2.3-two-hits.svg "The two-hit model. In nonheritable retinoblastoma, both copies of the gene have to be broken in the same cell, which is rare. In heritable retinoblastoma, every cell starts with one broken copy, so a single further hit in any cell can start a tumor, and several cells often take that hit. Based on Knudson (1971).")

The gene was later found to be *RB1*. When researchers compared tumors with normal cells
from the same children, the tumor cells had lost the working copy and kept only the
broken one, often through losing a chromosome or through recombination ([Cavenee et al.,
1983](https://doi.org/10.1038/305779a0)). When the remaining chromosome is copied, or
the change comes from recombination, the cell still has two copies of the gene. This is
the copy-neutral loss of heterozygosity that shows up in [allele
fractions](../03-genomic-variation/05-copy-number-variation.md#allele-fractions).

A child with heritable retinoblastoma may have inherited the broken copy from a parent,
or it may have arisen new in a sperm or egg cell or early in development ([National
Cancer
Institute](https://www.cancer.gov/types/retinoblastoma/hp/retinoblastoma-treatment-pdq#_sm_CDR0000779398_6)).
Either way, the two-hit model explains why inheriting one broken copy of an important
gene can create a predisposition to cancer without causing it directly. [Inherited
Risk](06-inherited-risk.md) returns to this idea.

## Genes That Guard the Genome

DNA repair genes fix damaged DNA. Cells with mutations in these genes tend to pick up
more mutations and chromosome changes ([National Cancer
Institute](https://www.cancer.gov/about-cancer/understanding/what-is-cancer#types-of-genes-that-cause-cancer)).
Losing them doesn't make a cell grow on its own. It speeds up the changes in other genes
that do.

- **Mismatch repair** genes, such as *MLH1* and *MSH2*, fix mistakes made when DNA is
  copied. Tumors that have lost mismatch repair can carry thousands of mutations, and
  the [microsatellite
  instability](../03-genomic-variation/03-insertions-and-deletions.md#where-indels-happen)
  they cause shows up clearly in sequencing data.
- **Checkpoint** genes, such as *TP53* and *ATM*, help the body get rid of cells whose
  DNA is damaged. When they are lost, damaged cells survive and keep dividing, including
  cells that carry large changes, such as a translocation or an extra chromosome.

[Inherited Risk](06-inherited-risk.md) covers what happens when a child is born with a
broken copy of one of these genes.

## Drivers and Passengers

Only a few of a tumor's mutations help it grow. In common solid tumors, such as those of
the colon, breast, brain and pancreas, an average of 33 to 66 genes carry mutations that
would be expected to change their proteins. A typical tumor has only two to eight
**driver** mutations, and the rest are passengers. [Single Nucleotide
Variation](../03-genomic-variation/02-single-nucleotide-variation.md#linking-snvs-to-disease)
shows how a mutation that recurs across many tumors points to a driver.

Where the mutations fall in a gene also shows which kind of driver it is. Oncogenes are
mutated again and again at the same few positions, because only certain changes switch
the protein on. Tumor suppressors are often hit by changes that cut the protein short,
spread along much of the gene, because a break in many different places can switch it
off. Vogelstein and colleagues turned this into the **20/20 rule**. A gene counts as an
oncogene if more than 20% of its recorded mutations are missense changes at recurring
positions, and as a tumor suppressor if more than 20% inactivate it. In 2013, 125 genes
met the rule, 54 oncogenes and 71 tumor suppressors.

Figure 2.4 shows the oncogene pattern in real tumors. It plots the mutations in *KRAS*
found in tumors sequenced for the NCI Genomic Data Commons, drawn the same way as the
*BRAF* plot in [Figure
3.4](../03-genomic-variation/02-single-nucleotide-variation.md#figure-3-4). The bar
along the bottom is the KRAS protein, from its first amino acid on the left to its last
on the right. Each circle above it is one protein change, and the number inside is how
many tumors carry it. The labels follow the same naming as *BRAF* V600E, so G12D means
that the glycine (G) at position 12 has become an aspartic acid (D).

Most of the large circles sit at just three positions, amino acids 12, 13 and 61, and
the most common changes there are each found in hundreds of tumors. These are the
positions where changes switch on *KRAS* and the two closely related RAS genes, and
*KRAS* is the most often mutated of the three ([Prior et al.,
2012](https://doi.org/10.1158/0008-5472.CAN-11-2612)). The rest of the protein carries
smaller circles, most of them found in only a few tumors.

<ProteinPaint
  number="2.4"
  gene="KRAS"
  dslabel="GDC"
  description="A lollipop plot of the KRAS protein, about 190 amino acids long, drawn as a bar with its domains shaded. Somatic variants from tumors stand above it as circles on stems, sized and numbered by how many tumors carry each one. Tall stacks of large circles sit at positions 12, 13 and 61, and the largest, G12D, G12V and G12C, are each found in hundreds of tumors. Small circles, each found in only a few tumors, are scattered along the rest of the protein."
>
  Somatic variants in <em>KRAS</em> from tumors in the NCI Genomic Data Commons. Each circle is
  one protein change, labeled with its name and sized by the number of tumors that carry it.
  Most of the recurrent changes fall at amino acids 12, 13 and 61. Drawn with{" "}
  <a href="https://proteinpaint.stjude.org">ProteinPaint</a> (<a href="https://doi.org/10.1038/ng.3466">Zhou et al., 2016</a>), which
  loads current data, so the counts grow as new tumors are added.
</ProteinPaint>

The pattern can overturn a first guess. *IDH1* was first thought to be a tumor
suppressor, but nearly all of its mutations change the same amino acid, at position 132,
which marked it as an oncogene.

The pattern is a strong clue rather than a rule, and *TP53* shows why (Figure 2.5). It
is a tumor suppressor, but about 90% of its mutations are missense changes. They fall at
about 190 positions in the part of the protein that binds DNA, and just eight changes,
at six of those positions, account for about 28% of all its mutations. These changes
weaken the protein's hold on DNA, so they switch off its normal job rather than
switching it on. Some of the changed proteins may also gain new activities that help the
tumor ([Baugh et al., 2018](https://doi.org/10.1038/cdd.2017.180)).

<ProteinPaint
  number="2.5"
  gene="TP53"
  dslabel="GDC"
  description="A lollipop plot of the TP53 protein, about 390 amino acids long, drawn as a bar with its domains shaded. Somatic variants from tumors stand above it as circles on stems, sized and numbered by how many tumors carry each one. Most circles are missense changes packed into the middle of the protein, the part that binds DNA, and a handful of positions there are found in far more tumors than the rest. Smaller circles for changes that cut the protein short are scattered along its length."
>
  Somatic variants in <em>TP53</em> from tumors in the NCI Genomic Data Commons. Each circle is
  one protein change, labeled with its name and sized by the number of tumors that carry it.
  Unlike most tumor suppressors, <em>TP53</em> is hit mostly by missense changes, and a few
  positions recur in many tumors. Drawn with{" "}
  <a href="https://proteinpaint.stjude.org">ProteinPaint</a> (<a href="https://doi.org/10.1038/ng.3466">Zhou et al., 2016</a>), which
  loads current data, so the counts grow as new tumors are added.
</ProteinPaint>

## Up Next

Driver genes don't act alone. Their proteins work in a small number of pathways that
control whether a cell divides, whether it survives and how it maintains its genome.
[Signaling Pathways](04-signaling-pathways.md) follows some of the most important.
