"""Figure 1.8: Translation by the ribosome."""

import math

from figures.core import (
    BLUE, DARK, DARK_PAGE, GREY_LINE, INK, LBLUE, NAVY, ORANGE, T, copyright_text, main, svg_doc,
)
from figures.drawing import smooth
from figures.biology import LCIRC_FILL, LCIRC_STROKE, NUC_COL

NAME = "1.8-ribosome"


def fig():
    W, H = 404.0, 296.0
    MUTED = "#4d4d4f"
    seq = "AUGCCUGAGCCAAGGCUUGAAAACGCCGGU"
    comp = {"A": "U", "U": "A", "G": "C", "C": "G"}
    X0, PITCH, P = 34.0, 35.5, 10.5
    YB = 220.0                                    # mRNA backbone
    lx = lambda i, j: X0 + i * PITCH + P * (j + 0.5)
    ccx = lambda i: X0 + i * PITCH + 1.5 * P
    base_col = lambda b: LBLUE if b == "U" else NUC_COL[b]
    out = []
    # ribosome: large subunit above the mRNA, small subunit below
    large = [(101, 216), (93, 176), (100, 128), (128, 103), (178, 100), (210, 114), (222, 160), (217, 216)]
    small = [(106, 223), (128, 222), (184, 222), (207, 224), (209, 246), (188, 262), (126, 262), (104, 248)]
    out.append('<g class="ribosome">'
               f'<path class="large-subunit" d="{smooth(large, True)}" fill="{NAVY}" fill-opacity="0.09" stroke="{NAVY}" stroke-opacity="0.45" stroke-width="1"/>'
               f'<path class="small-subunit" d="{smooth(small, True)}" fill="{NAVY}" fill-opacity="0.18" stroke="{NAVY}" stroke-opacity="0.45" stroke-width="1"/></g>')
    # mRNA: backbone, base ticks, letters, cap and ends
    out.append('<g class="mrna">')
    for k, b in enumerate(seq):
        x = lx(k // 3, k % 3)
        out.append(f'<path d="M{x:.2f} {YB:.2f}V{YB - 9.5:.2f}" stroke="{base_col(b)}" stroke-width="1.6"/>')
        out.append(T(x, YB + 12.5, b, 9, 400, anchor="middle"))
    out.append(f'<path d="M30 {YB}H{lx(9, 2) + 6:.2f}" stroke="{BLUE}" stroke-width="1.6"/>')
    out.append(f'<circle cx="27" cy="{YB}" r="3.6" fill="{NAVY}"/>')
    out.append(T(20, YB + 3, "5\u2032", 8, 400, anchor="end"))
    out.append(T(lx(9, 2) + 9, YB + 3, "3\u2032", 8, 400))
    out.append("</g>")

    def trna(i, by, rot=0.0, piv=None, dx=0.0, dy=0.0, op=1.0, paired=True, cls="trna", codon_i=None):
        cx = ccx(i)
        ci = i if codon_i is None else codon_i
        ac = "".join(comp[b] for b in seq[3 * ci:3 * ci + 3])
        pts = [(cx - 16, by), (cx + 16, by), (cx + 16, by - 13), (cx + 4, by - 13), (cx + 4, by - 46), (cx + 13, by - 46),
               (cx + 13, by - 55), (cx - 13, by - 55), (cx - 13, by - 46), (cx - 4, by - 46), (cx - 4, by - 13), (cx - 16, by - 13)]
        px, py = piv or (cx, by)
        tr = f' transform="translate({dx:g},{dy:g}) rotate({rot:g},{px:.2f},{py:.2f})"' if (rot or dx or dy) else ""
        # Fade only the shapes: group opacity would also fade the letters below 4.5:1.
        fade = f' opacity="{op:g}"' if op < 1 else ""
        g = [f'<g class="{cls}"{tr}>']
        g.append(f'<path{fade} d="M' + "L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + f'Z" fill="{ORANGE}" fill-opacity="0.3" '
                 f'stroke="{ORANGE}" stroke-width="1.1" stroke-linejoin="round"/>')
        g.append(f'<path{fade} d="M{cx:.2f} {by - 55:.2f}V{by - 61:.2f}" stroke="{ORANGE}" stroke-width="1.6"/>')
        for j, b in enumerate(ac):
            g.append(T(lx(i, j), by - 3.6, b, 8, 600, MUTED if op < 1 else None, "middle"))
            if paired:
                g.append(f'<path d="M{lx(i, j):.2f} {by + 0.6:.2f}V{YB - 9.5:.2f}" stroke="{base_col(b)}" stroke-width="1.6"/>')
        g.append("</g>")
        return "".join(g), (cx, by - 61)

    def bead(x, y, ch):
        return (f'<circle cx="{x:.2f}" cy="{y:.2f}" r="8.5" fill="{LCIRC_FILL}" stroke="{LCIRC_STROKE}" stroke-width="1.2"/>'
                + T(x, y + 2.9, ch, 8.5, 500, INK, "middle", dark=DARK_PAGE))

    BY = 199.0
    # leaving, empty tRNA over GAG (codon 3)
    e, _ = trna(2, BY, -20, (ccx(2) - 16, BY), -4, -7, 0.5, False, "trna leaving")
    out.append(e)
    # tRNA over CCA (codon 4) holding the growing chain M-P-E-P
    t4, top4 = trna(3, BY, cls="trna with-chain")
    out.append(t4)
    chain = [(top4[0], top4[1] - 8.5), (top4[0] - 4, top4[1] - 27), (top4[0] - 12, top4[1] - 45), (top4[0] - 24, top4[1] - 61)]
    out.append(f'<g class="protein"><path d="M{top4[0]:.2f} {top4[1]:.2f}' + "".join(f"L{x:.2f} {y:.2f}" for x, y in chain)
               + f'" fill="none" stroke="{GREY_LINE}" stroke-width="1.4"/>'
               + "".join(bead(x, y, ch) for (x, y), ch in zip(chain, "PEPM")) + "</g>")
    # tRNA over AGG (codon 5) that has just arrived with arginine
    t5, top5 = trna(4, BY, cls="trna arriving")
    out.append(t5 + '<g class="amino-acid">' + bead(top5[0], top5[1] - 8.5, "R") + "</g>")
    # free tRNA with leucine drifting in (anticodon GAA for CUU)
    fi = 7
    tf, topf = trna(fi, 178, 12, None, 0, 0, 1.0, False, "trna free", codon_i=5)
    fx, fy = topf
    a = math.radians(12)
    bx, by_ = ccx(fi) + (fx - ccx(fi)) * math.cos(a) - (fy - 8.5 - 178) * math.sin(a), 178 + (fx - ccx(fi)) * math.sin(a) + (fy - 8.5 - 178) * math.cos(a)
    out.append(tf + '<g class="amino-acid">' + bead(bx, by_, "L") + "</g>")
    q0, q1, q2, q3 = (ccx(fi) - 26, 150), (254, 140), (242, 144), (232, 157)
    ux, uy = q3[0] - q2[0], q3[1] - q2[1]
    L = math.hypot(ux, uy); ux, uy = ux / L, uy / L
    hb = (q3[0] - 6 * ux, q3[1] - 6 * uy)
    out.append(f'<g class="incoming"><path d="M{q0[0]:.2f} {q0[1]}C{q1[0]} {q1[1]} {q2[0]} {q2[1]} {hb[0]:.2f} {hb[1]:.2f}" fill="none" '
               f'stroke="{MUTED}" stroke-width="0.9" stroke-dasharray="2.5 2"/>'
               f'<path d="M{hb[0] - 3 * uy:.2f} {hb[1] + 3 * ux:.2f}L{q3[0]} {q3[1]}L{hb[0] + 3 * uy:.2f} {hb[1] - 3 * ux:.2f}Z" fill="{MUTED}"/></g>')
    # labels
    out.append('<g class="labels">')
    lead = lambda d: f'<path d="{d}" fill="none" stroke="{DARK}" stroke-width="0.6"/>'
    out.append(T(X0, YB - 14, "mRNA", 8, 600))
    out.append(lead(f"M{ccx(4) + 13:.2f} 147L250 112M{ccx(fi) - 10:.2f} 120L262 112"))
    out.append(T(256, 108, "tRNA", 8, 600, anchor="middle"))
    out.append(lead(f"M{ccx(fi) + 16:.2f} 172L332 172"))
    out.append(T(335, 174.8, "Anticodon", 8, 600))
    i = 5
    out.append(lead(f"M{lx(i, 0) - 4:.2f} {YB + 16:.2f}V{YB + 19:.2f}H{lx(i, 2) + 4:.2f}V{YB + 16:.2f}"))
    out.append(T(ccx(i), YB + 29, "Codon", 8, 600, anchor="middle"))
    out.append(lead("M98 252L80 262"))
    out.append(T(78, 269, "Ribosome", 8, 600, anchor="end"))
    cx0, cy0 = chain[-1]
    out.append(lead(f"M{cx0 - 9.5:.2f} {cy0:.2f}H{cx0 - 15:.2f}"))
    out.append(T(cx0 - 17, cy0 + 2.8, "Growing protein chain", 8, 600, anchor="end"))
    out.append("</g>")
    # direction of travel
    ay = 276.0
    out.append(f'<g class="direction"><path d="M112 {ay}H146" stroke="{MUTED}" stroke-width="1.2"/>'
               f'<path d="M145 {ay - 3.5}L151 {ay}L145 {ay + 3.5}Z" fill="{MUTED}"/></g>')
    out.append(T(157, ay + 2.8, "Ribosome moves 5\u2032 \u2192 3\u2032, one codon at a time", 8, 400, MUTED))
    out.append(T(8, 54, "Translation by the ribosome", 10, 700))
    out.append(copyright_text(W - 6, H - 4))
    svg = svg_doc(W, H, out, "Translation by the ribosome")
    # crop to content plus about 4 units of padding
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       'width="398" height="254" viewBox="4 42.5 398 254"')


if __name__ == "__main__":
    main(NAME, fig)
