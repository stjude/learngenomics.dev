"""Figure 4.13: Hi-C."""

from figures.core import (
    BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, ORANGE, PURPLE, T, TEAL, main, svg_doc,
)
from figures.drawing import panel_head

NAME = "4.13-hi-c"

A_C, B_C, BIO = TEAL, PURPLE, ORANGE
X0, X1 = 92.0, 392.0


def seg(x0, x1, y, col=BLUE, op=1.0, w=3):
    return f'<path d="M{x0:.2f} {y:.2f}H{x1:.2f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round" opacity="{op:g}"/>'


def biotin(x, y):
    return f'<circle class="biotin" cx="{x:.2f}" cy="{y:.2f}" r="2.8" fill="{BIO}" stroke="#c98200" stroke-width="0.7"/>'


def crosslinks(xs, y0, y1):
    return "".join(f'<path class="crosslink" d="M{x:.2f} {y0:.2f}V{y1:.2f}" stroke="{DARK}" stroke-width="1"/>' for x in xs)


def loop(x, Y):
    # the long stretch of DNA between region A (bottom strand) and region B (top strand)
    return (f'<path class="dna-loop" d="M{x + 66:.2f} {Y + 8:.2f}C{x + 90:.2f} {Y + 8:.2f} {x + 96:.2f} {Y - 14:.2f} {x + 88:.2f} {Y - 30:.2f}'
            f'C{x + 80:.2f} {Y - 46:.2f} {x + 58:.2f} {Y - 44:.2f} {x + 58:.2f} {Y - 30:.2f}'
            f'C{x + 58:.2f} {Y - 20:.2f} {x + 68:.2f} {Y - 22:.2f} {x + 72:.2f} {Y - 16:.2f}'
            f'C{x + 75:.2f} {Y - 11:.2f} {x + 72:.2f} {Y - 8:.2f} {x + 66:.2f} {Y - 8:.2f}" '
            f'fill="none" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>')


def note(x, y, lines):
    return "".join(T(x, y + 15 * i, s, LBL, 400, MUTED) for i, s in enumerate(lines))


def arrow(x0, x1, y, col):
    d = 1 if x1 > x0 else -1
    return (f'<path d="M{x0:.2f} {y:.2f}H{x1 - d * 6:.2f}" stroke="{col}" stroke-width="5"/>'
            f'<path d="M{x1 - d * 7:.2f} {y - 6:.2f}L{x1:.2f} {y:.2f}L{x1 - d * 7:.2f} {y + 6:.2f}Z" fill="{col}"/>')


def fig():
    W = 400.0
    out = []
    PX = [6.0 + 98.0 * i for i in range(4)]
    Y = 78.0
    heads = ["Crosslink", "Cut and mark", "Join", "Pull down"]
    notes = [["Fix the DNA in", "its folded shape"], ["Cut, and tag the", "ends with biotin"], ["Join ends that", "were touching"], ["Shear, then keep", "the tagged joins"]]
    for i, x in enumerate(PX):
        if i:
            out.append(f'<path class="divider" d="M{x - 2:.2f} 8V148" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
        out.append(panel_head(x + 2, 20, str(i + 1), heads[i]).replace(f"{i + 1}. ", f"{i + 1}  "))
        out.append(note(x + 2, 124, notes[i]))
    yb, yt = Y + 8, Y - 8
    # 1. crosslink: region A (bottom) and region B (top) held side by side
    x = PX[0]
    out.append(loop(x, Y) + seg(x + 4, x + 66, yb) + seg(x + 4, x + 66, yt)
               + seg(x + 20, x + 52, yb, A_C) + seg(x + 20, x + 52, yt, B_C)
               + crosslinks([x + 28, x + 44], yt + 2.5, yb - 2.5))
    out.append(T(x + 36, yb + 17, "A", LBL, 700, A_C, "middle") + T(x + 36, yt - 8, "B", LBL, 700, B_C, "middle"))
    # 2. cut and mark
    x = PX[1]
    c = x + 36
    out.append(loop(x, Y) + seg(x + 4, c - 4, yb) + seg(c + 4, x + 66, yb) + seg(x + 4, c - 4, yt) + seg(c + 4, x + 66, yt)
               + seg(x + 20, c - 4, yb, A_C) + seg(c + 4, x + 52, yb, A_C) + seg(x + 20, c - 4, yt, B_C) + seg(c + 4, x + 52, yt, B_C)
               + crosslinks([x + 26, x + 46], yt + 2.5, yb - 2.5)
               + biotin(c - 4, yb) + biotin(c + 4, yb) + biotin(c - 4, yt) + biotin(c + 4, yt))
    # 3. join: the left-hand cut ends of A and B are joined into one molecule
    x = PX[2]
    c = x + 36
    r = 8
    out.append(loop(x, Y) + seg(x + 4, c - 4, yb) + seg(c + 12, x + 66, yb) + seg(x + 4, c - 4, yt) + seg(c + 12, x + 66, yt)
               + seg(x + 20, c - 4, yb, A_C) + seg(c + 12, x + 52, yb, A_C) + seg(x + 20, c - 4, yt, B_C) + seg(c + 12, x + 52, yt, B_C)
               + f'<path class="join" d="M{c - 4:.2f} {yb:.2f}A{r} {r} 0 0 0 {c - 4 + r:.2f} {Y:.2f}" fill="none" stroke="{A_C}" stroke-width="3"/>'
               + f'<path class="join" d="M{c - 4 + r:.2f} {Y:.2f}A{r} {r} 0 0 0 {c - 4:.2f} {yt:.2f}" fill="none" stroke="{B_C}" stroke-width="3"/>'
               + crosslinks([x + 22], yt + 2.5, yb - 2.5)
               + biotin(c - 4 + r, Y) + biotin(c + 12, yb) + biotin(c + 12, yt))
    # 4. pull down: a sheared chimeric fragment held by a bead through its biotin
    x = PX[3]
    j = x + 48
    out.append(f'<path d="M{j:.2f} {Y - 14:.2f}V{Y + 6:.2f}" stroke="{DARK}" stroke-width="1.6"/>'
               + f'<circle class="bead" cx="{j:.2f}" cy="{Y - 24:.2f}" r="9" fill="{GREY_LINE}" fill-opacity="0.3" stroke="{GREY_LINE}" stroke-width="1"/>'
               + seg(j - 26, j, Y + 8, A_C) + seg(j, j + 26, Y + 8, B_C) + biotin(j, Y + 8))
    out.append(T(j + 13, Y - 34.5, "Bead", LBL, 400, MUTED))
    out.append(seg(x + 8, x + 30, Y + 24, BLUE, 0.3) + seg(x + 62, x + 88, Y + 24, A_C, 0.3))

    # ---- reads
    YH = 176.0
    out.append(f'<path class="divider" d="M8 {YH - 18:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
    out.append(T(8, YH, "Reads mapped to the genome", LBL, 700))
    YF = 214.0
    m = 242.0
    out.append(seg(m - 52, m, YF, A_C) + seg(m, m + 52, YF, B_C) + biotin(m, YF))
    out.append(arrow(m - 52, m - 18, YF - 12, A_C) + arrow(m + 52, m + 18, YF + 12, B_C))
    out.append(T(m - 60, YF - 8, "Read 1", LBL, 600, None, "end") + T(m + 60, YF + 16, "Read 2", LBL, 600))
    # reference chromosome, 0 to 60 Mb
    YR = 286.0
    mb = lambda v: X0 + (X1 - X0) * v / 60
    xa, xb = mb(12), mb(48)
    out.append(f'<path class="leader" d="M{m - 35:.2f} {YF + 5:.2f}L{xa:.2f} {YR - 9:.2f}" stroke="{A_C}" stroke-width="1.2" stroke-dasharray="3 2.5" fill="none"/>')
    out.append(f'<path class="leader" d="M{m + 35:.2f} {YF + 19:.2f}L{xb:.2f} {YR - 9:.2f}" stroke="{B_C}" stroke-width="1.2" stroke-dasharray="3 2.5" fill="none"/>')
    rl = f'<g class="reference-axis"><path d="M{X0:.2f} {YR:.2f}H{X1:.2f}" stroke="{DARK}" stroke-width="1"/>'
    for v in range(0, 61, 10):
        xv = mb(v)
        big = v % 20 == 0
        rl += f'<path d="M{xv:.2f} {YR:.2f}V{YR + (5 if big else 2.5):.2f}" stroke="{DARK}" stroke-width="{1 if big else 0.8}"/>'
        if big:
            rl += T(xv, YR + 18, f"{v} Mb", LBL, 400, MUTED, "start" if v == 0 else "end" if v == 60 else "middle")
    out.append(T(8, YR + 4.5, "Reference", LBL, 600) + rl + "</g>")
    out.append(f'<rect x="{xa - 4:.2f}" y="{YR - 6:.2f}" width="8" height="6" fill="{A_C}"/><rect x="{xb - 4:.2f}" y="{YR - 6:.2f}" width="8" height="6" fill="{B_C}"/>')
    out.append(T(xa, YR - 14, "A", LBL, 700, A_C, "middle") + T(xb, YR - 14, "B", LBL, 700, B_C, "middle"))
    YB = YR + 34
    out.append(f'<path class="bracket" d="M{xa:.2f} {YB - 4:.2f}V{YB:.2f}H{xb:.2f}V{YB - 4:.2f}" fill="none" stroke="{DARK}" stroke-width="1"/>')
    out.append(T((xa + xb) / 2, YB + 15, "36 million bases apart", LBL, 400, None, "middle"))
    H = YB + 44
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 7, out, "Hi-C: crosslinking, cutting and marking, joining and pulling down DNA, then the two reads of a pair mapping far apart on the reference", origin=(4, 7))


if __name__ == "__main__":
    main(NAME, fig)
