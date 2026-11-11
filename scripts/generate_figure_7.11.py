"""Figure 7.11: The structure of RNA."""

import math

from figures.core import COPYRIGHT, DARK, DARK_PAGE, GREEN, GREY_LINE, LBLUE, MUTED, ORANGE, PURPLE, T, main, svg_doc
from figures.molecules import TINT
from figures.rna_atoms import panel

NAME = "7.11-rna-structure"

BASE_COL = {"A": PURPLE, "T": LBLUE, "U": LBLUE, "G": GREEN, "C": ORANGE}
PURINES = "AG"


def hairpin(out, y0):
    # 5'-GGAC UUCG GUCC-3' drawn lying on its side: GGAC runs left to right along the top,
    # turns through the UUCG loop, and GUCC runs back along the bottom to pair with it.
    top, loop, bot = "GGAC", "UUCG", "GUCC"
    s, bw, g = 36.0, 22.0, 16.0
    R = 48.0                      # loop radius; equals half the stem height, so no bulge
    D = 2 * R
    span = D - g
    x1 = 112.0
    xs = [x1 + i * s for i in range(4)]
    xc = xs[-1] + 18.0
    yt = y0 + 46
    yb = yt + D
    ym = yt + R
    xl = x1 - 26
    out.append(f'<path d="M{xl:.2f} {yt:.2f}H{xc:.2f}A{R:.2f} {R:.2f} 0 0 1 {xc:.2f} {yb:.2f}H{xl:.2f}" '
               f'fill="none" stroke="{DARK}" stroke-width="2.2" stroke-linecap="round"/>')

    def block(cx, cy, ang, L, b):
        out.append(f'<g transform="translate({cx:.2f} {cy:.2f}) rotate({ang:.2f})">'
                   f'<rect x="0" y="{-bw / 2}" width="{L:.2f}" height="{bw}" rx="3" fill="{BASE_COL[b]}"/></g>')
        a = math.radians(ang)
        out.append(T(cx + math.cos(a) * L / 2, cy + math.sin(a) * L / 2 + 4.5, b, 13, 700,
                     "#ffffff" if b == "A" else DARK, "middle", dark=None if b == "A" else DARK_PAGE))

    for x, a, b in zip(xs, top, reversed(bot)):
        la = span * (0.56 if a in PURINES else 0.44)
        lb = span - la
        block(x, yt, 90, la, a)
        block(x, yb, -90, lb, b)
        n = 3 if a in "GC" else 2
        for o in ([-6, 0, 6] if n == 3 else [-3.5, 3.5]):
            out.append(ln(x + o, yt + la + 3, x + o, yb - lb - 3, DARK, 1.4, ' stroke-dasharray="3 2"'))
    for k, b in enumerate(loop):
        th = math.radians(67.5 - 45 * k)
        px, py = xc + R * math.cos(th), ym - R * math.sin(th)
        block(px, py, math.degrees(math.atan2(ym - py, xc - px)), 18.0, b)

    for x, y, lab in ((xl - 8, yt + 5, "5\u2032"), (xl - 8, yb + 5, "3\u2032")):
        out.append(T(x, y, lab, 14, 700, DARK, "end"))
    ay = yt - 16
    out.append(ln(xs[0] - 10, ay, xs[-1] + 10, ay, DARK, 1.4))
    out.append(f'<path d="M{xs[-1] + 16:.2f} {ay:.2f}l-8 -4v8Z" fill="{DARK}"/>')
    ay = yb + 16
    out.append(ln(xs[0] - 4, ay, xs[-1] + 16, ay, DARK, 1.4))
    out.append(f'<path d="M{xs[0] - 10:.2f} {ay:.2f}l8 -4v8Z" fill="{DARK}"/>')
    tx = xc + R + 14
    out.append(T(tx, ym - 4, "UUCG", 12, 400, MUTED))
    out.append(T(tx, ym + 12, "tetraloop", 12, 400, MUTED))
    out.append(f'<path d="M{xs[0] - 9:.2f} {yb + 30:.2f}v6H{xs[-1] + 9:.2f}v-6" fill="none" stroke="{GREY_LINE}" stroke-width="0.9"/>')
    out.append(T((xs[0] + xs[-1]) / 2, yb + 52, "stem: four base pairs", 12, 400, MUTED, "middle"))
    return yb + 60


def ln(x1, y1, x2, y2, col=DARK, sw=1.6, extra=""):
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"{extra}/>'


def fig():
    W = 400.0
    out = []
    out.append(T(16, 24, "Two linked RNA nucleotides", 13, 700, DARK))
    body, (x0, y0, x1, y1) = panel()
    tx, ty = (W - (x1 - x0)) / 2 - x0, 44 - y0
    out.append(f'<g transform="translate({tx:.2f} {ty:.2f})">')
    out += body
    out.append("</g>")
    ly = y1 + ty + 24
    leg = [(TINT["phosphate"], "phosphate"), (TINT["sugar"], "ribose")]
    tw = sum(25 + len(t) * 6.6 for _, t in leg) + 22
    x = (W - tw) / 2
    for col, txt in leg:
        out.append(f'<rect x="{x:.2f}" y="{ly - 8:.2f}" width="18" height="14" rx="4" fill="{col}"/>')
        out.append(T(x + 25, ly + 3.5, txt, 12, 400, DARK))
        x += 25 + len(txt) * 6.6 + 22
    y1 = ly + 26
    out.append(ln(16, y1, 384, y1, "#d1d3d4", 1))
    out.append(T(16, y1 + 28, "One strand folding back on itself", 13, 700, DARK))
    yb = hairpin(out, y1 + 20)
    H = yb + 20
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "The structure of RNA.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
