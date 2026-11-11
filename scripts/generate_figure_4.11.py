"""Figure 4.11: ChIP-seq."""

import math
import random

from figures.core import (
    BLUE, COPYRIGHT, DARK, GREEN, GREY_LINE, LBL, MUTED, ORANGE, PURPLE, T, TEAL, main, svg_doc,
)
from figures.drawing import leader, panel_head
from figures.biology import nucleosome

NAME = "4.11-chip-seq"

DNA_C, TGT_C, OTHER_C = BLUE, ORANGE, GREEN


def dna(x0, x1, y, op=1.0):
    return f'<path class="dna" d="M{x0:.2f} {y:.2f}H{x1:.2f}" stroke="{DNA_C}" stroke-width="3" stroke-linecap="round" opacity="{op:g}"/>'


def target(cx, y, op=1.0):
    # transcription factor sitting on the DNA
    return (f'<g class="target" opacity="{op:g}"><ellipse cx="{cx:.2f}" cy="{y - 9.5:.2f}" rx="11" ry="9" fill="{TGT_C}" '
            f'stroke="#c98200" stroke-width="0.8"/></g>')


def other(cx, y, op=1.0):
    return (f'<g class="other-protein" opacity="{op:g}"><rect x="{cx - 7.5:.2f}" y="{y - 15.5:.2f}" width="15" height="13.5" rx="4" '
            f'fill="{OTHER_C}" stroke="#4e8a26" stroke-width="0.8"/></g>')


def nuc(cx, y, op=1.0):
    return f'<g opacity="{op:g}">' + nucleosome(cx, y, 7) + "</g>"


def crosslinks(cx, y):
    return "".join(f'<path class="crosslink" d="M{cx + dx:.2f} {y - 3.4:.2f}V{y - 0.6:.2f}" stroke="{DARK}" stroke-width="1"/>' for dx in (-4, 0, 4))


def antibody(cx, ytop, ybot):
    # bead on top, Y-shaped antibody gripping the target from above
    yf = ybot - 11                                    # fork
    return (f'<g class="bead-antibody"><circle cx="{cx:.2f}" cy="{ytop:.2f}" r="9" fill="{GREY_LINE}" fill-opacity="0.3" stroke="{GREY_LINE}" stroke-width="1"/>'
            f'<path d="M{cx:.2f} {ytop + 9:.2f}V{yf:.2f}M{cx:.2f} {yf:.2f}L{cx - 6.5:.2f} {ybot:.2f}M{cx:.2f} {yf:.2f}L{cx + 6.5:.2f} {ybot:.2f}" '
            f'stroke="{DARK}" stroke-width="2" stroke-linecap="round" fill="none"/></g>')


def note(x, y, lines):
    return "".join(T(x, y + 15 * i, s, LBL, 400, MUTED) for i, s in enumerate(lines))


def fig():
    W, H = 400.0, 416.0
    out = []
    PX = [6.0 + 98.0 * i for i in range(4)]
    Y = 90.0                                          # DNA line in the step panels
    heads = ["Crosslink", "Shear", "Pull down", "Release"]
    notes = [["Fix proteins", "to the DNA"], ["Break into", "pieces"], ["An antibody", "grabs the target"], ["Free the DNA,", "then sequence"]]
    for i, x in enumerate(PX):
        if i:
            out.append(f'<path class="divider" d="M{x - 2:.2f} 8V148" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
        out.append(panel_head(x + 2, 20, str(i + 1), heads[i]).replace(f"{i + 1}. ", f"{i + 1}  "))
        out.append(note(x + 2, 124, notes[i]))
    # 1. crosslink
    x = PX[0]
    out.append(dna(x + 3, x + 91, Y) + nuc(x + 13, Y) + other(x + 34, Y) + target(x + 56, Y) + nuc(x + 80, Y)
               + crosslinks(x + 34, Y) + crosslinks(x + 56, Y))
    out.append(T(x + 56, Y - 26, "Target", LBL, 400, MUTED, "middle"))
    # 2. shear: three pieces, nudged apart
    x = PX[1]
    out.append(dna(x + 3, x + 25, Y + 6) + nuc(x + 14, Y + 6)
               + dna(x + 30, x + 50, Y - 22) + other(x + 40, Y - 22)
               + dna(x + 54, x + 78, Y + 2) + target(x + 66, Y + 2)
               + dna(x + 78, x + 92, Y - 30))
    # 3. pull down
    x = PX[2]
    tx = x + 48
    out.append(T(tx + 13, 44.5, "Bead", LBL, 400, MUTED))
    out.append(antibody(tx, 40, Y - 18) + dna(tx - 12, tx + 12, Y) + target(tx, Y))
    out.append(dna(x + 3, x + 23, Y + 8, 0.3) + nuc(x + 13, Y + 8, 0.3) + dna(x + 74, x + 94, Y + 8, 0.3) + other(x + 84, Y + 8, 0.3))
    # 4. release
    x = PX[3]
    out.append(dna(x + 36, x + 60, Y) + f'<ellipse cx="{x + 48:.2f}" cy="{Y - 28:.2f}" rx="11" ry="9" fill="none" stroke="{TGT_C}" stroke-width="1" stroke-dasharray="2.5 2"/>')

    # ---- tracks
    YH = 176.0
    out.append(f'<path class="divider" d="M8 {YH - 18:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
    out.append(T(8, YH, "Reads mapped to the genome", LBL, 700))
    X0, X1, N = 92.0, 392.0, 96
    CW = (X1 - X0) / N
    PEAK, G0, G1, BG = 22, 26, 64, 82
    rnd = random.Random(11)
    g = lambda p, c, s: math.exp(-((p - c) / s) ** 2 / 2)
    ramp = lambda p: 1 / (1 + math.exp(-(p - G0 - 2) / 1.2)) * 1 / (1 + math.exp((p - G1 + 2) / 1.2))
    base = [2.0 + 1.5 * rnd.random() for _ in range(N)]
    jit = lambda: 0.85 + 0.3 * rnd.random()
    fac = [base[p] * jit() + 27 * g(p, PEAK, 1.35) + 8 * g(p, BG, 2.4) for p in range(N)]
    mark = [base[p] * jit() + ramp(p) * (9 + 3 * rnd.random()) + 8 * g(p, BG, 2.4) for p in range(N)]
    inp = [base[p] * jit() + 8 * g(p, BG, 2.4) for p in range(N)]
    DK = 1.4
    xc = lambda p: X0 + CW * (p + 0.5)

    def track(vals, yb, col, op, cls):
        d = f"M{X0:.2f} {yb:.2f}"
        for p, v in enumerate(vals):
            d += f"V{yb - v * DK:.2f}H{X0 + CW * (p + 1):.2f}"
        d += f"V{yb:.2f}Z"
        return (f'<path class="{cls}" d="{d}" fill="{col}" fill-opacity="{op}" stroke="{col}" stroke-width="0.9" stroke-linejoin="round"/>'
                f'<path class="axis" d="M{X0:.2f} {yb:.2f}H{X1:.2f}" stroke="{GREY_LINE}" stroke-width="1"/>')

    def label(yb, l1, l2=None):
        if l2 is None:
            return T(8, yb - 4, l1, LBL, 600)
        return T(8, yb - 17, l1, LBL, 600) + T(8, yb - 3, l2, LBL, 400, MUTED)
    YF, YM, YI, YG = 246.0, 300.0, 336.0, 356.0
    out.append(label(YF, "ChIP", "factor") + track(fac, YF, TEAL, 0.35, "chip-factor"))
    out.append(label(YM, "ChIP", "histone mark") + track(mark, YM, PURPLE, 0.3, "chip-mark"))
    out.append(label(YI, "Input") + track(inp, YI, GREY_LINE, 0.25, "input"))
    # gene: the factor binds its promoter, the mark covers its body
    gx0, gx1 = X0 + CW * G0, X0 + CW * G1
    out.append(T(8, YG + 4.5, "Gene", LBL, 600)
               + f'<g class="gene"><rect x="{gx0:.2f}" y="{YG - 3.5:.2f}" width="{gx1 - gx0 - 6:.2f}" height="7" rx="1" fill="{GREY_LINE}"/>'
               + f'<path d="M{gx1 - 7:.2f} {YG - 6.5:.2f}L{gx1:.2f} {YG:.2f}L{gx1 - 7:.2f} {YG + 6.5:.2f}Z" fill="{GREY_LINE}"/></g>')
    # reference genome ruler: 20 kb window, 96 bins of about 208 bases
    YR = YG + 22
    rl = f'<g class="reference-axis"><path d="M{X0:.2f} {YR:.2f}H{X1:.2f}" stroke="{DARK}" stroke-width="1"/>'
    for k in range(5):
        x = X0 + (X1 - X0) * k / 4
        rl += f'<path d="M{x:.2f} {YR:.2f}V{YR + 5:.2f}" stroke="{DARK}" stroke-width="1"/>'
        rl += T(x, YR + 18, f"{5 * k} kb", LBL, 400, MUTED, "start" if k == 0 else "end" if k == 4 else "middle")
    for k in range(20):
        if k % 5:
            x = X0 + (X1 - X0) * k / 20
            rl += f'<path d="M{x:.2f} {YR:.2f}V{YR + 2.5:.2f}" stroke="{DARK}" stroke-width="0.8"/>'
    out.append(T(8, YR + 4.5, "Reference", LBL, 600) + rl + "</g>")
    ty = YF - 27 * DK - 14
    out.append(leader(xc(PEAK), ty + 4, xc(PEAK), YF - 27 * DK - 4) + T(xc(PEAK) - 3, ty, "Narrow peak: a bound factor", LBL, 400, None, "start"))
    out.append(T((gx0 + gx1) / 2, YM - 13 * DK - 7, "Broad peak: a mark across the gene", LBL, 400, None, "middle"))
    out.append(T(X1, YF - 8 * DK - 22, "High in input too:", LBL, 400, MUTED, "end")
               + T(X1, YF - 8 * DK - 8, "background", LBL, 400, MUTED, "end"))
    out.append(T(392, 409, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W - 8, H - 8, out, "ChIP-seq: crosslinking, shearing, pulling down and releasing DNA, then a peak of reads at the bound site compared with an input control", origin=(4, 7))
    return svg


if __name__ == "__main__":
    main(NAME, fig)
