---
title: Common Genomics Tools
track: Engineering Ecosystem
---

Bioinformatics programmers rely on a growing array of tools written by research scientists. These tools were developed for diverse purposes and were written in different languages. The tools run at different levels of efficiency and differ in reliability. Over time the community of bioinformaticians have built up resources to identify the best packages and handle any quirks or deficiencies they may have. Online resources like GitHub, StackOverflow, and Biostars answer questions and offer community support. Further, developers have provided new tools and methods to ease common problems.

A common problem everyone faces is the installation of unfamiliar packages. While there is no perfect system for coordinating the installation these packages, Bioconda comes close. Bioconda is channel or repository of bioinformatics software "recipes" that can be built into conda packages. conda is a package manager that is language and platform independent and is designed to simplify the distribution, installation and management of software packages. conda helps end users easily install packages from other repositories, such as pip, CRAN, CPAN, and Bioconductor. We strongly recommend the use of bioconda, since it is emerging as the modern way to install and work with genomics tools.

## Common Tools

### BLAST

One of the first software packages to align sequences was [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi). BLAST stands for **B**asic **L**ocal **A**lignment **S**earch **T**ool. It is used to find biological similarity between a query sequence and database of sequences. BLAST comes in different forms that can test DNA, RNA or protein sequences and was developed to improve alignment speed which is necessary to perform the large-scale scans. BLAST uses a rule-based similarity metric that is an approximation of slower more exact methods so BLAST is not guaranteed to find the best alignment and may miss potential alignments. It works by first finding short sequences or "words" from the query sequence, ignoring low complexity words. Then, BLAST uses the best words as "seeds" to find likely sequences. Only sequences in the database that have exact seed matches are retained and tested. This greatly reduces the search space speeding up the test. For matched sequences, the region around the seed is extended in both directions and scored for similarity with the query sequence. If the overall score increases, it is extended further; if not, the extension stops. BLAST retains the best score for each test sequence and reports those that pass a statistical test. BLAST has been used extensively to identify genes with similar functions across multiple species.

For more information, see [the NCBI\'s dedicated page to BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi).

### BLAT

The **B**LAST-**l**ike **A**lignment **T**ool (BLAT) is an alignment tool that works like BLAST but is designed to test against genomes rather than discrete sequences. Like BLAST, BLAT tests for short perfect or near-perfect matches and works well matching sequences with a high degree of similarity. BLAT gets its speed by using an indexed version of the genome or database which it retains in memory. BLAT combines more HSPs into larger alignments compared to BLAST.

### BWA

Though foundational in the field, BLAST and BLAT were not designed to handle the large-scale alignment of millions of short sequences to a reference genome. The **B**urrows **W**heeler **A**ligner, or bwa, was developed to do exactly this task. This software relies on the **B**urrows **W**heeler **T**ransform (BWT) that changes strings into sorted array of all suffixes of a string. This is a space saving reversible transform that speeds up alignment so that large scale genomic studies can be completed in a timely manner. The reference genome is transformed once and is then used repeatedly for alignment tasks. The software package BWA includes methods for mapping single and paired-end reads and is commonly used for DNA mapping.

BWA is widely considered to be the standard for mapping DNA sequences to a reference genome---learn more about it at [the associated documentation pages](http://bio-bwa.sourceforge.net/).

### STAR

STAR is an RNA-seq aligner for transcripts that incorporates information about splicing. STAR uses knowledge about the location of exons to index the genome and refine the search for transcript reads. This means that reads that span two exons across a splice site can be accurately mapped. STAR was developed for ENCODE, a public project designed to identify the functional elements in the human genome.

STAR "2-pass mapping" is widely considered to be the standard for mapping RNA sequence to a reference genome ---learn more about it at [the associated documentation pages](https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf).

### Samtools

Samtools is a set of utilities used to perform common operations on SAM/BAM files. Samtools has functions to view, sort, index, merge and assess the quality of aligned sequences contained in a SAM/BAM. Further, samtools can easily transform between SAM/BAM/CRAM files. Samtools is widely used today and is part of every genomic engineer\'s toolkit: find out more about samtools at [the associated documentation pages](http://www.htslib.org/doc/samtools.html).

### Tabix

Tabix is a generic tool for indexing tab-delimited text files allowing efficient seek and retrieval. Tabix was written by the author of samtools and can search through bgzipped compressed files. The indexes it produces allow genomic viewers to efficiently view local regions. Tabix indexes sorted tab-delimited data into large intervals called **bins**. Searches for records begin by looking in bins that overlap the query interval.

## Future Tools

- Picard

- bedtools

- Python libraries

  - pysam

  - BioPython

- R libraries

  - BioConductor

- PERL libraries

  - BioPerl
