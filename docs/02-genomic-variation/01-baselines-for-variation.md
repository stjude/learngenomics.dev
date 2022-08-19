# Baselines for Variation

## Introduction

Before we can dive into the types of changes that can occur within a particular
individual's genome, we must first answer the question "changes _in reference to
what_?" After all, there is no "average" human's DNA to compare against—genetic
code is diverging within individuals and larger geographical populations all the
time. How can we compare a single organism's genetic code against a baseline
that is more accurately represented as a graph that is constantly evolving?

## Reference Genome

At least for the moment, the answer is "we don't". The current solution chooses
practicality over the ideal state of things: there is, in fact, a single model
known as the **reference genome** that attempts to recapitulate a consensus
representation for the human genome. This consensus model is curated by the
[Genome Reference Consortium (GRC)], and **patches** to the genome are released
on a regular basis to further improve the model as we learn more about the human
genome.

Genomes for multiple species are maintained by the GRC, and you can view them on
the [GRC's website](https://www.ncbi.nlm.nih.gov/grc/data). In the past, the
naming conventions were more confusing and versions differed based on where you
got the data. However, the academic world has now helpfully synced on the
versioning.

For example, the current version of the human genome is `GRCh38` where `GRC`
stands for the Genome Reference Consortium, `h` stands for human, and `38`
stands for version 38. The UCSC nomenclature (`hg38`) is also used
interchangeably with this version. Unfortunately, previous versions of the
genome versions did not match up on versioning or nomenclature (e.g., `hg19` is
equivalent to `GRCh37` or sometimes `GRCh37-lite` depending on the context), so
you'll need to be careful when using non-current versions of the human genome.
If you find yourself using an older version of the reference genome, the
[Wikipedia page](https://en.wikipedia.org/wiki/Reference_genome) has a helpful
table for comparing these historical genome versions.

:::info

One of the criticisms of the approach outlined above is the lack of accounting
for the diversity amongst the world's populations. For example, [~70% of the
material for the Human Genome Project (the foundation for the reference genome)
came from an anonymous, white male from Buffalo, NY known only as RP11][rp11].
Using this linear, haploid reference genome to quantify variation across diverse
populations is far from perfect, but (from a scientific perspective) the
international genomics community has come up with several strategies for
contextualizing genomic variation within this framework (e.g. population
frequency databases).

Note that in the next version of the reference genome (hg39), the preferred
approach appears to be a graph-based structure that can define variation in a
much wider variety of populations. Clearly this is a step forward, but it also
introduces significant computational challenges to the processing of data. As
such, the correct way to define the next iteration of the reference genome is
currently being discussed, and the release is [indefinitely on
hold](https://www.ncbi.nlm.nih.gov/grc) per the notice on the Genome Reference
Consortium's website.
:::

## The Analysis of Tumors vs. Germline Mutations

Having a matched pair of tumor and germline data is especially valuable in
variant detection because germline data acts as a precise control. The analyst
uses the paring to sort out common but irrelevant SNVs found in the normal
germline tissue from the new cancer driving mutations in the tumor.

Studies that consist only of tumor samples are useful in diagnosing subtypes of
the disease. Cancer subtypes often differ in their rate of progression and
require distinct treatments. Subtyping helps clinicians provide the precise
course of treatment most suited for a given tumor.

Studies that consist only of germline samples are general useful for discovering
genes and variations that are associated with disease. Germline studies are
basic research studies where hundreds of thousands of candidate variations are
systematically filtered to find a few significant variants. Disease associated
variants could be markers for elevated risk or causative mutations that
predispose the subject to disease.


[rp11]: https://www.theatlantic.com/science/archive/2018/11/human-genome-300-million-missing-letters-dna/576481/
[Genome Reference Consortium (GRC)]: https://www.ncbi.nlm.nih.gov/grc