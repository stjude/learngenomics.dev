"""Figure 4.5: Nanopore sequencing."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, NAVY, SANS, T, TEAL, main, svg_doc
from figures.drawing import leader, panel_head
from figures.sequences import BASE_C, base_cells

NAME = "4.5-nanopore-sequencing"


def fig():
    import random
    W, H = 400.0, 460.0
    MUTED = "#4d4d4f"
    out = []
    # a. pore in a membrane
    out.append(panel_head(8, 20, "a", "Pore in a membrane"))
    MT, MB, PX = 100.0, 126.0, 150.0
    s = f'<g class="membrane"><rect x="8" y="{MT:.2f}" width="{PX - 18 - 8:.2f}" height="{MB - MT:.2f}" fill="{GREY_LINE}" fill-opacity="0.15"/>'
    s += f'<rect x="{PX + 18:.2f}" y="{MT:.2f}" width="{392 - PX - 18:.2f}" height="{MB - MT:.2f}" fill="{GREY_LINE}" fill-opacity="0.15"/>'
    x = 11.0
    while x < 392:
        if not (PX - 21 < x < PX + 21):
            s += f'<circle cx="{x:.2f}" cy="{MT + 2.8:.2f}" r="2.6"/><circle cx="{x:.2f}" cy="{MB - 2.8:.2f}" r="2.6"/>'
        x += 7
    s = s.replace("<circle ", f'<circle fill="{GREY_LINE}" fill-opacity="0.6" ')
    out.append(s + "</g>")
    out.append(f'<g class="nanopore" fill="{BLUE}"><rect x="{PX - 18:.2f}" y="{MT - 10:.2f}" width="11" height="{MB - MT + 20:.2f}" rx="4"/>'
               f'<rect x="{PX + 7:.2f}" y="{MT - 10:.2f}" width="11" height="{MB - MT + 20:.2f}" rx="4"/></g>')
    # double strand above, single strand through the pore
    ds = '<g class="dna" fill="none" stroke-width="1.6">'
    ds += f'<path d="M{PX - 4:.2f} 64C{PX - 4:.2f} 50 {PX - 22:.2f} 44 {PX - 22:.2f} 28" stroke="{DARK}"/>'
    ds += f'<path d="M{PX + 4:.2f} 64C{PX + 4:.2f} 50 {PX - 14:.2f} 44 {PX - 14:.2f} 28" stroke="{DARK}"/>'
    for t in [0.15, 0.35, 0.55, 0.75]:
        yy = 64 - 36 * t
        xx = PX - 18 * (3 * t * t - 2 * t * t * t)
        ds += f'<path d="M{xx - 3:.2f} {yy:.2f}H{xx + 3:.2f}" stroke="{GREY_LINE}" stroke-width="0.8"/>'
    ds += f'<path d="M{PX:.2f} 80V{MB + 22:.2f}C{PX:.2f} {MB + 34:.2f} {PX + 6:.2f} {MB + 38:.2f} {PX + 18:.2f} {MB + 40:.2f}" stroke="{DARK}"/>'
    cols = "TGCAGTAC"
    for i, b in enumerate(cols):
        yy = MT - 6 + 6 * i
        ds += f'<path d="M{PX - 2.8:.2f} {yy:.2f}H{PX - 0.8:.2f}" stroke="{BASE_C[b]}" stroke-width="2.2"/>'
    out.append(ds + "</g>")
    out.append(f'<ellipse class="motor-protein" cx="{PX:.2f}" cy="{MT - 24:.2f}" rx="23" ry="13" fill="{NAVY}" fill-opacity="0.85"/>')
    ions = [(PX + 4, MT + 2), (PX + 4.2, MT + 14), (PX + 4, MB - 2), (PX - 30, MT - 6), (PX + 30, MB + 10), (PX + 22, MB + 20)]
    out.append('<g class="ions">' + "".join(f'<circle cx="{a:.2f}" cy="{b:.2f}" r="2.2" fill="{TEAL}"/>' for a, b in ions) + "</g>")
    AX = PX + 40
    out.append(f'<g class="ion-arrow"><path d="M{AX:.2f} {MB + 4:.2f}V{MB + 24:.2f}" stroke="{TEAL}" stroke-width="1.4"/>'
               f'<path d="M{AX - 3.5:.2f} {MB + 22:.2f}L{AX:.2f} {MB + 29:.2f}L{AX + 3.5:.2f} {MB + 22:.2f}Z" fill="{TEAL}"/></g>')
    out.append(T(AX + 8, MB + 22, "Ions", LBL))
    out.append(leader(PX + 24, MT - 26, 196, MT - 40) + T(200, MT - 36, "Motor protein", LBL))
    out.append(T(392, MT - 8, "Membrane", LBL, anchor="end"))
    out.append(leader(PX - 19, MB + 6, PX - 34, MB + 14) + T(PX - 38, MB + 20, "Nanopore", LBL, anchor="end"))
    for sign, yy in (("−", 52), ("+", MB + 32)):
        out.append(f'<circle cx="28" cy="{yy:.2f}" r="9" fill="none" stroke="{GREY_LINE}" stroke-width="1"/>' + T(28, yy + 5.2, sign, 15, 600, None, "middle"))

    # b. current trace
    YC = 196.0
    out.append(f'<path class="divider" d="M8 {YC - 22:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.5"/>')
    out.append(panel_head(8, YC, "b", "Current trace"))
    SEQ = "TGCAGAAAAACTGCTA"
    X0, CW = 64.0, 20.0
    TT, TB = YC + 22, YC + 102
    HP0, HP1 = 5, 10
    out.append(f'<rect class="homopolymer" x="{X0 + CW * HP0:.2f}" y="{TT - 4:.2f}" width="{CW * (HP1 - HP0):.2f}" height="{TB - TT + 4 + 84:.2f}" rx="4" '
               f'fill="{GREY_LINE}" fill-opacity="0.1"/>')
    out.append(f'<g class="axes" stroke="{GREY_LINE}" stroke-width="1" fill="none"><path d="M{X0 - 6:.2f} {TT - 6:.2f}V{TB + 6:.2f}H{X0 + CW * 16 + 4:.2f}"/>'
               f'<path d="M{X0 + CW * 16:.2f} {TB + 2.5:.2f}L{X0 + CW * 16 + 6:.2f} {TB + 6:.2f}L{X0 + CW * 16:.2f} {TB + 9.5:.2f}Z" fill="{GREY_LINE}" stroke="none"/></g>')
    cy_ = (TT + TB) / 2
    out.append(f'<text x="{X0 - 14:.2f}" y="{cy_:.2f}" font-family="{SANS}" font-size="{LBL:g}" font-weight="400" fill="{MUTED}" text-anchor="middle" '
               f'transform="rotate(-90 {X0 - 14:.2f} {cy_:.2f})">Current</text>')
    out.append(T(X0 + CW * 16 + 6, TB + 22, "Time", LBL, 400, MUTED, "end"))
    # step levels: breakpoints in base units (not one per base); the run of A is one flat level
    bps = [0, 1.4, 2.2, 3.5, 4.3, 5.0, 10.0, 11.1, 12.3, 13.2, 14.5, 16]
    lv = [0.35, 0.8, 0.5, 0.15, 0.62, 0.42, 0.88, 0.25, 0.7, 0.45, 0.1]
    rnd = random.Random(7)
    yv = lambda f: TB - 8 - f * (TB - TT - 16)
    d = ""
    for k in range(len(lv)):
        xa, xb = X0 + CW * bps[k], X0 + CW * bps[k + 1]
        n = max(2, int((xb - xa) / 3))
        for j in range(n + 1):
            xx = xa + (xb - xa) * j / n
            yy = yv(lv[k]) + rnd.gauss(0, 1.1)
            d += f"{'M' if not d else 'L'}{xx:.2f} {yy:.2f}"
    out.append(f'<path class="trace" d="{d}" fill="none" stroke="{DARK}" stroke-width="1.3" stroke-linejoin="round"/>')
    # basecaller
    YA0, YA1 = TB + 14, TB + 40
    BX = X0 + CW * 0.5
    out.append(f'<g class="basecaller-arrow"><path d="M{BX:.2f} {YA0:.2f}V{YA1 - 6:.2f}" stroke="{GREY_LINE}" stroke-width="1.4"/>'
               f'<path d="M{BX - 3.5:.2f} {YA1 - 7:.2f}L{BX:.2f} {YA1:.2f}L{BX + 3.5:.2f} {YA1 - 7:.2f}Z" fill="{GREY_LINE}"/></g>')
    out.append(T(BX + 10, (YA0 + YA1) / 2 + 4.5, "Basecaller", LBL, 600))
    YS = YA1 + 16
    out.append(T(8, YS + LBL * 0.36, "Sequence", LBL, 600) + base_cells(X0, CW, YS, list(SEQ), size=15))
    bx0, bx1 = X0 + CW * HP0 + 3, X0 + CW * HP1 - 3
    out.append(f'<path class="run-bracket" d="M{bx0:.2f} {YS + 13:.2f}v4H{bx1:.2f}v-4" fill="none" stroke="{GREY_LINE}" stroke-width="1"/>')
    mx = (bx0 + bx1) / 2
    out.append(T(mx, YS + 34, "A run of one base looks flat,", LBL, 400, MUTED, "middle") + T(mx, YS + 48, "so its length is hard to count", LBL, 400, MUTED, "middle"))
    out.append(T(W - 8, YS + 74, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, out, "Nanopore sequencing: a strand fed through a pore in a membrane, and the current trace turned into a sequence")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="392" height="427.5" viewBox="4 6.75 392 427.5"')


if __name__ == "__main__":
    main(NAME, fig)
