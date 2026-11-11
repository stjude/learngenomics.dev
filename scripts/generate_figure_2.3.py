"""Figure 2.3: Knudson's two-hit model in nonheritable and heritable retinoblastoma."""

from figures.core import COPYRIGHT, DARK, MUTED, T, main, svg_doc
from figures.two_hits import CH, CW, N, TUMOR, X0, bar, cell

NAME = "2.3-two-hits"


def cellrow(out, y, label, hits):
    out.append(T(X0, y, label, 12, 400, MUTED))
    y += 7
    for i, h in enumerate(hits):
        cell(out, X0 + i * CW, y, h, h >= 2)
    return y + CH


def panel(out, y, title, sub, birth, later, note):
    out.append(T(X0, y, title, 13, 700, DARK))
    out.append(T(X0, y + 16, sub, 12, 400, MUTED))
    y = cellrow(out, y + 38, "At birth", birth)
    y = cellrow(out, y + 22, "Later", later)
    out.append(T(X0, y + 19, note, 12, 400, DARK))
    return y + 19


def fig():
    W = 400.0
    out = []
    y = 22
    kx = X0
    bar(out, kx + 3, y - 12, 15, False)
    out.append(T(kx + 11, y, "working copy", 12, 400, MUTED))
    kx += 11 + 78 + 16
    bar(out, kx + 3, y - 12, 15, True)
    out.append(T(kx + 11, y, "broken copy", 12, 400, MUTED))
    kx += 11 + 70 + 16
    out.append(f'<rect x="{kx:.2f}" y="{y - 12:.2f}" width="16" height="15" rx="4" fill="{TUMOR}" stroke="{DARK}" stroke-width="1.4"/>')
    out.append(T(kx + 22, y, "can start a tumor", 12, 400, MUTED))
    y += 40

    y = panel(out, y, "Nonheritable", "Every cell starts with two working copies.",
              [0] * N, [0, 0, 1, 0, 0, 2, 0, 1, 0, 0],
              "Both hits have to happen in the same cell.")
    y += 40
    y = panel(out, y, "Heritable", "Every cell starts with one broken copy.",
              [1] * N, [1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
              "One more hit in any cell is enough. It often happens more than once.")
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Knudson's two-hit model in nonheritable and heritable retinoblastoma.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
