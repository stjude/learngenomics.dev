"""Figure 3.9: Copy number variation."""

from figures.core import (
    BLUE, COPYRIGHT, DARK, GREEN, GREY_LINE, LBL, LBLUE, NAVY, ORANGE, PURPLE, SANS, T, TEAL, TEXT_FILL,
    main, svg_doc,
)
from figures.copy_number import GAIN_C, LOSS_C, cn_dots

NAME = "3.9-copy-number-variation"

SV_COLS = {"A": BLUE, "B": TEAL, "C": ORANGE, "D": GREEN, "E": PURPLE, "F": NAVY, "G": LBLUE}


def sv_block(x, y, w, L, h=18.0):
    col = SV_COLS[L]
    hh = h / 2
    pts = [(x, y - hh), (x + w - 5, y - hh), (x + w, y), (x + w - 5, y + hh), (x, y + hh), (x + 5, y)]
    d = "M" + "L".join(f"{a:.2f} {b:.2f}" for a, b in pts) + "Z"
    return (f'<path d="{d}" fill="{col}" fill-opacity="0.16" stroke="{col}" stroke-width="1.1"/>'
            + T(x + w / 2 + 0.6, y + 12.5 * 0.36, L, 12.5, 700, DARK, "middle", mono=True))


def fig():
    import random
    W, H = 400.0, 360.0
    MUTED = "#4d4d4f"
    rnd = random.Random(11)
    X0, P, BW = 72.0, 42.0, 40.0                      # track start, segment pitch, block width
    SEGS = "ABCDEF"
    depth = {"A": 2, "B": 3, "C": 2, "D": 2, "E": 1, "F": 2}
    colof = {"B": GAIN_C, "E": LOSS_C}
    XE = X0 + P * len(SEGS) - (P - BW)
    out = []
    lab = lambda y, t: T(8, y + LBL * 0.36, t, LBL, 600)

    def row(y, letters):
        return '<g class="segments">' + "".join(sv_block(X0 + i * P, y, BW, L) for i, L in enumerate(letters)) + "</g>"

    YR, Y1, Y2 = 22.0, 58.0, 82.0
    out += [lab(YR, "Reference"), row(YR, SEGS), lab(Y1, "Copy 1"), row(Y1, "ABBCDEF"), lab(Y2, "Copy 2"), row(Y2, "ABCDF")]
    out.append(f'<text x="{X0:.2f}" y="{Y2 + 28:.2f}" font-family="{SANS}" font-size="{LBL:g}" fill="{MUTED}">Copy 1 has '
               f'<tspan fill="{TEXT_FILL[GAIN_C]}" font-weight="600">an extra B</tspan>; copy 2 has <tspan fill="{TEXT_FILL[LOSS_C]}" font-weight="600">lost E</tspan></text>')

    # reads, stacked over reference coordinates
    YB0, RH, RP = 204.0, 3.0, 5.0                     # stack bottom, read height, row pitch
    PER = 2                                           # rows per copy
    YT = YB0 - 3 * PER * RP
    Y0, SC = 266.0, 40.0
    for L in colof:                                   # shaded columns over B and E
        i = SEGS.index(L)
        out.append(f'<rect x="{X0 + i * P - 1:.2f}" y="{YT - 26:.2f}" width="{BW + 2:g}" height="{Y0 + SC + 12 - (YT - 26):.2f}" '
                   f'fill="{colof[L]}" fill-opacity="0.07"/>')
    out.append(T(X0, 130, "Reads from both copies map back to the reference", LBL, 400, MUTED))
    out.append('<g class="coords">' + "".join(T(X0 + i * P + BW / 2, YT - 12, L, 10, 600, MUTED, "middle", mono=True)
                                              for i, L in enumerate(SEGS)) + "</g>")
    out.append(lab(YB0 - 12, "Reads"))
    s = '<g class="reads">'
    for i, L in enumerate(SEGS):
        for k in range(depth[L] * PER):
            o = (k * 5) % 6 - 2
            y = YB0 - k * RP - RH
            for xa, ln in ((o, 17 + (k % 2)), (o + 20, 17 - (k % 3) * 0.5)):
                s += (f'<rect x="{X0 + i * P - 1 + xa + 1:.2f}" y="{y:.2f}" width="{ln:g}" height="{RH:g}" rx="1" '
                      f'fill="{GREY_LINE}" fill-opacity="0.6"/>')
    out.append(s + "</g>")
    out.append(f'<path d="M{X0:.2f} {YB0 + 1.5:.2f}H{XE:.2f}" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    out.append(T(X0 + 1 * P + BW / 2, YB0 + 15, "×1.5", LBL, 600, GAIN_C, "middle"))
    out.append(T(X0 + 4 * P + BW / 2, YB0 + 15, "×0.5", LBL, 600, LOSS_C, "middle"))

    # log2 ratio track
    y_of = lambda v: Y0 - v * SC
    out.append(T(8, Y0 - 34 + 4.5, "log2", LBL, 600) + T(8, Y0 - 20 + 4.5, "ratio", LBL, 600))
    for v, t, c in ((0.58, "+0.58", GAIN_C), (0.0, "0", None), (-1.0, "−1", LOSS_C)):
        out.append(f'<path class="grid" d="M{X0:.2f} {y_of(v):.2f}H{XE:.2f}" stroke="{GREY_LINE}" stroke-width="0.6" stroke-dasharray="2 2"/>')
        out.append(T(X0 - 6, y_of(v) + 3.6, t, 10, 400, MUTED, "end"))
    for v, t, c in ((0.58, "3 copies", GAIN_C), (0.0, "2 copies", DARK), (-1.0, "1 copy", LOSS_C)):
        out.append(T(XE + 8, y_of(v) + 4.5, t, LBL, 600 if c != DARK else 400, c if c != DARK else MUTED))
    s = '<g class="bins">'
    for i, L in enumerate(SEGS):
        lv = {2: 0.0, 3: 0.58, 1: -1.0}[depth[L]]
        s += cn_dots(rnd, X0 + i * P - 1, X0 + i * P + P - 1, 6, y_of, lv, 0.11, colof.get(L, GREY_LINE))
    out.append(s + "</g>")
    s = '<g class="segments-cn">'
    runs = [(0, 1, 0.0, DARK), (1, 2, 0.58, GAIN_C), (2, 4, 0.0, DARK), (4, 5, -1.0, LOSS_C), (5, 6, 0.0, DARK)]
    for a, b, v, c in runs:
        s += (f'<path d="M{X0 + a * P - 1 + 1.5:.2f} {y_of(v):.2f}H{X0 + b * P - 1 - 1.5:.2f}" stroke="{c}" stroke-width="2.4" '
              f'stroke-linecap="round"/>')
    out.append(s + "</g>")
    # "Bins" and "Segment" callouts
    out.append(T(X0 + 2 * P + 6, y_of(-0.62), "Segment", 10, 400, MUTED))
    out.append(f'<path d="M{X0 + 2 * P + 14:.2f} {y_of(-0.62) - 9:.2f}L{X0 + 2 * P + 10:.2f} {y_of(0) + 3:.2f}" stroke="{GREY_LINE}" stroke-width="0.7"/>')
    out.append(T(X0 + 3 * P + 10, y_of(0.5), "Bins", 10, 400, MUTED))
    out.append(f'<path d="M{X0 + 3 * P + 14:.2f} {y_of(0.5) + 2:.2f}L{X0 + 3 * P + 12:.2f} {y_of(0.16):.2f}" stroke="{GREY_LINE}" stroke-width="0.7"/>')
    out.append(T(W - 8, Y0 + SC + 30, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, [o for o in out if o], "Copy number variation: read depth and log2 ratio reveal a gain and a loss")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="391.5" height="333.75" viewBox="4.25 8.5 391.5 333.75"')


if __name__ == "__main__":
    main(NAME, fig)
