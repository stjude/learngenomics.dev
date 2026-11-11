---
title: Signaling Pathways
description: "How growth signals pass from the cell surface to the nucleus, and how cancer locks the relay on or disables the RB and p53 brakes."
---

A cell in the body doesn't decide to divide on its own. It waits for signals from
outside, such as **growth factors**, small proteins released by other cells. The signal
arrives at the cell's surface, but the genes that carry out division sit in the nucleus,
so a chain of proteins has to carry the message inward. Each protein in the chain
switches on the next, like runners passing a baton. A chain like this is called a
**signaling pathway**.

More than 600 genes are now known to drive cancer when they're mutated
([IntOGen](https://www.intogen.org/search)), but many of their proteins work in the same
few pathways. In a study of more than 9,000 tumors from 33 kinds of cancer, 89% had at
least one driver change in just ten well-known pathways ([Sanchez-Vega et al.,
2018](https://doi.org/10.1016/j.cell.2018.03.035)). This page follows one relay that is
switched on in a large share of cancers, then two brakes, RB and p53, that a tumor has
to get past.

## Passing the Signal

The best-studied relay is the RAS–MAPK pathway, which passes growth signals from the
cell surface to the nucleus. It starts when a growth factor binds a **receptor**, a
protein that spans the cell membrane with one end outside the cell and the other inside.
One example is EGFR, the receptor for epidermal growth factor. EGFR is a kinase, an
enzyme that adds phosphate groups to proteins, and [Kinases as
Switches](../01-biological-foundations/05-protein-folding-and-modification.md#kinases-as-switches)
shows how a phosphate can switch a protein on or off. When the growth factor binds, the
receptor switches on and draws in helper proteins that switch on RAS.

RAS works like a light switch. It holds a small molecule called GDP when it is off and
swaps it for a similar molecule, GTP, to switch on. RAS can turn GTP back into GDP and
switch itself off, but only slowly. Proteins called **GAPs** speed this up, so a pulse
of signal fades quickly once the growth factor is gone ([Simanshu et al.,
2017](https://doi.org/10.1016/j.cell.2017.06.009)).

While RAS is on, it draws in a kinase called RAF. RAF adds a phosphate to a second
kinase, MEK, and MEK does the same to a third, ERK. ERK adds phosphates to many
proteins, which together control whether the cell grows, divides, survives, moves or
matures ([Lavoie et al., 2020](https://doi.org/10.1038/s41580-020-0255-7)). Among the
genes that growth signals switch on is the one for cyclin D1, which comes back in the RB
brake below ([Asghar et al., 2015](https://doi.org/10.1038/nrd4504)).

![A vertical diagram of a cell. At the top, outside the cell, a growth factor sits in the cup of a receptor that crosses the cell membrane. Arrows lead down from the receptor to RAS, then RAF, MEK and ERK, drawn as boxes, and from ERK into the nucleus, where genes for growth and division switch on. A box for NF1 beside RAS has a blunt line pointing at RAS, labeled turns RAS off. Warning markers connect four points to changes found in cancer. The receptor: EGFR or ERBB2, mutated or amplified. RAS: KRAS G12, G13 or Q61, hard to switch off. NF1: NF1 lost, RAS is slow to switch off. RAF: BRAF V600E, on even without RAS.](../images/2.6-ras-mapk.svg "The RAS–MAPK relay. A growth factor switches on its receptor, which switches on RAS, and each protein below switches on the next until the signal reaches the nucleus. NF1 helps switch RAS off. The changes marked on the right, found in tumors, make the relay signal more strongly, for longer or without a growth factor. Based on Simanshu et al. (2017) and Davies et al. (2002).")

## Locking the Relay On

A change in any of several proteins in the relay can keep the signal going after it
should have faded (Figure 2.6). Mutations in RAS genes drive about a third of all human
cancers ([National Cancer
Institute](https://www.cancer.gov/research/key-initiatives/ras/about)). The changes at
amino acids 12, 13 and 61 of KRAS that stand out in [Figure
2.4](03-oncogenes-and-tumor-suppressors.md#figure-2-4) make RAS resistant to GAPs. Once
it picks up GTP, it switches itself off only slowly, so it spends far more of its time
switched on.

*BRAF*, one of the genes for RAF, sits one step further down. When researchers screened
cancers for *BRAF* mutations in 2002, they found them in 66% of the melanomas they
tested, and a single change, now called V600E, made up 80% of them. The changed protein
was a more active kinase, and cancer cells that carried it kept growing without needing
RAS ([Davies et al., 2002](https://doi.org/10.1038/nature00766)).

The relay can also jam when an off switch is lost. *NF1* makes neurofibromin, a GAP for
RAS. In tumors that lose it, RAS stays on for longer, with an effect much like a
mutation in RAS itself. *NF1* is a tumor suppressor that works inside a relay of
oncogenes.

Because so many genes feed into the same relay, the pathway often tells you more than
any one gene. In a study of 230 lung adenocarcinomas, 33% of tumors had a *KRAS*
mutation and 14% had an *EGFR* mutation, but the two were not found in the same tumor.
Changes in *NF1*, *ERBB2* and a few other genes in the relay were more common in the
tumors that had neither. Altogether, 76% of the tumors had the relay switched on in some
way ([Cancer Genome Atlas Research Network, 2014](https://doi.org/10.1038/nature13385)).
A tumor without a *KRAS* mutation may well have the same relay switched on through a
different gene.

## The RB Brake

The decision to divide is made in the nucleus, where RB, the protein made by the
retinoblastoma gene *RB1* from [Two
Hits](03-oncogenes-and-tumor-suppressors.md#two-hits), guards it. RB holds on to
proteins called E2F, which switch on the genes a cell needs to copy its DNA and divide
([Dyson, 2016](https://doi.org/10.1101/gad.282145.116)). Growth signals raise the level
of cyclin D, which partners with the kinases CDK4 and CDK6. Together they add phosphates
to RB, RB lets go of E2F and the cell commits to dividing. A protein called p16, made by
the gene *CDKN2A*, blocks CDK4 and CDK6 and keeps the brake on (Figure 2.7).

![Two diagrams, one above the other. The RB brake: p16 blocks a box for cyclin D plus CDK4/6, which adds phosphates to RB. RB is drawn holding E2F; an arrow labeled RB lets go leads to E2F on its own, which switches on the genes for dividing. Warning markers show ways tumors break this brake: CDKN2A deleted, next to p16; cyclin D1 too much made, and CDK4 or CDK6 extra copies, under the kinase box; RB1 lost, under RB. The p53 brake: oncogene signals switch on ARF, which blocks MDM2. DNA damage also blocks MDM2. MDM2 blocks p53, and p53 leads to dividing stops or the cell dies. Warning markers show CDKN2A deleted under ARF, MDM2 amplified under MDM2 and TP53 mutated under p53. A key marks proteins that push toward division and proteins that hold division back.](../images/2.7-two-brakes.svg "The RB and p53 brakes. In the top half, cyclin D and CDK4/6 add phosphates to RB, which then lets go of E2F, and p16 keeps the brake on by blocking the kinases. In the bottom half, MDM2 keeps p53 in check until oncogene signals, through ARF, or DNA damage block MDM2 and free p53. The marked changes are ways tumors break each brake. CDKN2A appears in both because it makes both p16 and ARF. Based on Asghar et al. (2015) and Kastenhuber and Lowe (2017).")

The brake also responds to the relay. When a relay is jammed on, the cell can make more
p16, which holds RB in place and halts division in a lasting state called **senescence**
([Serrano et al., 1997](https://doi.org/10.1016/s0092-8674(00)81902-9)). To keep
growing, a tumor has to get past this, for example by losing p16.

A tumor can break the brake at any step. It can lose *RB1*, make too much cyclin D1,
carry extra copies of *CDK4* or *CDK6* or delete *CDKN2A*. These changes tend not to
appear together, and different kinds of tumor favor different ones. RB loss is a
hallmark of small cell lung cancer ([George et al.,
2015](https://doi.org/10.1038/nature14664)), too much cyclin D1 is common in breast
cancer ([Tobin and Bergh, 2012](https://doi.org/10.1007/s12609-012-0083-7)) and losing
p16 is particularly common in glioblastoma ([Brennan et al.,
2013](https://doi.org/10.1016/j.cell.2013.09.034)). Some viruses that cause cancer make
proteins that switch RB off.

## The p53 Brake

The protein p53, made by *TP53*, responds to trouble rather than to growth signals. Most
of the time a protein called MDM2 keeps the level of p53 low by marking it for
destruction. Damaged DNA, or the stress caused by an oncogene, frees p53 from MDM2. DNA
damage adds a phosphate to p53 that blocks MDM2 ([Shieh et al.,
1997](https://doi.org/10.1016/s0092-8674(00)80416-x)), and signals from an oncogene
switch on a protein called ARF ([Zindy et al.,
1998](https://doi.org/10.1101/gad.12.15.2424)), which blocks MDM2 directly ([Pomerantz
et al., 1998](https://doi.org/10.1016/s0092-8674(00)81400-2)). Once free, p53 switches
on genes that stop the cell from dividing, such as the gene for p21, which blocks the
kinases that drive the cell cycle. If the damage is too great, p53 can make the cell die
instead ([Kastenhuber and Lowe, 2017](https://doi.org/10.1016/j.cell.2017.08.028)), as
the lower half of Figure 2.7 shows. This is the checkpoint described in [Genes That
Guard the Genome](03-oncogenes-and-tumor-suppressors.md#genes-that-guard-the-genome).

*TP53* is the most frequently mutated gene in human cancer ([Kandoth et al.,
2013](https://doi.org/10.1038/nature12634)), and [Figure
2.5](03-oncogenes-and-tumor-suppressors.md#figure-2-5) shows where its mutations fall. A
tumor can also switch off p53 without touching *TP53*. In a 1992 study, *MDM2* was
amplified in more than a third of 47 sarcomas, which suggested that the extra MDM2 helps
these tumors escape p53's control ([Oliner et al.,
1992](https://doi.org/10.1038/358080a0)).

*CDKN2A* connects the two brakes. The same stretch of DNA is read in two different
[reading frames](../01-biological-foundations/04-translation.md#reading-frames) to make
two unrelated proteins, p16 for the RB brake and ARF for the p53 brake ([Quelle et al.,
1995](https://doi.org/10.1016/0092-8674%2895%2990214-7)). Deleting the gene removes both
at once. [Copy Number
Variation](../03-genomic-variation/05-copy-number-variation.md#copy-number-in-cancer)
describes how tumors lose both copies of *CDKN2A* in many kinds of cancer.

## Up Next

A tumor rarely gets all of these changes at once. [How Tumors
Evolve](05-how-tumors-evolve.md) follows how they build up over time, and why tumors
often find a way around the drugs aimed at them.
