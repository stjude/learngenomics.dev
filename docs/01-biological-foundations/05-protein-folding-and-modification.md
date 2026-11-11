---
title: Protein Folding and Modification
description: "What happens to a protein after translation: folding into shape, reaching the right place in the cell, and being switched on and off by chemical marks."
---

import ProteinViewer from '@site/src/components/ProteinViewer';

:::info A Brief Detour

This is a guide to *genomics*, so proteins only get a cameo; **proteomics**, the study
of proteins, could fill a guide of its own. But after following a protein through
transcription and translation, it felt rude to abandon it as a floppy chain at the
ribosome. So here's the rest of its story, in brief.

:::

## From Chain to Shape

The ribosome releases a protein as a long chain of amino acids, but a chain alone can't
do much. To work, it must fold into a precise three-dimensional shape, a process called
**protein folding**. Some amino acids are attracted to water and others repel it, some
carry an electric charge, and some can bond to each other. As the chain folds, the
water-repelling amino acids tend to tuck inside and the charged ones stay on the
surface, until the protein settles into a stable shape. Folding often begins while the
chain is still emerging from the ribosome, and helper proteins called **chaperones**
guide many proteins into the right shape and keep them from clumping together.

A protein's shape decides what it does. An enzyme's shape forms a pocket that fits only
the molecules it acts on, a receptor's shape lets it recognize one particular signal,
and a structural protein such as collagen forms long, strong cables. Larger proteins are
often built from several **domains**, compact sections that each fold on their own and
do one job, such as gripping DNA. Knowing which domain a variant falls in is a strong
clue to what it might break. Because the amino acid sequence largely determines the
shape, scientists can now predict a protein's structure from its sequence alone with
programs such as [AlphaFold](https://alphafold.ebi.ac.uk/), work recognized with the
2024 Nobel Prize in Chemistry.

This also means a small change in the DNA can ruin a protein. The most common variant
behind cystic fibrosis deletes three bases from the *CFTR* gene. Three bases make
exactly one codon, so the reading frame is kept and only one amino acid is lost (see
[Reading Frames](04-translation.md#reading-frames)). Yet that single missing amino acid
is enough to make the protein misfold, and the cell destroys it before it reaches its
place on the cell surface. Misfolded proteins that build up instead of being cleared are
also linked to diseases such as Alzheimer's and Parkinson's.

<ProteinViewer
  number="1.11"
  src="https://files.rcsb.org/download/6MSM.pdb"
  poster="/structures/cftr-6msm"
  description="An interactive 3D model of the CFTR protein, drawn as ribbons. The two membrane domains, in two shades of blue, stand side by side at the top. The two ATP-binding domains, in two shades of green, sit below them. A red sphere marks Phe508 on the first ATP-binding domain, where it meets the membrane domains."
>
  The CFTR protein in 3D. The two membrane domains (blue) form a channel through the cell
  membrane, and the two ATP-binding domains (green) sit just inside the cell. Phe508
  (red) is the amino acid lost in the most common cystic fibrosis variant. Structure from{" "}
  <a href="https://www.rcsb.org/structure/6MSM">PDB 6MSM</a> (Zhang, Liu and Chen, 2018).
</ProteinViewer>

## Getting to the Right Place

A protein also has to end up where it's needed. Proteins that work in the fluid inside
the cell are simply released there, but others carry an address label. A short stretch
at the start of the chain, called a **signal peptide**, sends the ribosome to dock on
the **endoplasmic reticulum** (**ER**), a network of membranes next to the nucleus. The
protein is threaded into the ER as it is made, then passed to the **Golgi apparatus**,
which sorts it and ships it to the cell surface or out of the cell entirely. Other
labels send proteins into the nucleus or the mitochondria. The ER also checks the
folding of everything that passes through it, which is where the misfolded cystic
fibrosis protein is caught and destroyed.

![A simplified cell. At top left, a free ribosome makes a protein chain with no label, which stays in the fluid inside the cell. Beside the nucleus, a ribosome sits on the membrane of the endoplasmic reticulum (ER). The start of its chain, the signal peptide, threads through the membrane into the ER. A misfolded, tangled protein leaves the ER and breaks into fragments, with the note that CFTR F508del is an example. A small bubble carries a finished protein from the ER to the Golgi, a stack of curved sacs. From the Golgi, one bubble delivers a channel protein into the cell membrane at the cell surface, and another fuses with the membrane and releases proteins out of the cell. Along the bottom, a protein with a purple label enters the nucleus and one with an orange label enters a mitochondrion.](../images/1.12-protein-sorting.svg "Getting proteins to the right place. A protein with no address label stays in the fluid inside the cell. A signal peptide sends the ribosome to the ER, where the chain is threaded inside, checked, and passed to the Golgi for delivery to the cell surface or out of the cell. Misfolded proteins are caught at the ER and destroyed, and other labels send proteins into the nucleus or a mitochondrion.")

## Post-Translational Modifications

Many proteins are changed further after they are made, through **post-translational
modifications** (**PTMs**). Other enzymes attach small chemical groups, add sugars, or
cut the chain. Hundreds of kinds are known; a few common ones are:

- **Phosphorylation** adds a phosphate group, which can switch a protein on or off.
  Enzymes called kinases add phosphates and others remove them, so the switch can flip
  within seconds. [Kinases as Switches](#kinases-as-switches) below looks at this switch
  more closely.
- **Glycosylation** adds chains of sugars as proteins pass through the ER and Golgi.
  Most of these proteins are bound for the cell surface or for export, and the sugars
  help them fold, stay stable and be recognized. Your ABO blood type depends on which
  sugars an enzyme encoded by the *ABO* gene adds.
- **Cleavage** cuts a protein into its working form. Insulin, for example, is made as
  one longer chain; a middle piece is cut out, leaving two shorter chains joined
  together.
- **Ubiquitination** attaches a small protein called ubiquitin, which often marks a
  protein for destruction.

Modifications mean that one gene can give rise to many forms of a protein, each with
different activity, and that the amount of a protein in a cell doesn't tell you how much
of it is active. They are also why some medicines can't be made in bacteria: bacteria
can't add human-style sugars, so proteins such as therapeutic antibodies are made in
mammalian cells instead.

## Kinases as Switches

Phosphorylation controls so much of what a cell does, and comes up so often in cancer,
that it's worth a closer look. A **protein kinase**, or kinase for short, is an enzyme
that takes a phosphate group from ATP, the molecule cells use to carry energy, and
attaches it to a serine, threonine or tyrosine in a protein, leaving ADP behind ([Ardito
et al., 2017](https://doi.org/10.3892/ijmm.2017.3036)). The phosphate carries a negative
charge, so adding one can change the protein's shape and, with it, what the protein
does. Enzymes called **phosphatases** take the phosphates off again, which makes the
switch reversible. Human cells make about 535 protein kinases, though about 50 of them
have lost the ability to add phosphates ([Wilson et al.,
2018](https://doi.org/10.1158/0008-5472.can-17-2291)).

Kinases are proteins themselves, and most of them share the same basic shape (Figure
1.13). The chain folds into two lobes, a smaller upper lobe and a larger lower lobe,
joined by a short hinge. ATP fits into the cleft between the lobes, and the target
protein binds right beside it ([Modi & Dunbrack,
2019](https://doi.org/10.1073/pnas.1814279116)). A flexible stretch of the lower lobe,
the **activation loop**, decides whether the target can get in. In many kinases that are
off, the loop folds onto the surface and covers the spot where the target would bind. In
a kinase called ERK, a tyrosine on the loop sits right in that spot ([Zhang et al.,
1994](https://doi.org/10.1038/367704a0)).

Many kinases are switched on when phosphates are added to their activation loop, often
by another kinase. When ERK is switched on, it carries phosphates on a threonine and a
tyrosine in the loop. Their negative charges pair with positively charged arginines on
the kinase, and the loop refolds into a new shape that opens the site where the target
binds ([Canagarajah et al., 1997](https://doi.org/10.1016/s0092-8674(00)80351-7)). Not
every kinase is controlled this way, but the shape of the activation loop governs the
activity of many of them ([Nolen et al.,
2004](https://doi.org/10.1016/j.molcel.2004.08.024)).

![Three stacked steps. Step 1, off: a kinase drawn as an upper lobe and a lower lobe joined on the left by a hinge, with ATP in the cleft between them. The activation loop, a thick curved line, folds into the mouth of the cleft, and a bead marked Y for tyrosine sits inside a dashed circle marking the target site. A bead marked T for threonine sits further along the loop. A down arrow labeled another kinase adds two phosphates, and an up arrow labeled a phosphatase can remove them, lead to step 2. Step 2, on: the same kinase, but the T and Y beads each carry a phosphate marked P, and each phosphate is linked to two small plus signs on the lower lobe. The loop has moved down away from the dashed circle, and a target protein, drawn as a short chain of beads, has docked there with a bead marked S for serine sitting in the circle next to ATP. A short arrow points from ATP's last phosphate to that serine. Step 3, at work, labeled the phosphate moves onto the serine: ATP, drawn as a block marked A with three phosphates, gives its last phosphate to a bead marked S for serine in a chain of beads labeled target protein, with the serine from step 2. An arrow leads to ADP, now with two phosphates, labeled ADP leaves, and a new ATP takes its place, and to the target protein, whose S bead now carries a phosphate, labeled target leaves, now switched on or off.](../images/1.13-kinase-switch.svg "A kinase as a switch. (1) The kinase's two lobes are joined by a hinge, and ATP sits in the cleft between them. While the kinase is off, its activation loop folds shut and a tyrosine (Y) blocks the site where the target protein binds. (2) When another kinase adds phosphates to a threonine (T) and the tyrosine on the loop, their negative charges pair with positive charges on the kinase. The loop refolds, the target site opens, and the target protein docks there. A phosphatase can remove the phosphates and switch the kinase back off. (3) The active kinase moves a phosphate from ATP onto a serine (S) or threonine in the target protein. The target and ADP then leave, the phosphate switches the target on or off, and a new ATP moves in. Simplified from structures of the kinase ERK (Zhang et al., 1994; Canagarajah et al., 1997).")

Once the phosphate has moved, the target lets go, and its new phosphate switches it on
or off. ADP leaves the cleft too, a fresh ATP takes its place, and the kinase is ready
for another target.

Because an active kinase can switch on another kinase, kinases often work in chains,
each one passing the signal to the next. In one well-studied chain, RAF switches on MEK,
and MEK switches on ERK by adding those two phosphates to its activation loop. ERK in
turn adds phosphates to proteins such as ELK1 that switch on genes in the nucleus
([Roskoski, 2012](https://doi.org/10.1016/j.phrs.2012.04.005)). Phosphatases can switch
each step back off, so the signal lasts only as long as something keeps it going.

A kinase that can't be switched off keeps passing its signal on, and many cancers depend
on one. A change called V600E in BRAF, a member of the RAF family, is found in many
melanomas ([Davies et al., 2002](https://doi.org/10.1038/nature00766)). It breaks up the
contacts that hold BRAF's activation loop in its off position, so the kinase stays on
([Wan et al., 2004](https://doi.org/10.1016/s0092-8674(04)00215-6)). Kinases are also
drug targets. The US Food and Drug Administration has approved 94 small-molecule drugs
that block protein kinases, about 80 of them for cancers ([Roskoski,
2026](https://doi.org/10.1016/j.phrs.2026.108107)). [Signaling
Pathways](../02-cancer-biology/04-signaling-pathways.md) follows this chain of kinases
from the cell surface to the nucleus.

## Proteins at Work

Folded, modified and delivered, a protein finally gets to work: building structures,
speeding up chemical reactions, carrying signals and switching genes on and off. Added
up across the trillions of cells in a body, that work produces the traits we can
observe, which is where the next page picks up.
