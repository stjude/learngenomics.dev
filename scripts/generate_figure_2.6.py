"""Figure 2.6: The RAS–MAPK relay and the changes in cancer that lock it on."""

from figures.core import COPYRIGHT, DARK, GREY_LINE, MUTED, NAVY, ORANGE, PURPLE, T, main, svg_doc
from figures.drawing import CALLOUT

NAME = "2.6-ras-mapk"

X0, X1 = 10.0, 390.0
CX = 118.0
NW, NH = 72.0, 26.0
NODE = ("#a9dcec", "#4f9fbb")
MEMB = "#efeeec"
BX = 230.0


def node(out, cy, label, w=NW, x=None, fill=NODE[0], stroke=NODE[1]):
    x = CX - w / 2 if x is None else x
    out.append(f'<rect x="{x:.2f}" y="{cy - NH / 2:.2f}" width="{w:.2f}" height="{NH:.2f}" rx="7" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    out.append(T(x + w / 2, cy + 4.5, label, 13, 700, DARK, "middle"))
    return x, x + w


def down(out, y0, y1):
    out.append(f'<path d="M{CX:.2f} {y0:.2f}V{y1 - 6:.2f}" stroke="{DARK}" stroke-width="1.6" fill="none"/>')
    out.append(f'<path d="M{CX - 4.5:.2f} {y1 - 7:.2f}L{CX:.2f} {y1:.2f}L{CX + 4.5:.2f} {y1 - 7:.2f}Z" fill="{DARK}"/>')


def badge(out, x, y, r=6.5):
    out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{ORANGE}" stroke="#a8650a" stroke-width="1"/>')
    out.append(f'<path d="M{x:.2f} {y - 3.4:.2f}V{y + 0.6:.2f}" stroke="{DARK}" stroke-width="1.6" stroke-linecap="round"/>')
    out.append(f'<circle cx="{x:.2f}" cy="{y + 3.1:.2f}" r="0.95" fill="{DARK}"/>')


def callout(out, x_from, y_from, cy, title, desc):
    out.append(f'<path d="M{x_from:.2f} {y_from:.2f}L{BX - 9:.2f} {cy:.2f}" {CALLOUT}/>')
    badge(out, BX, cy)
    out.append(T(BX + 12, cy + 4.5, title, 12, 700, DARK))
    out.append(T(BX + 12, cy + 19.5, desc, 12, 400, MUTED))


def fig():
    W = 400.0
    out = []
    y = 20
    badge(out, X0 + 6.5, y - 4)
    out.append(T(X0 + 18, y, "changes in cancer that lock the relay on", 12, 400, MUTED))

    # membrane
    m0, m1 = 72.0, 86.0
    out.append(f'<rect x="{X0:.2f}" y="{m0:.2f}" width="{X1 - X0:.2f}" height="{m1 - m0:.2f}" fill="{MEMB}"/>')
    out.append(f'<path d="M{X0:.2f} {m0:.2f}H{X1:.2f}M{X0:.2f} {m1:.2f}H{X1:.2f}" stroke="{GREY_LINE}" stroke-width="0.9" fill="none"/>')
    out.append(T(X1 - 2, m0 - 6, "cell membrane", 12, 400, MUTED, "end"))
    out.append(T(X0, 44, "outside the cell", 12, 400, MUTED))
    out.append(T(X0, m1 + 16, "inside the cell", 12, 400, MUTED))

    # receptor with a cup at the top holding the growth factor
    rt, rb = 54.0, 104.0
    out.append(f'<path d="M{CX - 9:.2f} {rt:.2f}V{rb - 6:.2f}q0 6 6 6h6q6 0 6 -6V{rt:.2f}" fill="{NAVY}"/>')
    out.append(f'<path d="M{CX - 3.4:.2f} {rt:.2f}V{rt + 9:.2f}q0 3 3.4 3q3.4 0 3.4 -3V{rt:.2f}Z" fill="#ffffff"/>')
    out.append(f'<circle cx="{CX:.2f}" cy="{rt - 2:.2f}" r="6.5" fill="{PURPLE}"/>')
    out.append(T(CX + 12, rt - 4, "growth factor", 12, 400, DARK))
    out.append(T(CX - 14, rt + 12, "receptor", 12, 400, DARK, "end"))
    callout(out, CX + 9, rb - 8, rb - 8, "EGFR or ERBB2", "mutated or amplified")

    ras = 128.0
    down(out, rb + 2, ras - NH / 2 - 1)
    _, rx1 = node(out, ras, "RAS")
    callout(out, rx1, ras, ras, "KRAS G12, G13 or Q61", "hard to switch off")

    # NF1, the off switch for RAS
    nf = ras + 34
    nx0, nx1 = node(out, nf, "NF1", w=44, x=rx1 + 12, fill="#ffffff", stroke=GREY_LINE)
    ax, ay = rx1 + 4, ras + NH / 2 - 2
    out.append(f'<path d="M{nx0 + 4:.2f} {nf - NH / 2:.2f}L{ax + 2:.2f} {ay + 3:.2f}" stroke="{GREY_LINE}" stroke-width="1.4" fill="none"/>')
    out.append(f'<path d="M{ax - 2.6:.2f} {ay + 0.6:.2f}L{ax + 5.6:.2f} {ay + 6.4:.2f}" stroke="{GREY_LINE}" stroke-width="1.6" fill="none"/>')
    out.append(T(nx0 - 18, nf + 22, "turns RAS off", 12, 400, MUTED))
    callout(out, nx1, nf, nf, "NF1 lost", "RAS is slow to switch off")

    raf = nf + 46
    down(out, ras + NH / 2 + 1, raf - NH / 2 - 1)
    _, fx1 = node(out, raf, "RAF")
    callout(out, fx1, raf, raf, "BRAF V600E", "on even without RAS")

    mek = raf + 52
    down(out, raf + NH / 2 + 1, mek - NH / 2 - 1)
    node(out, mek, "MEK")
    erk = mek + 52
    down(out, mek + NH / 2 + 1, erk - NH / 2 - 1)
    node(out, erk, "ERK")
    out.append(T(CX + NW / 2 + 12, (raf + erk) / 2 + 4, "each one switches", 12, 400, MUTED))
    out.append(T(CX + NW / 2 + 12, (raf + erk) / 2 + 19, "on the next", 12, 400, MUTED))

    nt = erk + NH / 2 + 26
    down(out, erk + NH / 2 + 1, nt)
    nb = nt + 54
    out.append(f'<rect x="{X0:.2f}" y="{nt:.2f}" width="{X1 - X0:.2f}" height="{nb - nt:.2f}" rx="12" fill="{MEMB}" stroke="{GREY_LINE}" stroke-width="0.9"/>')
    out.append(T(X0 + 12, nt + 20, "nucleus", 12, 700, DARK))
    out.append(T(X0 + 12, nt + 38, "Genes for growth and division switch on.", 12, 400, DARK))

    H = nb + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "The RAS–MAPK relay and the changes in cancer that lock it on.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
