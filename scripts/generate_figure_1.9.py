"""Figure 1.9: Codon lookup table."""

from figures.core import BLUE, NAVY, T, copyright_text, main, svg_doc
from figures.drawing import pill

NAME = "1.9-codon-table"


def fig():
    k = 0.25
    W, H = 1178 * k, 275.35
    X0, X1, Y0, YH, Y1 = 102, 1077, 112, 155, 1054
    cw, rh = (X1 - X0) / 4, (Y1 - YH) / 16
    bases = "UCAG"
    groups = [
        [(0, 2, "phe"), (2, 4, "leu"), (4, 8, "leu"), (8, 11, "ile"), (11, 12, "met"), (12, 16, "val")],
        [(0, 4, "ser"), (4, 8, "pro"), (8, 12, "thr"), (12, 16, "ala")],
        [(0, 2, "tyr"), (2, 4, "STOP"), (4, 6, "his"), (6, 8, "gln"), (8, 10, "asn"), (10, 12, "lys"),
         (12, 14, "asp"), (14, 16, "glu")],
        [(0, 2, "cys"), (2, 3, "STOP"), (3, 4, "trp"), (4, 8, "arg"), (8, 10, "ser"), (10, 12, "arg"), (12, 16, "gly")],
    ]
    out = ['<g class="shading">']
    for b in (0, 2):
        out.append(f'<rect x="{X0 * k:.2f}" y="{(YH + rh * 4 * b) * k:.2f}" width="{(X1 - X0) * k:.2f}" '
                   f'height="{rh * 4 * k:.2f}" fill="#e8f0fb"/>')
    out.append("</g>")
    out.append(f'<rect class="header" x="{X0 * k:.2f}" y="{Y0 * k:.2f}" width="{(X1 - X0) * k:.2f}" '
               f'height="{(YH - Y0) * k:.2f}" fill="{BLUE}"/>')
    # grid: column dividers, then group boundaries inside each column
    d = ""
    for c in range(1, 4):
        d += f"M{(X0 + cw * c) * k:.2f} {Y0 * k:.2f}V{Y1 * k:.2f}"
    for c, gs in enumerate(groups):
        for r0, r1, _ in gs[1:]:
            y = (YH + rh * r0) * k
            d += f"M{(X0 + cw * c) * k:.2f} {y:.2f}H{(X0 + cw * (c + 1)) * k:.2f}"
    out.append(f'<path class="grid" d="{d}" stroke="#7b8a9c" stroke-width="0.35" fill="none"/>')
    out.append(f'<rect class="border" x="{X0 * k:.2f}" y="{Y0 * k:.2f}" width="{(X1 - X0) * k:.2f}" '
               f'height="{(Y1 - Y0) * k:.2f}" fill="none" stroke="{NAVY}" stroke-width="0.6"/>')
    out.append('<g class="header-labels">')
    for c in range(4):
        out.append(T((X0 + cw * c + 61) * k, 140 * k, "code", 4.9, 600, "#ffffff", "middle"))
        out.append(T((X0 + cw * c + 183) * k, 140 * k, "amino acid", 4.9, 600, "#ffffff", "middle"))
    out.append("</g>")
    for c, gs in enumerate(groups):
        out.append(f'<g class="second-{bases[c]}">')
        for r in range(16):
            codon = bases[r // 4] + bases[c] + bases[r % 4]
            out.append(T((X0 + cw * c + 61) * k, (YH + rh * (r + 0.5) + 7) * k, codon, 4.9, 400, anchor="middle"))
        for r0, r1, name in gs:
            cy = (YH + rh * (r0 + r1) / 2 + 7) * k
            if name == "met":  # AUG doubles as the start codon
                out.append(T((X0 + cw * c + 150) * k, cy, name, 4.9, 400, anchor="middle"))
                out.append(pill((X0 + cw * c + 205) * k, cy - 1.7, 17, 6.2, "START", size=4.2))
                continue
            out.append(T((X0 + cw * c + 183) * k, cy, name, 4.9, 400, anchor="middle"))
        out.append("</g>")
    out.append('<g class="position-labels" fill="' + NAVY + '">')
    for c in range(4):
        out.append(T((224 + 243.75 * c) * k, 101 * k, bases[c], 11.5, 700, NAVY, "middle"))
        out.append(T(47 * k, (YH + rh * (4 * c + 2) + 25) * k, bases[c], 15.5, 700, NAVY, "middle"))
        for j in range(4):
            out.append(T(1131 * k, (YH + rh * (4 * c + j + 0.5) + 11) * k, bases[j], 8.6, 700, NAVY, "middle"))
    out.append("</g>")
    out.append('<g class="axis-titles">')
    out.append(T(47 * k, 25 * k, "FIRST", 4.1, 400, anchor="middle"))
    out.append(T(47 * k, 45 * k, "POSITION", 4.1, 400, anchor="middle"))
    out.append(T(589 * k, 35 * k, "SECOND POSITION", 4.1, 400, anchor="middle"))
    out.append(T(1131 * k, 25 * k, "THIRD", 4.1, 400, anchor="middle"))
    out.append(T(1131 * k, 45 * k, "POSITION", 4.1, 400, anchor="middle"))
    out.append("</g>")
    out.append(copyright_text(291, 272.11))
    return svg_doc(W, H, out, "Codon lookup table")


if __name__ == "__main__":
    main(NAME, fig)
