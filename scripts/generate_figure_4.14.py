"""Figure 4.14: A Hi-C contact map drawn as a triangle over the chromosome."""

import math
import random

from figures.core import COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, PURPLE, T, TEAL, main, svg_doc
from figures.drawing import leader

NAME = "4.14-hi-c-contact-map"

A_C, B_C = TEAL, PURPLE
HOT, HOT_DK = (0xe0, 0x30, 0x30), (0x7a, 0x00, 0x14)


def mix(c0, c1, t):
    return "#%02x%02x%02x" % tuple(round(a + (b - a) * t) for a, b in zip(c0, c1))


def colour(t):
    t = max(0.0, min(1.0, t))
    return mix((255, 255, 255), HOT, t / 0.75) if t < 0.75 else mix(HOT, HOT_DK, (t - 0.75) / 0.25)


def fig():
    W = 400.0
    out = []
    N = 40
    X0, X1 = 16.0, 384.0
    cw = (X1 - X0) / N               # genome width of one bin
    h = cw / 2
    YB = 206.0                       # genome axis
    TADS = [(0, 9), (9, 24), (24, 32), (32, 40)]
    LI, LJ = 9, 23
    tad = lambda i: next(k for k, (a, b) in enumerate(TADS) if a <= i < b)
    rnd = random.Random(3)
    vals = {}
    for i in range(N):
        for j in range(i, N):
            v = 1.0 / (abs(i - j) + 1) ** 1.05
            if tad(i) == tad(j):
                v *= 3.2
            v += 1.6 * math.exp(-((i - LI) ** 2 + (j - LJ) ** 2) / 0.5)
            v *= 0.8 + 0.4 * rnd.random()
            vals[i, j] = v
    lo, hi = math.log(min(vals.values())), math.log(sorted(vals.values())[-N - 1])
    pos = lambda i, j: (X0 + (i + j + 1) * h, YB - (j - i) * h)
    out.append(f'<defs><clipPath id="hic-tri"><rect x="{X0 - 1:.2f}" y="0" width="{X1 - X0 + 2:.2f}" height="{YB:.2f}"/></clipPath></defs>')
    body = ['<g class="contact-map" clip-path="url(#hic-tri)">']
    for (i, j), v in vals.items():
        t = (math.log(v) - lo) / (hi - lo)
        x, y = pos(i, j)
        e = h + 0.25
        body.append(f'<path d="M{x:.2f} {y - e:.2f}L{x + e:.2f} {y:.2f}L{x:.2f} {y + e:.2f}L{x - e:.2f} {y:.2f}Z" fill="{colour(t ** 1.25)}"/>')
    body.append("</g>")
    out += body
    out.append(f'<path d="M{X0:.2f} {YB:.2f}L{(X0 + X1) / 2:.2f} {YB - N * h:.2f}L{X1:.2f} {YB:.2f}" fill="none" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    # genome axis
    rl = f'<g class="reference-axis"><path d="M{X0:.2f} {YB:.2f}H{X1:.2f}" stroke="{DARK}" stroke-width="1"/>'
    for k in range(5):
        x = X0 + (X1 - X0) * k / 4
        rl += f'<path d="M{x:.2f} {YB:.2f}V{YB + 5:.2f}" stroke="{DARK}" stroke-width="1"/>'
    rl += "</g>"
    out.append(rl + T(X0, YB + 18, "0", LBL, 400, MUTED, "start") + T(X1, YB + 18, "4 Mb", LBL, 400, MUTED, "end"))
    out.append(T((X0 + X1) / 2, YB + 36, "Position along one chromosome", LBL, 400, MUTED, "middle"))
    # the highlighted cell, traced down to A and B
    lx, ly = pos(LI, LJ)
    xa, xb = X0 + (LI + 0.5) * cw, X0 + (LJ + 0.5) * cw
    out.append(f'<path d="M{lx - h:.2f} {ly + h:.2f}L{xa:.2f} {YB:.2f}" stroke="{A_C}" stroke-width="1.4" stroke-dasharray="3 2.5"/>')
    out.append(f'<path d="M{lx + h:.2f} {ly + h:.2f}L{xb:.2f} {YB:.2f}" stroke="{B_C}" stroke-width="1.4" stroke-dasharray="3 2.5"/>')
    e = h + 1.6
    out.append(f'<path d="M{lx:.2f} {ly - e:.2f}L{lx + e:.2f} {ly:.2f}L{lx:.2f} {ly + e:.2f}L{lx - e:.2f} {ly:.2f}Z" fill="none" stroke="{DARK}" stroke-width="1.4"/>')
    out.append(f'<rect x="{xa - h:.2f}" y="{YB + 2:.2f}" width="{cw:.2f}" height="5" fill="{A_C}"/>' + T(xa, YB + 20, "A", LBL, 700, A_C, "middle"))
    out.append(f'<rect x="{xb - h:.2f}" y="{YB + 2:.2f}" width="{cw:.2f}" height="5" fill="{B_C}"/>' + T(xb, YB + 20, "B", LBL, 700, B_C, "middle"))
    # notes in the empty corners
    ty = ly - 72
    out.append(leader(lx - 26, ty + 6, lx - 3, ly - e - 1) + T(lx - 28, ty - 8, "Loop:", LBL, 600, None, "end") + T(lx - 28, ty + 6, "A touches B", LBL, 400, MUTED, "end"))
    a, b = TADS[3]
    tx, tyy = pos(a, b - 1)
    out.append(leader(tx + 8, tyy - 22, tx + 2, tyy - h - 2) + T(tx + 10, tyy - 26, "TAD", LBL, 600))
    nx = X0 + 2.5 * cw
    out.append(leader(nx - 6, YB - 66, nx, YB - 6) + T(X0, YB - 84, "Near", LBL, 600) + T(X0, YB - 70, "neighbors", LBL, 600))
    # colour key
    KY = YB + 54
    KX = 200 - 60
    stops = "".join(f'<stop offset="{k / 10:g}" stop-color="{colour(k / 10)}"/>' for k in range(11))
    out.append(f'<defs><linearGradient id="hic-key">{stops}</linearGradient></defs>'
               f'<rect x="{KX:.2f}" y="{KY:.2f}" width="120" height="8" fill="url(#hic-key)" stroke="{GREY_LINE}" stroke-width="0.6"/>')
    out.append(T(KX - 8, KY + 8, "Fewer", LBL, 400, MUTED, "end") + T(KX + 128, KY + 8, "More contacts", LBL, 400, MUTED))
    H = KY + 34
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 14, out, "A Hi-C contact map drawn as a triangle over the chromosome: dark along the bottom edge, darker triangles for TADs, and a dark dot where two distant regions form a loop", origin=(4, 14))


if __name__ == "__main__":
    main(NAME, fig)
