---
title: Setting Up
description: "Install the bioinformatics tools from Bioconda and download the HG002 reads, reference and truth set used in this chapter's hands-on steps."
---

The Try It sections in this chapter run every step on real reads from HG002. This page
installs the tools and downloads the data they need. It takes a few minutes and about
200 MB of disk space; the later steps bring the total to about 500 MB.

You'll need a terminal on macOS or Linux. On Windows, use the [Windows Subsystem for
Linux](https://learn.microsoft.com/windows/wsl/install).

## Install the Tools

The tools come from [Bioconda](https://bioconda.github.io/), a collection of
bioinformatics software packaged for the `conda` package manager. If you don't have
`conda` yet, install [Miniforge](https://conda-forge.org/download/), a small installer
that sets `conda` up to use the community-run `conda-forge` channel.

Then create an environment, a self-contained folder of software, with the four tools
this chapter uses:

```bash
# Create an environment named reads-to-variants with the four tools, at fixed versions
conda create -n reads-to-variants --strict-channel-priority -c conda-forge -c bioconda \
  minimap2=2.31 samtools=1.24 bcftools=1.24 rtg-tools=3.13
# Switch to the environment so its tools are on your path
conda activate reads-to-variants
```

- `minimap2` maps reads to a reference.
- `samtools` works with mapped reads.
- `bcftools` calls and filters variants.
- `rtg`, from RTG Tools, compares variant calls with a truth set.

The version numbers pin each tool to the release used to write these pages, so your
output should match ours. Run `conda activate reads-to-variants` again whenever you open
a new terminal.

Then make a folder to work in. Every command in this chapter runs from inside it:

```bash
# Make a folder for the exercise
mkdir reads-to-variants
# Move into it
cd reads-to-variants
```

## Download the Reference

The full GRCh38 reference (see [Baselines for
Variation](../03-genomic-variation/01-baselines-for-variation.md)) is about 3 GB. The
exercise only needs chromosome 20, about 64 million bases, which the UCSC Genome Browser
offers as its own file:

```bash
# Download chromosome 20 of GRCh38 from UCSC
curl -fLO https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chr20.fa.gz
# Decompress it to chr20.fa
gunzip chr20.fa.gz
# Index it so tools can jump to any position
samtools faidx chr20.fa
```

`samtools faidx` writes a small index, `chr20.fa.fai`, that lets tools jump to any
position without reading the whole file. Some of the sequence is in lowercase letters.
UCSC uses lowercase to mark repeats. The tools treat lowercase and uppercase bases
alike, though you may see some lowercase letters in your variant calls.

## Download the Reads

Genome in a Bottle sequenced HG002 to about 300× coverage on Illumina instruments and
published the reads already mapped to GRCh38. We use a 60× subset, which as a single BAM
file is 126 GB, far more than the exercise needs. Fortunately, `samtools` can read one
region of a BAM file over the internet. It first downloads the file's index, then
fetches only the part of the file that covers the region:

```bash
# The address of HG002's 60x BAM file on AWS
BAM=https://giab.s3.amazonaws.com/data/AshkenazimTrio/HG002_NA24385_son/NIST_HiSeq_HG002_Homogeneity-10953946/NHGRI_Illumina300X_AJtrio_novoalign_bams/HG002.GRCh38.60x.1.bam
# Fetch only the reads in one million bases of chromosome 20
samtools view -b -o hg002.region.bam "$BAM" chr20:10000000-11000000
# Put each pair's two reads together, then write Read 1 and Read 2 to separate FASTQs
samtools collate -u -O hg002.region.bam \
  | samtools fastq -1 reads_1.fq.gz -2 reads_2.fq.gz -s /dev/null -0 /dev/null -
```

The region, `chr20:10000000-11000000`, is an ordinary stretch of one million bases that
the truth set covers almost completely. The first command saves its reads to
`hg002.region.bam`. The data is served from the [AWS Open
Data](https://registry.opendata.aws/giab/) copy of Genome in a Bottle, so no account is
needed. `samtools` also leaves a copy of the index, `HG002.GRCh38.60x.1.bam.bai`, in
your folder. It is 9 MB, and you can delete it.

These reads were already mapped, but we want to map them ourselves, so the next two
commands turn them back into FASTQ. `samtools collate` brings the two reads of each pair
together, and `samtools fastq` writes them to two files, Read 1 in `reads_1.fq.gz` and
Read 2 in `reads_2.fq.gz`. Some reads near the edges of the region have a mate that lies
outside it. Those have nowhere to go, so `-s /dev/null` throws them away, and `-0
/dev/null` does the same for any read not marked as either half of a pair. `samtools`
reports what it did:

```text
[M::bam2fq_mainloop] discarded 900 singletons
[M::bam2fq_mainloop] processed 416496 reads
```

That leaves 415,596 reads in 207,798 pairs, stored in the format described on [FASTQ
Files](../06-genomic-file-formats/02-FASTQ-files.md).

## Download the Truth Set

The last download is the truth set you'll check your calls against on [Filtering and
Checking Calls](05-filtering-and-checking-calls.md):

```bash
# The address of the version 5.0q truth set on NCBI
GIAB=https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/AshkenazimTrio/HG002_NA24385_son/v5.0q
# The known variants
curl -fLO "$GIAB/HG002_GRCh38_v5.0q_smvar.vcf.gz"
# Their index
curl -fLO "$GIAB/HG002_GRCh38_v5.0q_smvar.vcf.gz.tbi"
# The regions where the truth set is confident
curl -fLO "$GIAB/HG002_GRCh38_v5.0q_smvar.benchmark.bed"
```

This is Genome in a Bottle's version 5.0q truth set for HG002's small variants. It is
built from a near-complete assembly of both copies of his genome ([Hansen et al.,
2025](https://doi.org/10.1101/2025.09.21.677443)). The truth set comes as a pair. The
VCF lists his variants, with a `.tbi` index, and the BED file lists the regions where
Genome in a Bottle is confident that list is complete and correct. NIST describes
version 5.0q as a draft that is still being refined. Its
[README](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/AshkenazimTrio/HG002_NA24385_son/v5.0q/NIST_HG002_v5.0q_variant-benchmarksets_README.md)
recommends looking closely at a sample of disagreements to see whether the error is in
your calls, in the truth set, or just a different way of writing the same variant.

## Check What You Have

`ls -lh` should now list these files, with these sizes:

```text
8.8M HG002.GRCh38.60x.1.bam.bai
669K HG002_GRCh38_v5.0q_smvar.benchmark.bed
 40M HG002_GRCh38_v5.0q_smvar.vcf.gz
1.5M HG002_GRCh38_v5.0q_smvar.vcf.gz.tbi
 63M chr20.fa
 23B chr20.fa.fai
 37M hg002.region.bam
 24M reads_1.fq.gz
 26M reads_2.fq.gz
```

This dataset covers one million bases of one chromosome, and the reads were picked
because an earlier mapping placed them there. A real analysis maps every read against
the whole genome. That takes far more time and memory, and gives more chances for a read
to land in the wrong place, so the numbers you get here won't match a whole-genome run.

## About the Data

Genome in a Bottle is hosted by the US National Institute of Standards and Technology
(NIST). Data made by NIST staff is not under copyright in the United States, and NIST
asks that you credit it as the source. The reads are described in [Zook et al.,
2016](https://doi.org/10.1038/sdata.2016.25).

Next, map the reads: [Read Mapping](02-read-mapping.md).
