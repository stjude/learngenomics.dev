"""Figure 2.10: An inherited variant in a normal sample and a tumor sample."""

from figures.core import BLUE, COPYRIGHT, DARK, MUTED, ORANGE, T, main, svg_doc
from figures.two_hits import CH, CW, N, TUMOR, X0, X1, bar, cell

NAME = "2.10-germline-second-hit"


def afbar(out, y, frac, label):
    h = 12.0
    w = X1 - X0
    out.append(f'<rect x="{X0:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h}" rx="3" fill="{BLUE}"/>')
    out.append(f'<path d="M{X0 + 3:.2f} {y:.2f}H{X0 + w * frac:.2f}V{y + h:.2f}H{X0 + 3:.2f}q-3 0 -3 -3V{y + 3:.2f}q0 -3 3 -3Z" fill="{ORANGE}"/>')
    out.append(f'<line x1="{X0 + w * frac:.2f}" y1="{y - 3:.2f}" x2="{X0 + w * frac:.2f}" y2="{y + h + 3:.2f}" stroke="{DARK}" stroke-width="1.4"/>')
    out.append(T(X0, y + h + 18, label, 12, 400, DARK))
    return y + h + 18


def panel(out, y, title, sub, hits, label, frac):
    out.append(T(X0, y, title, 13, 700, DARK))
    out.append(T(X0, y + 16, sub, 12, 400, MUTED))
    y += 30
    for i, h in enumerate(hits):
        cell(out, X0 + i * CW, y, h, h >= 2)
    y += CH + 26
    out.append(T(X0, y, "Copies carrying the variant", 12, 400, MUTED))
    return afbar(out, y + 9, frac, label)


def fig():
    W = 400.0
    out = []
    y = 22
    kx = X0
    bar(out, kx + 3, y - 12, 15, False)
    out.append(T(kx + 11, y, "working copy", 12, 400, MUTED))
    kx += 11 + 78 + 16
    bar(out, kx + 3, y - 12, 15, True)
    out.append(T(kx + 11, y, "inherited variant", 12, 400, MUTED))
    kx += 11 + 98 + 16
    out.append(f'<rect x="{kx:.2f}" y="{y - 12:.2f}" width="16" height="15" rx="4" fill="{TUMOR}" stroke="{DARK}" stroke-width="1.4"/>')
    out.append(T(kx + 22, y, "tumor cell", 12, 400, MUTED))
    y += 40

    y = panel(out, y, "Normal sample", "Every cell has one copy with the variant.",
              [1] * N, "10 of 20 copies, so about 50% of reads", 0.5)
    y += 40
    y = panel(out, y, "Tumor sample, 60% tumor", "Tumor cells replaced the working copy with the variant.",
              [2, 1, 2, 2, 1, 2, 1, 2, 2, 1], "16 of 20 copies, so about 80% of reads", 0.8)
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "An inherited variant in a normal sample and a tumor sample.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
