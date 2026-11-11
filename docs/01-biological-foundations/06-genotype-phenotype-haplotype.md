---
title: Haplotype, Genotype and Phenotype
track: Biological Foundations
---

So far, we've followed a single gene from DNA to a working protein. But as the [first
page of this chapter](01-cells-genomes-dna-chromosomes.md) explained, chromosomes come
in pairs, one inherited from each parent, so nearly every gene comes in two copies. The
two copies often differ, and both are transcribed and translated. This page introduces
three terms for describing those two copies and what they produce, using the *CFTR* gene
from the [previous page](05-protein-folding-and-modification.md) as a running example.

## Haplotype

Each copy of a stretch of DNA is a **haplotype**: the particular sequence on the copy
you inherited from one parent. The different versions of the sequence found at one
position are called **alleles**. For *CFTR*, you might inherit a typical copy from one
parent and, from the other, a copy carrying F508del, the three-base deletion that causes
the protein to misfold.

![Figure showing the relationship between a genotype, a phenotype, and a haplotype](../images/1.14-genotype-phenotype-haplotype.svg "Two copies of the same stretch of DNA. Each copy is a haplotype, the pair of alleles at one position (A/G at position 7) is the genotype, and together they shape observable traits, the phenotype.")

Haplotypes matter because variants on the same copy travel together. They were inherited
together, and they end up in the same transcript and the same protein.

## Genotype

**Genotype** is an overloaded term that can mean one of two things:

- Most commonly within the area of computational genomics, the term genotype refers to
  the particular alleles found at a given position or locus within the genome. For
  example, if position 7 on the chromosome in the figure above contains an `A` on one
  copy and a `G` on the other copy, this is said to be a genotype call of `A/G` at
  position 7.
- Less commonly within the area of computational genomics, the term genotype will be
  used to reference an organism's complete set of genetic material, including all of the
  variants included therein.

Which definition is implied is largely based on the context of the conversation: if one
is talking about a system-wide effect that is likely to be caused by the complicated
interaction(s) between various parts of the organism's genetic code, then the second
definition is more suited. Within computational genomics, we are often concerned with
highly focal changes, hence the preference of the first definition above.

:::info

Throughout this guide, we'll assume the first definition for genotype unless otherwise
specified.

:::

When both copies carry the same allele, the genotype is **homozygous**; when they
differ, it is **heterozygous**. A person with one typical copy of *CFTR* and one F508del
copy is heterozygous at that position.

## Phenotype

An observable trait is called a **phenotype**: eye color, height, blood type, or a
disease such as cystic fibrosis. Phenotypes come from what proteins do, so the question
is what a person's two copies produce together.

For *CFTR*, one working copy makes enough channel protein to do the job. People with one
F508del copy, called **carriers**, don't have cystic fibrosis; only people with no
working copy, such as those with two F508del copies, do. A variant that causes a
phenotype only when both copies carry it is called **recessive**, and cystic fibrosis is
a recessive condition. A variant that causes a phenotype with a single copy, often
because half the normal amount of protein isn't enough or because the faulty protein
interferes with the working one, is called **dominant**.

Most traits are far less tidy. Height, for example, is shaped by thousands of variants
across many genes, plus diet and environment. Untangling these genotype-phenotype
relationships is one of the central goals of genomics. In cancer, the features of the
disease are the phenotype, and the variants in the patient's genome and tumor make up
the genotype, and linking the two helps explain how cancer works.

## Same Genotype, Different Haplotypes

Here's where the three terms come together. Suppose a person is heterozygous for two
different harmful variants in *CFTR*: F508del and G542X, which turns codon 542 into a
stop codon. The genotype calls at both positions are the same either way, but the
phenotype depends on the haplotypes:

- If both variants are on the same copy, the other copy is intact. The person is a
  carrier and, because cystic fibrosis is recessive, doesn't have the disease.
- If one variant is on each copy, neither copy makes a working protein. The person has
  cystic fibrosis.

![Two panels, each showing a person's two copies of the CFTR gene, one from each parent, with the positions of the variants F508del and G542X marked. Left panel, both variants on one copy: the copy from parent 1 carries both variants and makes no working protein. The copy from parent 2 is typical at both positions and makes a working channel. The outcome is a carrier who does not have cystic fibrosis. Right panel, one variant on each copy: the copy from parent 1 carries F508del and the copy from parent 2 carries G542X, so neither makes a working channel. The outcome is cystic fibrosis. Under each panel, the genotype calls are identical, F508del heterozygous and G542X heterozygous, joined by an equals sign.](../images/1.15-same-genotype-different-haplotypes.svg "Same genotype, different haplotypes. Both people have the same genotype calls for two harmful CFTR variants, F508del and G542X. When both variants sit on the same copy, the other copy still makes working protein, so the person is a carrier without the disease. When each copy carries one variant, neither copy works and the person has cystic fibrosis.")

Genotype calls alone can't tell these two cases apart. Working out which variants sit on
the same copy is called **phasing**. Sequencing reads that span both positions can
reveal it directly, and so can the genotypes of the person's parents (if one parent
carries only F508del and the other carries only G542X, the person must have inherited
one variant on each copy).

## Up Next

This chapter used variants such as F508del in *CFTR* to show how a change in DNA can
change a protein and a person. Some of the most consequential changes are the ones that
let a cell grow out of control. [Cancer
Biology](../02-cancer-biology/00-introduction.md) looks at what cancer is, which genes
drive it and how a tumor changes as it grows.
