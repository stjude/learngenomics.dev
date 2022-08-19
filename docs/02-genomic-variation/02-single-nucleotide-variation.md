---
title: Single Nucleotide Variation
track: Genomic Variation
---

[Single Nucleotide Variants (SNVs) and Single Nucleotide Polymorphisms
(SNPs)](https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism) are the
smallest unit of variation in the genome. Here, just one nucleotide, or base, is
substituted at a single position in the genome (such as changing a 'C' to an 'A'
on chromosome 5, position 1,485,234). The term "**SNV"** is used broadly to
describe an event where a single nucleotide substitution, insertion or deletion
occurs. Single nucleotide polymorphisms, or **SNPs**, are a subset of SNVs where
the change is found in some non-trivial percentage of a population (e.g. \> 1%,
though an exact threshold is not universally agreed upon). By contrast, SNVs
that are not considered SNPs can be very rare and may cause cancer or other
diseases.

![An example single nucleotide variation where an 'A' is substituted in for a 'C'](../images/2.1-SNV.jpg)

In cancer genomics, SNPs are less interesting to researchers than SNVs due to
their prevalence within the population. To illustrate, consider a SNP event
where 45% of the people have an "A" at the specified position and 55% have a "T"
at that position. 45% of the human population does not have cancer, so the
variation is less likely to play a major role in oncogenesis (though they can
absolutely play a role in cancer predisposition).
The [dbSNP](https://www.ncbi.nlm.nih.gov/snp/) database is perhaps the most
widely-used population frequency database.

Determining which of the hundreds of thousands of possible SNVs are important in
a particular disease is done by statistical association or through applying
biological knowledge. Genome-wide association studies (**GWAS**) collect data
from thousands of patient samples with the same disease and statistically
compare their SNVs to those in a normal population. GWAS studies work well for
common diseases that are well-defined and reliably diagnosed. This is especially
true if the number of disease-causing variants is small. However, most diseases
have many genetic variants that influence the disease. Importantly, GWAS studies
only find variants that are linked to disease more closely than expected by
chance. Very often these variants only indicate an interesting genomic location
and do not themselves result in disease.

One downside of GWAS studies is that they require a relatively large number of
samples to gain enough statistical power. In rare diseases like pediatric
cancer, GWAS studies are not as practical due to low sample count. Thus,
researchers apply biological knowledge _a priori_ to improve the odds of finding
relevant SNVs. Commonly scientists focus their efforts on SNVs that fall within
exons of genes that are known be associated with cancer or that are predicted to
alter the protein product. Databases such
as [COSMIC](https://cancer.sanger.ac.uk/cosmic) track variants in cancer genomes
to help identify genes and genomic locations that are commonly mutated and are,
therefore, more likely to be relevant to disease.

As an aside, SNVs and SNPs are often both colloquially referred to "snips".
Strictly speaking, SNVs are not all SNPs, but it is difficult to imagine an easy
pronunciation for "SNVs", so individuals often mix the two concepts in speech
(e.g. "we need to look at the called snips"). You'll need to use context to
delineate whether one is talking about polymorphisms or just single nucleotide
variation in general.
