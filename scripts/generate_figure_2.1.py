"""Figure 2.1: A tumor grows from one cell through successive mutations and clonal expansion."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, ORANGE, T, main, svg_doc

NAME = "2.1-clonal-expansion"

N = 17
X0, X1 = 10.0, 390.0
CW = (X1 - X0) / N
BH, PH = 30.0, 19.0
STYLE = {0: ("#ffffff", "#c4c5c8"), 1: ("#a9dcec", "#4f9fbb"), 2: (BLUE, "#0b3f80"), 3: (ORANGE, "#a8650a")}
STROMA = "#efeeec"


def cell(out, x, y, w, h, k, rx=5.0):
    fill, nuc = STYLE[k]
    out.append(f'<rect x="{x + 0.6:.2f}" y="{y + 0.6:.2f}" width="{w - 1.2:.2f}" height="{h - 1.2:.2f}" rx="{rx}" '
               f'fill="{fill}" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    cy = y + h * (0.62 if h > 24 else 0.5)
    out.append(f'<ellipse cx="{x + w / 2:.2f}" cy="{cy:.2f}" rx="{w * 0.2:.2f}" ry="{min(h * 0.17, 4.2):.2f}" fill="{nuc}"/>')


def line(x0, y0, x1, y1, col=GREY_LINE, sw=0.8):
    return f'<path d="M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}" stroke="{col}" stroke-width="{sw}" fill="none"/>'


def row(out, y, title, base, piles, stroma_h, invade=None, gap=None, notes=()):
    """base: list of N kinds. piles: list of (layer, start_halfcol, kinds) from the base upward."""
    num, title = title.split("  ")
    out.append(T(X0, y, num, 13, 700, DARK))
    out.append(T(X0 + 13, y, title, 13, 700, DARK))
    layers = max([p[0] for p in piles], default=0)
    top = y + 12
    yb = top + layers * PH
    for layer, start, kinds in piles:
        ly = yb - layer * PH
        for j, k in enumerate(kinds):
            x = X0 + (start / 2 + j) * CW
            cell(out, x, ly, CW, PH, k, 7)
    for i, k in enumerate(base):
        cell(out, X0 + i * CW, yb, CW, BH, k)
    ym = yb + BH + 1.4
    out.append(f'<rect x="{X0:.2f}" y="{ym:.2f}" width="{X1 - X0:.2f}" height="{stroma_h:.2f}" fill="{STROMA}"/>')
    if gap:
        g0, g1 = X0 + gap[0] * CW, X0 + gap[1] * CW
        out.append(f'<path d="M{X0:.2f} {ym:.2f}H{g0:.2f}M{g1:.2f} {ym:.2f}H{X1:.2f}" stroke="{DARK}" stroke-width="2.4" fill="none"/>')
        out.append(f'<path d="M{g0:.2f} {ym:.2f}l3 4M{g1:.2f} {ym:.2f}l-3 4" stroke="{DARK}" stroke-width="1.6" fill="none"/>')
    else:
        out.append(f'<path d="M{X0:.2f} {ym:.2f}H{X1:.2f}" stroke="{DARK}" stroke-width="2.4" fill="none"/>')
    for (cx, cy) in invade or ():
        cell(out, X0 + cx * CW, ym + cy, CW, PH, 3, 7)
    for fn in notes:
        fn(out, yb, ym)
    return ym + stroma_h


def fig():
    W = 400.0
    out = []
    y = 20
    # key
    kx = X0
    for k, lab in ((0, "normal"), (1, "1 mutation"), (2, "2 mutations"), (3, "3 mutations")):
        cell(out, kx, y - 11, 18, 14, k, 4)
        out.append(T(kx + 23, y, lab, 12, 400, MUTED))
        kx += 23 + {0: 46, 1: 66, 2: 72, 3: 0}[k] + 14
    y += 36

    c = N // 2
    b1 = [0] * N; b1[c] = 1

    def n1(out, yb, ym):
        out.append(T(X1 - 4, ym + 13, "basement membrane", 11, 400, MUTED, "end"))
    y = row(out, y, "1  One cell gains a mutation", b1, [], 18, notes=[n1]) + 30

    b2 = [0] * N
    for i in range(c - 3, c + 4): b2[i] = 1
    y = row(out, y, "2  Its descendants outgrow their neighbors", b2, [(1, 2 * (c - 2), [1] * 5)], 18) + 30

    b3 = [0] * N
    for i in range(c - 5, c + 6): b3[i] = 1
    b3[c + 1] = 2
    p3 = [(1, 2 * (c - 4), [1, 1, 1, 2, 2, 2, 2, 1, 1]), (2, 2 * (c - 2) + 1, [1, 2, 2, 2, 1]), (3, 2 * (c - 1) + 1, [2, 2])]

    y = row(out, y, "3  One descendant gains a second mutation", b3, p3, 18) + 30

    b4 = [0] * N
    for i in range(c - 6, c + 7): b4[i] = 1
    for i in range(c - 3, c + 3): b4[i] = 2
    b4[c - 1] = 3; b4[c] = 3
    p4 = [(1, 2 * (c - 5), [1, 1, 2, 2, 2, 3, 3, 2, 2, 1, 1]),
          (2, 2 * (c - 4) + 1, [1, 2, 2, 3, 3, 2, 2, 1]),
          (3, 2 * (c - 3), [2, 2, 3, 3, 2, 2]),
          (4, 2 * (c - 2) + 1, [2, 3, 2])]
    inv = [(c - 1.5, 6), (c - 0.2, 9), (c + 1.0, 4), (c - 0.9, 28), (c + 0.5, 32)]

    def n4(out, yb, ym):
        x = X0 + (c - 1.6) * CW
        out.append(line(x - 30, ym + 15, x - 4, ym + 15))
        out.append(T(x - 34, ym + 19, "cells invade", 12, 400, MUTED, "end"))
        out.append(T(x - 34, ym + 34, "the tissue below", 12, 400, MUTED, "end"))
    y = row(out, y, "4  A third mutation lets cells invade", b4, p4, 56, invade=inv, gap=(c - 1, c + 1), notes=[n4])
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "A tumor grows from one cell through successive mutations and clonal expansion.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
