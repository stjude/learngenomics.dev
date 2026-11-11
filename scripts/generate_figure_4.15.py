"""Figure 4.15: Single-cell RNA-seq."""

import os

from PIL import ImageFont

from figures.core import (
    BLUE, COPYRIGHT, DARK, FONT_DIR, GREEN, GREY_LINE, LBL, MUTED, ORANGE, PURPLE, RED, T, TEAL,
    main, svg_doc,
)
from figures.drawing import zoom_lines

NAME = "4.15-single-cell"

CHAN, CHAN_EDGE = "#ececed", "#b9babc"
_F = {w: ImageFont.truetype(os.path.join(FONT_DIR, "SourceSans3-VF.ttf"), 100) for w in (400,)}


def tw(s, size=LBL):
    return _F[400].getlength(s) * size / 100


def note(x, y, lines, anchor=None):
    return "".join(T(x, y + 15 * i, s, LBL, 400, MUTED, anchor) for i, s in enumerate(lines))


def channel(d):
    return (f'<path class="channel-edge" d="{d}" stroke="{CHAN_EDGE}" stroke-width="20" fill="none" stroke-linecap="butt" stroke-linejoin="round"/>'
            f'<path class="channel" d="{d}" stroke="{CHAN}" stroke-width="18" fill="none" stroke-linecap="butt" stroke-linejoin="round"/>')


def cell(x, y, r=6):
    return (f'<circle class="cell" cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{RED}" fill-opacity="0.18" stroke="{RED}" stroke-width="1.1"/>'
            f'<circle cx="{x + 1:.2f}" cy="{y - 0.5:.2f}" r="{r * 0.38:.2f}" fill="{RED}" fill-opacity="0.55"/>')


def bead(x, y, col, r=5.5):
    return f'<circle class="bead" cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{col}" fill-opacity="0.35" stroke="{col}" stroke-width="1.6"/>'


def mono(x, y, s, size=LBL, fill=DARK, anchor="middle", weight=500):
    return T(x, y, s, size, weight, fill, anchor, mono=True)


def fig():
    W = 400.0
    out = []
    BC = [TEAL, ORANGE, PURPLE]

    # ---- 1: cells and beads meet oil and leave in droplets
    YC = 74.0
    out.append(channel(f"M8 44H84C110 44 118 {YC} 142 {YC}"))
    out.append(channel(f"M8 104H84C110 104 118 {YC} 142 {YC}"))
    out.append(channel(f"M164 30V118"))
    out.append(channel(f"M142 {YC}H392"))
    out.append(T(8, 26, "Cells", LBL, 600) + T(8, 130, "Barcoded beads", LBL, 600))
    out.append(T(174, 26, "Oil", LBL, 600))
    out.append(f'<path d="M164 34V48M159 43L164 49L169 43" stroke="{GREY_LINE}" stroke-width="1.2" fill="none"/>'
               f'<path d="M164 114V100M159 105L164 99L169 105" stroke="{GREY_LINE}" stroke-width="1.2" fill="none"/>')
    out.append(cell(30, 44) + cell(62, 44))
    out.append(bead(30, 104, BLUE) + bead(62, 104, GREEN))
    DX = [214.0, 276.0, 338.0]
    for x, c in zip(DX, BC):
        out.append(f'<ellipse class="droplet" cx="{x:.2f}" cy="{YC:.2f}" rx="25" ry="8" fill="white" stroke="{GREY_LINE}" stroke-width="0.9"/>')
    for x, c in zip(DX, BC):
        out.append(cell(x - 9, YC, 5) + bead(x + 9, YC, c, 4.6))
    out.append(note(196, 104, ["Each droplet holds", "one cell and one bead"]))

    # ---- 2: zoom into one bead's strand (the purple droplet), strand running left
    BX, BY, BR = 366.0, 198.0, 24.0
    ZC = PURPLE
    out.append(zoom_lines((DX[2] + 9, YC), 4.6, (BX, BY), BR))
    out.append(f'<circle class="bead" cx="{BX:.2f}" cy="{BY:.2f}" r="{BR}" fill="{ZC}" fill-opacity="0.25" stroke="{ZC}" stroke-width="1.8"/>')
    out.append(T(BX, BY + 4.5, "Bead", LBL, 600, None, "middle"))
    Y = BY
    h = 14.0
    blocks = [(270.0, BX - BR), (194.0, 266.0), (118.0, 190.0)]
    x0, x1 = blocks[0]
    out.append(f'<rect class="cell-barcode" x="{x0:.2f}" y="{Y - h / 2:.2f}" width="{x1 - x0:.2f}" height="{h}" fill="{ZC}"/>')
    x0, x1 = blocks[1]
    out.append(f'<rect class="umi" x="{x0:.2f}" y="{Y - h / 2:.2f}" width="{x1 - x0:.2f}" height="{h}" fill="{GREY_LINE}" fill-opacity="0.22" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    out.append(mono((x0 + x1) / 2, Y + 4.3, "GGCT", 11.5))
    x0, x1 = blocks[2]
    out.append(f'<rect class="poly-t" x="{x0:.2f}" y="{Y - h / 2:.2f}" width="{x1 - x0:.2f}" height="{h}" fill="white" stroke="{DARK}" stroke-width="0.9"/>')
    out.append(mono((x0 + x1) / 2, Y + 4.3, "TTTTTT", 11.5))
    # mRNA paired over the poly-T by its poly-A tail, running off to the left
    YM = Y - 22
    pc = (x0 + x1) / 2
    out.append(mono(pc, YM + 4.3, "AAAAAA", 11.5, RED))
    a_left = pc - 6 * 0.6 * 11.5 / 2
    out.append(f'<path class="mrna" d="M{a_left - 4:.2f} {YM:.2f}H12" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>')
    out.append(T(12, YM - 10, "mRNA", LBL, 600, RED))
    # cDNA copied from the mRNA, extending the bead's strand
    out.append(f'<path class="cdna" d="M{x0:.2f} {Y:.2f}H18" stroke="{DARK}" stroke-width="3" stroke-dasharray="6 3"/>'
               f'<path d="M22 {Y - 5:.2f}L14 {Y:.2f}L22 {Y + 5:.2f}" fill="none" stroke="{DARK}" stroke-width="1.6"/>')
    labels = [("cDNA", ["Copied from", "the mRNA"]), ("Poly-T", ["Catches the", "poly-A tail"]),
              ("UMI", ["Different on", "every strand"]), ("Cell barcode", ["Same on the", "whole bead"])]
    centers = [64.0, sum(blocks[2]) / 2, sum(blocks[1]) / 2, sum(blocks[0]) / 2]
    YL = Y + 24
    spans = []
    for (head, ls), cx in zip(labels, centers):
        out.append(T(cx, YL, head, LBL, 600, None, "middle") + note(cx, YL + 15, ls, "middle"))
        w = max(tw(s) for s in [head] + ls)
        spans.append((cx - w / 2, cx + w / 2))
    for a, b in zip(spans, spans[1:]):
        assert a[1] + 4 < b[0], (a, b)
    assert spans[0][0] > 4 and spans[-1][1] < 396

    # ---- 3: reads sorted by barcode and counted
    YH = YL + 66
    out.append(f'<path class="divider" d="M8 {YH - 20:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
    out.append(T(8, YH, "Reads sorted into cells and counted", LBL, 700))
    reads = [(0, "GATC", 1), (0, "GATC", 1), (0, "CCAT", 3), (1, "TAGG", 2), (1, "ACTA", 2), (2, "GGCT", 1)]
    YR0 = YH + 26
    RS = 19.0
    XB, XU, XG = 8.0, 42.0, 80.0
    out.append(T(XB, YR0, "Barcode", 10.5, 400, MUTED) + T(XU + 15, YR0, "UMI", 10.5, 400, MUTED, "middle") + T(XG, YR0, "Gene", 10.5, 400, MUTED))
    for i, (c, u, g) in enumerate(reads):
        y = YR0 + RS * (i + 1)
        out.append(f'<rect x="{XB:.2f}" y="{y - 9:.2f}" width="26" height="10" fill="{BC[c]}"/>')
        out.append(mono(XU + 15, y, u, 11.5))
        out.append(T(XG, y, f"Gene {g}", LBL))
    # duplicate reads from one molecule
    yA, yB = YR0 + RS - 4, YR0 + 2 * RS - 4
    bx = XG + tw("Gene 1") + 6
    out.append(f'<path class="bracket" d="M{bx:.2f} {yA - 5:.2f}H{bx + 4:.2f}V{yB + 5:.2f}H{bx:.2f}" fill="none" stroke="{DARK}" stroke-width="1"/>')
    out.append(note(bx + 9, yA + 1, ["Same UMI:", "counted once"]))
    # count table
    TX = 212.0
    CW = 42.0
    cx = [TX + 46 + CW * (j + 0.5) for j in range(3)]
    counts = [[1, 0, 1], [0, 2, 0], [1, 0, 0]]  # genes x cells
    yh = YR0 + RS
    for j in range(3):
        out.append(f'<rect x="{cx[j] - 13:.2f}" y="{YR0 - 9:.2f}" width="26" height="10" fill="{BC[j]}"/>')
        out.append(T(cx[j], yh, f"Cell {j + 1}", LBL, 600, None, "middle"))
    out.append(f'<path d="M{TX:.2f} {yh + 7:.2f}H{cx[2] + CW / 2:.2f}" stroke="{DARK}" stroke-width="0.9"/>')
    for g in range(3):
        y = yh + RS * (g + 1) + 4
        out.append(T(TX, y, f"Gene {g + 1}", LBL, 600))
        for j in range(3):
            v = counts[g][j]
            if v:
                out.append(f'<rect x="{cx[j] - CW / 2 + 3:.2f}" y="{y - 14:.2f}" width="{CW - 6:.2f}" height="18" rx="2" fill="{BC[j]}" fill-opacity="0.2"/>')
            out.append(T(cx[j], y, str(v), LBL, 600 if v else 400, None if v else MUTED, "middle"))
    assert cx[2] + CW / 2 <= 392
    assert bx + 9 + tw("counted once") < TX - 6
    H = YR0 + RS * 7 + 16
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 7, out, "Single-cell RNA-seq: cells and barcoded beads sealed into droplets, the parts of a bead's capture strand, and reads sorted by barcode into a table of counts per cell", origin=(4, 7))


if __name__ == "__main__":
    main(NAME, fig)
