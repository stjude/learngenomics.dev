---
title: Long-Read Sequencing
---

import YouTube from '@site/src/components/YouTube';

Short reads are accurate and cheap, but a few hundred bases is often too short.
Long-read instruments read single molecules thousands to hundreds of thousands of bases
long. Two companies make nearly all of them, Pacific Biosciences (PacBio) and Oxford
Nanopore Technologies (ONT), and they read DNA in very different ways. There are other
ways to get long-range information, such as methods that tag short reads from the same
long molecule so software can link them back together, but this page focuses on the two
companies that read long molecules directly. This isn't a complete picture, and the
field changes quickly.

## What Long Reads Are For

A short read that falls inside a repeat longer than itself can't say which copy of the
repeat it came from. A long read can run all the way through the repeat and into unique
sequence on both sides. That one advantage helps in several places:

- **Repeats and hard regions.** Long reads were key to the first complete, gapless
  sequence of a human genome, which filled in the centromeres and other repeats left out
  of the reference for twenty years ([Nurk et al., 2022][nurk]).
- **Structural variants.** A single read can span a whole deletion, insertion or
  inversion, showing both breakpoints and the sequence in between. Many [structural
  variants](../03-genomic-variation/04-structural-variation.md) are invisible to short
  reads ([Chaisson et al., 2019][chaisson]).
- **Phasing.** A read long enough to cover two variants shows whether they sit on the
  same copy of the chromosome, the same
  [haplotype](../01-biological-foundations/06-genotype-phenotype-haplotype.md#haplotype).
- **Whole transcripts.** A long read can cover an entire RNA molecule from end to end,
  showing exactly which exons it contains instead of inferring the
  [splicing](../01-biological-foundations/03-transcription.md#alternative-splicing) from
  pieces. That makes it easier to find new isoforms: long reads of human tissues turned
  up more than 70,000 transcripts missing from gene annotations, some of them shown to
  make protein, and revealed rare variants that disrupt splicing ([Glinos et al.,
  2022][glinos]).
- **Methylation.** Both technologies read the original molecule rather than a copy, so
  chemical marks on the bases, such as methylation, change the signal and can be
  detected directly ([Flusberg et al., 2010][flusberg]; [Simpson et al.,
  2017][simpson]). See [Epigenetic
  Modifications](../07-advanced-topics/epigenetic-modifications.md) under Advanced
  Topics.

## PacBio HiFi Sequencing

PacBio instruments watch a single polymerase copy a single molecule. The library is made
by closing each double-stranded fragment into a loop with hairpin adapters on both ends.
Each loop sits at the bottom of a tiny well, so small that the camera sees light only
from the very bottom, where one polymerase works. As the polymerase adds each base, its
dye gives off a flash, and the camera records the color.

<YouTube
  id="7yYPHatccgw"
  title="PacBio sequencing: how it works"
  provider="PacBio"
  duration="2:46"
>
  PacBio's animation of single-molecule sequencing and HiFi reads.
</YouTube>

Because the molecule is a loop, the polymerase goes around it again and again, reading
both strands many times. Any single pass has many errors, but they fall in different
places on each pass, so software combines the passes into one consensus read. These
**HiFi reads** are typically 10,000 to 20,000 bases long and about 99.8% accurate, on
par with short reads ([Wenger et al., 2019][wenger]). PacBio's current instruments are
the [Revio][revio], built for large projects, and the smaller benchtop [Vega][vega].

![Three panels. a, a double-stranded DNA insert closed into a loop by a hairpin adapter at each end. b, the loop in a tiny well, seen from the side, sitting on a single polymerase at the bottom. Only a thin zone at the bottom of the well is lit, and a flash of light shows a base being added. c, five passes around the loop read the same 12-base sequence, each with one or two errors in a different place. Combining them gives an error-free HiFi read.](../images/4.4-pacbio-hifi.svg "PacBio HiFi sequencing. a, each fragment is closed into a loop by hairpin adapters on both ends. b, the loop sits in a tiny well where a single polymerase copies it, and each added base gives off a flash of light. c, the polymerase goes around the loop many times. Each pass has errors, but in different places, so combining the passes gives one accurate HiFi read.")

## Nanopore Sequencing

ONT instruments pull a single strand of DNA or RNA through a **nanopore**, a protein
pore set in a membrane, with a voltage across it. The bases inside the pore partly block
the flow of ions, and each combination of bases blocks it differently. The instrument
records the current as the strand moves through, and software called a **basecaller**
turns that changing current into a sequence.

<YouTube
  id="VxGliKyYuFQ"
  title="How Oxford Nanopore sequencing works"
  provider="Oxford Nanopore"
  duration="1:04"
>
  Oxford Nanopore's animation of a strand passing through a nanopore.
</YouTube>

There is no fixed read length. A read lasts as long as the molecule, so the length
depends on how gently the DNA was handled. With care, reads can be hundreds of thousands
of bases long; one early study recorded a single read of 882,000 bases ([Jain et al.,
2018][jain]). With current chemistry, the most common read accuracy is about 99%
([Sereika et al., 2022][sereika]). The errors that remain are mostly small insertions
and deletions in runs of the same base, because a run of identical bases looks much the
same in the current as it passes through the pore.

![Two panels. a, a membrane with a single protein pore, with a minus sign above and a plus sign below for the voltage. A motor protein sits on top of the pore and feeds one strand of DNA down through it, while ions flow through the pore. b, a step-like trace of current over time. A basecaller turns it into the sequence T G C A G A A A A A C T G C T A. The run of five A's matches one long flat stretch of the trace, with the note that a run of one base looks flat, so its length is hard to count.](../images/4.5-nanopore-sequencing.svg "Nanopore sequencing. a, a motor protein feeds a single strand through a protein pore in a membrane, with a voltage across it. b, the bases in the pore partly block the flow of ions, so the current changes as the strand moves. A basecaller turns the current trace into a sequence. Runs of the same base give a long flat stretch, which is why most remaining errors are small insertions and deletions in those runs.")

Nanopore instruments range from the [MinION][minion], a pocket-sized device that plugs
into a laptop, to the [PromethION][promethion], which runs many flow cells at once.
Reads stream out while the run is going, so analysis can start, or a run can be stopped,
as soon as there is enough data. ONT can also read RNA directly, without copying it into
cDNA first.

## Short Reads or Long Reads?

| | Short reads (Illumina) | PacBio HiFi | Oxford Nanopore |
| --- | --- | --- | --- |
| Typical read length | 2 × 150 bases | 10,000–20,000 bases | Thousands to over 100,000 bases |
| Typical accuracy | About 99.9% | About 99.8% | About 99% |
| Main errors | Substitutions | Insertions and deletions | Insertions and deletions in runs of one base |
| Methylation | Needs a separate assay | Read directly | Read directly |
| Best for | Small variants, counting, large studies | Accurate genomes, structural variants, phasing | Very long reads, speed, portability |

Short reads cost less per base and remain the default for most work, including
everything on the [assay pages](05-types-of-sequencing/00-introduction.md) that follow.
Long reads are chosen when the question needs them: repeats, structural variants,
phasing or whole transcripts. Many projects use both.

[nurk]: https://doi.org/10.1126/science.abj6987
[chaisson]: https://doi.org/10.1038/s41467-018-08148-z
[glinos]: https://doi.org/10.1038/s41586-022-05035-y
[flusberg]: https://doi.org/10.1038/nmeth.1459
[simpson]: https://doi.org/10.1038/nmeth.4184
[wenger]: https://doi.org/10.1038/s41587-019-0217-9
[jain]: https://doi.org/10.1038/nbt.4060
[sereika]: https://doi.org/10.1038/s41592-022-01539-7
[revio]: https://www.pacb.com/revio/
[vega]: https://www.pacb.com/vega/
[minion]: https://nanoporetech.com/products/sequence/minion
[promethion]: https://nanoporetech.com/products/sequence/promethion
