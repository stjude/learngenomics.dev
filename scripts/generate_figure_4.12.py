"""Figure 4.12: ATAC-seq."""

import math
import random

from figures.core import (
    BLUE, COPYRIGHT, DARK, GREEN, GREY_LINE, LBL, MUTED, ORANGE, PURPLE, T, TEAL, main, svg_doc,
)
from figures.biology import nucleosome

NAME = "4.12-atac-seq"

X0, X1 = 92.0, 392.0


def dna(x0, x1, y, op=1.0):
    return f'<path class="dna" d="M{x0:.2f} {y:.2f}H{x1:.2f}" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" opacity="{op:g}"/>'


def factor(cx, y):
    return f'<ellipse class="factor" cx="{cx:.2f}" cy="{y - 9:.2f}" rx="7.5" ry="7.5" fill="{GREEN}" stroke="#4e8a26" stroke-width="0.8"/>'


def cut(x, y):
    # Tn5 cut: a small teal wedge pointing at the DNA
    return f'<path class="tn5-cut" d="M{x - 3.6:.2f} {y - 9:.2f}H{x + 3.6:.2f}L{x:.2f} {y - 3:.2f}Z" fill="{TEAL}" stroke="#0d7f8f" stroke-width="0.6"/>'


def ghost(cx, y, r=10):
    return f'<circle class="removed-nucleosome" cx="{cx:.2f}" cy="{y:.2f}" r="{r}" fill="none" stroke="{PURPLE}" stroke-width="0.9" stroke-dasharray="2.5 2" opacity="0.7"/>'


def fragment(a, b, y, nucs):
    ad = 6.0
    return (''.join(ghost(c, y) for c in nucs)
            + f'<path class="adapter" d="M{a - ad:.2f} {y:.2f}H{a:.2f}M{b:.2f} {y:.2f}H{b + ad:.2f}" stroke="{ORANGE}" stroke-width="3.4"/>'
            + dna(a, b, y))


def fig():
    W, H = 400.0, 392.0
    out = []
    NUC = [110, 146, 182, 290, 326, 362]
    GAP = (200, 272)
    TF = 237
    CUTS = [128, 164, 200, 210, 226, 248, 264]
    # ---- 1. chromatin and cuts
    out.append(T(8, 20, "Tn5 cuts only where it can reach", LBL, 700))
    lx = 392 - 4
    out.append(T(lx, 20, "Tn5 cut", LBL, 400, MUTED, "end") + cut(lx - 50, 20 - 1.5))
    YC = 60.0
    out.append(T(8, YC + 4.5, "Chromatin", LBL, 600))
    out.append(dna(X0, X1, YC) + "".join(nucleosome(c, YC, 10) for c in NUC) + factor(TF, YC))
    out.append("".join(cut(c, YC) for c in CUTS))
    # labels under the chromatin
    yb = YC + 18
    out.append(f'<path class="bracket" d="M{GAP[0] + 2:.2f} {yb - 4:.2f}V{yb:.2f}H{GAP[1] - 2:.2f}V{yb - 4:.2f}" fill="none" stroke="{DARK}" stroke-width="1"/>')
    out.append(T(sum(GAP) / 2, yb + 15, "Open region", LBL, 400, None, "middle"))
    out.append(T(146, yb + 15, "Nucleosomes", LBL, 400, MUTED, "middle"))
    out.append(T(TF, YC - 24, "Bound factor", LBL, 400, MUTED, "middle"))

    # ---- 2. fragments
    YH2 = 128.0
    out.append(f'<path class="divider" d="M8 {YH2 - 18:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
    out.append(T(8, YH2, "The fragments, with proteins removed", LBL, 700))
    rows = [
        ([(210, 226, []), (248, 264, [])], "No nucleosome", "under 100 bases"),
        ([(164, 200, [182])], "One nucleosome", "about 200 bases"),
        ([(128, 200, [146, 182])], "Two nucleosomes", "about 400 bases"),
    ]
    y = YH2 + 26
    for frags, l1, l2 in rows:
        for a, b, n in frags:
            out.append(fragment(a, b, y, n))
        xr = max(b for _, b, _ in frags) + 16
        out.append(T(xr, y - 1, l1, LBL, 600) + T(xr, y + 13, l2, LBL, 400, MUTED))
        y += 36

    # ---- 3. track
    YH3 = y + 8
    out.append(f'<path class="divider" d="M8 {YH3 - 18:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
    out.append(T(8, YH3, "Reads mapped to the genome", LBL, 700))
    N = 60
    CW = (X1 - X0) / N
    rnd = random.Random(5)
    plateau = lambda p: 1 / (1 + math.exp(-(p - 21.6) / 0.9)) * 1 / (1 + math.exp((p - 35.6) / 0.9))
    vals = [2.0 + 1.6 * rnd.random() + 26 * plateau(p) * (0.88 + 0.24 * rnd.random()) for p in range(N)]
    DK = 1.45
    YT = YH3 + 74
    d = f"M{X0:.2f} {YT:.2f}"
    for p, v in enumerate(vals):
        d += f"V{YT - v * DK:.2f}H{X0 + CW * (p + 1):.2f}"
    d += f"V{YT:.2f}Z"
    out.append(T(8, YT - 4, "ATAC", LBL, 600))
    out.append(f'<path class="atac-track" d="{d}" fill="{TEAL}" fill-opacity="0.35" stroke="{TEAL}" stroke-width="0.9" stroke-linejoin="round"/>'
               f'<path class="axis" d="M{X0:.2f} {YT:.2f}H{X1:.2f}" stroke="{GREY_LINE}" stroke-width="1"/>')
    top = YT - max(vals) * DK
    out.append(T(TF + 42, top + 6, "Peak over the", LBL, 400, None, "start") + T(TF + 42, top + 20, "open region", LBL, 400, None, "start"))
    # reference ruler: 36 px per 200 bases
    YR = YT + 20
    bp = lambda b: X0 + b * 36 / 200
    rl = f'<g class="reference-axis"><path d="M{X0:.2f} {YR:.2f}H{X1:.2f}" stroke="{DARK}" stroke-width="1"/>'
    for k, lab in enumerate(["0", "500", "1,000", "1,500 bases"]):
        x = bp(500 * k)
        rl += f'<path d="M{x:.2f} {YR:.2f}V{YR + 5:.2f}" stroke="{DARK}" stroke-width="1"/>'
        rl += T(x, YR + 18, lab, LBL, 400, MUTED, "start" if k == 0 else "middle")
    for b in range(100, 1601, 100):
        if b % 500:
            x = bp(b)
            rl += f'<path d="M{x:.2f} {YR:.2f}V{YR + 2.5:.2f}" stroke="{DARK}" stroke-width="0.8"/>'
    out.append(T(8, YR + 4.5, "Reference", LBL, 600) + rl + "</g>")
    H = YR + 46
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 7, out, "ATAC-seq: Tn5 cuts open DNA between nucleosomes, fragment lengths show how many nucleosomes each spans, and reads pile up over the open region", origin=(4, 7))


if __name__ == "__main__":
    main(NAME, fig)
