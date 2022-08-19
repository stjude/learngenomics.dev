# Genomic File Formats

When working with genomics data for the first time, many engineers are surprised
to find that genomics file types are quite simple in structure. In fact, a
majority of universal file formats such as
[SAM/BAM](https://samtools.github.io/hts-specs/SAMv1.pdf),
[VCF](https://samtools.github.io/hts-specs/VCFv4.2.pdf),
[BED](https://uswest.ensembl.org/info/website/upload/bed.html),
[GFF/GTF](https://uswest.ensembl.org/info/website/upload/gff.html) and many
other custom formats are essentially tab-delimited text files with some form of
compression and/or serialization. In this chapter, we cover the main file
formats one might run into when working in the genomics domain, starting with
common compression schemes.

:::tip
 
Mastery of Unix command line tools such as `vim`,
`grep`, `less`, `cut`, `join`, `sort`, `sed`, and `awk` are essential to working
effectively in this domain. Be sure to brush up on your UNIX command line
skills!

:::
