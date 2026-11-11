"""Figure 3.10: Copy number signals."""

from figures.core import COPYRIGHT, DARK, GREY_LINE, LBL, PURPLE, T, main, svg_doc
from figures.copy_number import GAIN_C, LOSS_C, cn_dots

NAME = "3.10-copy-number-signals"

LOH_C = PURPLE


def fig():
    import random
    W, H = 400.0, 340.0
    MUTED = "#4d4d4f"
    rnd = random.Random(5)
    X0, XE = 40.0, 392.0
    RW = (XE - X0) / 4
    regions = [("Normal", None, "A/B", DARK, GREY_LINE, 0.0, [0.5]),
               ("Gain", None, "A/A/B", GAIN_C, GAIN_C, 0.58, [1 / 3, 2 / 3]),
               ("Loss", None, "A/–", LOSS_C, LOSS_C, -1.0, [0.0, 1.0]),
               ("Copy-neutral", "LOH", "A/A", LOH_C, LOH_C, 0.0, [0.0, 1.0])]
    out = []
    YC = 66.0
    YD0, SD = 132.0, 30.0
    yd = lambda v: YD0 - v * SD
    YA1, YA0 = 206.0, 266.0
    ya = lambda f: YA0 - f * (YA0 - YA1)
    # copy-neutral LOH highlight
    lx = X0 + 3 * RW
    out.append(f'<rect class="loh-highlight" x="{lx:.2f}" y="8" width="{RW:.2f}" height="{YA0 + 10 - 8:.2f}" fill="{LOH_C}" fill-opacity="0.07"/>')
    s = '<g class="regions">'
    for i, (n1, n2, gt, c, dc, lv, afs) in enumerate(regions):
        cx = X0 + (i + 0.5) * RW
        if n2:
            s += T(cx, 20, n1, LBL, 600, c, "middle") + T(cx, 34, n2, LBL, 600, c, "middle")
        else:
            s += T(cx, 27, n1, LBL, 600, c, "middle")
        s += T(cx, 51, gt, LBL, 500, MUTED, "middle", mono=True)
        s += (f'<rect x="{X0 + i * RW + 1:.2f}" y="{YC - 5:.2f}" width="{RW - 2:.2f}" height="10" rx="3" '
              f'fill="{c if c != DARK else GREY_LINE}" fill-opacity="{0.25 if c != DARK else 0.15}" stroke="{c if c != DARK else GREY_LINE}" stroke-width="0.9"/>')
        if i:
            s += f'<path d="M{X0 + i * RW:.2f} {YC + 12:.2f}V{YA0 + 6:.2f}" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.6"/>'
    out.append(s + "</g>")
    # depth track
    out.append(T(8, 94, "Depth (log2 ratio)", LBL, 600))
    for v, t in ((0.58, "0.58"), (0.0, "0"), (-1.0, "−1")):
        out.append(f'<path class="grid" d="M{X0:.2f} {yd(v):.2f}H{XE:.2f}" stroke="{GREY_LINE}" stroke-width="0.6" stroke-dasharray="2 2"/>')
        out.append(T(X0 - 6, yd(v) + 3.6, t, 10, 400, MUTED, "end"))
    s = '<g class="depth">'
    for i, (n1, n2, gt, c, dc, lv, afs) in enumerate(regions):
        dcol = GREY_LINE if n2 else dc
        lcol = DARK if (n2 or c == DARK) else c
        s += cn_dots(rnd, X0 + i * RW, X0 + (i + 1) * RW, 10, yd, lv, 0.1, dcol)
        s += f'<path d="M{X0 + i * RW + 3:.2f} {yd(lv):.2f}H{X0 + (i + 1) * RW - 3:.2f}" stroke="{lcol}" stroke-width="2.4" stroke-linecap="round"/>'
    out.append(s + "</g>")
    # allele fraction track
    out.append(T(8, YA1 - 14, "Allele fraction", LBL, 600))
    for f, t in ((1.0, "1"), (0.5, "0.5"), (0.0, "0")):
        out.append(f'<path class="grid" d="M{X0:.2f} {ya(f):.2f}H{XE:.2f}" stroke="{GREY_LINE}" stroke-width="0.6" stroke-dasharray="2 2"/>')
        out.append(T(X0 - 6, ya(f) + 3.6, t, 10, 400, MUTED, "end"))
    s = '<g class="allele-fractions">'
    n = 16
    for i, (n1, n2, gt, c, dc, lv, afs) in enumerate(regions):
        for j in range(n):
            x = X0 + i * RW + (j + 0.5) * RW / n
            f = afs[j % len(afs)]
            if f in (0.0, 1.0):
                f = abs(rnd.gauss(0, 0.012)) if f == 0 else 1 - abs(rnd.gauss(0, 0.012))
            else:
                f += rnd.gauss(0, 0.03)
            s += f'<circle cx="{x:.2f}" cy="{ya(f):.2f}" r="1.9" fill="{dc}" fill-opacity="0.75"/>'
    out.append(s + "</g>")
    out.append(T(XE, YA0 + 24, "Copy-neutral LOH: depth normal, allele fractions split", LBL, 400, LOH_C, "end"))
    out.append(T(W - 8, YA0 + 46, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, out, "Copy number signals: read depth and allele fraction across normal, gain, loss and copy-neutral LOH regions")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="392" height="314.25" viewBox="4 4 392 314.25"')


if __name__ == "__main__":
    main(NAME, fig)
