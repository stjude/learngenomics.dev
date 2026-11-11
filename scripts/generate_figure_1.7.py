"""Figure 1.7: Translation from mRNA to protein."""

import math

from figures.core import BLUE, DARK, T, copyright_text, main, svg_doc
from figures.drawing import arrow, pill, sine_path
from figures.biology import AA, LCIRC_FILL, LCIRC_STROKE, NUC_COL, protein_chain

NAME = "1.7-mrna-to-protein"


def codon_row(out, k, seq, x0, cw, y_lab, y_nuc, y_br, y_aa, aa_labels, show_labels=True):
    """Codon N labels, letters, bracket and amino-acid labels (inputs in guide px, scaled by k)."""
    n = len(seq) // 3
    if show_labels:
        out.append('<g class="codon-labels">')
        for i in range(n):
            out.append(T((x0 + cw * (i + 0.5)) * k, y_lab * k, f"Codon {i + 1}", 5, 400, anchor="middle"))
        out.append("</g>")
    out.append('<g class="nucleotides">')
    for i, ch in enumerate(seq):
        out.append(T((x0 + cw * (i // 3) + cw * (2 * (i % 3) + 1) / 6) * k, y_nuc * k, ch, 11.8, 300, anchor="middle"))
    out.append("</g>")
    d = f"M{x0 * k:.2f} {y_br * k:.2f}H{(x0 + cw * n) * k:.2f}"
    for i in range(n + 1):
        x = (x0 + cw * i) * k
        d += f"M{x:.2f} {(y_br - 16) * k:.2f}V{y_br * k:.2f}"
    out.append(f'<path class="codon-bracket" d="{d}" stroke="{DARK}" stroke-width="0.6" fill="none"/>')
    out.append('<g class="amino-acid-labels">')
    for i, lab in enumerate(aa_labels):
        out.append(T((x0 + cw * (i + 0.5)) * k, y_aa * k, lab, 6.9, 300, anchor="middle"))
    out.append("</g>")


def fig():
    k = 0.30125
    W, H = 2410 / 4, 1077 / 4
    seq = "AUGCCUGAGCCAAGGCUUGAAAACGCCGGU"
    letters = "MPEPRLENAG"
    out = [T(86 * k, 118 * k, "Translation from mRNA to Protein", 12.8, 700)]
    for (a, b), (ya, yb) in ((("Mature", "mRNA"), (325, 365)), (("Nucleotides", "As Codons"), (527, 567)),
                              (("Amino", "Acid Sequence"), (710, 750))):
        out.append(T(86 * k, ya * k, a, 12.3, 700)); out.append(T(86 * k, yb * k, b, 12.3, 700))
    # mRNA wave with nucleotide ticks (4 per trough/peak)
    ticks = seq[:24] + "GCAA" + "GAGU"
    wx0, wcy, wamp, wper = 483, 322, 45, 298
    out.append('<g class="mrna">')
    for g in range(8):
        cx = wx0 + wper / 4 + wper / 2 * g
        trough = g % 2 == 0
        for j in range(4):
            gx = cx - 31.5 + 21 * j
            # Keep the inner ends level and run each tick out until it meets the strand.
            wave = wcy + wamp * math.sin(2 * math.pi * (gx - wx0) / wper)
            y0, y1 = (wave + 2, 320) if trough else (wave - 2, 322)
            out.append(f'<path d="M{gx * k:.2f} {y0 * k:.2f}V{y1 * k:.2f}" stroke="{NUC_COL[ticks[g * 4 + j]]}" stroke-width="1.2"/>')
    out.append(f'<path class="strand" d="{sine_path(wx0 * k, 1680 * k, wcy * k, wamp * k, wper * k)}" stroke="{BLUE}" stroke-width="1.5" fill="none"/>')
    out.append("</g>")
    codon_row(out, k, seq, 505, 116.7, 447, 503, 516, 545,
              [f"{AA[c]} ({c})" for c in letters])
    out.append(pill(563 * k, 591 * k, 90 * k, 26 * k, "START"))
    protein_chain(out, k, 505, 116.7, 10, 735, letters, LCIRC_FILL, LCIRC_STROKE, x_end=1683)
    for y in (322, 537, 735):
        out.append(arrow(1765 * k, 1888 * k, y * k))
    out.append(copyright_text(1953 * k, 865 * k))
    svg = svg_doc(W, H, out, "Translation from mRNA to protein")
    # crop used in the guide
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       'width="570.51" height="248.03" viewBox="21.83 18.55 570.51 248.03"')


if __name__ == "__main__":
    main(NAME, fig)
