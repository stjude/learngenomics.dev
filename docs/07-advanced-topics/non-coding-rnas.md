---
title: Noncoding RNAs
description: "Noncoding RNAs, from the RNAs that run the cell to microRNAs and long noncoding RNAs, how they are measured, and their role in cancer."
track: Advanced Topics
sidebar_position: 3
---

In [The Central
Dogma](../01-biological-foundations/02-the-central-dogma.md#from-dna-to-protein), genes
are copied into RNA, and the RNA is translated into protein. Many RNAs skip the last
step and do their work as RNA. These noncoding RNAs are usually sorted by length. Those
longer than 200 nucleotides (nt) are called long noncoding RNAs, and the rest are called
small ([Mattick et al., 2023](https://doi.org/10.1038/s41580-022-00566-8)). As that
review notes, the cutoff was chosen arbitrarily, because 200 nt is a convenient size
limit in the lab methods used to purify RNA. [Figure 7.6](#figure-7-6) shows how long
each kind usually is. This page covers the main kinds, how they're measured and how they
turn up in cancer.

![A chart of RNA lengths on a log scale from 10 to 10,000 nucleotides. A dashed line at 200 nucleotides divides a shaded side labeled small from a side labeled long. Rows from top: microRNAs, a point at about 22; piRNAs, a bar from 21 to 35; tRNAs, a bar from 76 to 90; snoRNAs, a bar from 68 to 213 with a median of 118; snRNAs, a bar from 107 to 188; rRNAs, four points labeled 5S, 5.8S, 18S and 28S, at 119, 157, 1,869 and 5,070; lncRNAs, a bar from 369 to 2,264 with a median of 813; and, for comparison, mRNAs, a bar from 760 to 9,142 with a median of 2,941. A key identifies a bar as the typical range and a dot on a bar as the median.](../images/7.6-rna-lengths.svg "How long noncoding RNAs are, with mRNAs for comparison. MicroRNAs, piRNAs and tRNAs fall below 200 nucleotides, snoRNAs and rRNAs span that line, and most long noncoding RNAs are shorter than most mRNAs. For snoRNAs, lncRNAs and mRNAs, the bar covers the middle 90% of transcripts in GENCODE release 50, with mRNAs limited to one transcript per gene. The snRNA bar spans the five spliceosome snRNAs in GENCODE, and the rRNA lengths are from RefSeq.")

## The RNAs That Run the Cell

Some noncoding RNAs are part of the basic machinery that every cell needs.

**Ribosomal RNA (rRNA)** makes up most of a cell's RNA, which is why RNA-seq [removes it
first](../04-next-generation-sequencing/05-types-of-sequencing/03-rna-seq.md#how-the-library-is-made).
A human ribosome is built from two subunits and four rRNAs. The small subunit holds the
18S rRNA, and the large subunit holds the 28S, 5.8S and 5S rRNAs. The 18S, 5.8S and 28S
rRNAs are all cut from one long precursor RNA, and 5S is made from separate genes
([Henras et al., 2015](https://doi.org/10.1002/wrna.1269)). The rRNA does more than hold
the ribosome together. When the structure of the large subunit was solved in a microbe
that lives in very salty water, the spot where amino acids are joined into a protein
turned out to be made entirely of RNA, with no protein within about 18 ångströms
([Nissen et al., 2000](https://doi.org/10.1126/science.289.5481.920)). An RNA that
speeds up a chemical reaction is called a **ribozyme**, and the ribosome is one.

[Transfer RNAs](../01-biological-foundations/04-translation.md#decoding-the-transcript)
bring each amino acid to the ribosome. Most are 76 to 90 nt long ([Berg and Brandl,
2021](https://doi.org/10.1080/15476286.2020.1809197)).

**Small nuclear RNAs (snRNAs)** are the RNA inside the
[spliceosome](alternative-splicing.md#how-splice-sites-are-chosen). The main spliceosome
is assembled from five snRNAs, U1, U2, U4, U5 and U6, each bound to proteins, with U4
and U6 paired together. The snRNAs find the splice sites partly by pairing with them.
One of the first steps in splicing is U1 snRNA pairing with the 5′ splice site at the
start of an intron ([Will and Lührmann,
2011](https://doi.org/10.1101/cshperspect.a003707)).

**Small nucleolar RNAs (snoRNAs)** work in the nucleolus, the part of the nucleus where
ribosomes are built, as Henras et al. describe. Many of them help make small chemical
changes to other RNAs, mostly rRNAs and snRNAs. Each of these snoRNAs carries an enzyme
to one spot on its target RNA, which it finds by pairing with the bases there. The
enzyme then changes a single nucleotide at that spot. Some snoRNAs bring an enzyme that
adds a [methyl group](epigenetic-modifications.md#dna-methylation). Others bring one
that turns a uridine into pseudouridine, a rearranged form of the same base ([Bratkovič
et al., 2020](https://doi.org/10.1093/nar/gkz1140)).

## MicroRNAs

**MicroRNAs** are about 22 nt long, and they turn down other genes by pairing with their
mRNAs ([Bartel, 2018](https://doi.org/10.1016/j.cell.2018.03.006)). Each one starts out
as part of a much longer RNA that folds back on itself into a hairpin, and it takes two
cuts to free it ([Figure 7.7](#figure-7-7)). In the nucleus, an enzyme called Drosha,
working with a partner protein called DGCR8, cuts the hairpin out of the long RNA. The
hairpin, about 70 nt at this stage ([Lee et al.,
2003](https://doi.org/10.1038/nature01957)), is carried out to the cytoplasm, where an
enzyme called **Dicer** cuts off the loop. That leaves a short double-stranded piece
about 20 base pairs long. One strand, the mature microRNA, is loaded into a protein
called **Argonaute**, and the other strand is broken down.

![Four numbered steps, each a drawing of RNA. Step 1, In the nucleus, Drosha cuts the hairpin free: a long RNA with loose ends on the left folds back on itself into a paired stem that ends in a loop on the right. One side of the stem is highlighted as the microRNA and the other as its partner strand. Drosha cuts across the stem near the loose ends. Step 2, In the cytoplasm, Dicer cuts off the loop: the freed hairpin, its ends labeled 5′ and 3′, with Dicer cutting across the stem next to the loop. Step 3, Argonaute keeps one strand: the microRNA sits inside Argonaute, and the partner strand lies in pieces, labeled broken down. Step 4, The seed pairs with a site in an mRNA: an mRNA with a 5′ cap, a coding sequence and a 3′ UTR ending in AAAA, with Argonaute and its microRNA bound in the 3′ UTR. A close-up shows the mRNA site, GCUGCU written 5′ to 3′, paired base by base with six letters of miR-16, which is written 3′ to 5′ as GCGGUUAUAAAUGCACGACGAU. The six paired letters, next to the microRNA's 5′ end, are highlighted as the seed. A key identifies the microRNA, its partner strand, the rest of the RNA and proteins.](../images/7.7-microrna-path.svg "How a microRNA is made and how it finds its targets. Drosha cuts the hairpin from a longer RNA in the nucleus, and Dicer cuts off its loop in the cytoplasm. Argonaute keeps one strand of what's left, the mature microRNA, and the other strand is broken down. The microRNA then guides Argonaute to mRNAs with a site that pairs with its seed, nucleotides 2 to 7, usually in the 3′ UTR. The microRNA shown is miR-16, with its sequence from GRCh38. The mRNA site is drawn to match its seed and doesn't come from a particular gene.")

Inside Argonaute, the microRNA works as a guide. Its key part is the **seed**,
nucleotides 2 to 7 counted from its 5′ end, which pairs with matching sites in mRNAs,
mostly in their [3′
UTRs](../01-biological-foundations/03-transcription.md#genomic-regions-and-transcription),
as Bartel's review explains. Once Argonaute is bound, the mRNA makes less protein,
mainly because the mRNA is broken down faster. In one study, lower mRNA levels accounted
for at least 84% of the drop in protein ([Guo et al.,
2010](https://doi.org/10.1038/nature09267)).

A six-letter seed can match many genes, so each microRNA has many targets. When a single
microRNA was added to human cells, about 100 mRNAs dropped within 12 hours ([Lim et al.,
2005](https://doi.org/10.1038/nature03315)). Two studies that measured proteins directly
found that one microRNA lowered hundreds of proteins, most of them only a little
([Selbach et al., 2008](https://doi.org/10.1038/nature07228); [Baek et al.,
2008](https://doi.org/10.1038/nature07242)). Across the genome, more than 60% of human
protein-coding genes have kept sites that pair with microRNAs over the course of
evolution ([Friedman et al., 2009](https://doi.org/10.1101/gr.082701.108)). MicroRNAs
with the same seed are grouped into a seed family, and members of a family often do
overlapping jobs, as Bartel's review notes.

A second group of small RNAs works the same way. **PIWI-interacting RNAs (piRNAs)** are
21 to 35 nt long and guide PIWI proteins, a branch of the Argonaute family ([Höck and
Meister, 2008](https://doi.org/10.1186/gb-2008-9-2-210)). Their main job is in the germ
line, the cells that give rise to eggs and sperm, where they silence transposons,
stretches of DNA that can copy themselves into new places in the genome ([Ozata et al.,
2019](https://doi.org/10.1038/s41576-018-0073-3)).

## Long Noncoding RNAs

**Long noncoding RNAs (lncRNAs)** are the biggest group. GENCODE lists more lncRNA genes
than protein-coding genes, as you'll see in Try It below. Most are made by the same RNA
polymerase that makes mRNA, and many are spliced and given a 5′ cap and a poly-A tail,
just as mRNAs are, though some aren't, as Mattick's review notes. A few have
well-understood jobs:

- **XIST** silences one of the two X chromosomes in female cells, the X inactivation
  mentioned in [Epigenetic Modifications](epigenetic-modifications.md#dna-methylation).
  It's made only from the X chromosome that will be silenced ([Brown et al.,
  1991](https://doi.org/10.1038/349038a0)), it spreads along that same chromosome and
  coats it ([Clemson et al., 1996](https://doi.org/10.1083/jcb.132.3.259)), and X
  inactivation can't happen without it ([Loda and Heard,
  2019](https://doi.org/10.1371/journal.pgen.1008333)).
- **NEAT1** is the scaffold of paraspeckles, small bodies in the nucleus ([Clemson et
  al., 2009](https://doi.org/10.1016/j.molcel.2009.01.026)). Mice without NEAT1 live and
  breed normally in the lab and lose only their paraspeckles ([Nakagawa et al.,
  2011](https://doi.org/10.1083/jcb.201011110)), though a later study found that some of
  the females fail to become pregnant ([Nakagawa et al.,
  2014](https://doi.org/10.1242/dev.110544)).
- **Telomerase RNA** is part of
  [telomerase](../02-cancer-biology/02-hallmarks-of-cancer.md#refusing-to-die), the
  enzyme that rebuilds the ends of chromosomes. At 451 nt, it's long enough to count as
  a lncRNA ([Klump and Schmidt, 2023](https://doi.org/10.1042/BST20230269)). The core of
  the enzyme is this RNA plus a protein called TERT ([Nguyen et al.,
  2018](https://doi.org/10.1038/s41586-018-0062-x)). Eleven of its bases, CUAACCCUAAC,
  form the template that telomerase copies to add TTAGGG repeats to chromosome ends
  ([Feng et al., 1995](https://doi.org/10.1126/science.7544491)).

Most lncRNAs look quite different from mRNAs in sequencing data. They're usually made at
lower levels and in fewer tissues, and their exons change faster over evolution than
protein-coding exons, though more slowly than old repeated DNA thought to have no
function. Some of that tissue specificity may come from their low levels, which make
them easy to miss in tissues where they are made ([Derrien et al.,
2012](https://doi.org/10.1101/gr.132159.111)). In one catalog of lncRNAs found between
genes, 78% were specific to a tissue, against about 19% of protein-coding genes ([Cabili
et al., 2011](https://doi.org/10.1101/gad.17446611)).

How many lncRNAs have a real job is still argued over. Mattick's review counts about
50,000 papers on lncRNAs, more than 2,000 of them reporting a tested function, though
most of those functions haven't been followed up in detail. Others argue that most
lncRNAs are noise from transcription or play only minor roles ([Ponting and Haerty,
2022](https://doi.org/10.1146/annurev-genom-112921-123710)). Sometimes a lncRNA gene
does its job without needing the RNA at all. In a study of 12 lncRNA loci in mouse
cells, 5 changed the activity of a neighboring gene, and none of those effects needed
the lncRNA. They came from the act of transcription, from splicing, or from the lncRNA's
promoter acting like an enhancer ([Engreitz et al.,
2016](https://doi.org/10.1038/nature20149)). Even a skeptic's estimate leaves plenty to
study. As Palazzo and Lee put it, "even if 10% of current lncRNAs prove to be
functional, this would represent a wealth of new biology" ([Palazzo and Lee,
2015](https://doi.org/10.3389/fgene.2015.00002)).

Splicing can also close an RNA into a loop. In **back-splicing**, the end of an exon is
joined to the start of an earlier exon, making a **circular RNA**. With no free ends, a
circular RNA has no 5′ cap or poly-A tail ([Patop et al.,
2019](https://doi.org/10.15252/embj.2018100836)).

## Measuring Them

How a library is made decides which noncoding RNAs it can see. As
[RNA-seq](../04-next-generation-sequencing/05-types-of-sequencing/03-rna-seq.md#how-the-library-is-made)
describes, poly-A selection loses RNAs without a tail, such as circular RNAs and some
lncRNAs, and total RNA-seq keeps them.

MicroRNAs and other very short RNAs need their own method. In standard RNA-seq, they're
too short to be copied reliably and are lost when fragments are selected by size.
**Small RNA-seq** attaches adapters directly to both ends of each small RNA before
copying it into DNA ([Sun and Chen, 2020](https://doi.org/10.1186/s13045-020-00945-8)).
Some kits add a poly-A tail to each small RNA in place of one adapter. Most start from
all of a sample's RNA, and the short inserts are selected by size after the adapters are
added ([Benesova et al., 2021](https://doi.org/10.3390/diagnostics11060964)).

## Noncoding RNAs in Cancer

### MicroRNAs Lost in Leukemia

Chronic lymphocytic leukemia (CLL) is a cancer of B cells, a type of white blood cell. A
region of chromosome 13 called 13q14 is deleted in more than half of CLL cases. Calin et
al. found two microRNA genes in this region, *MIR15A* and *MIR16-1*, and found them
deleted or turned down in about 68% of cases ([Calin et al.,
2002](https://doi.org/10.1073/pnas.242606799)). Their microRNAs, miR-15a and miR-16,
lower Bcl-2, a protein that keeps cells from dying, and restoring them made leukemia
cells die in a lab model ([Cimmino et al.,
2005](https://doi.org/10.1073/pnas.0506654102)). Bcl-2 is the relative of Bcl-xL from
[Alternative Splicing](alternative-splicing.md#why-it-matters). Mice missing the stretch
of 13q14 that holds both microRNAs developed the range of B cell disorders seen in human
CLL, and losing the two microRNAs made B cells divide faster ([Klein et al.,
2010](https://doi.org/10.1016/j.ccr.2009.11.019)).

### DICER1 and Childhood Tumors

Inherited loss-of-function variants in *DICER1*, the gene for Dicer, predispose children
to pleuropulmonary blastoma (PPB), a rare lung tumor. Hill et al. found them in 11
families with PPB ([Hill et al., 2009](https://doi.org/10.1126/science.1174334)). The
tumors follow the [two-hit
pattern](../02-cancer-biology/06-inherited-risk.md#the-second-hit) in their own way. In
15 tumors studied, every one had a variant that broke one copy of *DICER1*, inherited in
12 and acquired in the tumor in 3. Each also had an acquired change that swapped one
amino acid in one of Dicer's two cutting regions ([Pugh et al.,
2014](https://doi.org/10.1038/onc.2014.150)). People who inherit a *DICER1* variant can
also develop other tumors, including Sertoli–Leydig cell tumors of the ovary, cystic
nephroma of the kidney and thyroid nodules. The risk is highest in early childhood, and
the variants are inherited in an autosomal dominant pattern with reduced
[penetrance](../02-cancer-biology/06-inherited-risk.md), so many people who carry one
never develop a tumor ([Schultz et al.,
2018](https://doi.org/10.1158/1078-0432.CCR-17-3089)).

### A Spliceosome RNA in Medulloblastoma

Medulloblastoma is a brain tumor, and one group of these tumors is named for the Sonic
hedgehog (SHH) signaling pathway that drives them. About half of SHH medulloblastomas
carry the same mutation in U1 snRNA, an A changed to G at its third base. It's found in
97% of adults with this kind of tumor and 25% of adolescents, but it's largely absent in
infants ([Suzuki et al., 2019](https://doi.org/10.1038/s41586-019-1650-0)). That base
sits in the part of U1 that pairs with the 5′ splice site, so the mutant U1 picks out
new [cryptic splice sites](alternative-splicing.md#when-splicing-goes-wrong). As Suzuki
et al. found, the changed splicing switches off the [tumor
suppressor](../02-cancer-biology/03-oncogenes-and-tumor-suppressors.md#tumor-suppressors)
*PTCH1* and switches on the oncogenes *GLI2* and *CCND2*. A different change at the same
base, A to C, turns up in other cancers, including about 4% of CLL and about 6% of liver
cancers ([Shuai et al., 2019](https://doi.org/10.1038/s41586-019-1651-z); [Niño et al.,
2022](https://doi.org/10.3390/cancers14020281)).

## Setting Up

This page uses `samtools` and `curl`, as in [Setting
Up](../05-from-reads-to-variants/01-setting-up.md) in From Reads to Variants. If you
made the `reads-to-variants` or `file-formats` environment, activate it with `conda
activate reads-to-variants` or `conda activate file-formats`. Otherwise, follow [Install
the Tools](../05-from-reads-to-variants/01-setting-up.md#install-the-tools) on that
page. The files on this page take up about 250 MB.

## Try It

Make a folder, download the GENCODE annotation from [GTF/GFF3
Files](../06-genomic-file-formats/06-GTF-GFF3-files.md#try-it), and save its gene lines
to a smaller file:

```bash
# Make a folder for this page and move into it
mkdir ncrna && cd ncrna
# Download the GTF file for GENCODE release 50
curl -fLO https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.annotation.gtf.gz
# Save the gene lines to their own file
gunzip -c gencode.v50.annotation.gtf.gz | awk -F '\t' '$3 == "gene"' > genes.gtf
# Count the genes of each kind of RNA on this page, with protein-coding genes for comparison
grep -o 'gene_type "[^"]*"' genes.gtf | grep -E '"(protein_coding|lncRNA|miRNA|snRNA|snoRNA|rRNA|Mt_tRNA|Mt_rRNA)"' | sort | uniq -c | sort -rn
```

```text
34866 gene_type "lncRNA"
20107 gene_type "protein_coding"
1901 gene_type "snRNA"
1878 gene_type "miRNA"
 985 gene_type "snoRNA"
  47 gene_type "rRNA"
  22 gene_type "Mt_tRNA"
   2 gene_type "Mt_rRNA"
```

There are about 35,000 lncRNA genes, against about 20,000 protein-coding genes. Two
kinds of RNA from this page are thin on the ground. The only tRNA genes here are the 22
in the mitochondrial genome, because GENCODE keeps its predicted nuclear tRNA genes in a
separate file ([GENCODE release
50](https://www.gencodegenes.org/human/release_50.html)). And none of the 47 rRNA genes
is an 18S or 28S gene:

```bash
# Count the rRNA genes named 18S or 28S
grep 'gene_type "rRNA";' genes.gtf | grep -c '18S\|28S'
```

```text
0
```

The 18S and 28S genes sit in long arrays of repeated copies, called rDNA, that the
GRCh38 reference genome leaves as unknown sequence ([Nurk et al.,
2022](https://doi.org/10.1126/science.abj6987)).

Next, find the two microRNA genes from 13q14:

```bash
# Show the position, strand and name of MIR15A, MIR16-1 and DLEU2
grep -E 'gene_name "(MIR15A|MIR16-1|DLEU2)";' genes.gtf | awk -F '\t' '{split($9, a, ";"); print $1, $4, $5, $7 a[3]}'
```

```text
chr13 49956669 50126118 - gene_name "DLEU2"
chr13 50048973 50049061 - gene_name "MIR16-1"
chr13 50049119 50049201 - gene_name "MIR15A"
```

*MIR15A* and *MIR16-1* sit about 60 bases apart, and both fall inside *DLEU2*, a lncRNA
gene, on the same strand. Each microRNA gene here is only 80 to 90 bases long, about the
size of the hairpin. To see their sequences, download chromosome 13 of the reference:

```bash
# Download chromosome 13 of GRCh38 from UCSC
curl -fLO https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chr13.fa.gz
# Decompress it to chr13.fa
gunzip chr13.fa.gz
# Index it so tools can jump to any position
samtools faidx chr13.fa
# Read both hairpins on the - strand, each on one line
samtools faidx -i -n 100 chr13.fa chr13:50048973-50049061 chr13:50049119-50049201
```

```text
>chr13:50048973-50049061/rc
GTCAGCAGTGCCTTAGCAGCACGTAAATATTGGCGTTAAGATTCTAAAATTATCTCCAGTATTAACTGTGCTGCTGAAGTAAGGTTGAC
>chr13:50049119-50049201/rc
CCTTGGAGTAAAGTAGCAGCACATAATGGTTTGTGGATTTTGAAAAGGTGCAGGCCATATTGTGCTGCCTCAAAAATACAAGG
```

Both genes are on the `-` strand, which means their RNA is copied from the opposite
strand to the one the reference spells out. The `-i` option turns each region around and
swaps every base for its partner, so you see the sequence the way the RNA reads, from 5′
to 3′. [Alternative Splicing](alternative-splicing.md#try-it) uses the same option. `-n
100` keeps each sequence on one line. The reference is DNA, so it shows T where the RNA
has U.

Each sequence folds back on itself to form a hairpin, so stretches in its first half
pair with stretches in its second half. In the first hairpin, bases 15 to 22 read
AGCAGCAC, and bases 68 to 75 read GTGCTGCT. Write the second stretch backward under the
first, and every base lines up with its partner, A with T and G with C:

```text
bases 15 to 22            5′ AGCAGCAC 3′
                             ||||||||
bases 68 to 75, backward  3′ TCGTCGTG 5′
```

As you'll see below, bases 15 to 22 are part of miR-16, and bases 68 to 75 are part of
its partner strand, as in step 1 of [Figure 7.7](#figure-7-7).

miRBase, a catalog of microRNAs, lists miR-16 as UAGCAGCACGUAAAUAUUGGCG ([miRBase
MIMAT0000069](https://www.mirbase.org/mature/MIMAT0000069)) and miR-15a as
UAGCAGCACAUAAUGGUUUGUG ([miRBase
MIMAT0000068](https://www.mirbase.org/mature/MIMAT0000068)). Each starts at the 14th
base of its hairpin. Read just those 22 bases:

```bash
# Read the mature miR-16 and miR-15a
samtools faidx -i chr13.fa chr13:50049027-50049048 chr13:50049167-50049188
```

```text
>chr13:50049027-50049048/rc
TAGCAGCACGTAAATATTGGCG
>chr13:50049167-50049188/rc
TAGCAGCACATAATGGTTTGTG
```

The two microRNAs differ after their ninth base, but they share their seed, AGCAGC at
positions 2 to 7, so both belong to the miR-15/16 seed family and can pair with the same
sites. The first is the miR-16 in [Figure 7.7](#figure-7-7), where it's written
backward, from 3′ to 5′.

That's the end of this exercise. Move out of the folder and delete it:

```bash
# Move up out of the folder
cd ..
# Delete the folder and everything in it
rm -r ncrna
```
