---
title: Alternative Splicing
description: "How cells choose splice sites, the types of alternative splicing events, their role in health and disease, and how to see them in sequencing data."
track: Advanced Topics
sidebar_position: 1
---

[Transcription](../01-biological-foundations/03-transcription.md#alternative-splicing)
introduced alternative splicing, where one gene joins its exons in more than one way to
make several mRNAs, called isoforms, which can encode different versions of its protein.
About 95% of human genes with more than one exon are alternatively spliced ([Pan et al.,
2008](https://doi.org/10.1038/ng.259)). This page looks at how the cell decides where to
splice, the forms those decisions take, how they affect health and disease, and how to
see them in sequencing data.

## How Splice Sites Are Chosen

Splicing is done by the **spliceosome**, a large machine built from RNA and proteins. It
recognizes short sequences at each end of an intron. The start of the intron is the **5′
splice site**, or donor, and the end is the **3′ splice site**, or acceptor. Nearly
every intron starts with GT and ends with AG (GU and AG in the RNA). In a survey of
mammalian splice sites, 98.71% used this pair, and 0.56% used GC and AG instead ([Burset
et al., 2000](https://doi.org/10.1093/nar/28.21.4364)).

Two letters at each end can't be the whole story, since GT and AG turn up everywhere in
the genome. Short stretches of sequence in exons and introns, called **splicing
enhancers** and **splicing silencers**, are bound by RNA-binding proteins that make the
spliceosome more or less likely to use a nearby site ([Wang & Burge,
2008](https://doi.org/10.1261/rna.876308)). Which of these proteins a cell makes, and
how much of each, differs between cell types. Most alternative splicing events vary
between tissues, so the same gene can be spliced one way in one tissue and another way
in the next ([Wang et al., 2008](https://doi.org/10.1038/nature07509)).

## Types of Events

![Seven pairs of transcript diagrams, each showing two isoforms of one gene as boxes joined by lines, with the exon or part of an exon that differs highlighted. Five pairs show exon skipping, intron retention, alternative 5′ and 3′ splice sites and mutually exclusive exons. Below a divider, two pairs show an alternative first exon and an alternative last exon.](../images/7.1-alternative-splicing-events.svg "Common types of alternative splicing. Each pair of rows is two transcripts of the same gene, with exons as boxes and introns as lines. The two pairs at the bottom also depend on where transcription starts or stops. The data are made up.")

[Figure 7.1](#figure-7-1) shows the main ways two isoforms can differ:

- **Exon skipping.** An exon is kept in one isoform and left out of the other.
- **Intron retention.** An intron stays in the mRNA. This affects up to three-quarters
  of mammalian genes with more than one exon, and it often lowers how much of the gene's
  mRNA there is ([Braunschweig et al., 2014](https://doi.org/10.1101/gr.177790.114)).
  One way is **nonsense-mediated decay (NMD)**, a quality check that destroys mRNAs with
  a stop codon too early in them.
- **Alternative 5′ splice site.** The spliceosome uses a different donor, so the exon
  before the intron ends earlier or later.
- **Alternative 3′ splice site.** It uses a different acceptor, so the exon after the
  intron starts earlier or later.
- **Mutually exclusive exons.** Of two or more exons, exactly one is kept. The fruit fly
  gene *Dscam* takes this to the extreme, with alternative splicing that could make more
  than 38,000 isoforms ([Schmucker et al.,
  2000](https://doi.org/10.1016/S0092-8674(00)80878-8)).

The last two rows involve more than splicing. An **alternative first exon** depends on
transcription starting at a different promoter. An **alternative last exon** depends on
where the mRNA is cut and given its tail, called **alternative polyadenylation**. A
different cut can also just lengthen or shorten the untranslated region in the same last
exon. [Wang et al.](https://doi.org/10.1038/nature07509) grouped these changes with the
five splicing events, for eight types in all.

In every one of these events, the exons that are kept stay in the order they have in the
gene. Most human pre-mRNAs are spliced into linear mRNAs that keep this order ([Salzman
et al., 2012](https://doi.org/10.1371/journal.pone.0030733)), so an isoform can be exons
1, 2 and 4, with exon 3 skipped, but almost never 1, 4, 2 and 3. Transcripts of the gene
*DCC* with exons joined out of order were found in 1991, at low levels and mostly without
a poly-A tail ([Nigro et al., 1991](https://doi.org/10.1016/0092-8674(91)90244-S)). Deep
sequencing later showed that many such "scrambled" transcripts are [circular
RNAs](./non-coding-rnas.md#long-noncoding-rnas), where the end of a later exon is joined
back to the start of an earlier one ([Salzman et al.,
2012](https://doi.org/10.1371/journal.pone.0030733)).

## Why It Matters

Isoforms of the same gene can do different things, even opposite ones. *BCL2L1* makes
two well-studied proteins. The longer one, Bcl-xL, is 233 amino acids and protects cells
from dying at least as well as its relative Bcl-2. The shorter one, Bcl-xS, is 170 amino
acids and blocks Bcl-2 from protecting the cell. Bcl-xS was found at high levels in
cells that turn over quickly, such as developing immune cells, and Bcl-xL in long-lived
cells such as those of the adult brain ([Boise et al.,
1993](https://doi.org/10.1016/0092-8674(93)90508-N); [UniProt
Q07817](https://www.uniprot.org/uniprotkb/Q07817/entry)). The two isoforms differ by a
single alternative 5′ splice site, which you'll find in Try It below.

## When Splicing Goes Wrong

Because the spliceosome reads such short signals, small changes in DNA can redirect it.
A variant that breaks a GT or AG can make the spliceosome skip an exon or use a nearby
site instead. A variant elsewhere can create a new site that the spliceosome uses by
mistake, called a **cryptic splice site**. These variants are easy to miss, because many
lie in introns or don't change the amino acid they sit in (see [Single-Nucleotide
Variation](../03-genomic-variation/02-single-nucleotide-variation.md) and [Insertions
and Deletions](../03-genomic-variation/03-insertions-and-deletions.md)). Using a deep
learning model called SpliceAI, Jaganathan et al. estimated that 9% to 11% of
disease-causing mutations in patients with rare genetic disorders act through cryptic
splicing ([Jaganathan et al., 2019](https://doi.org/10.1016/j.cell.2018.12.015)).

Spinal muscular atrophy (SMA) shows what a difference one base can make. It's caused by
the loss of both working copies of the gene *SMN1*, through deletion or mutation. A
nearly identical gene, *SMN2*, codes for the same protein, but a C-to-T change in its
exon 7, which doesn't change the amino acid, weakens a splicing enhancer and makes the
spliceosome skip that exon in most of its mRNA ([Lorson et al.,
1999](https://doi.org/10.1073/pnas.96.11.6307); [Monani et al.,
1999](https://doi.org/10.1093/hmg/8.7.1177)). One approved drug for SMA is an antisense
oligonucleotide, a short synthetic strand that binds the *SMN2* RNA in the intron after
exon 7 and makes the spliceosome more likely to keep the exon ([Hoy,
2017](https://doi.org/10.1007/s40265-017-0711-7)). In a trial in infants with SMA, 41%
of those given the drug had a motor-milestone response at an interim analysis, compared
with none in the control group ([Finkel et al.,
2017](https://doi.org/10.1056/NEJMoa1702752)).

Splicing can also go wrong across many genes at once. In blood cancers with features of
myelodysplasia, mutations in genes for parts of the splicing machinery, such as *SF3B1*,
*SRSF2*, *U2AF1* (U2AF35) and *ZRSR2*, were found in 45% to 85% of cases, depending on
the type. Most of the mutated parts help recognize the 3′ splice site ([Yoshida et al.,
2011](https://doi.org/10.1038/nature10496)). For more on how cancer develops, see
[Cancer Biology](../02-cancer-biology/00-introduction.md).

## Seeing It in Data

Sequencing reads show which exons were joined. In
[RNA-Seq](../04-next-generation-sequencing/05-types-of-sequencing/03-rna-seq.md), a read
that crosses from one exon to the next shows that the two were spliced together, and a
splice-aware aligner such as `STAR` maps it in two pieces (see [Read
Mapping](../05-from-reads-to-variants/02-read-mapping.md#how-an-aligner-works)). Each
short read covers at most a junction or two, so full isoforms have to be pieced
together. [Long
reads](../04-next-generation-sequencing/04-long-read-sequencing.md#what-long-reads-are-for)
can cover a whole mRNA in one read, showing every exon of an isoform at once.

Annotations such as GENCODE list the known isoforms of each gene. In [GTF/GFF3
Files](../06-genomic-file-formats/06-GTF-GFF3-files.md#try-it), *CFTR* has 45
transcripts, and the MANE Select tag picks one to represent it. Which transcript you
choose makes a difference when you describe a variant, since the same variant can fall
in an exon of one isoform and an intron of another.

## Setting Up

This page uses `samtools` and `curl`, as in [Setting
Up](../05-from-reads-to-variants/01-setting-up.md) in From Reads to Variants. If you
made the `reads-to-variants` or `file-formats` environment, activate it with `conda
activate`. Otherwise, follow [Install the
Tools](../05-from-reads-to-variants/01-setting-up.md#install-the-tools) on that page.
The files on this page take up about 200 MB.

## Try It

Make a folder, then download the GENCODE annotation from [GTF/GFF3
Files](../06-genomic-file-formats/06-GTF-GFF3-files.md#try-it) and pull out the lines
for *BCL2L1*:

```bash
# Make a folder for this page and move into it
mkdir splicing && cd splicing
# Download the GTF file for GENCODE release 50
curl -fLO https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50/gencode.v50.annotation.gtf.gz
# Save every line for BCL2L1 to a file
gunzip -c gencode.v50.annotation.gtf.gz | grep 'gene_name "BCL2L1";' > bcl2l1.gtf
# Show the first eight columns of the gene line
awk -F '\t' '$3 == "gene"' bcl2l1.gtf | cut -f 1-8
# Count its transcripts by type
awk -F '\t' '$3 == "transcript"' bcl2l1.gtf | grep -o 'transcript_type "[^"]*"' | sort | uniq -c | sort -rn
```

```text
chr20	HAVANA	gene	31664452	31723989	.	-	.
  36 transcript_type "protein_coding"
   6 transcript_type "nonsense_mediated_decay"
   1 transcript_type "protein_coding_CDS_not_defined"
```

*BCL2L1* is on chromosome 20, on the `-` strand, so the gene runs from high coordinates
to low. GENCODE lists 43 transcripts for it. Six are labeled `nonsense_mediated_decay`,
because their coding sequence ends more than 50 bases before a splice site, so NMD is
expected to destroy them ([GENCODE
biotypes](https://www.gencodegenes.org/pages/biotypes.html)).

On the GTF page, you added up the `CDS` lines of one transcript to get the length of its
coding sequence. Do the same for every transcript at once, and divide by 3 to get each
protein's length in amino acids:

```bash
# Add up the CDS lengths of each transcript, divide by 3, and count the transcripts with each protein length
awk -F '\t' '$3 == "CDS" {split($9, a, ";"); n[a[2]] += $5 - $4 + 1} END {for (t in n) print n[t] / 3}' bcl2l1.gtf | sort | uniq -c | sort -rn
```

```text
  17 233
   9 170
   6 200
   3 241
   2 307
   2 250
   1 251
   1 231
   1 207
```

`split($9, a, ";")` breaks the attributes apart at each semicolon, so `a[2]` is the
transcript ID, and `n[a[2]]` keeps a running total for each transcript. Many transcripts
make proteins of the same length. Seventeen code for 233 amino acids, the length of
Bcl-xL, and nine for 170, the length of Bcl-xS. Now compare one of each, `BCL2L1-201`
and `BCL2L1-202`:

```bash
# Save the lines for each transcript
grep 'transcript_name "BCL2L1-201";' bcl2l1.gtf > bcl2l1-201.gtf
grep 'transcript_name "BCL2L1-202";' bcl2l1.gtf > bcl2l1-202.gtf
# Show the protein length of each
awk -F '\t' '$3 == "CDS" {n += $5 - $4 + 1} END {print n / 3}' bcl2l1-201.gtf
awk -F '\t' '$3 == "CDS" {n += $5 - $4 + 1} END {print n / 3}' bcl2l1-202.gtf
# Show each exon's 5′ and 3′ ends, one row per exon, with BCL2L1-201 in columns 2–3
# and BCL2L1-202 in columns 4–5
paste <(awk -F '\t' '$3 == "exon" {print $5 "\t" $4}' bcl2l1-201.gtf) \
      <(awk -F '\t' '$3 == "exon" {print $5 "\t" $4}' bcl2l1-202.gtf) | awk '{print NR "\t" $0}'
```

```text
233
170
1	31722868	31722618	31723529	31722618
2	31722348	31721655	31722348	31721844
3	31666086	31664458	31666086	31664452
```

`BCL2L1-201` makes Bcl-xL and is the gene's MANE Select transcript, and `BCL2L1-202`
makes Bcl-xS. Both have three exons, and the GTF lists them in transcript order.
*BCL2L1* is on the `-` strand, so it's read from high coordinates to low. Column 4 of a
GTF line is always the lower coordinate, whatever the strand, which means a `-` strand
exon begins at column 5 and ends at column 4. The command prints them in that order, so
each row reads from an exon's 5′ end to its 3′ end. Each transcript begins at the top
left of its pair of columns, at exon 1, and finishes at the bottom right, at the end of
exon 3.

Exon 1 differs only at its 5′ end, where transcription begins, and the protein doesn't
start until exon 2. Exon 2 is where they part ways. Both copies begin at 31,722,348, but
Bcl-xL's copy runs 31,721,844 − 31,721,655 = 189 bases further before it ends. That's an
alternative 5′ splice site. The 189 bases are 63 codons, and 233 − 170 = 63. UniProt
lists Bcl-xS as missing amino acids 126 to 188 of Bcl-xL. Exon 3 begins at the same
place in both and ends 6 bases apart, after the stop codon.

To see the splice sites themselves, download chromosome 20 of the reference, as in From
Reads to Variants:

```bash
# Download chromosome 20 of GRCh38 from UCSC
curl -fLO https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chr20.fa.gz
# Decompress it to chr20.fa
gunzip chr20.fa.gz
# Index it so tools can jump to any position
samtools faidx chr20.fa
```

`samtools faidx -i` reads a region and reverse-complements it, so it shows the `-`
strand the way the gene reads it ([samtools
faidx](https://www.htslib.org/doc/samtools-faidx.html)). The first two regions below are
the last 8 bases of exon 2 and the first 2 of the intron after it, for Bcl-xS and then
Bcl-xL. The third is the last 10 bases of the intron before exon 2:

```bash
# Read three splice sites on the - strand: the Bcl-xS donor, the Bcl-xL donor and the acceptor before exon 2
samtools faidx -i chr20.fa chr20:31721842-31721851 chr20:31721653-31721662 chr20:31722349-31722358
```

```text
>chr20:31721842-31721851/rc
TTGAACAGGT
>chr20:31721653-31721662/rc
GCGGCTGGGT
>chr20:31722349-31722358/rc
TTTCCTGAAG
```

![Two panels. Top, labeled What samtools faidx -i does: ten bases of chromosome 20, positions 31,721,842 to 31,721,851. The + strand, stored in chr20.fa, reads ACCTGTTCAA from 5′ to 3′. Below it, the − strand, the gene's strand, pairs with each base and reads TGGACAAGTT from 3′ to 5′. Lines cross from each − strand base to its place in the bottom row, labeled -i flips the order. The bottom row, labeled -i prints, holds the same bases backward, TTGAACAGGT, read 5′ to 3′. The first two − strand bases, TG, are highlighted and become the final GT, labeled Bcl-xS donor. Bottom, labeled Three splice sites around exon 2: two transcripts, Bcl-xS and Bcl-xL, drawn as lines for introns and a box for exon 2, starting at 31,722,348. The Bcl-xS exon ends at 31,721,844. The Bcl-xL exon continues 189 more bases, highlighted, to 31,721,655. Each coordinate sits above an exon edge, and a dashed line drops from it to one of three sequences: the acceptor, TTTCCTGAAG, ending in a highlighted AG; the Bcl-xS donor, TTGAACAG then a highlighted GT; and the Bcl-xL donor, GCGGCTGG then a highlighted GT.](../images/7.2-bcl2l1-splice-sites.svg "Reading the splice sites of BCL2L1. Top: chr20.fa holds the + strand, so -i pairs each base with its complement and reads the result backward, giving the sequence the way the gene reads it. Bottom: the three regions from the command, in order along the gene. The Bcl-xS and Bcl-xL donors both start the intron with GT, 189 bases apart, and the acceptor ends the intron before exon 2 with AG. A bar marks the edge of the exon in each sequence. The sequences are from GRCh38.")

[Figure 7.2](#figure-7-2) shows how `-i` gets these sequences and where they sit in the
gene. `/rc` marks each sequence as reverse-complemented. Both donors start the intron
with GT, 189 bases apart, and the acceptor ends it with AG. The spliceosome can use
either GT, and which one it picks decides whether the cell makes a protein that protects
it from dying or one that works against that protection.

That's the end of this exercise. Move out of the folder and delete it:

```bash
# Move up out of the folder
cd ..
# Delete the folder and everything in it
rm -r splicing
```
