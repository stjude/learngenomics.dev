---
title: Cells, Chromosomes, and Genomes
track: Biological Foundations
---

## Introduction

:::info Disclaimer

This Guide is written specifically by and for computer scientists and
engineers. The underlying biology in cancer genomics can be exceedingly complex
and requires years of study. Making the content palatable requires drawing
abstractions around these concepts. This guide should be treated as an
introduction to the domain that teaches our audience the material in a
"broad-strokes" fashion. Please be forgiving if you feel we have glossed over
your favorite quirk of cancer genomics. Further, everything within the guide is
presented within a research context and may not be relied on in making decisions
about patients. If you feel anything has been stated incorrectly, you can file
an issue on the Github repository. Please see [the LICENSE.md](https://github.com/stjude/learngenomics.dev/blob/main/LICENSE.md)
for more information.

:::

:::info

Everything in this guide refers to eukaryotic molecular biology, which is the
study of organisms whose DNA is enclosed within a nucleus. Broadly speaking,
most familiar species are eukaryotes, except bacteria which has DNA spread
throughout the cell. At times, this document will be geared towards the
sequencing of human cells specifically.

:::

**Cells** are the smallest unit of life and are the building blocks of organisms, from a
single-celled bacteria to the [trillions of cells that make up the human
body](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002533).
Cells are complicated organized structures that take a variety of forms, forming tissues
and organs and completing the body's functions.

Within nearly every cell is a **genome**. A genome is the complete inherited instruction
set for producing, operating and maintaining a living cell or organism. This information
is physically encoded in a molecule called deoxyribonucleic acid or **DNA**. Among other
things, DNA contains instructions for the assembly of tens of thousands of different
molecular products. These instructions (or recipes) are called **genes**, and the
physical, molecular products genes encode for are called **proteins**. Cells are
constantly reading and interpreting genes stored within the DNA in order to assemble
various proteins. Each cell type in the body produces a complex ecosystem of proteins
that keep the cell alive and executing its specific function.

### Bakery Analogy

To illustrate this phenomenon, imagine the cell as a bakery that makes many different
types of cakes. In this analogy, the genome stored within the DNA is the master recipe
book containing more than 20,000 different cake recipes (genes). The physical cakes that
are made from these recipes are the proteins. Notably, there are a limited number of
copies of the recipe/gene (two copies in the normal case for humans), but you may make
thousands or more physical cakes from those recipes. Depending on the type of cell, the
mixture of different cake flavors, their quantities, and how they interact together will
be different.

:::tip
Keep an eye on this analogy—we will refer back to and build upon it a number of times
during the course of this guide.
:::

## A Mental Model for DNA 

Conceptually, you can think of DNA laid end-to-end as a ~3 billion character long string
consisting only of 'A's, 'C's, 'T's and 'G's. This string and any substring contained
within are commonly referred to as genomic **sequences**. These characters represent the
physical Adenine, Guanine, Thymine, and Cytosine **bases** (or **nucleotides**)
respectively.

Importantly, though it's easy to conceptualize DNA as a single, very long
string, the reality is more complex. DNA is comprised of two complementary sequences
known as **strands**. Each base is actually a member of a **base pair**, whereby
nucleotides complement each other uniquely—'A's pair only with 'T's, and 'G's only with
'C's. Up close, this structure resembles a spiral staircase as seen in the figure below.

![Figure showing computational model and then physical helix for DNA](../images/1.1-DNA.jpg)

When cells divide, the spiral unwinds; each base pair is split; and the molecule is
split into two strands, each one containing the information needed to replicate the
original DNA structure. Normal healthy cells then copy the genetic code very accurately,
rarely introducing variation.

### Physical Structure

In plants and animals, DNA is broken up into a number of large sequences
called **chromosomes** that are tucked into the nucleus. Chromosomes typically
come in pairs (one from your father and one from your mother) and are wrapped
around proteins called **histones**. These histones keep the DNA string tightly 
packaged and help control which gene products are made in a given cell. For humans,
there are normally 22 pairs of **autosomes** (chromosomes shared by both sexes)
and a pair of sex chromosomes (XX for females or XY for males), totaling 23 pairs
of chromosomes. Autosomes are numbered from 1 to 22 based on size, arranged from
largest to smallest. The full set of chromosomes makes up the genome.

## Conclusion

The genome is a vast search space for biological questions. Each genome is a biochemical
database that, if properly accessed, can inform how our bodies function. Genomes account
for the natural differences between individuals, define family traits, and distinguish
how cells in tissues and organs vary. When genomes acquire adverse mutation(s), cancer
as well as other genetic diseases can occur. By examining the relationship between
physical traits (e.g. blood pressure or the development of a tumor) and the genome,
known as **genotype-phenotype relationships**, clinicians can develop personalized
medical treatment based on an individual's genetic makeup.
