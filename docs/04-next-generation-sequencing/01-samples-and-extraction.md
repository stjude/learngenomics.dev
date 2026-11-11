---
title: Samples and Extraction
description: "Samples for sequencing, such as blood, tumor tissue and cells, how DNA and RNA are kept intact, and how extraction and quality checks work."
---

Every sequencing run starts with something physical: a tube of blood, a piece of a
tumor, a dish of cells. What the sample is and how it was handled decide what the data
can show and which errors it carries, long before any instrument is switched on.

## Kinds of Samples

- **Tumor tissue** comes from a biopsy or from surgery. It is never pure tumor. Blood
  vessels, immune cells and connective tissue are mixed in, and the share of cells that
  are tumor, called the tumor purity, sets how strongly the tumor's variants show up in
  the data. Low purity weakens the signal of copy number changes, as the [copy number
  variation
  page](../03-genomic-variation/05-copy-number-variation.md#tumors-complicate-things)
  shows.
- **A normal sample** carries the person's inherited, germline DNA. Blood is the usual
  source: a standard draw yields plenty, and the white blood cells in it carry the
  person's full genome. (Mature red blood cells have no nucleus and no DNA.) Saliva or a
  cheek swab works too and needs no needle. On its own, a normal sample is all that's
  needed to look for inherited variants. Sequenced alongside a tumor from the same
  patient, it's called a matched normal. Variants found in both are germline and can be
  set aside, leaving the somatic ones, as described in [A Second
  Baseline](../03-genomic-variation/01-baselines-for-variation.md#a-second-baseline-the-persons-own-dna).
  In leukemias, the blood itself carries the cancer, so the normal has to come from
  somewhere else, such as a small skin sample.
- **Cell-free DNA** floats in blood plasma, released by cells as they die. Its fragments
  are short, with one study finding a peak at 166 bases ([Lo et al., 2010][lo]), about
  the length of DNA wrapped around one nucleosome plus a short linker. In healthy
  people, most of it comes from dying blood cells ([Snyder et al., 2016][snyder]), but
  in a person with cancer, some comes from the tumor. That makes it a second way to
  sample a tumor, with different strengths. Tumor tissue needs a biopsy or surgery and
  shows one piece of the tumor at one moment. Cell-free DNA needs only a blood draw,
  which can be repeated to follow a tumor over time, and it can carry DNA from tumors
  anywhere in the body. The catch is that tumor DNA is often a tiny share of what's
  there, so finding it takes [very deep
  sequencing](05-types-of-sequencing/04-targeted-sequencing.md#depth-and-read-setup).
  Sequencing cell-free DNA to study a tumor is called a **liquid biopsy**. The same idea
  lets prenatal tests read a fetus's DNA from the mother's blood.

Samples also come from cultured cell lines and model organisms such as mice, where the
same choices about tissue and handling apply.

## Keeping DNA and RNA Intact

Once tissue is removed from the body, its molecules start to break down, RNA fastest of
all. There are two main ways to stop the clock.

**Fresh frozen** tissue is frozen in liquid nitrogen as soon as possible after
collection and stored at very low temperature. It gives the best DNA and RNA, so it's
generally preferred when it's available. But it needs a freezer chain from the operating
room to the lab.

**FFPE** (formalin-fixed, paraffin-embedded) tissue is soaked in formalin, which locks
molecules in place, then embedded in a block of paraffin wax. FFPE was developed for
looking at tissue under a microscope, long before sequencing, and it is still how
pathology labs keep nearly every biopsy. The blocks keep for decades at room
temperature, so archives hold millions of samples, many with years of follow-up on how
each patient did.

The cost is in the molecules. Formalin breaks DNA into short pieces and chemically
damages bases. The most common damage turns cytosine into uracil, which the sequencer
reads as thymine, so FFPE data carries false C-to-T changes (G-to-A on the other strand)
at low fractions that look like real variants ([Do and Dobrovic, 2015][do-dobrovic]).
Treating the DNA with an enzyme that removes uracil, before it is copied, sharply cuts
these false changes ([Do et al., 2012][do-udg]). Even so, low-fraction C-to-T calls from
FFPE samples deserve suspicion, and important ones are worth confirming with a second
method ([Do and Dobrovic, 2015][do-dobrovic]).

## Extraction and Quality Checks

Extraction breaks cells open, strips away proteins and other debris, and keeps the DNA
or RNA. Before a sample goes further, the lab checks how much there is, how clean it is,
and how intact it is.

For DNA, the amount is usually measured with a fluorescent dye that binds only
double-stranded DNA. An older method, which measures how much UV light the sample
absorbs, also picks up RNA and broken-down DNA, so it reads high, especially for FFPE
samples. It is still useful for spotting leftover protein or chemicals from extraction
([Simbolo et al., 2013][simbolo]). Intactness is measured by sorting the DNA by fragment
size, which gives a **DNA Integrity Number** (DIN). In one study of FFPE tumor samples,
those with a low DIN were far more likely to fail sequencing, though more than half of
them still worked ([Hiramatsu et al., 2023][din]).

For RNA, the most common integrity measure is the **RNA Integrity Number** (RIN), which
scores a sample from 1, badly degraded, to 10, intact ([Schroeder et al., 2006][rin]).

These measurements usually travel with the data as sample metadata. When a sample's
results look strange, its preservation method and quality scores are the first things to
check.

[lo]: https://doi.org/10.1126/scitranslmed.3001720
[snyder]: https://doi.org/10.1016/j.cell.2015.11.050
[do-dobrovic]: https://doi.org/10.1373/clinchem.2014.223040
[do-udg]: https://doi.org/10.18632/oncotarget.503
[simbolo]: https://doi.org/10.1371/journal.pone.0062692
[din]: https://doi.org/10.1093/ajcp/aqad046
[rin]: https://doi.org/10.1186/1471-2199-7-3
