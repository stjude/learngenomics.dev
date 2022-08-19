# BAM Files

The **Sequence Alignment/Map** (or SAM) format is the most common output file format after the read alignment. Typically, these files will be encoded in a binary format, bgzipped, indexed, at which point the file is referred to as a Binary Alignment/Map Format or BAM file. Each BAM file contains a header (typically used for storing metadata) followed by millions of reads, stored as one read per line. Each read contains all of the information available in the FASTQ file (read name, sequence, associated quality score), as well as additional information added by the aligner, including where the read maps to the reference genome, whether the read was produced by PCR or optical duplication, and the quality of the alignment assigned by the mapping software.

Ultimately, a SAM file is a tab-delimited text file that could be piped into standard Unix tools for processing. BAM files can be treated in much the same way if passed through samtools view first. Learn more about it in the associated [documentation](https://samtools.github.io/hts-specs/SAMv1.pdf).

![](../images/6.2-BAM.jpg)