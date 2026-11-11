---
title: Baselines for Variation
---

A variant is a difference, which raises an awkward question: different *from what*?
There is no single "normal" human genome to compare against. Any two people differ at
millions of positions, and as the [Introduction](00-introduction.md) explained, even the
cells within one body slowly drift apart. Genomics settles the question practically:
everyone agrees to compare against the same sequence.

## The Reference Genome

That shared sequence is the **reference genome**. In practice it is a file of about 3.1
billion bases, with one long sequence for each chromosome. You have two copies of each,
but the reference has just one, so it can't show both of a person's haplotypes. Nor is
it any one person. About 70% of it comes from a single anonymous volunteer from Buffalo,
New York, known as RP11, and the rest is stitched together from [more than 20
others][hprc-home].

Because everyone uses the same reference, any position in the genome can be named by a
**coordinate**: the chromosome, then the position counting from its start. F508del, for
example, sits at `chr7:117,559,592`. At each position, the base in the reference is
called the **reference allele** (often shortened to REF), and a different base seen in a
sample is an **alternate allele** (ALT). These are the names of two columns you will
meet in [VCF files](../06-genomic-file-formats/04-VCF-files.md).

The reference also gives genotypes a fixed point of comparison. You have two copies of
most positions, so the labels [homozygous and
heterozygous](../01-biological-foundations/06-genotype-phenotype-haplotype.md#genotype)
can be stated relative to it. If both copies carry the reference allele, the genotype is
**homozygous (ref)**. If one carries the reference allele and the other an alternate
allele, it is heterozygous. If both carry the same alternate allele, it is **homozygous
(alt)**. Nearly every position in anyone's genome is homozygous (ref), so a list of
variant calls usually includes only the other two. VCF files write these three as `0/0`,
`0/1` and `1/1`. Each number stands for the allele on one of the two copies: `0` is the
reference allele and `1` is the alternate allele. If a position has a second alternate
allele, it is written as `2`.

![A reference sequence of 14 bases at positions 101 to 114 on chromosome 7, above a person's two copies, one from each parent. At position 105, the copy from parent 1 has A where the reference has G, and the other copy matches. At position 111, both copies have T where the reference has C. A variant calls table lists the two: chr7:105, REF G, ALT A, heterozygous; and chr7:111, REF C, ALT T, homozygous (alt).](../images/3.1-reference-and-variant-calls.svg "From reference to variant calls. The reference gives every position a coordinate. Wherever one of a person's two copies differs from it, the difference is recorded as a variant call: its position, the reference base (REF), the sample's base (ALT) and the genotype.")

The reference allele only means "whatever the reference has". It isn't necessarily the
healthy version or even the most common one. At many positions the reference carries the
[rarer allele][ballouz]. Historically, it's even carried alleles [linked to a higher
risk of disease][chen-butte], including type 1 diabetes.

## Versions and Their Traps

The human reference is maintained by the [Genome Reference Consortium (GRC)], which also
looks after the mouse, zebrafish and chicken genomes. The current version is `GRCh38`:
`GRC` for the consortium, `h` for human and `38` for the version. The UCSC Genome
Browser calls the same version `hg38`, and the previous version, `GRCh37`, is known
there as `hg19`. The GRC also releases **patches** (the latest is `GRCh38.p14`, from
2022), which fix errors and add sequence without moving any existing coordinates.

Versions cause some of the most common mistakes in genomics:

- **Coordinates don't carry over between versions.** F508del is at `chr7:117,559,592` in
  GRCh38 but `chr7:117,199,646` in GRCh37. Always record which version your data uses.
  Converting positions from one version to another is called **liftover**, and it can
  fail in regions that changed a lot.
- **Chromosome names differ.** UCSC names chromosomes `chr1`, `chr2` and `chrM`, while
  the GRC and Ensembl use `1`, `2` and `MT`. Tools given files with different
  conventions often report no matches at all instead of raising an error.
- **Similar names hide small differences.** `hg19` and `GRCh37` have the same chromosome
  sequences, but different mitochondrial sequences, and distributions such as
  `GRCh37-lite` add or leave out extra sequences. Files built on one don't always work
  with another. If you have to work with older versions, the [Wikipedia
  page](https://en.wikipedia.org/wiki/Reference_genome) has a helpful table comparing
  them.

## How Common Is a Variant?

Comparing against the reference says only that a sample is different. To learn whether
that difference is unusual, analysts turn to population frequency databases such as
[gnomAD](https://gnomad.broadinstitute.org/), which collects sequencing data from
hundreds of thousands of people and records how often each allele appears, overall and
within different ancestry groups. A variant carried by one person in ten is very
unlikely to cause a rare, severe disease, while one never seen before deserves a closer
look (as does one seen frequently in people with the disease). That last kind of
evidence comes from a different source: databases such as
[ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) collect reports from labs and
researchers on which variants have been linked to disease, and how confidently.

## Beyond a Single Reference

One genome, mostly from one person, can't represent everyone. Because so much of the
reference is RP11, his DNA quietly became the yardstick for everyone else's. Wherever he
happened to carry a rare allele, most people show up as "different", and any stretch of
DNA he lacked can be missing from the reference altogether. A [2019 study][sherman] of
910 people of African descent found about 300 million bases of DNA missing from the
reference. Reads from those regions have nowhere to map, so the variants in them are
easy to miss, and people whose ancestry is less well represented are affected most.

Two newer efforts are filling the gaps. In 2022, the Telomere-to-Telomere Consortium
published [T2T-CHM13](https://www.science.org/doi/10.1126/science.abj6987), the first
complete, gap-free human genome, adding about 8% of the genome that GRCh38 was missing.
In 2023, the Human Pangenome Reference Consortium released a [draft human
pangenome](https://www.nature.com/articles/s41586-023-05896-x) built from 47 people, and
a [second release][hprc-r2] in 2025 expanded it to 232. Instead of one sequence, a
pangenome stores many genomes together, branching wherever they differ. That eases the
yardstick problem, but a graph brings [challenges of its own][hprc]:

- **No single set of coordinates.** A position in a graph depends on which path you take
  through it, while gene annotations, disease databases and VCF files all use linear
  coordinates. Today's pangenome workflows usually map reads to the graph, then
  translate the results back onto GRCh38.
- **No single right way to build one.** Aligning many whole genomes involves judgment
  calls, especially for repeated and duplicated DNA. In the draft pangenome, one
  construction method merged the extra copies of duplicated genes and repeats into a
  single copy, while the others kept them separate. Another left out most centromeric
  repeats, which are hard to align and often misassembled.
- **More variation can make mapping harder.** Every rare branch is another place a read
  might plausibly land. The draft pangenome's graph for mapping short reads leaves out
  any sequence carried by fewer than 9 of its 90 genome copies, about 10%.
- **New tools and formats.** Graphs need their own file formats and software, while most
  of the ecosystem, including the rest of this guide, is still built around a linear
  reference.
- **Only as diverse as the people in it.** A few hundred people is still a small sample
  of humanity, and any group left out faces the same gaps as before.

In the meantime, the GRC has [postponed GRCh39
indefinitely](https://www.ncbi.nlm.nih.gov/grc) while it evaluates these new models, and
most data is still analyzed against GRCh38.

## A Second Baseline: The Person's Own DNA

For somatic variants, the best baseline is the person themselves. In cancer, analysts
often sequence the tumor alongside a **matched normal** sample, usually blood, from the
same person. Variants found in both are germline, and variants found only in the tumor
are likely somatic. Both are important: for example, an inherited variant in *BRCA1*
raises the risk of breast and ovarian cancer, while the somatic variants are what drive
this particular tumor.

![Three rows of DNA bases at positions 101 to 114 on chromosome 17: the reference genome, a matched normal sample from blood, and the tumor. The normal differs from the reference at positions 106 and 112. These germline variants are shown in purple and appear again in the tumor. The tumor also differs from the normal at positions 103 and 109. These somatic variants are shown in red. A final row compares the tumor directly with the reference: all four differences appear in the same grey, with no way to tell germline from somatic.](../images/3.2-reference-normal-tumor.svg "Separating germline from somatic variants. Differences between the matched normal and the reference are germline variants, which the tumor also carries. Differences between the tumor and the normal are somatic variants. Compared with the reference alone, the tumor shows both kinds mixed together.")

Without a matched normal, a tumor-only analysis has to guess which variants are
germline, usually by checking how common they are in population databases. That works
less well, especially for people whose ancestry is underrepresented in those databases.
Studies of germline samples alone answer a different question: which variants run in
families or raise the risk of disease.

[Genome Reference Consortium (GRC)]: https://www.ncbi.nlm.nih.gov/grc
[ballouz]: https://doi.org/10.1186/s13059-019-1774-4
[chen-butte]: https://pubmed.ncbi.nlm.nih.gov/21121051/
[sherman]: https://www.nature.com/articles/s41588-018-0273-y
[hprc]: https://www.nature.com/articles/s41586-023-05896-x
[hprc-r2]: https://humanpangenome.org/news/hprc-data-release-2/
[hprc-home]: https://humanpangenome.org/
