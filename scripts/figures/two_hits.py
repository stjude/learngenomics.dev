"""Cells with two gene copies, shared by the two-hit figures 2.3 and 2.10."""

from figures.core import BLUE, DARK, GREY_LINE, ORANGE

N = 10
X0, X1 = 10.0, 390.0
CW = (X1 - X0) / N
CH = 40.0
TUMOR = "#fbe3c4"


def bar(out, x, y, h, broken):
    w = 5.0
    if not broken:
        out.append(f'<rect x="{x - w / 2:.2f}" y="{y:.2f}" width="{w}" height="{h:.2f}" rx="1.5" fill="{BLUE}"/>')
        return
    m = y + h * 0.48
    out.append(f'<path d="M{x - w / 2:.2f} {y + 1.5:.2f}q0 -1.5 1.5 -1.5h2q1.5 0 1.5 1.5V{m - 3:.2f}l-5 3.2Z" fill="{ORANGE}"/>')
    out.append(f'<path d="M{x - w / 2:.2f} {m + 5.4:.2f}l5 -3.2V{y + h - 1.5:.2f}q0 1.5 -1.5 1.5h-2q-1.5 0 -1.5 -1.5Z" fill="{ORANGE}"/>')


def cell(out, x, y, hits, tumor=False):
    fill = TUMOR if tumor else "#ffffff"
    sw = 1.6 if tumor else 0.8
    col = DARK if tumor else GREY_LINE
    out.append(f'<rect x="{x + 1:.2f}" y="{y:.2f}" width="{CW - 2:.2f}" height="{CH:.2f}" rx="6" fill="{fill}" stroke="{col}" stroke-width="{sw}"/>')
    cx = x + CW / 2
    bar(out, cx - 5.5, y + 9, CH - 18, hits >= 1)
    bar(out, cx + 5.5, y + 9, CH - 18, hits >= 2)
