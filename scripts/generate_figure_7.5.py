"""Figure 7.5: Histone tails, how a histone mark is named, and how marks relate to packing."""

import math

from figures.biology import nucleosome
from figures.core import BLUE, COPYRIGHT, DARK, FAINT_TEXT, GREEN, GREY_LINE, LBL, MUTED, ORANGE, PURPLE, T, main, svg_doc

NAME = "7.5-histone-marks"

# Human histone H3.1 (UniProt P68431), residues 1-36, numbered without the first methionine.
H3_TAIL = "ARTKQTARKSTGGKAPRKQLATKAARKSAPATGGVK"
KEY_LYSINES = (4, 9, 27, 36)
METHYL_FILL, METHYL_LINE = "#fbd38a", ORANGE   # the methyl highlight used in figures 7.3 and 7.4
ACETYL_FILL, ACETYL_LINE = "#cfe8bd", GREEN


def dot(x, y, kind, r=4.2):
    fill, line = (METHYL_FILL, METHYL_LINE) if kind == "me" else (ACETYL_FILL, ACETYL_LINE)
    return f'<circle class="{"methyl" if kind == "me" else "acetyl"}" cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}" stroke="{line}" data-dark-fill="{line}" stroke-width="1.3"/>'


def tail(cx, cy, r, deg, length, kind=None):
    """A short histone tail leaving the nucleosome at angle deg, with an optional mark at its end."""
    a = math.radians(deg)
    x0, y0 = cx + r * math.cos(a), cy - r * math.sin(a)
    x1, y1 = cx + (r + length) * math.cos(a), cy - (r + length) * math.sin(a)
    # a gentle wiggle so tails read as flexible chains
    nx, ny = -math.sin(a), -math.cos(a)
    mx, my = (x0 + x1) / 2 + nx * 2.5, (y0 + y1) / 2 + ny * 2.5
    s = f'<path class="tail" d="M{x0:.2f} {y0:.2f}Q{mx:.2f} {my:.2f} {x1:.2f} {y1:.2f}" fill="none" stroke="{PURPLE}" stroke-width="1.6" stroke-linecap="round"/>'
    if kind:
        s += dot(x1 + 3.2 * math.cos(a), y1 - 3.2 * math.sin(a), kind, 3.4)
    return s


def divider(y):
    return f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>'


def section_name(out, y0):
    """The H3 tail as its sequence, leading into a nucleosome, then the name H3K27me3 decoded."""
    out.append(T(8, y0, "Reading a mark\u2019s name", LBL, 700))
    ys = y0 + 52                     # baseline of the sequence letters
    cw = 6.9                         # letter pitch
    x0 = 16
    xe = x0 + cw * len(H3_TAIL)
    NX, NR = xe + 52, 30
    out.append(f'<path class="tail" d="M{x0 - 4:.2f} {ys + 6:.2f}H{xe:.2f}Q{xe + 14:.2f} {ys + 6:.2f} {NX - NR:.2f} {ys - 2:.2f}" '
               f'fill="none" stroke="{PURPLE}" stroke-width="1.6" stroke-linecap="round"/>')
    out.append(nucleosome(NX, ys - 4, NR))
    for deg, ln in ((70, 16), (130, 14), (250, 15), (305, 14)):
        out.append(tail(NX, ys - 4, NR, deg, ln))
    out.append(T(NX, ys + 46, "nucleosome", LBL, 400, MUTED, "middle"))
    for i, aa in enumerate(H3_TAIL, 1):
        x = x0 + cw * (i - 0.5)
        key = i in KEY_LYSINES
        out.append(T(x, ys, aa, 10.5, 700 if key else 400, DARK if key else FAINT_TEXT, "middle", mono=True))
        if key:
            out.append(T(x, ys + 21, str(i), 10.5, 600, BLUE, "middle"))
    xk = x0 + cw * (27 - 0.5)
    out.append(f'<path d="M{xk:.2f} {ys - 11:.2f}V{ys - 17:.2f}" stroke="{DARK}" stroke-width="1"/>')
    out.append(dot(xk - 9, ys - 22, "me") + dot(xk, ys - 25, "me") + dot(xk + 9, ys - 22, "me"))
    out.append(T(x0 - 4, ys - 24, "histone H3 tail", LBL, 400, MUTED))
    # the name, decoded
    yn = ys + 68
    size = 22
    w = 0.6 * size
    name = "H3K27me3"
    nx0 = 196 - w * len(name) / 2
    out.append(T(196, yn, name, size, 700, DARK, "middle", mono=True))
    parts = ((0, 2, "histone", "H3"), (2, 5, "lysine (K)", "at position 27"), (5, 8, "three methyl", "groups"))
    cols = (64, 196, 328)
    for (a, b, l1, l2), xc in zip(parts, cols):
        xa, xb = nx0 + a * w + 1.5, nx0 + b * w - 1.5
        yb = yn + 7
        xm = (xa + xb) / 2
        out.append(f'<path d="M{xa:.2f} {yb:.2f}V{yb + 4:.2f}H{xb:.2f}V{yb:.2f}M{xm:.2f} {yb + 4:.2f}L{xc:.2f} {yb + 20:.2f}" '
                   f'fill="none" stroke="{DARK}" stroke-width="1"/>')
        out.append(T(xc, yb + 34, l1, LBL, 600, DARK, "middle") + T(xc, yb + 49, l2, LBL, 400, MUTED, "middle"))
    return yn + 96


def section_packing(out, y0):
    out.append(T(8, y0, "Marks and packing", LBL, 700))
    yc = y0 + 58
    # closed: two staggered rows of nucleosomes, tails carrying methyl marks
    r = 11
    xs = [30 + 22 * k for k in range(7)]
    for k, x in enumerate(xs):
        y = yc - 9 if k % 2 == 0 else yc + 9
        out.append(tail(x, y, r, 90 if k % 2 == 0 else 270, 7, "me"))
    out.append(f'<path class="dna" d="M{xs[0] - 14:.2f} {yc:.2f}' + "".join(
        f'L{x:.2f} {yc - 9 if k % 2 == 0 else yc + 9:.2f}' for k, x in enumerate(xs)) + f'L{xs[-1] + 14:.2f} {yc:.2f}" '
        f'fill="none" stroke="{BLUE}" stroke-width="1.6" stroke-linejoin="round"/>')
    for k, x in enumerate(xs):
        out.append(nucleosome(x, yc - 9 if k % 2 == 0 else yc + 9, r))
    # open: spaced nucleosomes on a stretch of DNA, tails carrying acetyl marks
    xo = [236, 290, 344]
    out.append(f'<path class="dna" d="M214 {yc:.2f}H382" stroke="{BLUE}" stroke-width="1.6" stroke-linecap="round"/>')
    for x in xo:
        out.append(tail(x, yc, r, 60, 8, "ac") + tail(x, yc, r, 120, 8, "ac") + tail(x, yc, r, 270, 8, "ac"))
        out.append(nucleosome(x, yc, r))
    yl = yc + 48
    out.append(T(98, yl, "H3K9me3, H3K27me3", LBL, 600, DARK, "middle"))
    out.append(T(98, yl + 15, "tightly packed, genes kept off", LBL, 400, MUTED, "middle"))
    out.append(T(298, yl, "H3K27ac", LBL, 600, DARK, "middle"))
    out.append(T(298, yl + 15, "loosely packed, genes active", LBL, 400, MUTED, "middle"))
    return yl + 34


def fig():
    out = []
    y = section_name(out, 20)
    out.append(divider(y - 18))
    y = section_packing(out, y)
    out.append(divider(y - 14))
    y += 8
    out.append(dot(26, y - 4, "me") + T(36, y + 0.5, "methyl group", LBL, 400, MUTED))
    out.append(dot(216, y - 4, "ac") + T(226, y + 0.5, "acetyl group", LBL, 400, MUTED))
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(392, H - 7, out, "Histone tails carry chemical marks; the name H3K27me3 means three methyl groups on lysine 27 of histone H3; some marks go with tightly packed DNA and others with open DNA", origin=(4, 7))


if __name__ == "__main__":
    main(NAME, fig)
