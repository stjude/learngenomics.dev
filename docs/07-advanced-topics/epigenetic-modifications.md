---
title: Epigenetic Modifications
description: "Epigenetic marks: DNA methylation and histone modifications, how they hold gene activity in place, how they are measured, and their role in cancer."
track: Advanced Topics
sidebar_position: 2
---

Nearly every cell in your body carries the same genome, yet a neuron and a white blood
cell look and behave nothing alike. What differs is which genes each cell uses. Part of
what holds those choices in place is a layer of chemical marks on the DNA and on the
histones it wraps around. Epigenetics is the study of changes in gene activity that can
be passed on when a cell divides but can't be explained by changes in the DNA sequence
([Bird, 2002](https://doi.org/10.1101/gad.947102)). This guide covers the two
best-studied kinds of marks, how they're measured and what happens to them in cancer.

## DNA Methylation

The most common mark on human DNA is a **methyl group**, one carbon atom with three
hydrogens (CH3), attached to carbon 5 of a cytosine. The result is called
**5-methylcytosine** ([Moore et al., 2013](https://doi.org/10.1038/npp.2012.112)). In
most human cells it's found almost only at **CpG sites**, where a C is followed by a G
on the same strand; the "p" stands for the phosphate that links them. CG read 5′ to 3′
is its own [reverse complement](dna-structure.md#reading-the-other-strand), so the other
strand has a CpG at the same spot, and the two cytosines sit diagonally across from each
other ([Figure 7.3](#figure-7-3)). In human body cells, 70% to 80% of all CpG sites are
methylated, as Bird's review notes.

![Two stacked DNA base pairs drawn atom by atom, on two strands that run in opposite directions. The left strand reads from its 5′ end at the top to its 3′ end at the bottom: 5-methylcytosine above guanine. The right strand runs the other way: guanine on top paired with the upper 5-methylcytosine, and 5-methylcytosine at the bottom paired with the lower guanine. Each 5-methylcytosine carries a CH3 group, highlighted as the methyl group, on carbon 5 of the cytosine ring, on the side away from the hydrogen bonds. Each pair is held together by three dotted hydrogen bonds. Phosphates and deoxyribose sugars form the backbone of each strand.](../images/7.3-methylated-cpg.svg "A methylated CpG site. Both strands read 5′-CG-3′, so their two cytosines sit diagonally across from each other, and each carries a methyl group on carbon 5. The methyl group points away from the hydrogen bonds, so each 5-methylcytosine pairs with guanine through the same three bonds as an ordinary C⁠–⁠G pair.")

CpG sites are scarce across most of the genome but cluster in stretches about 1,000
bases long called **CpG islands**, which normally stay unmethylated ([Deaton and Bird,
2011](https://doi.org/10.1101/gad.2037511)). About 70% of gene
[promoters](../01-biological-foundations/03-transcription.md#genomic-regions-and-transcription)
sit in a CpG island ([Saxonov et al., 2006](https://doi.org/10.1073/pnas.0510310103)).
Dense methylation of a promoter's island helps lock the gene in a silent state. Bird's
review names two places where cells do this on purpose during development: the inactive
X chromosome in females, and imprinted genes, where only the copy inherited from one
parent is used.

### Copying the Marks

When a cell divides, its methylation is copied along with its DNA, so the marks outlast
the cell that made them ([Figure 7.4](#figure-7-4)). A new strand is built from plain
cytosines, so right after copying, each CpG that was methylated on both strands now
carries a methyl group on the old strand only, a state called **hemimethylated**. A
protein called UHRF1 binds these half-marked sites ([Bostick et al.,
2007](https://doi.org/10.1126/science.1147939)), and the enzyme **DNMT1** adds a methyl
group to the new strand's C wherever the old strand has one. The copying isn't perfect,
so now and then a site loses its mark.

![Three rows, each showing DNA as pairs of horizontal strands with cytosines at three CpG sites drawn as small circles on stems. Row 1, both strands carry the marks: one duplex of two old strands, with every circle filled to show a methylated cytosine. Row 2, copying makes two half-marked duplexes: each duplex has one old strand with filled circles and one new strand with open circles, unmethylated. Row 3, DNMT1 marks the new strands to match: the same two duplexes, now with every circle filled. A key identifies filled circles as methylated cytosine, open circles as unmethylated cytosine, and the two strand shades as old strand and new strand.](../images/7.4-methylation-copying.svg "How methylation is copied when a cell divides. Copying pairs each old strand with a new strand that has no methyl groups, leaving two hemimethylated duplexes. DNMT1 then methylates each new strand opposite the old strand's marks, so both copies match the original.")

Other enzymes change the pattern. DNMT3A and DNMT3B add methyl groups to sites that had
none ([Okano et al., 1999](https://doi.org/10.1016/s0092-8674(00)81656-6)). TET enzymes
start the work of removing marks by converting 5-methylcytosine to
**5-hydroxymethylcytosine** ([Tahiliani et al.,
2009](https://doi.org/10.1126/science.1170116)).

## Histone Modifications

[Histones](../01-biological-foundations/01-cells-genomes-dna-chromosomes.md#how-dna-is-packaged)
are the proteins DNA wraps around. Each nucleosome is a core of eight histones with 145
to 147 base pairs of DNA wound around it, and flexible **tails**, 15 to 36 amino acids
long, stick out from it ([McGinty and Tan, 2015](https://doi.org/10.1021/cr500373h)).
Enzymes attach small chemical groups to particular amino acids in these tails, most
often lysines.

This page covers two kinds of marks ([Bannister and Kouzarides,
2011](https://doi.org/10.1038/cr.2011.22)):

- **Acetylation** adds an acetyl group to a lysine. That cancels the lysine's positive
  charge and can weaken its hold on DNA. Enzymes called histone acetyltransferases add
  these marks, and histone deacetylases remove them.
- **Methylation** adds one, two or three methyl groups to a lysine. The same lysine can
  carry either kind of mark.

Each mark is named with a short code: the histone, then the amino acid and its position
in the tail, then the mark ([Figure 7.5](#figure-7-5)). H3K27me3 means three methyl
groups (me3) on lysine (K) 27 of histone H3, and H3K27ac is an acetyl group on the same
lysine. Positions are counted without the methionine that starts the protein, because
the cell trims it off soon after the protein is made ([Blasco-Santana et al.,
2024](https://doi.org/10.3390/ijms25158498)).

![Two sections. Section 1, reading a mark's name: the first 36 amino acids of the histone H3 tail written as letters, leading into a nucleosome, a ball with DNA wrapped around it and short tails sticking out. Lysines at positions 4, 9, 27 and 36 are bold and numbered, and three methyl groups sit on lysine 27. Below, the name H3K27me3 is split into three parts: H3 means histone H3, K27 means lysine at position 27, and me3 means three methyl groups. Section 2, marks and packing: on the left, nucleosomes packed tightly in a zigzag, with tails carrying methyl groups, labeled H3K9me3, H3K27me3, tightly packed, genes kept off. On the right, three nucleosomes spaced along a stretch of DNA, with tails carrying acetyl groups, labeled H3K27ac, loosely packed, genes active.](../images/7.5-histone-marks.svg "Histone marks. A mark's name gives the histone, the amino acid and its position in the tail, and the chemical group, so H3K27me3 is three methyl groups on lysine 27 of histone H3. Some marks tend to go with tightly packed DNA where genes are kept off, and others with loosely packed DNA where genes are active, though each has exceptions.")

Each mark is associated with a particular kind of region. The Roadmap Epigenomics
project mapped the most common ones in 111 human tissues and cell types ([Roadmap
Epigenomics Consortium, 2015](https://doi.org/10.1038/nature14248)):

| Mark     | Usually found at                                                          |
| -------- | ------------------------------------------------------------------------- |
| H3K4me3  | Promoters                                                                 |
| H3K4me1  | [Enhancers](../01-biological-foundations/03-transcription.md#genomic-regions-and-transcription) |
| H3K27ac  | Active promoters and enhancers                                            |
| H3K36me3 | The bodies of genes being transcribed                                     |
| H3K27me3 | Genes switched off by Polycomb proteins, which may be on in other cells   |
| H3K9me3  | Heterochromatin, especially repeat-rich DNA that is usually packed tight  |

H3K27me3 is made by PRC2, a group of Polycomb proteins that helps cells keep their
identity ([Margueron and Reinberg, 2011](https://doi.org/10.1038/nature09784)). It
usually marks DNA that's packed away in one cell type but may be opened in another,
while H3K9me3 tends to mark DNA that stays packed across many cell types ([Saksouk et
al., 2015](https://doi.org/10.1186/1756-8935-8-3)).

These tendencies have exceptions. In embryonic stem cells, many developmental genes
carry H3K4me3 and H3K27me3 at once, which keeps them off but ready to switch on later
([Bernstein et al., 2006](https://doi.org/10.1016/j.cell.2006.02.041)). A family of
active genes that code for zinc finger proteins carries H3K9me3 near their ends
([Blahnik et al., 2011](https://doi.org/10.1371/journal.pone.0017121)). And when
engineered cells lost most of the H3K27ac at their enhancers, their genes' activity
barely changed ([Zhang et al., 2020](https://doi.org/10.1186/s13059-020-01957-w)). A
mark tells you what usually goes on at a region, but it doesn't always cause it.

Some histone marks can also be passed on when a cell divides, at least those that keep
genes off. When DNA is copied, the old histones are shared between the two new copies,
so each inherits about half the marks, and enzymes that recognize a mark and add more of
it fill in the rest. For H3K9me3 and H3K27me3, that refilling can take more than one
cell cycle ([Alabert et al., 2015](https://doi.org/10.1101/gad.256354.114)). In fruit
flies, H3K27me3 carried a gene's off state through several divisions ([Coleman and
Struhl, 2017](https://doi.org/10.1126/science.aai8236)), though keeping it going also
needed the DNA sequences that call in PRC2 ([Laprell et al.,
2017](https://doi.org/10.1126/science.aai8266)). Histones from active regions aren't
kept in place the same way ([Escobar et al.,
2019](https://doi.org/10.1016/j.cell.2019.10.009)), so whether marks of active genes are
inherited is less clear.

## Measuring the Marks

Standard sequencing reads 5-methylcytosine as an ordinary C, and [PCR copies lose the
marks](../04-next-generation-sequencing/02-library-preparation.md#making-copies), so
methylation needs its own methods.

- **Bisulfite sequencing** treats DNA with sodium bisulfite, which turns unmethylated
  cytosine into uracil but leaves 5-methylcytosine alone. PCR then copies each uracil as
  T ([Frommer et al., 1992](https://doi.org/10.1073/pnas.89.5.1827)). After alignment, a
  C that stayed C was methylated, and a C that became T wasn't. Run across a whole
  genome, it maps methylation at nearly every C. One such study found that 99.98% of the
  methylation in a fibroblast cell line was at CpG sites, while in embryonic stem cells
  nearly a quarter was elsewhere ([Lister et al.,
  2009](https://doi.org/10.1038/nature08514)). Bisulfite can't tell 5-methylcytosine
  from 5-hydroxymethylcytosine, because neither one becomes uracil, so both are read as
  C ([Huang et al., 2010](https://doi.org/10.1371/journal.pone.0008888)).
- **Enzymatic methyl-seq (EM-seq)** makes the same distinction with enzymes in place of
  bisulfite, which damages and breaks DNA. Because it's gentler, it works with as little
  as 100 picograms of DNA ([Vaisvila et al.,
  2021](https://doi.org/10.1101/gr.266551.120)). Like bisulfite, it reads both modified
  forms as C.
- **[Long reads](../04-next-generation-sequencing/04-long-read-sequencing.md)** come
  from the original molecule, so methylation changes the signal itself and can be
  detected without any conversion.

Histone marks are measured through the DNA they're attached to.
[ChIP-seq](../04-next-generation-sequencing/05-types-of-sequencing/05-chip-seq.md) uses
an antibody against one mark, such as H3K27me3, to pull out the DNA wrapped around
nucleosomes carrying it.
[ATAC-seq](../04-next-generation-sequencing/05-types-of-sequencing/06-atac-seq.md) shows
which stretches of DNA are open enough for an enzyme to reach, though it can't say which
marks are present.

## Epigenetics in Cancer

### Too Little and Too Much Methylation

In 1983, two labs independently reported that cancer cells carry less DNA methylation
than normal cells. One looked at specific genes ([Feinberg and Vogelstein,
1983](https://doi.org/10.1038/301089a0)), and the other measured total 5-methylcytosine
in 103 tumors ([Gama-Sosa et al., 1983](https://doi.org/10.1093/nar/11.19.6883)). At the
same time, CpG islands at the promoters of some tumor suppressor genes gain methylation,
which can silence those genes without any change to their sequence. Genes silenced this
way include CDKN2A (p16), VHL, APC and MLH1 ([Baylin and Jones,
2016](https://doi.org/10.1101/cshperspect.a019505)).

MLH1 is a mismatch repair gene, and losing it causes [microsatellite
instability](../03-genomic-variation/03-insertions-and-deletions.md#where-indels-happen)
(MSI). In colorectal cancers that aren't inherited, MSI usually traces back to
methylation. One study found a heavily methylated MLH1 promoter in 11 of 13 tumors with
MSI and in only 2 of 21 tumors without it. In cell lines, removing the methylation
switched MLH1 back on and restored mismatch repair ([Herman et al.,
1998](https://doi.org/10.1073/pnas.95.12.6870)).

### Mutations in the Machinery

Some childhood cancers show how directly the epigenome can drive cancer. In diffuse
intrinsic pontine glioma (DIPG), a brainstem tumor of children, 78% of tumors carry a
mutation in a histone H3 gene that swaps lysine 27 for methionine, called K27M ([Wu et
al., 2012](https://doi.org/10.1038/ng.1102)). An independent study published the same
year found mutations at lysine 27 or glycine 34 of histone H3.3 in 31% of pediatric
glioblastomas, the first time recurrent mutations in a human histone had been reported
([Schwartzentruber et al., 2012](https://doi.org/10.1038/nature10833)). The K27M histone
blocks PRC2, so tumors carrying it have greatly reduced H3K27me3 ([Lewis et al.,
2013](https://doi.org/10.1126/science.1232245)). The World Health Organization now
groups these tumors as diffuse midline glioma, H3 K27-altered, a category that also
covers tumors that lose H3K27me3 in other ways ([Louis et al.,
2021](https://doi.org/10.1093/neuonc/noab106)). Newer papers write the same mutation as
K28M, because they count the first methionine.

Other cancers disrupt the enzymes that write or erase marks:

- **IDH mutations.** Mutant IDH1 makes a molecule called 2-hydroxyglutarate ([Dang et
  al., 2009](https://doi.org/10.1038/nature08617)), which blocks TET enzymes and other
  enzymes that remove marks ([Xu et al.,
  2011](https://doi.org/10.1016/j.ccr.2010.12.014)). Leukemias with IDH mutations carry
  extra methylation across the genome ([Figueroa et al.,
  2010](https://doi.org/10.1016/j.ccr.2010.11.015)), and adding mutant IDH1 to cultured
  brain cells was enough to give them the heavy CpG island methylation seen in
  IDH-mutant gliomas ([Turcan et al., 2012](https://doi.org/10.1038/nature10866)). In
  children with malignant gliomas, one study found IDH1 mutations only in patients aged
  14 or older ([Pollack et al., 2011](https://doi.org/10.1007/s00381-010-1264-1)).
- **Rhabdoid tumors**, including atypical teratoid/rhabdoid tumors (ATRT) of the brain,
  carry very few mutations, about 0.19 per million bases on average. Loss of SMARCB1,
  part of a protein complex that remodels chromatin, is essentially the only one they
  share ([Lee et al., 2012](https://doi.org/10.1172/JCI64400)).
- **Ependymomas** of the hindbrain showed no significant recurrent single-base mutations
  when 47 tumors were sequenced, yet the group with the worst outcomes showed heavy CpG
  island methylation ([Mack et al., 2014](https://doi.org/10.1038/nature13108)).

Methylation patterns are distinctive enough to identify a tumor type. A classifier built
from methylation profiles of 2,801 reference samples, covering 82 kinds of brain tumor
plus normal tissue, matched 88% of 1,104 new cases to a class, and it changed the
original diagnosis in 129 of them, about 12% ([Capper et al.,
2018](https://doi.org/10.1038/nature26000)).
