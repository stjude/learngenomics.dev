"""Figure 2.8: A tumor's family tree and the allele fractions it produces."""

import math
import random

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, PURPLE, T, main, svg_doc
from figures.tumor_evolution import CA, X0, X1, ln

NAME = "2.8-trunk-and-branches"

CB = PURPLE
NORMAL = "#ffffff"


def mut(x, y, col):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3.4" fill="#ffffff" stroke="{col}" stroke-width="1.6"/>'


def tree(out, y):
    out.append(T(X0, y, "A tumor\u2019s family tree", 13, 700, DARK))
    out.append(T(X0, y + 16, "Later mutations are carried only by the descendants of", 12, 400, MUTED))
    out.append(T(X0, y + 31, "the cell where they arose.", 12, 400, MUTED))
    cy = y + 112
    fx, sx, ex = 22.0, 104.0, 196.0
    ya, yb = cy - 50, cy + 50
    out.append(f'<circle cx="{fx:.2f}" cy="{cy:.2f}" r="7" fill="{BLUE}" stroke="#0b3f80" stroke-width="1"/>')
    out.append(T(fx - 10, cy + 24, "first", 11, 400, MUTED))
    out.append(T(fx - 10, cy + 37, "cancer cell", 11, 400, MUTED))
    out.append(ln(fx + 7, cy, ex, cy, BLUE, 5))
    out.append(f'<path d="M{sx:.2f} {cy:.2f}C{sx + 30:.2f} {cy:.2f} {sx + 26:.2f} {ya:.2f} {sx + 56:.2f} {ya:.2f}H{ex:.2f}" stroke="{CA}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    out.append(f'<path d="M{sx:.2f} {cy:.2f}C{sx + 30:.2f} {cy:.2f} {sx + 26:.2f} {yb:.2f} {sx + 56:.2f} {yb:.2f}H{ex:.2f}" stroke="{CB}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    for x in (44, 64, 84):
        out.append(mut(x, cy, BLUE))
    for x in (168, 184):
        out.append(mut(x, ya, CA))
    for x in (168, 184):
        out.append(mut(x, yb, CB))
    out.append(T(60, cy - 12, "trunk", 12, 700, BLUE, "middle"))
    out.append(T(166, ya - 10, "subclone A", 12, 700, CA, "middle"))
    out.append(T(166, yb + 20, "subclone B", 12, 700, CB, "middle"))
    for yy in (ya, cy, yb):
        out.append(ln(ex + 6, yy, ex + 14, yy, GREY_LINE, 0.8))
    out.append(T(ex + 18, ya + 4, "50%", 12, 400, DARK))
    out.append(T(ex + 18, cy + 4, "30%", 12, 400, DARK))
    out.append(T(ex + 18, yb + 4, "20%", 12, 400, DARK))
    out.append(mut(X0 + 4, cy + 96, GREY_LINE))
    out.append(T(X0 + 13, cy + 100, "mutation", 11, 400, MUTED))
    out.append(T(X0 + 74, cy + 100, "% = share of cancer cells", 11, 400, MUTED))

    # the sample: tumor cells in clumps, mixed with normal cells
    tx, ty, R = 316.0, cy, 64.0
    rnd = random.Random(7)
    pts = []
    step = 9.4
    j = 0
    yy = ty - R
    while yy <= ty + R:
        off = step / 2 if j % 2 else 0
        xx = tx - R + off
        while xx <= tx + R:
            if math.hypot(xx - tx, yy - ty) <= R - 3.5:
                pts.append((xx, yy))
            xx += step
        yy += step * 0.866
        j += 1
    rnd.shuffle(pts)
    nn = round(len(pts) * 0.4)
    normal = set(pts[:nn])
    cancer = pts[nn:]

    def ang(p):
        a = math.degrees(math.atan2(p[1] - ty, p[0] - tx))
        return (a + 200) % 360

    cancer.sort(key=ang)
    na, nt = round(len(cancer) * 0.5), round(len(cancer) * 0.3)
    col = {}
    for i, p in enumerate(cancer):
        col[p] = CA if i < na else (BLUE if i < na + nt else CB)
    out.append(f'<circle cx="{tx:.2f}" cy="{ty:.2f}" r="{R:.2f}" fill="#f7f6f4" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    for p in pts:
        c = NORMAL if p in normal else col[p]
        sc = GREY_LINE if p in normal else "#ffffff"
        out.append(f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="3.7" fill="{c}" stroke="{sc}" stroke-width="0.7"/>')
    out.append(T(tx, ty - R - 22, "The sample", 12, 700, DARK, "middle"))
    out.append(T(tx, ty - R - 8, "60% cancer cells", 11, 400, MUTED, "middle"))
    out.append(f'<circle cx="{tx - 50:.2f}" cy="{ty + 96:.2f}" r="3.7" fill="{NORMAL}" stroke="{GREY_LINE}" stroke-width="0.7"/>')
    out.append(T(tx - 42, ty + 100, "normal cell", 11, 400, MUTED))
    return cy + 104


def histogram(out, y):
    out.append(T(X0, y, "What the reads show", 13, 700, DARK))
    out.append(T(X0, y + 16, "Each mutation\u2019s share of the reads, in the same sample", 12, 400, MUTED))
    rnd = random.Random(3)
    groups = [(BLUE, 0.30, 46), (CA, 0.15, 34), (CB, 0.06, 26)]
    bw = 0.02
    nb = 25
    counts = [[0] * nb for _ in groups]
    for gi, (_, f, n) in enumerate(groups):
        for _ in range(n):
            depth = rnd.randint(90, 140)
            k = sum(1 for _ in range(depth) if rnd.random() < f)
            v = k / depth
            b = min(nb - 1, int(v / bw))
            counts[gi][b] += 1
    top = y + 44
    ph = 104.0
    ax0, ax1 = X0 + 26, X1 - 6
    base = top + ph
    mx = max(sum(c[b] for c in counts) for b in range(nb))
    unit = ph / (mx + 2)
    xs = lambda v: ax0 + v / 0.5 * (ax1 - ax0)
    for b in range(nb):
        h0 = 0.0
        for gi, (c, _, _) in enumerate(groups):
            h = counts[gi][b] * unit
            if h:
                out.append(f'<rect x="{xs(b * bw) + 0.6:.2f}" y="{base - h0 - h:.2f}" width="{xs(bw) - xs(0) - 1.2:.2f}" height="{h:.2f}" fill="{c}"/>')
            h0 += h
    out.append(ln(ax0, base, ax1, base, DARK, 1))
    for v in (0, 0.1, 0.2, 0.3, 0.4, 0.5):
        x = xs(v)
        out.append(ln(x, base, x, base + 4, DARK, 1))
        out.append(T(x, base + 17, f"{int(v * 100)}%", 11, 400, MUTED, "middle"))
    out.append(T((ax0 + ax1) / 2, base + 34, "share of reads showing the mutation", 12, 400, DARK, "middle"))
    out.append(T(X0 + 8, base - ph / 2, "mutations", 12, 400, DARK, "middle", extra=f' transform="rotate(-90 {X0 + 8:.2f} {base - ph / 2:.2f})"'))
    peak = lambda gi: max(range(nb), key=lambda b: counts[gi][b])
    for gi, (c, f, _), lab in zip(range(3), groups, ("trunk", "A", "B")):
        b = peak(gi)
        h = sum(cc[b] for cc in counts) * unit
        out.append(T(xs(f), base - h - 6, lab, 12, 700, c, "middle"))
    hx = xs(0.30)
    out.append(ln(hx, top - 10, hx, base, DARK, 1, ' stroke-dasharray="3 3"'))
    out.append(T(hx + 5, top - 2, "half of 60%", 11, 400, MUTED))
    return base + 34


def fig():
    W = 400.0
    out = []
    y = tree(out, 22)
    y = histogram(out, y + 40)
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "A tumor's family tree and the allele fractions it produces.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
