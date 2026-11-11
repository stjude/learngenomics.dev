"""Figure 1.10: A frameshift from one deleted base."""

from figures.core import DARK, DARK_PAGE, FAINT_TEXT, GREY_LINE, INK, PURPLE, T, copyright_text, main, svg_doc
from figures.drawing import pill
from figures.biology import AA, LCIRC_FILL, LCIRC_STROKE, PCIRC_FILL, protein_chain

NAME = "1.10-reading-frames"

PCIRC_STROKE = PURPLE


def frame_row(out, k, x0, cw, n, y_line, y_lab, y_aa, aa_labels):
    d = f"M{x0 * k:.2f} {y_line * k:.2f}H{(x0 + cw * n) * k:.2f}"
    for i in range(n + 1):
        d += f"M{(x0 + cw * i) * k:.2f} {(y_line - 16) * k:.2f}V{y_line * k:.2f}"
    out.append(f'<path class="codon-bracket" d="{d}" stroke="{DARK}" stroke-width="0.6" fill="none"/>')
    out.append('<g class="codon-labels">')
    for i in range(n):
        out.append(T((x0 + cw * (i + 0.5)) * k, y_lab * k, f"Codon {i + 1}", 4.6, 400, anchor="middle"))
    out.append("</g>")
    out.append('<g class="amino-acid-labels">')
    for i, lab in enumerate(aa_labels):
        out.append(T((x0 + cw * (i + 0.5)) * k, y_aa * k, lab, 6.9, 300, anchor="middle"))
    out.append("</g>")


def fig():
    k = 0.30125
    W, H = 2000 * k, 969 * k
    seq = "AUGCCUGAGCCAAGGCUUGAAAACGCCGGUA"
    f1, f2 = "MPEPRLENAG", "MLSQGLKTPV"
    cw, lp = 116.7, 38.97
    MUTED, ns = "#4d4d4f", round(12 * 570.42 / 647.45, 2)
    out = [T(86 * k, 115 * k, "A frameshift from one deleted base", 12.8, 700),
           T(86 * k, 215 * k, "mRNA Sequence", 9.4, 700)]
    out.append('<g class="mrna-sequence">')
    for i, ch in enumerate(seq):
        out.append(T((522 + lp * i) * k, 218 * k, ch, 11.2, 300, anchor="middle"))
    out.append("</g>")
    out.append(f'<path d="M{500 * k:.2f} {236 * k:.2f}H{1722 * k:.2f}" stroke="#111111" stroke-width="1"/>')
    out.append(pill(562 * k, 291 * k, 90 * k, 26 * k, "START"))
    out.append(T(86 * k, 142.2, "Original", 9.4, 700))
    out.append(T(86 * k, 228, "One base", 9.4, 700)); out.append(T(86 * k, 237.5, "deleted", 9.4, 700))
    out.append('<g class="frame-original">')
    frame_row(out, k, 505, cw, 10, 352, 342, 380, [f"{AA[c]} ({c})" for c in f1])
    protein_chain(out, k, 505, cw, 10, 461, f1, LCIRC_FILL, LCIRC_STROKE, x_end=1683)
    out.append("</g>")
    # one-base deletion: C at position 4 removed; codon 1 keeps its place, codons 2-10 move one base right
    y_lab, y_nuc, y_br, y_aa, y_bead = 181, 194.5, 200, 208.7, 232
    starts = [505] + [505 + lp + cw * j for j in range(1, 10)]
    xc = [(s + cw / 2) * k for s in starts]
    hx0, hx1 = starts[1] * k - 1.5, (starts[9] + cw) * k + 1.5
    out.append('<g class="frame-deletion">')
    out.append(f'<rect class="shifted" x="{hx0:.2f}" y="{y_lab - 7.5:.2f}" width="{hx1 - hx0:.2f}" '
               f'height="{y_bead + 18 - (y_lab - 7.5):.2f}" rx="5" fill="{PURPLE}" fill-opacity="0.07"/>')
    out.append('<g class="codon-labels">')
    for i, x in enumerate(xc):
        out.append(T(x, y_lab, f"Codon {i + 1}", 4.6, 400, anchor="middle"))
    out.append("</g>")
    out.append('<g class="nucleotides">')
    for i, ch in enumerate(seq):
        if i != 3:
            out.append(T((522 + lp * i) * k, y_nuc, ch, 11.2, 300, anchor="middle"))
    out.append("</g>")
    xd = (522 + lp * 3) * k
    out.append(f'<g class="deleted-base">{T(xd, y_nuc, "C", 11.2, 400, FAINT_TEXT, "middle")}'
               f'<path d="M{xd - 4.4:.2f} {y_nuc + 1:.2f}L{xd + 4.4:.2f} {y_nuc - 9:.2f}" stroke="{MUTED}" stroke-width="1.1"/>'
               f'{T(xd, 168, "C deleted", ns, 400, MUTED, "middle")}'
               f'<path d="M{xd:.2f} {170.5:.2f}V{183:.2f}" stroke="{MUTED}" stroke-width="0.6"/></g>')
    d = ""
    for a, b in ((starts[0], starts[0] + cw), (starts[1], starts[9] + cw)):
        d += f"M{a * k:.2f} {y_br:.2f}H{b * k:.2f}"
    for s in starts + [starts[0] + cw, starts[9] + cw]:
        d += f"M{s * k:.2f} {y_br - 3.5:.2f}V{y_br:.2f}"
    out.append(f'<path class="codon-bracket" d="{d}" stroke="{DARK}" stroke-width="0.6" fill="none"/>')
    out.append('<g class="amino-acid-labels">')
    for x, c in zip(xc, f2):
        out.append(T(x, y_aa, f"{AA[c]} ({c})", 6.9, 300, anchor="middle"))
    out.append("</g>")
    out.append(f'<g class="protein"><path d="M{xc[0]:.2f} {y_bead:.2f}H{1722 * k:.2f}" stroke="{GREY_LINE}" stroke-width="1.5" fill="none"/>')
    for i, (x, ch) in enumerate(zip(xc, f2)):
        fill, stroke = (LCIRC_FILL, LCIRC_STROKE) if i == 0 else (PCIRC_FILL, PCIRC_STROKE)
        out.append(f'<circle cx="{x:.2f}" cy="{y_bead:.2f}" r="14.2" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>')
        out.append(T(x, y_bead + 4.4, ch, 13.2, 500, INK, "middle", dark=DARK_PAGE))
    out.append("</g></g>")
    out.append('<g class="shift-note">')
    for txt, y in (("Deleting one base", 172), ("shifts every codon", 184.5), ("after it", 197)):
        out.append(T(134, y, txt, ns, 400, MUTED, "end"))
    out.append("</g>")
    out.append(copyright_text(1953 * k, 930 * k))
    svg = svg_doc(W, H, out, "A frameshift from one deleted base")
    # crop used in the guide
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       'width="570.42" height="268.52" viewBox="21.91 17.64 570.42 268.52"')


if __name__ == "__main__":
    main(NAME, fig)
