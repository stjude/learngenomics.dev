"""Figure 1.12: Getting proteins to the right place."""

import math

from figures.core import (
    BLUE, DARK, GREEN, GREY_LINE, NAVY, ORANGE, PURPLE, T, TEAL, copyright_text, main, svg_doc,
)
from figures.drawing import smooth
from figures.biology import LCIRC_FILL, PCIRC_FILL

NAME = "1.12-protein-sorting"


def fig():
    W, H = 400.0, 290.0
    MUTED = "#4d4d4f"
    MX = 322.0                                   # straight right-hand stretch of the cell membrane
    out = [T(8, 18, "Getting proteins to the right place", 10, 700)]

    def bead(x, y, fill=LCIRC_FILL, stroke=BLUE, r=3.3):
        return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="0.8"/>'

    def chain(pts, tag=None, tag_n=1, line=True):
        """Bead chain through pts; the first tag_n beads (the chain's start) take the tag colour."""
        s = ""
        if line:
            s += f'<path d="{smooth(pts)}" fill="none" stroke="{GREY_LINE}" stroke-width="1"/>'
        for i, (x, y) in enumerate(pts):
            s += bead(x, y, *(tag if tag and i < tag_n else (LCIRC_FILL, BLUE)))
        return s

    def carrow(pts, col=GREY_LINE, sw=1.0, dash=None):
        d = smooth(pts)
        (x0, y0), (x1, y1) = pts[-2], pts[-1]
        a = math.atan2(y1 - y0, x1 - x0)
        hl, hw = 5.0, 2.6
        bx, by = x1 - hl * math.cos(a), y1 - hl * math.sin(a)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<g class="arrow"><path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}"{da}/>'
                f'<path d="M{bx - hw * math.sin(a):.2f} {by + hw * math.cos(a):.2f}L{x1:.2f} {y1:.2f}'
                f'L{bx + hw * math.sin(a):.2f} {by - hw * math.cos(a):.2f}Z" fill="{col}"/></g>')

    def ribosome(cx, cy, mrna=(-24, 24)):
        return (f'<g class="ribosome"><path d="M{cx + mrna[0]:.2f} {cy - 6:.2f}H{cx + mrna[1]:.2f}" stroke="{BLUE}" stroke-width="1.3"/>'
                f'<ellipse cx="{cx:.2f}" cy="{cy - 12:.2f}" rx="9.5" ry="5.5" fill="{NAVY}" fill-opacity="0.18" stroke="{NAVY}" stroke-opacity="0.5" stroke-width="0.9"/>'
                f'<ellipse cx="{cx:.2f}" cy="{cy + 1:.2f}" rx="12.5" ry="7.5" fill="{NAVY}" fill-opacity="0.1" stroke="{NAVY}" stroke-opacity="0.5" stroke-width="0.9"/></g>')

    def folded(cx, cy):
        """A whole folded protein: a short chain of small beads curled up."""
        pts = [(cx - 2.6, cy + 1.6), (cx - 1.4, cy - 2.4), (cx + 2.4, cy - 1.8), (cx + 1.6, cy + 2.4)]
        return (f'<path d="{smooth(pts)}" fill="none" stroke="{GREY_LINE}" stroke-width="0.7"/>'
                + "".join(bead(x, y, r=1.75) for x, y in pts))

    def vesicle(cx, cy, r=7.5, col=TEAL, inner=None):
        s = f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{col}" fill-opacity="0.12" stroke="{col}" stroke-width="1"/>'
        if inner is None:
            inner = folded(cx, cy)
        return '<g class="vesicle">' + s + inner + "</g>"

    # cell (membrane on the right runs straight so the channel can sit in it)
    cell = [(40, 34), (180, 30), (300, 34), (MX, 62), (MX, 150), (MX, 240), (300, 266), (160, 270), (36, 266), (10, 232),
            (8, 150), (12, 62)]
    out.append(f'<path class="cell-membrane" d="{smooth(cell, True)}" fill="{BLUE}" fill-opacity="0.06" stroke="{BLUE}" stroke-width="1.3"/>')
    # nucleus
    NC, NR = (58.0, 148.0), 42.0
    out.append(f'<circle class="nucleus" cx="{NC[0]}" cy="{NC[1]}" r="{NR}" fill="{PURPLE}" fill-opacity="0.12" stroke="{PURPLE}" stroke-width="1"/>')
    out.append(T(NC[0], NC[1] + 3, "Nucleus", 8, 600, anchor="middle"))
    # ER: two flattened sacs beside the nucleus
    ER1 = (100.0, 114.0, 220.0, 138.0)
    ER2 = (104.0, 146.0, 208.0, 168.0)
    for x0, y0, x1, y1 in (ER1, ER2):
        r = (y1 - y0) / 2
        out.append(f'<rect class="er" x="{x0}" y="{y0}" width="{x1 - x0:g}" height="{y1 - y0:g}" rx="{r:g}" '
                   f'fill="{TEAL}" fill-opacity="0.14" stroke="{TEAL}" stroke-width="1.1"/>')
    # 1. free ribosome: no label, the protein stays in the cell fluid
    out.append(ribosome(40, 84, (-20, 20)))
    out.append('<g class="free-protein">' + chain([(44, 93), (51, 98), (59, 99), (67, 96), (75, 99), (83, 96)]) + "</g>")
    out.append(T(26, 53, "No label: stays in", 8, 600))
    out.append(T(26, 63, "the cell fluid", 8, 600))
    # 2. ribosome docked on the ER; the signal peptide (chain start) leads the chain inside
    RX = 146.0
    out.append(ribosome(RX, ER1[1] - 8.5, (-26, 26)))
    out.append(f'<g class="translocon" fill="{NAVY}" fill-opacity="0.55">'
               f'<rect x="{RX - 7:.2f}" y="{ER1[1] - 2.5:.2f}" width="3" height="6" rx="1"/>'
               f'<rect x="{RX + 4:.2f}" y="{ER1[1] - 2.5:.2f}" width="3" height="6" rx="1"/></g>')
    er_chain = [(196, 127), (189, 128), (182, 127), (175, 126), (168, 127), (161, 128), (154, 127), (147.5, 123.5), (RX, 117)]
    out.append('<g class="er-protein">' + chain(er_chain, (TEAL, TEAL), 2) + "</g>")
    out.append(f'<path d="M206 92L194 123" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(196, 88, "Signal peptide", 8, 600))
    out.append(f'<path d="M{RX - 13:.2f} {ER1[1] - 14:.2f}L126 82" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(125, 81, "Ribosome", 8, 600, anchor="end"))
    out.append(T(214, 160, "ER", 8, 600))
    # quality control: misfolded protein leaves the ER and is destroyed
    clump = [(128, 157), (134, 152), (140, 158), (134, 161), (127, 151), (141, 152)]
    out.append('<g class="misfolded">' + f'<path d="{smooth(clump)}" fill="none" stroke="{GREY_LINE}" stroke-width="1"/>'
               + "".join(bead(x, y, "#c9c9cb", GREY_LINE) for x, y in clump) + "</g>")
    out.append(carrow([(134, 166), (134, 182)]))
    frags = [(127, 190), (134, 193), (141, 189), (131, 197), (139, 197)]
    out.append('<g class="destroyed">' + "".join(bead(x, y, "#c9c9cb", GREY_LINE, 1.8) for x, y in frags) + "</g>")
    out.append(T(148, 193, "Misfolded: destroyed", 8, 600))
    out.append(T(148, 203, "e.g. CFTR F508del", 7.5, 400, MUTED))
    # ER -> Golgi
    out.append(vesicle(232, 117))
    out.append(carrow([(240, 120), (246, 128)]))
    GC = (266.0, 152.0)
    out.append('<g class="golgi">')
    for i in range(4):
        y = GC[1] - 15 + i * 10
        w = 34 - abs(i - 1.5) * 4
        out.append(f'<path d="M{GC[0] - w / 2:.2f} {y - 3:.2f}Q{GC[0]:.2f} {y + 3:.2f} {GC[0] + w / 2:.2f} {y - 3:.2f}'
                   f'Q{GC[0] + w / 2 + 2.5:.2f} {y - 0.5:.2f} {GC[0] + w / 2:.2f} {y + 2:.2f}'
                   f'Q{GC[0]:.2f} {y + 8:.2f} {GC[0] - w / 2:.2f} {y + 2:.2f}'
                   f'Q{GC[0] - w / 2 - 2.5:.2f} {y - 0.5:.2f} {GC[0] - w / 2:.2f} {y - 3:.2f}Z" '
                   f'fill="{GREEN}" fill-opacity="0.16" stroke="{GREEN}" stroke-width="1"/>')
    out.append("</g>")
    out.append(T(GC[0], GC[1] + 34, "Golgi", 8, 600, anchor="middle"))
    # Golgi -> cell surface (membrane protein: the channel glyph from 1.14, lying across the membrane)
    out.append(vesicle(292, 118, col=GREEN))
    out.append(carrow([(283, 136), (287, 127)]))
    out.append(carrow([(299, 112), (310, 104)]))
    CY = 96.0
    out.append(f'<g class="channel" fill="{BLUE}" fill-opacity="0.45" stroke="{BLUE}" stroke-width="1">'
               f'<rect x="{MX - 11:.2f}" y="{CY - 9:.2f}" width="22" height="7.5" rx="3.5"/>'
               f'<rect x="{MX - 11:.2f}" y="{CY + 1.5:.2f}" width="22" height="7.5" rx="3.5"/></g>')
    out.append(T(MX + 16, CY + 3, "Cell surface", 8, 600))
    # Golgi -> out of the cell
    out.append(vesicle(298, 186, col=GREEN))
    out.append(carrow([(282, 166), (291, 178)]))
    out.append(f'<path class="fusing" d="M{MX:.2f} 197A8 8 0 0 0 {MX:.2f} 213" fill="{GREEN}" fill-opacity="0.12" stroke="{GREEN}" stroke-width="1"/>')
    out.append(carrow([(305, 190), (311, 197)]))
    out.append('<g class="secreted">' + folded(345, 200) + folded(356, 216) + "</g>")
    out.append(carrow([(MX - 4, 205), (334, 205)]))
    out.append(T(MX + 12, 238, "Out of the cell", 8, 600))
    # cell membrane label
    out.append(f'<path d="M{MX + 14:.2f} 54L{MX - 2:.2f} 64" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(MX + 16, 53, "Cell membrane", 8, 600))
    # other labels: into the nucleus and into a mitochondrion
    out.append('<g class="to-nucleus">' + chain([(54, 214), (47, 220), (40, 216), (33, 222)], (PCIRC_FILL, PURPLE), 1) + "</g>")
    out.append(carrow([(57, 207), (58, 194)]))
    out.append(T(18, 240, "To the nucleus", 8, 600))
    MC = (232.0, 236.0)
    out.append(f'<g class="mitochondrion"><ellipse cx="{MC[0]}" cy="{MC[1]}" rx="24" ry="11" fill="{ORANGE}" fill-opacity="0.2" stroke="{ORANGE}" stroke-width="1"/>'
               f'<path d="M{MC[0] - 17:.2f} {MC[1]:.2f}l4 -6 4 11 4 -11 4 11 4 -11 4 11 4 -11 4 6" fill="none" stroke="{ORANGE}" stroke-width="0.8"/></g>')
    out.append('<g class="to-mitochondrion">' + chain([(199, 234), (192, 238), (185, 234), (178, 238)], ("#fdd27f", ORANGE), 1) + "</g>")
    out.append(carrow([(201, 236), (206, 236)]))
    out.append(T(MC[0], MC[1] + 23, "To a mitochondrion", 8, 600, anchor="middle"))
    out.append(copyright_text(W - 6, H - 6))
    svg = svg_doc(W, H, out, "Getting proteins to the right place")
    # crop to content plus about 4 units of padding
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       'width="395.5" height="282.5" viewBox="2.5 6.75 395.5 282.5"')


if __name__ == "__main__":
    main(NAME, fig)
