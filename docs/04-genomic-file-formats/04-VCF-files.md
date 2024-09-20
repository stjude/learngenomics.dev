# VCF Files

The **Variant Call Format** (or VCF) is the most common format for storing variants detected in next-generation sequencing data. Typically, these files will be bgzipped and indexed. Each VCF file contains a header (typically used for storing metadata) and a list of variants. Minimally, each variant contains information about the where the variant lives in the genome and a definition of the change caused by the variant. It also supports storing information about the cohort samples and which samples contain which variants (effectively a [num_variants] X [num_samples] matrix with information on every sample, variant pair.)

Concretely, the minimal VCF looks like this.

| **CHROM** | **POS**   | **ID**     | **REF** | **ALT** | **QUAL** | **FILTER** | **INFO** |
| --------- | --------- | ---------- | ------- | ------- | -------- | ---------- | -------- |
| chr1      | 114713908 | rs11554290 | T       | A       | .        | .          |
| chr17     | 7683718   | .          | C       | CT      | .        | .          |

These fields describe:

- **Variant Location.** Typically, the chromosome, position, reference base(s), and alternative base(s) fields are used to create an "address" of the variant in the genome using the form chrom-pos-ref-alt.

- **Variant Identifier.** The ID field is used to store one or more unique identifiers for the variant. Commonly, the rs numbers from [dbSNP](https://www.ncbi.nlm.nih.gov/snp/) are used.

- **Quality of the Variant.** A measure of confidence in the called variant or lack thereof. This field follows the common practice of encoding qualities as a Phred-scaled quality score with the formula Q = -10 log10(p), where p is the probability of an incorrect variant call. A score of 10 means there is a 1 in 10 chance of the call being incorrect, 20 means a 1 in 100 chance of the call being incorrect, and so on. If unknown, the value should be the missing value, a period.

- **Filter Status.** This denotes the status of whether the variant passed all quality filters from the caller. If the variant passes, the value will be PASS. If the variant fails any filters, the value will be a semi-colon separated list of codes for the filters. If unknown, the value should be the missing value.

- **Additional Information.** A field which can contain an arbitrary number of key-value pairs separated by semicolons of the form /<key/>=/<value1/>[,/<value2/>]. While there are some reserved keys specified in the documentation, anything can be denoted here. If there is no additional information, this field is empty.

As alluded to earlier, the VCF format is flexible in that it *may* specify one or more samples and indicate whether the sample contains any of the variants specified in the file. A simplified version of this would be something like:

**Chromosome** **Position** **ID** **REF** **ALT** **Sample1** **Sample2** **Sample3**

---

chr1 114713908 rs11554290 T A YES NO NO
chr17 7683718 . C CT NO YES YES

However, in practice this is complicated by the fact that variants can have various genotypes (homozygous reference allele, homozygous alternate allele, or heterozygous) and evidence depth. For more information, see the "Genotype fields" section of the [VCF specification](https://samtools.github.io/hts-specs/VCFv4.2.pdf).

Ultimately, a VCF file is just a tab-delimited text file that could be piped into standard Unix tools for processing. Learn more about it [here](https://samtools.github.io/hts-specs/VCFv4.3.pdf).
