"""Figure 1.14: Genotype, haplotype and phenotype."""

from figures.core import BLUE, NAVY, RED, T, copyright_text, main, svg_doc
from figures.drawing import arrow, pill
from figures.biology import base_path

NAME = "1.14-genotype-phenotype-haplotype"


def fig():
    k = 0.282375
    out = [T(125 * k, 110 * k, "Genomic Sequence", 12.4, 300),
           T(1378 * k, 110 * k, "Physical Effects", 12.4, 300),
           T(125 * k, 200 * k, "Position", 7.6, 400)]
    out.append('<g class="positions">')
    for i in range(12):
        out.append(T((355 + 60 * i) * k, 205 * k, str(i + 1), 11.6, 400, anchor="middle"))
    out.append("</g>")
    for n, seq, label_y, bar_y, stick_top, letter_y in ((1, "AACTCGAGACTG", 408, 412, 308, 483),
                                                        (2, "AATTCGGGACTG", 663, 665, 561, 738)):
        out.append(f'<g class="dna-copy-{n}">')
        out.append(T(125 * k, label_y * k, f"DNA Copy {n}", 8.1, 400))
        for i, ch in enumerate(seq):
            p = base_path(ch, 0, 0, (bar_y - stick_top) * k, 12 * k)
            out.append(p.replace('transform="translate(0.00,0.00)"',
                                 f'transform="translate({(355 + 60 * i) * k:.2f},{bar_y * k:.2f}) rotate(-90)"'))
        out.append(f'<rect x="{340 * k:.2f}" y="{bar_y * k:.2f}" width="{704 * k:.2f}" height="{21 * k:.2f}" fill="{BLUE}"/>')
        for i, ch in enumerate(seq):
            out.append(T((355 + 60 * i) * k, letter_y * k, ch, 11.6, 400, anchor="middle"))
        out.append("</g>")
    out.append(f'<g class="haplotype"><rect x="{318 * k:.2f}" y="{540 * k:.2f}" width="{750 * k:.2f}" height="{225 * k:.2f}" '
               f'rx="{22 * k:.2f}" fill="none" stroke="{RED}" stroke-width="1.4" stroke-dasharray="5 3"/>')
    out.append(T(315 * k, 806 * k, "Haplotype", 8.4, 700, RED) + "</g>")
    out.append(f'<g class="genotype"><rect x="{683 * k:.2f}" y="{283 * k:.2f}" width="{67 * k:.2f}" height="{514 * k:.2f}" '
               f'rx="{30 * k:.2f}" fill="none" stroke="{NAVY}" stroke-width="2.2" stroke-dasharray="0.1 3.4" stroke-linecap="round"/>')
    out.append(T(768 * k, 838 * k, "Genotype at", 8.4, 700, NAVY, "middle"))
    out.append(T(768 * k, 871 * k, "Position 7", 8.4, 700, NAVY, "middle") + "</g>")
    out.append(arrow(1140 * k, 1270 * k, 495 * k))
    out.append('<g class="phenotype">')
    out.append(T(1432 * k, 200 * k, "Phenotype", 8.4, 700, BLUE, "middle"))
    out.append(T(1432 * k, 234 * k, "Examples", 8.4, 700, BLUE, "middle"))
    out.append(f'<circle cx="{1637 * k:.2f}" cy="{529 * k:.2f}" r="{293 * k:.2f}" fill="none" stroke="{BLUE}" '
               f'stroke-width="1.7" stroke-dasharray="3.6 2.4"/>')
    hp = [(1637, 418), "C", (1600, 375), (1520, 368), (1490, 412), "C", (1460, 458), (1470, 515), (1510, 562),
          "L", (1642, 715), "L", (1775, 553), "C", (1812, 505), (1815, 445), (1780, 408), "C", (1740, 365),
          (1670, 375), (1637, 418)]
    d = "M"
    for p in hp:
        if isinstance(p, str):
            d += p
        else:
            d += f"{p[0] * k:.2f} {p[1] * k:.2f} "
    out.append(f'<path class="heart" d="{d.strip()}Z" fill="{RED}"/>')
    out.append(f'<path class="cross" d="M{1622 * k:.2f} {483 * k:.2f}H{1652 * k:.2f}V{514 * k:.2f}H{1684 * k:.2f}V{544 * k:.2f}'
               f'H{1652 * k:.2f}V{575 * k:.2f}H{1622 * k:.2f}V{544 * k:.2f}H{1590 * k:.2f}V{514 * k:.2f}H{1622 * k:.2f}Z" fill="#ffffff" data-dark-fill="#ffffff"/>')
    out.append(pill(1549 * k, 325 * k, 124 * k, 28 * k, "Eye Color", size=4.9))
    out.append(pill(1468 * k, 653 * k, 102 * k, 28 * k, "Cancer", size=4.9))
    out.append(pill(1775 * k, 694 * k, 166 * k, 28 * k, "Blood Pressure", size=4.9))
    out.append("</g>")
    out.append(copyright_text(1963 * k, 913 * k))
    return svg_doc(527, 249.75, out, "Genotype, haplotype and phenotype", origin=(31.3, 14.06), fmt=".2f")


if __name__ == "__main__":
    main(NAME, fig)
