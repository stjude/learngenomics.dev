"""Figure 2.9: Treatment kills the main clone, and a resistant subclone grows back."""

import math

from figures.core import BLUE, COPYRIGHT, DARK, DARK_PAGE, INK, GREY_LINE, MUTED, PURPLE, T, main, svg_doc
from figures.tumor_evolution import CA, X0, X1, ln

NAME = "2.9-treatment-selects"

SHADE = "#efeeec"


def sig(z):
    return 1 / (1 + math.exp(-z))


def fig():
    W = 400.0
    out = []
    y = 22
    out.append(T(X0, y, "Treatment selects a resistant subclone", 13, 700, DARK))
    out.append(T(X0, y + 16, "Height shows how many cancer cells there are.", 12, 400, MUTED))
    top = y + 66
    HH = 120.0
    mid = top + HH / 2
    ax0, ax1 = X0 + 4, X1 - 4
    t0, td, t1 = 0.04, 0.46, 1.0
    xs = lambda t: ax0 + (t - t0) / (t1 - t0) * (ax1 - ax0)

    def main(t):
        if t <= td:
            return sig((t - 0.27) / 0.055)
        return sig((td - 0.27) / 0.055) * math.exp(-(t - td) / 0.02)

    def res(t):
        r = 0.95 * sig((t - 0.825) / 0.058) + 0.018
        s = min(1, max(0, (t - 0.25) / 0.07))
        return r * s * s * (3 - 2 * s)

    ts = [t0 + i * (t1 - t0) / 240 for i in range(241)]
    half = lambda v: v * HH / 2 * 0.98
    tot = [(t, main(t) + res(t), res(t)) for t in ts]
    # treatment band
    tr0, tr1 = xs(td), xs(0.62)
    out.append(f'<rect x="{tr0:.2f}" y="{top - 8:.2f}" width="{tr1 - tr0:.2f}" height="{HH + 16:.2f}" fill="{SHADE}"/>')
    out.append(T((tr0 + tr1) / 2, top + HH + 24, "treatment", 12, 400, DARK, "middle"))
    up = " ".join(f"{xs(t):.2f} {mid - half(v):.2f}" for t, v, _ in tot)
    dn = " ".join(f"{xs(t):.2f} {mid + half(v):.2f}" for t, v, _ in reversed(tot))
    out.append(f'<path d="M{up} L{dn}Z" fill="{BLUE}" stroke="#0b3f80" stroke-width="0.8" stroke-linejoin="round"/>')
    # a second subclone, killed along with the main clone
    def sub(t):
        u = min(1, max(0, (t - 0.17) / 0.16))
        return main(t) * 0.42 * u * u * (3 - 2 * u)
    st = [t for t in ts if sub(t) > 0.0005]
    cen = lambda t: mid - half(res(t)) - half(main(t)) / 2
    up = " ".join(f"{xs(t):.2f} {cen(t) - half(sub(t)):.2f}" for t in st)
    dn = " ".join(f"{xs(t):.2f} {cen(t) + half(sub(t)):.2f}" for t in reversed(st))
    out.append(f'<path d="M{up} L{dn}Z" fill="{PURPLE}" stroke="#4a2160" stroke-width="0.8" stroke-linejoin="round"/>')
    rt = [(t, r) for t, _, r in tot if r > 0.0005]
    up = " ".join(f"{xs(t):.2f} {mid - half(r):.2f}" for t, r in rt)
    dn = " ".join(f"{xs(t):.2f} {mid + half(r):.2f}" for t, r in reversed(rt))
    out.append(f'<path d="M{xs(rt[0][0]) - 2:.2f} {mid:.2f}L{up} L{dn}Z" fill="{CA}" stroke="#a8650a" stroke-width="0.8" stroke-linejoin="round"/>')

    # limit of detection
    lod = half(0.11)
    for yy in (mid - lod, mid + lod):
        out.append(f'<line x1="{ax0:.2f}" y1="{yy:.2f}" x2="{ax1:.2f}" y2="{yy:.2f}" stroke="{DARK}" stroke-width="0.9" stroke-dasharray="3 2.5"/>')
    out.append(T(xs(0.505), mid - lod - 4, "limit of detection", 10.5, 400, DARK))
    # markers along the top
    for t, lab in ((td, "diagnosis"), (0.66, "remission"), (0.985, "relapse")):
        x = xs(t)
        out.append(ln(x, top - 26, x, top - 10, DARK, 1))
        anc = "end" if t > 0.9 else "middle"
        out.append(T(x + (2 if anc == "end" else 0), top - 32, lab, 12, 700, DARK, anc))
    # labels
    mx = xs(0.36)
    out.append(T(mx, mid + 28, "main clone", 12, 700, "#ffffff", "middle"))
    out.append(T(xs(0.39), cen(0.39) + 4, "subclone", 12, 700, "#ffffff", "middle"))
    rx = xs(td)
    rr = half(res(td))
    out.append(ln(rx, mid + rr + 1, rx - 24, top + HH + 40, GREY_LINE, 0.8))
    out.append(T(rx - 30, top + HH + 46, "resistant subclone,", 12, 400, DARK, "end"))
    out.append(T(rx - 30, top + HH + 61, "already there but too", 12, 400, DARK, "end"))
    out.append(T(rx - 30, top + HH + 76, "small to notice", 12, 400, DARK, "end"))
    ex = xs(0.9)
    out.append(T(ex, mid - 20, "resistant cells", 12, 700, INK, "middle", dark=DARK_PAGE))
    rm = xs(0.66)
    out.append(ln(rm, mid + half(res(0.66) + main(0.66)) + 1, rm, top + HH + 33, GREY_LINE, 0.8))
    out.append(T(rm, top + HH + 46, "too few cells", 12, 400, DARK, "middle"))
    out.append(T(xs(0.66), top + HH + 61, "to detect", 12, 400, DARK, "middle"))
    out.append(ln(ax0, top + HH + 92, ax1 - 8, top + HH + 92, DARK, 1))
    out.append(f'<path d="M{ax1 - 8:.2f} {top + HH + 88:.2f}L{ax1:.2f} {top + HH + 92:.2f}L{ax1 - 8:.2f} {top + HH + 96:.2f}Z" fill="{DARK}"/>')
    out.append(T(ax0, top + HH + 108, "time", 12, 400, DARK))
    H = top + HH + 138
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Treatment kills the main clone, and a resistant subclone grows back.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
