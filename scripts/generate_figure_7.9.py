"""Figure 7.9: The structure of DNA."""

import math

from figures.core import (
    COPYRIGHT, DARK, DARK_PAGE, GREEN, GREY_LINE, LBLUE, MUTED, ORANGE, PURPLE, T, main, svg_doc,
)

NAME = "7.9-dna-ladder"

BASE_COL = {"A": PURPLE, "T": LBLUE, "G": GREEN, "C": ORANGE}
PAIR = {"A": "T", "T": "A", "G": "C", "C": "G"}
PURINE = {"A", "G"}
SUGAR_FILL = "#eceef1"
PR = 9.5
DY = 66.0
XL, XR = 138.0, 262.0
PDX = 23.0


# sugar ring for the left strand, before any rotation: O, C1', C2', C3', C4'
RING = [(0, -14), (14, -2), (9, 13), (-9, 13), (-14, -2)]


def rot(p, flip):
    return (-p[0], -p[1]) if flip else p


def ln(x1, y1, x2, y2, col=DARK, sw=1.6, extra="", cap="round"):
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="{cap}"{extra}/>'


def phosphate(out, x, y):
    out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{PR}" fill="#ffffff" stroke="{DARK}" stroke-width="1.4"/>')
    out.append(T(x, y + 4, "P", 11, 700, DARK, "middle"))


def sugar(out, cx, cy, flip):
    pts = [rot(p, flip) for p in RING]
    d = "M" + "L".join(f"{cx + x:.2f} {cy + y:.2f}" for x, y in pts) + "Z"
    out.append(f'<path d="{d}" fill="{SUGAR_FILL}" stroke="{DARK}" stroke-width="1.4" stroke-linejoin="round"/>')
    return [(cx + x, cy + y) for x, y in pts]


def toward(x0, y0, x1, y1, r):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    return x1 - dx / L * r, y1 - dy / L * r


def strand(out, cx, ys, flip):
    s = -1 if flip else 1
    sugars = []
    for y in ys:
        sugars.append(sugar(out, cx, y, flip))
    links = []
    for i, y in enumerate(ys):
        pts = sugars[i]
        c4, c3 = pts[4], pts[3]
        c5 = (cx - s * 22, y - s * 14)
        px5 = (cx - s * PDX, y - s * DY / 2)
        links.append(ln(*c4, *c5))
        links.append(ln(*c5, *toward(*c5, *px5, PR)))
        px3 = (cx - s * PDX, y + s * DY / 2)
        last = (i == 0) if flip else (i == len(ys) - 1)
        if not last:
            links.append(ln(*c3, *toward(*c3, *px3, PR)))
    out[:0] = links
    return sugars


def fig():
    W = 400.0
    seq = "ATGCC"
    y0 = 84.0
    ys = [y0 + i * DY for i in range(len(seq))]
    out = []
    # base pairs first so the sugars sit on top
    gap = 16.0
    h = 20.0
    xa, xb = XL + 13, XR - 13
    span = xb - xa - gap
    for i, b in enumerate(seq):
        y = ys[i]
        p = PAIR[b]
        la = span * (0.56 if b in PURINE else 0.44)
        lb = span - la
        out.append(f'<rect x="{xa:.2f}" y="{y - h / 2:.2f}" width="{la:.2f}" height="{h}" rx="3" fill="{BASE_COL[b]}"/>')
        out.append(f'<rect x="{xb - lb:.2f}" y="{y - h / 2:.2f}" width="{lb:.2f}" height="{h}" rx="3" fill="{BASE_COL[p]}"/>')
        for x, c, w in ((xa, b, la), (xb - lb, p, lb)):
            out.append(T(x + w / 2, y + 4.5, c, 13, 700, "#ffffff" if c == "A" else DARK, "middle", dark=None if c == "A" else DARK_PAGE))
        n = 3 if b in "GC" else 2
        offs = [-6, 0, 6] if n == 3 else [-3.5, 3.5]
        g0 = xa + la
        for o in offs:
            out.append(ln(g0 + 3, y + o, g0 + gap - 3, y + o, DARK, 1.4, " stroke-dasharray=\"3 2\"", "butt"))
    left, right = [], []
    lsug = strand(left, XL, ys, False)
    rsug = strand(right, XR, ys, True)
    out = left + right + out
    for i, y in enumerate(ys):
        phosphate(out, XL - PDX, y - DY / 2)
        phosphate(out, XR + PDX, y + DY / 2)
    # re-draw sugars on top of links
    for y in ys:
        sugar(out, XL, y, False)
        sugar(out, XR, y, True)
    # 3' ends: short stub with OH
    c3 = lsug[-1][3]
    out.append(ln(*c3, c3[0] - 6, c3[1] + 12))
    out.append(T(c3[0] - 8, c3[1] + 26, "OH", 11, 400, DARK, "middle"))
    c3 = rsug[0][3]
    out.append(ln(*c3, c3[0] + 6, c3[1] - 12))
    out.append(T(c3[0] + 8, c3[1] - 16, "OH", 11, 400, DARK, "middle"))
    # strand ends
    yt = y0 - DY / 2
    yb = ys[-1] + DY / 2
    out.append(T(XL - PDX, yt - 20, "5\u2032", 14, 700, DARK, "middle"))
    out.append(T(XL - 14, yb + 22, "3\u2032", 14, 700, DARK, "middle"))
    out.append(T(XR + 14, yt - 20, "3\u2032", 14, 700, DARK, "middle"))
    out.append(T(XR + PDX, yb + 22, "5\u2032", 14, 700, DARK, "middle"))
    # carbon numbers on the first sugar
    s0 = lsug[0]
    out.append(T(s0[1][0] + 1, s0[1][1] - 10, "1\u2032", 10, 400, MUTED))
    out.append(T(s0[3][0] + 2, s0[3][1] + 14, "3\u2032", 10, 400, MUTED))
    out.append(T(XL - 22 + 4, y0 - 14 - 2, "5\u2032", 10, 400, MUTED))
    # labels, left
    lx = XL - PDX - PR - 12
    out.append(T(lx, yt + 4, "phosphate", 12, 400, MUTED, "end"))
    out.append(ln(lx + 3, yt, XL - PDX - PR - 2, yt, GREY_LINE, 0.8))
    out.append(T(lx, y0 + 4, "sugar", 12, 400, MUTED, "end"))
    out.append(ln(lx + 3, y0, XL - 15, y0, GREY_LINE, 0.8))
    # labels, right
    # base label over first base
    out.append(T(xa + span * 0.56 / 2 + 6, y0 - 18, "base", 12, 400, MUTED, "middle"))
    # hydrogen-bond label
    gx = xa + span * 0.44 + gap / 2
    out.append(T(gx, ys[-1] + 44, "hydrogen bonds", 12, 400, MUTED, "middle"))
    out.append(ln(gx, ys[-1] + 31, gx, ys[-1] + 12, GREY_LINE, 0.8))
    # direction arrows outside the strands
    ax = 58.0
    out.append(ln(ax, ys[1] + 8, ax, ys[-1] + 14, DARK, 1.6))
    out.append(f'<path d="M{ax - 5:.2f} {ys[-1] + 12:.2f}L{ax:.2f} {ys[-1] + 22:.2f}L{ax + 5:.2f} {ys[-1] + 12:.2f}Z" fill="{DARK}"/>')
    bx = 342.0
    out.append(ln(bx, ys[-2] - 8, bx, ys[0] - 14, DARK, 1.6))
    out.append(f'<path d="M{bx - 5:.2f} {ys[0] - 12:.2f}L{bx:.2f} {ys[0] - 22:.2f}L{bx + 5:.2f} {ys[0] - 12:.2f}Z" fill="{DARK}"/>')
    H = yb + 50
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "The structure of DNA.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
