---
title: GTF/GFF3 Files
---

A **gene annotation** describes where the genes are in a reference genome and how each
one is built: its transcripts, the exons that make up each transcript, and, for genes
that make a protein, where the coding sequence starts and stops (see [Genomic Regions
and
Transcription](../01-biological-foundations/03-transcription.md#genomic-regions-and-transcription)).
Two closely related text formats carry it. **GFF3** is version 3 of the General Feature
Format ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)),
and **GTF**, the Gene Transfer Format, "borrows from GFF, but has additional structure"
for describing genes ([GTF2.2 specification](http://mblab.wustl.edu/GTF22.html)).

GFF has a messy history. Groups extended it to fit their own needs until, in the words
of the GFF3 specification, it had "fragmented into multiple incompatible dialects", and
GFF3 was written to bring the most common extensions together ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)).
Both formats are still in wide use, and some annotation projects publish both. GENCODE,
which annotates the human genome, is one ([GENCODE data
format](https://www.gencodegenes.org/pages/data_format.html)), and this page's Try It
uses its files.

## Genes, Transcripts and Exons

Both formats list **features**, one per line. A feature is any annotated stretch of the
genome, such as a gene, a transcript, an exon or the coding part of an exon. Features
nest inside each other. A gene can make several transcripts through alternative splicing
(see [Alternative
Splicing](../01-biological-foundations/03-transcription.md#alternative-splicing)), and
each transcript is made of exons. So besides saying where each feature is, a file has to
say which transcript an exon belongs to and which gene a transcript belongs to. The two
formats do this differently.

In GFF3, a feature can have an `ID`, and a feature inside it names that ID as its
`Parent`. An exon names its transcript, a transcript names its gene, and the lines link
up into a tree. An exon that belongs to two transcripts can name both, separated by a
comma ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)).
GTF doesn't link lines to each other. Instead, every line names the gene and the
transcript it belongs to, as `gene_id` and `transcript_id` ([GTF2.2
specification](http://mblab.wustl.edu/GTF22.html)), so an exon shared by two transcripts
is written twice.

![A made-up gene drawn along a ruler from 1,000 to 4,000. At top, the gene, labeled ID=G1, is a single bar. Below it are two transcripts. The first, labeled ID=T1;Parent=G1, has three exons, E1, E2 and E3, joined by lines, with E2 highlighted. The second, labeled ID=T2;Parent=G1, has only E1 and E3. Below a divider, column 9 of exon E2 is written two ways. GFF3: ID=E2;Parent=T1. GTF: gene_id "G1"; transcript_id "T1";.](../images/6.7-gtf-gff3-files.svg "One gene, two transcripts. In GFF3, each line names its own ID and its parent's, so exon E2 points to transcript T1, which points to gene G1. In GTF, each line names its gene and transcript directly. The data are made up.")

## The Columns

Both formats have nine columns, separated by tabs, and the first eight mean the same
thing in both ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md);
[GTF2.2 specification](http://mblab.wustl.edu/GTF22.html)):

1. **seqid** is the chromosome, named as in the reference. GTF calls it seqname.
2. **source** is where the feature came from, such as the program or database that made
   it. In GENCODE files, it's `HAVANA` or `ENSEMBL`.
3. **type** is what kind of feature it is, such as `gene`, `exon` or `CDS`.
4. **start** is where the feature starts.
5. **end** is where it ends.
6. **score** is a number, such as how confident a prediction program is in the feature.
7. **strand** is `+` or `-`, or `.` if the feature has no strand.
8. **phase** applies to `CDS` lines and says where the first whole codon begins (see
   below). GTF calls it frame.
9. **attributes** is a list of extra information, written differently in the two formats
   (see below).

A field with no value holds `.`. Lines starting with `#` are comments, and a GFF3 file
must begin with a line that names the version, such as `##gff-version 3` ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)).

Start and end are in-base, as in SAM and VCF and unlike BED (see [In-Base and Interbase
Coordinates](05-BED-files.md#in-base-and-interbase-coordinates)). Positions count from
1, and start is never greater than end ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)).
A feature includes the bases at both ends; in the GTF2.2 specification's example, a
start codon, three bases long, runs from 380 to 382 ([GTF2.2
specification](http://mblab.wustl.edu/GTF22.html)). So a feature's length is end minus
start plus 1. A feature on the `-` strand still has the smaller number as its start; the
strand says which way it reads.

In GFF3, the type must come from the Sequence Ontology, a shared list of terms for
features. GTF2.2 requires just three types, `CDS`, `start_codon` and `stop_codon`,
allows a few more, such as `exon`, `5UTR` and `3UTR`, and says that tools will ignore
any others. In GTF, `CDS` covers the coding sequence up to the last codon before the
stop, and the stop codon has a line of its own ([GTF2.2
specification](http://mblab.wustl.edu/GTF22.html)).

### Phase

Introns can fall in the middle of a codon, so the coding sequence of one exon can end
partway through a codon and the next exon finishes it. **Phase** says how many bases at
the start of a `CDS` line belong to a codon that began in the transcript's previous
coding part: 0 means the line starts with a whole codon, and 1 or 2 means that many
bases come first. On the `-` strand, a line reads from its end coordinate, so phase
counts from there. GFF3 requires phase on `CDS` lines and uses `.` on the others ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)).
GTF calls the column frame, defines it the same way and gives it for start and stop
codons too ([GTF2.2 specification](http://mblab.wustl.edu/GTF22.html)). Despite that
name, it isn't a reading frame in the sense of [Reading
Frames](../01-biological-foundations/04-translation.md#reading-frames); phase counts
from the start of each line, not from the start of the coding sequence.

## The Attributes

Column 9 is where the two formats differ most. GFF3 writes attributes as `tag=value`
pairs separated by semicolons, such as `ID=E2;Parent=T1`. Tags are case-sensitive, so
`Parent` isn't the same as `parent`. Characters with a special meaning, such as a tab,
semicolon, equals sign or comma, are written as a `%` and a code instead, such as `%3B`
for a semicolon ([GFF3
specification](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)).

GTF writes each attribute as a key and a value, ending with a semicolon, such as
`gene_id "G1"; transcript_id "T1";`. Text values go in double quotes, but numbers, such
as `exon_number 11;`, often don't. The list must begin with `gene_id` and
`transcript_id`, and each attribute is separated from the next by a single space
([GTF2.2 specification](http://mblab.wustl.edu/GTF22.html)).

Annotation projects add their own attributes. GENCODE gives every gene a `gene_type`,
such as `protein_coding` or `lncRNA`, and a `gene_name`, and every transcript a
`transcript_name`. Optional `tag` attributes flag things like which transcript to treat
as the main one ([GENCODE data
format](https://www.gencodegenes.org/pages/data_format.html)). GENCODE's GTF files also
have `gene` and `transcript` lines, which GTF2.2 doesn't define, and the `gene` lines
have no `transcript_id`. Like GFF before it, GTF has drifted from its specification, so
check the documentation from whoever made a file.

## Sorting and Indexing

GTF files don't have to be sorted. GTF2.2 says the order of lines "is not important"
([GTF2.2 specification](http://mblab.wustl.edu/GTF22.html)), and GENCODE's files go gene
by gene: a gene, then its first transcript and that transcript's exons, then its next
transcript, and so on. That keeps the lines roughly in order, but not exactly; when a
new transcript begins, the positions can jump back.

To look up regions with `tabix`, a file has to be sorted by chromosome and then by
start, compressed with BGZF and indexed with `tabix -p gff` ([tabix
documentation](https://www.htslib.org/doc/tabix.html)). The same option works for GTF,
since the columns are the same.

## Setting Up

This page uses `bgzip` and `tabix` from the `file-formats` environment, and `curl` to
download files, as in [Setting Up](../05-from-reads-to-variants/01-setting-up.md) in
From Reads to Variants. It doesn't need any files from earlier pages. If you've done the
Try It on [BED Files](05-BED-files.md#try-it), run `conda activate file-formats` and `cd
file-formats`. Otherwise, follow [Setting Up](02-FASTQ-files.md#setting-up) on FASTQ
Files. The files on this page take up about 300 MB, and sorting the annotation needs up
to 5 GB more while it runs.

## Try It

GENCODE's human annotation comes as both GTF and GFF3. Each file is over 100 MB
compressed, but you can read the start of one without downloading the whole thing, by
sending it straight to `gunzip`. Compare how the two files link the first three
features, a gene, one of its transcripts and that transcript's first exon:

```bash
# Set the address of GENCODE release 50
GENCODE=https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_50
# Show the first two attributes of the first three features in the GTF file
curl -fsL "$GENCODE/gencode.v50.annotation.gtf.gz" | gunzip -c | grep -v "^#" | head -n 3 | cut -f 9 | cut -d ";" -f 1-2
# Do the same for the GFF3 file
curl -fsL "$GENCODE/gencode.v50.annotation.gff3.gz" | gunzip -c | grep -v "^#" | head -n 3 | cut -f 9 | cut -d ";" -f 1-2
```

```text
gene_id "ENSG00000290825.2"; gene_type "lncRNA"
gene_id "ENSG00000290825.2"; transcript_id "ENST00000832824.1"
gene_id "ENSG00000290825.2"; transcript_id "ENST00000832824.1"
ID=ENSG00000290825.2;gene_id=ENSG00000290825.2
ID=ENST00000832824.1;Parent=ENSG00000290825.2
ID=exon:ENST00000832824.1:1;Parent=ENST00000832824.1
```

`grep -v "^#"` drops the header, and `cut -d ";" -f 1-2` keeps the first two attributes,
since the full lines are long. In the GTF file, the transcript and the exon both carry
the gene and transcript IDs. In the GFF3 file, the exon has an ID of its own and names
the transcript as its parent, and the transcript names the gene. Gene IDs start with
`ENSG` and transcript IDs with `ENST`.

The rest of the Try It uses the GTF file. Download it, about 125 MB, and look at its
header:

```bash
# Download the GTF file
curl -fLO "$GENCODE/gencode.v50.annotation.gtf.gz"
# Show the header
gunzip -c gencode.v50.annotation.gtf.gz | head -n 5
```

```text
##description: evidence-based annotation of the human genome (GRCh38), version 50 (Ensembl 116)
##provider: GENCODE
##contact: gencode-help@ebi.ac.uk
##format: gtf
##date: 2026-04-08
```

The header names the reference, GRCh38, so you know which genome the positions belong
to. GENCODE release 50 is the same annotation as Ensembl release 116. Now count the
features of each type:

```bash
# Count the features of each type, most common first
gunzip -c gencode.v50.annotation.gtf.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -rn
```

```text
5078384 exon
3210731 CDS
1518443 UTR
644292 transcript
358311 start_codon
353665 stop_codon
78733 gene
 155 Selenocysteine
```

There are 78,733 genes, with 644,292 transcripts between them. Not all genes make a
protein, though. Count the genes by their `gene_type`:

```bash
# Count the genes of each type and show the three most common
gunzip -c gencode.v50.annotation.gtf.gz | awk -F '\t' '$3 == "gene"' | grep -o 'gene_type "[^"]*"' | sort | uniq -c | sort -rn | head -n 3
```

```text
34866 gene_type "lncRNA"
20107 gene_type "protein_coding"
9484 gene_type "processed_pseudogene"
```

`awk -F '\t' '$3 == "gene"'` keeps the lines whose third column is `gene`, and `grep -o`
prints just the part of each line that matches. About 20,000 genes code for proteins.
More are long noncoding RNAs, and many are pseudogenes, copies of protein-coding genes
that can no longer make a working protein ([GENCODE
biotypes](https://www.gencodegenes.org/pages/biotypes.html)).

Next, look at one gene. *CFTR* is the gene behind cystic fibrosis from [Haplotype,
Genotype and
Phenotype](../01-biological-foundations/06-genotype-phenotype-haplotype.md). Pull out
its lines and find the gene:

```bash
# Save every line for CFTR to a file
gunzip -c gencode.v50.annotation.gtf.gz | grep 'gene_name "CFTR";' > cftr.gtf
# Show the first eight columns of the gene line
awk -F '\t' '$3 == "gene"' cftr.gtf | cut -f 1-8
# Count its transcripts
awk -F '\t' '$3 == "transcript"' cftr.gtf | wc -l
```

```text
chr7	HAVANA	gene	117287120	117715971	.	+	.
      45
```

*CFTR* spans 428,852 bases of chromosome 7, on the `+` strand, and GENCODE lists 45
transcripts for it. Often you want just one. The tag `MANE_Select` marks the transcript
that GENCODE and NCBI's RefSeq agree on as the representative one for a gene
([MANE](https://www.ncbi.nlm.nih.gov/refseq/MANE/)). Keep that transcript's lines and
count them by type:

```bash
# Save the lines for the MANE Select transcript
grep 'tag "MANE_Select"' cftr.gtf > cftr-201.gtf
# Count the features of each type
cut -f 3 cftr-201.gtf | sort | uniq -c
```

```text
  27 CDS
   2 UTR
  27 exon
   1 start_codon
   1 stop_codon
   1 transcript
```

The transcript, named CFTR-201, has 27 exons. Each has a `CDS` line for its coding part,
and the UTR lines cover the untranslated ends. Look at the phase of the first three
`CDS` lines:

```bash
# Show the start, end and phase of the first three CDS lines
awk -F '\t' '$3 == "CDS"' cftr-201.gtf | cut -f 4,5,8 | head -n 3
```

```text
117480095	117480147	0
117504253	117504363	1
117509034	117509142	1
```

The first `CDS` line runs from 117,480,095 to 117,480,147, which is 53 bases: 17 whole
codons and 2 bases of an 18th. The next exon supplies the 18th codon's last base, so its
`CDS` line has phase 1. Add up all the `CDS` lines to get the length of the coding
sequence:

```bash
# Add up the lengths of the CDS lines
awk -F '\t' '$3 == "CDS" {n += $5 - $4 + 1} END {print n}' cftr-201.gtf
```

```text
4440
```

`$5 - $4 + 1` is end minus start plus 1, the length of an in-base feature. 4,440 bases
make 1,480 codons, and CFTR is 1,480 amino acids long ([UniProt
P13569](https://www.uniprot.org/uniprotkb/P13569/entry)). The stop codon doesn't code
for an amino acid, and in GTF it isn't part of `CDS`, so the numbers match exactly.

F508del, the three-base deletion from Chapter 1, removes bases 117,559,591 to
117,559,593 of chr7 ([ClinVar
VCV000007105](https://www.ncbi.nlm.nih.gov/clinvar/variation/7105/)). Find the features
of CFTR-201 that hold all three:

```bash
# Show the type, start and end of each feature that holds the deletion
awk -F '\t' '$4 <= 117559591 && $5 >= 117559593' cftr-201.gtf | cut -f 3-5
# Show which exon it is
awk -F '\t' '$3 == "exon" && $4 <= 117559591 && $5 >= 117559593' cftr-201.gtf | grep -o 'exon_number [0-9]*'
```

```text
transcript	117480025	117668665
exon	117559464	117559655
CDS	117559464	117559655
exon_number 11
```

The deletion falls in exon 11, in its coding part. That exon's `CDS` line covers the
whole exon, since it's in the middle of the transcript, away from the UTRs.

Last, index the file so you can look up any region. The lines aren't sorted, so sort
them by chromosome and then by start, leaving out the header, and compress the result
with BGZF:

```bash
# Sort the features by chromosome and start, and compress them with BGZF
gunzip -c gencode.v50.annotation.gtf.gz | grep -v "^#" | LC_ALL=C sort -k 1,1 -k 4,4n | bgzip > genes.gtf.gz
# Index it as a GFF file
tabix -p gff genes.gtf.gz
# Count the features of each type that overlap the deletion
tabix genes.gtf.gz chr7:117559591-117559593 | cut -f 3 | sort | uniq -c
```

```text
  23 CDS
   3 UTR
  26 exon
   1 gene
  26 transcript
```

Sorting can take a minute or more, depending on your computer; the lookup is instant. 26
of *CFTR*'s 45 transcripts have an exon that overlaps the deletion, and in 23 of them
it's a coding part. Unlike with BED, both the file and the region you ask for are
in-base, so nothing needs converting.

That's the last exercise in this chapter. Move out of the folder and delete it:

```bash
# Move up out of the folder
cd ..
# Delete the folder and everything in it
rm -r file-formats
```

Next, a look back at the chapter, and where to practice more —
[Conclusion](07-conclusion.md).
