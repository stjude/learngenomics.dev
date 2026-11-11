---
title: The Structure of DNA
track: Advanced Topics
sidebar_position: 4
---

The main text treats DNA as a long string of A, C, G and T. That abstraction is all you
need for most genomics work, but a few everyday terms, such as 5′ and 3′, the template
strand, and the reverse complement, only make sense once you look at how the molecule is
built. This guide covers those details.

## Nucleotides

DNA is a chain of building blocks called nucleotides. Each nucleotide has three parts:

- a **phosphate group**;
- a five-carbon sugar called **deoxyribose**;
- one of four bases: adenine (A), guanine (G), cytosine (C) or thymine (T).

A and G are **purines**, which are larger and have two rings: a six-membered ring of
carbon and nitrogen atoms fused to a five-membered ring. C and T are **pyrimidines**,
which are smaller and have a single six-membered ring. Within each group, the bases
share the same ring framework and differ in the atoms attached to it. Adenine carries an
NH2 (amino) group, and guanine carries an oxygen and an NH2 group. Cytosine carries an
NH2 group and an oxygen, and thymine carries two oxygens and a CH3 (methyl) group.
Several of these attached atoms, along with nitrogens in the rings, form the hydrogen
bonds that hold base pairs together ([Figure 7.10](#figure-7-10)).

![The four DNA bases drawn atom by atom, in two rows. The top row, labeled purines, two rings: a six-membered ring fused to a five-membered ring, shows adenine (A) and guanine (G). Each is a six-membered ring of carbon and nitrogen atoms fused to a five-membered ring. Adenine carries an NH2 group, and guanine carries an oxygen and an NH2 group. The bottom row, labeled pyrimidines, one ring: a single six-membered ring, shows cytosine (C), which carries an NH2 group and an oxygen, and thymine (T), which carries two oxygens and a CH3 group. On each base, a short line labeled sugar marks the ring nitrogen that attaches to the sugar.](../images/7.8-dna-bases.svg "The four DNA bases. Adenine and guanine are purines, with a six-membered ring fused to a five-membered ring. Cytosine and thymine are pyrimidines, with a single six-membered ring. Each ring is lightly shaded, and each base attaches to its sugar through the ring nitrogen marked sugar.")

The "deoxy" in deoxyribonucleic acid means the sugar is missing one oxygen atom that the
sugar in RNA, **ribose**, still has.

## The Backbone and Its Direction

The five carbon atoms in each sugar are numbered 1′ to 5′ ("one prime" to "five prime").
The prime mark keeps them distinct from the numbered atoms in the base. The base is
attached to the 1′ carbon, and the oxygen that deoxyribose lacks is the one on the 2′
carbon.

Nucleotides join into a strand through their phosphates: each phosphate links the 3′
carbon of one sugar to the 5′ carbon of the next. This repeating sugar-phosphate chain
forms the **backbone** of the strand, and the bases stick out from it to one side.

Because every link runs from a 3′ carbon to a 5′ carbon, a strand has a direction. One
end, the **5′ end**, finishes with a 5′ carbon (usually carrying a phosphate), and the
other, the **3′ end**, finishes with a 3′ carbon. By convention, sequences are always
written from 5′ to 3′. [Figure 7.9](#figure-7-9) shows the backbone and both ends of
each strand, and [Figure 7.10](#figure-7-10), in the next section, numbers the carbons of
every sugar.

![A short stretch of double-stranded DNA drawn as an untwisted vertical ladder. Each side is a backbone of alternating phosphates, drawn as circles marked P, and sugars, drawn as pentagons. On the first sugar, the 5′ carbon links up to a phosphate, the 3′ carbon links down to the next phosphate, and the 1′ carbon holds the base. Each sugar carries a base pointing inward, and the bases meet in the middle as five pairs, top to bottom A–T, T–A, G–C, C–G and C–G. Purines, A and G, are drawn longer than pyrimidines, T and C, so every rung is the same width. Two dashed hydrogen bonds join each A–T pair and three join each G–C pair. The left strand runs from a 5′ phosphate at the top to a 3′ OH at the bottom, with an arrow pointing down. The right strand runs the other way, from a 5′ phosphate at the bottom to a 3′ OH at the top, with an arrow pointing up.](../images/7.9-dna-ladder.svg "The double helix drawn untwisted. Each strand is a backbone of alternating sugars and phosphates, with a base on each sugar. The strands run in opposite directions, and their bases pair through hydrogen bonds, two for A⁠–⁠T and three for G⁠–⁠C. The left strand reads 5′-ATGCC-3′, the sequence used in Reading the Other Strand.")

The direction matters because the enzymes that build DNA and RNA can only add new
nucleotides to the 3′ end of a growing strand, so every new strand is built from 5′ to
3′. For mRNA, this means:

- the front of the mRNA, made first, is its 5′ end, which is where the **5′ cap** goes;
- the back of the mRNA, made last, is its 3′ end, which is where the poly-A tail goes;
- ribosomes also read mRNA from 5′ to 3′, so they start at the cap end.

## Two Strands, Opposite Directions

The two strands of a DNA double helix run in opposite directions, which is called
**antiparallel**. Where one strand runs 5′ to 3′ from left to right, its partner runs 5′
to 3′ from right to left.

The strands are held together by hydrogen bonds between paired bases. A pairs with T
through two hydrogen bonds, and G pairs with C through three. GC-rich DNA is harder to
pull apart. The extra hydrogen bond explains only part of this. About half of the
difference comes from G and C stacking more strongly on the bases next to them
([Yakovchuk et al., 2006](https://doi.org/10.1093/nar/gkj454)). Every pair joins a
larger purine to a smaller pyrimidine, so each rung of the ladder in [Figure
7.4](#figure-7-9) is the same width.

![Two DNA base pairs drawn atom by atom, one above the other. Each base is a ring structure of carbon and nitrogen atoms in its own shaded area, attached to a deoxyribose sugar, a five-membered ring of four carbons and one oxygen. Phosphate groups, each a phosphorus atom with four oxygens, link the sugars along each strand. In the top pair, adenine on the left faces thymine on the right, joined by two dotted hydrogen bonds. One runs from an N–H on adenine's NH2 group to an oxygen on thymine, and the other from the ring N–H of thymine to a ring nitrogen of adenine. In the bottom pair, guanine on the left faces cytosine on the right, joined by three dotted hydrogen bonds. They run from an N–H on cytosine's NH2 group to guanine's oxygen, from the ring N–H of guanine to a ring nitrogen of cytosine, and from an N–H on guanine's NH2 group to cytosine's oxygen. The left strand runs from a 5′ end with a phosphate at the top to a 3′ end with an OH group at the bottom, with an arrow pointing down. The right strand runs the other way, from a 5′ end with a phosphate at the bottom to a 3′ end with an OH group at the top, with an arrow pointing up. Small numbers 1′ to 5′ label the carbons of each sugar. Each base attaches to the 1′ carbon, each phosphate links the 3′ carbon of one sugar to the 5′ carbon of the next, and each 2′ carbon carries a drawn hydrogen. A legend identifies the shading for phosphate and deoxyribose, and the dotted line for a hydrogen bond.](../images/7.10-dna-base-pairs.svg "Two base pairs drawn atom by atom. The carbons of each sugar are numbered 1′ to 5′: the base attaches to the 1′ carbon, and each phosphate links the 3′ carbon of one sugar to the 5′ carbon of the next. The 2′ carbon carries a hydrogen where RNA has an OH group. Each hydrogen bond links a hydrogen on one base to a nitrogen or oxygen on the other, two in the A⁠–⁠T pair and three in the G⁠–⁠C pair. The two strands run in opposite directions.")

The paired strands twist into a right-handed helix about 2 nanometers wide ([Watson and
Crick, 1953](https://doi.org/10.1038/171737a0)). In solution, each full turn spans about
10.4 base pairs ([Wang, 1979](https://doi.org/10.1073/pnas.76.1.200)). The twist leaves
two grooves of different sizes, the **major groove** and the **minor groove**, along the
outside of the helix. Proteins such as transcription factors read the edges of the bases
exposed in these grooves, so they can recognize a sequence while the DNA stays
double-stranded ([Seeman et al., 1976](https://doi.org/10.1073/pnas.73.3.804); [Rohs et
al., 2010](https://doi.org/10.1146/annurev-biochem-060408-091030)).

## Reading the Other Strand

Because the strands are antiparallel and their bases pair, each strand determines the
other. To write the partner of a sequence from 5′ to 3′, reverse it and swap each base
for its partner. The result is called the **reverse complement**:

```
Strand:              5′-ATGCC-3′
Partner in helix:    3′-TACGG-5′
Reverse complement:  5′-GGCAT-3′
```

This explains the template and coding strands from
[Transcription](../01-biological-foundations/03-transcription.md). RNA polymerase reads
the template strand from 3′ to 5′ so that it can build the RNA from 5′ to 3′. The RNA is
therefore the reverse complement of the template strand, which makes it the same
sequence as the coding strand, with U in place of T.

The reverse complement also comes up constantly in sequencing data. A sequencer reads
whichever strand a DNA fragment came from, so a read may match the reference genome
directly or only after taking its reverse complement. Aligners check both, and file
formats record which strand each read matched.

## How RNA Differs

RNA uses the same backbone chemistry and the same 5′ and 3′ ends, with three
differences:

- its sugar is ribose rather than deoxyribose;
- it uses uracil (U) in place of thymine (T);
- it is usually single-stranded, and often folds back on itself where short stretches of
  its own sequence pair up.

![Two panels. The top panel, titled two linked RNA nucleotides, shows a single RNA strand drawn atom by atom in the same style as the DNA base pairs earlier on this page, with shaded areas for the phosphates, the ribose sugars and the bases. From the 5′ end at the top, a phosphate attaches to the 5′ carbon of a ribose that carries adenine (A) on its 1′ carbon. A second phosphate links the 3′ carbon of that ribose to the 5′ carbon of a second ribose, which carries uracil (U). The second ribose ends in an OH group on its 3′ carbon, the 3′ end, and an arrow beside the strand points down from 5′ to 3′. The sugar carbons are numbered 1′ to 5′, and each ribose carries an OH group on its 2′ carbon. Uracil is a single ring carrying two oxygens and no CH3 group. A legend identifies the phosphate and ribose shading. The bottom panel, titled one strand folding back on itself, shows the strand 5′-GGACUUCGGUCC-3′ lying on its side. From the 5′ end at the top left, GGAC runs to the right along the top, the strand turns through a loop of four bases, UUCG, and GUCC runs back to the left along the bottom to the 3′ end. Arrows above and below the strand show its direction. Each base on top pairs with the base below it through dashed hydrogen bonds: G with C, G with C, A with U, and C with G, with three bonds for each G–C pair and two for the A–U pair. A bracket labels the paired region as the stem, four base pairs, and the loop is labeled UUCG tetraloop.](../images/7.11-rna-structure.svg "RNA up close and folded. The top panel shows the same backbone as DNA, but each ribose sugar carries an OH group on its 2′ carbon, and uracil, which is thymine without its CH3 group, replaces thymine. The bottom panel shows a short strand folded back on itself. GGAC near the 5′ end pairs with GUCC near the 3′ end to form a stem, and the four bases between them, UUCG, form a tetraloop, a loop of four bases.")

The extra oxygen in ribose, part of an OH group on the 2′ carbon, makes RNA less
chemically stable than DNA. It can attack the neighboring phosphate and break the
backbone ([Soukup and Breaker, 1999](https://doi.org/10.1017/s1355838299990891)). This
suits their roles: DNA is the long-term record, and mRNAs are short-lived working
copies. Other RNAs, such as those that make up ribosomes, are far more stable.
