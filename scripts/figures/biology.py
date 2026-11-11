"""Shared biology glyphs: nucleotide colors, base glyphs, nucleosomes and protein chains."""

import math

from figures.core import BLUE, DARK_PAGE, GREEN, GREY_LINE, INK, LBLUE, ORANGE, PURPLE, TEAL, T

# Base glyphs (A tip, T notch, C round notch, G round end), drawn pointing right,
# spanning x 0..w and y -h/2..h/2.
def base_path(kind, x, cy, w, h=3.6, flip=False):
    r = h / 2
    t = h * 0.6
    if kind == "A":
        d = f"M0 {-r}H{w - t}L{w} 0L{w - t} {r}H0Z"
    elif kind in ("T", "U"):
        d = f"M0 {-r}H{w}L{w - t} 0L{w} {r}H0Z"
    elif kind == "C":
        d = f"M0 {-r}H{w}A{r} {r} 0 0 0 {w} {r}H0Z"
    else:  # G
        d = f"M0 {-r}H{w - r}A{r} {r} 0 0 1 {w - r} {r}H0Z"
    col = {"A": PURPLE, "T": LBLUE, "U": LBLUE, "C": ORANGE, "G": GREEN}[kind]
    tf = f"translate({x:.2f},{cy:.2f})" + (f" scale(-1,1)" if flip else "")
    return f'<path transform="{tf}" fill="{col}" d="{d}"/>'


NUC_COL = {"A": PURPLE, "U": TEAL, "T": TEAL, "G": GREEN, "C": ORANGE}
LCIRC_FILL, LCIRC_STROKE = "#6ea6e6", BLUE
PCIRC_FILL = "#ab86bf"
AA = {"M": "Met", "P": "Pro", "E": "Glu", "K": "Lys", "L": "Leu", "N": "Asn", "A": "Ala", "G": "Gly",
      "C": "Cys", "S": "Ser", "Q": "Gln", "T": "Thr", "V": "Val", "R": "Arg"}


def protein_chain(out, k, x0, cw, n, cy, letters, fill, stroke, x_end=None):
    xs = [(x0 + cw * (i + 0.5)) * k for i in range(n)]
    xe = (x_end * k) if x_end else xs[-1]
    out.append(f'<g class="protein"><path d="M{xs[0]:.2f} {cy * k:.2f}H{xe:.2f}" stroke="{GREY_LINE}" stroke-width="1.5" fill="none"/>')
    for x, ch in zip(xs, letters):
        out.append(f'<circle cx="{x:.2f}" cy="{cy * k:.2f}" r="14.2" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>')
        out.append(T(x, cy * k + 4.4, ch, 13.2, 500, INK, "middle", dark=DARK_PAGE))
    out.append("</g>")


def nucleosome(cx, cy, r, tilt=-20):
    rx, ry, phi = r + 2.2, (r + 2.2) * 0.42, math.radians(tilt)
    p0 = (cx + rx * math.cos(phi), cy + rx * math.sin(phi))
    p1 = (cx - rx * math.cos(phi), cy - rx * math.sin(phi))
    arc = lambda sweep, w: (f'<path d="M{p1[0]:.2f} {p1[1]:.2f}A{rx:.2f} {ry:.2f} {tilt:g} 0 {sweep} {p0[0]:.2f} {p0[1]:.2f}" '
                            f'fill="none" stroke="{BLUE}" stroke-width="{w}" stroke-linecap="round"/>')
    return ('<g class="nucleosome">' + arc(1, 1.3)
            + f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{PCIRC_FILL}" stroke="{PURPLE}" stroke-width="0.9"/>'
            + arc(0, 1.6) + "</g>")
