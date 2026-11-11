"""Figure 1.3: Chromatin."""

import math

from figures.core import (
    BLUE, DARK, GREEN, LBLUE, NAVY, ORANGE, PURPLE, T, copyright_text, main, svg_doc,
)
from figures.drawing import CALLOUT, sine_path, smooth, zoom_lines
from figures.biology import NUC_COL, nucleosome

NAME = "1.3-chromatin"


def _ray_circle(px, py, ux, uy, cx, cy, r):
    """First positive distance along a ray from (px,py) in direction (ux,uy) to a circle, or None."""
    dx, dy = px - cx, py - cy
    b = ux * dx + uy * dy
    disc = b * b - (dx * dx + dy * dy - r * r)
    if disc < 0:
        return None
    sq = math.sqrt(disc)
    for t in (-b - sq, -b + sq):
        if t > 1e-6:
            return t
    return None


def _walk(rnd, x, y, a, steps, step, turn, inside, home):
    pts = [(x, y)]
    for _ in range(steps):
        a += rnd.gauss(0, turn)
        nx, ny = x + step * math.cos(a), y + step * math.sin(a)
        if not inside(nx, ny):
            want = math.atan2(home[1] - y, home[0] - x)
            a = want + rnd.gauss(0, 0.4)
            nx, ny = x + step * math.cos(a), y + step * math.sin(a)
        x, y = nx, ny
        pts.append((x, y))
    return pts


def dense_squiggle(rnd, pt, ks, depth, amp):
    """Irregular compact zigzag following pt(k, offset) at offsets depth +/- amp (varying wavelength/amplitude)."""
    phi, lam, a, pts, prev = rnd.uniform(0, 6.3), rnd.uniform(4, 7), rnd.uniform(0.6, 1.1), [], None
    for k in ks:
        base = pt(k, 0)
        if prev:
            phi += 2 * math.pi * math.hypot(base[0] - prev[0], base[1] - prev[1]) / lam
        prev = base
        lam = min(8.5, max(3.2, lam + rnd.gauss(0, 0.45)))
        a = min(1.25, max(0.45, a + rnd.gauss(0, 0.08)))
        pts.append(pt(k, depth + amp * a * math.sin(phi) + rnd.gauss(0, 0.12)))
    return f'<path d="{smooth(pts[::2])}"/>'


def nucleus_detail(cx, cy, R, seeds, nucleolus, n=360):
    """Interphase nucleus tiled by chromosome territories (Voronoi cells clipped to the envelope).

    Each territory mixes loose (open) chromatin with dense patches; territories touching the envelope or the
    nucleolus carry a dense patch along that face, and edge territories are denser than central ones."""
    import random
    rnd = random.Random(5)
    nx_, ny_, nr = nucleolus
    palette = [PURPLE, ORANGE, GREEN, LBLUE, BLUE]
    cells = []
    for i, (sx, sy) in enumerate(seeds):
        rays, nbrs = [], set()
        ph = [rnd.uniform(0, 6.3) for _ in range(3)]
        for k in range(n):
            th = 2 * math.pi * k / n
            ux, uy = math.cos(th), math.sin(th)
            t, kind = _ray_circle(sx, sy, ux, uy, cx, cy, R), "env"
            for j, (qx, qy) in enumerate(seeds):
                if j == i:
                    continue
                dx, dy = qx - sx, qy - sy
                den = dx * ux + dy * uy
                if den > 1e-9 and (dx * dx + dy * dy) / 2 / den < t:
                    t, kind = (dx * dx + dy * dy) / 2 / den, ("nbr", j)
            tn = _ray_circle(sx, sy, ux, uy, nx_, ny_, nr + 0.4)
            if tn is not None and tn < t:
                t, kind = tn, "nuc"
            if kind[0] == "nbr":
                nbrs.add(kind[1])
            wob = 0.35 * (1 + math.sin(3 * th + ph[0])) + 0.25 * (1 + math.sin(5 * th + ph[1]))
            gap = {"env": 0.7, "nuc": 0.5}.get(kind, 0.9) + (wob if kind != "env" else 0.2 * wob)
            rays.append((th, t - gap, kind if kind in ("env", "nuc") else "nbr"))
        cells.append((sx, sy, rays, nbrs))
    # colour so neighbouring territories differ
    cols = []
    for i, (_, _, _, nbrs) in enumerate(cells):
        used = {cols[j] for j in nbrs if j < len(cols)}
        cols.append(next(c for c in palette[i % 5:] + palette[:i % 5] if c not in used))

    out = ['<g class="nucleus-detail">',
           f'<circle class="envelope" cx="{cx}" cy="{cy}" r="{R}" fill="{PURPLE}" fill-opacity="0.05" stroke="{PURPLE}" stroke-width="1.2"/>']
    dense = []
    for (sx, sy, rays, nbrs), col in zip(cells, cols):
        P = lambda k, off=0.0: (sx + (rays[k % n][1] - off) * math.cos(rays[k % n][0]),
                                sy + (rays[k % n][1] - off) * math.sin(rays[k % n][0]))
        rr = lambda x, y: rays[round(math.atan2(y - sy, x - sx) / (2 * math.pi) * n) % n][1]
        edge = any(r[2] == "env" for r in rays)
        g = [f'<g class="territory {"edge" if edge else "central"}">',
             f'<path class="territory-fill" d="{smooth([P(k) for k in range(0, n, 4)], True)}" fill="{col}" fill-opacity="0.2"/>']
        # dense patches along envelope- or nucleolus-facing faces
        runs, k0 = [], next((k for k in range(n) if rays[k][2] != rays[k - 1][2]), 0)
        cur = None
        for k in range(k0, k0 + n):
            kind = rays[k % n][2]
            if cur and cur[0] == kind:
                cur[1].append(k)
            else:
                cur = [kind, [k]]
                runs.append(cur)
        for kind, ks in runs:
            if kind != "env" or len(ks) < 6:
                continue
            ks = ks[3:len(ks) - 3]
            band = [P(k, 0.2) for k in ks] + [P(k, 5.6) for k in reversed(ks)]
            g.append(f'<path class="dense-band" d="{smooth(band, True)}" fill="{NAVY}" fill-opacity="0.16"/>')
            dense.extend(dense_squiggle(rnd, P, ks, 2.9, 2.2) for _ in range(3))
        # loose (open) chromatin thread, denser in edge territories
        inside = lambda x, y: math.hypot(x - sx, y - sy) < 0.78 * rr(x, y)
        steps = 46 if edge else 30
        g.append(f'<path class="open-chromatin" d="{smooth(_walk(rnd, sx, sy, rnd.uniform(0, 6.3), steps, 2.4, 0.55, inside, (sx, sy)))}" '
                 f'fill="none" stroke="{BLUE}" stroke-width="0.75" stroke-linecap="round" stroke-linejoin="round"/>')
        # a few compact clumps mixed in (more in edge territories)
        for _ in range(2 if edge else 1):
            for _try in range(50):
                ang = rnd.uniform(0, 2 * math.pi)
                d = rnd.uniform(0.25, 0.55)
                px, py = sx + d * rays[round(ang / (2 * math.pi) * n) % n][1] * math.cos(ang), \
                    sy + d * rays[round(ang / (2 * math.pi) * n) % n][1] * math.sin(ang)
                if inside(px, py):
                    break
            near = lambda x, y, px=px, py=py: math.hypot(x - px, y - py) < 2.6
            dense.append(f'<path d="{smooth(_walk(rnd, px, py, ang, 34, 0.9, 1.1, near, (px, py)))}"/>')
        out.extend(g + ["</g>"])
    owner = [min(range(len(seeds)), key=lambda i: math.hypot(nx_ + (nr + 3) * math.cos(math.radians(d)) - seeds[i][0],
                                                             ny_ + (nr + 3) * math.sin(math.radians(d)) - seeds[i][1]))
             for d in range(360)]
    d0 = next(d for d in range(360) if owner[d] != owner[d - 1])
    runs = []
    for d in range(d0, d0 + 360):
        if runs and owner[d % 360] == runs[-1][0]:
            runs[-1][1].append(d)
        else:
            runs.append([owner[d % 360], [d]])
    NP = lambda d, off: (nx_ + (nr + 0.4 + off) * math.cos(math.radians(d)), ny_ + (nr + 0.4 + off) * math.sin(math.radians(d)))
    nuc = []
    for _, ds in runs:
        ds = ds[7:len(ds) - 7]
        if len(ds) < 12:
            continue
        band = [NP(d, 0) for d in ds] + [NP(d, 4.6) for d in reversed(ds)]
        nuc.append(f'<path class="dense-band" d="{smooth(band[::2], True)}" fill="{NAVY}" fill-opacity="0.16"/>')
        dense.extend(dense_squiggle(rnd, NP, ds, 2.3, 1.8) for _ in range(3))
    out.extend(nuc)
    out.append(f'<g class="dense-chromatin" fill="none" stroke="{NAVY}" stroke-width="0.6" '
               f'stroke-linecap="round" stroke-linejoin="round">' + "".join(dense) + "</g>")
    out.append(f'<circle class="nucleolus" cx="{nx_}" cy="{ny_}" r="{nr}" fill="{PURPLE}" fill-opacity="0.55"/>')
    out.append("</g>")
    nucleus_detail.info = (cells, cols)
    return out


def fig():
    import random
    out = []
    # titles
    out.append(T(72, 14, "Cell", 9.5, 700, anchor="middle"))
    out.append(T(245, 14, "Nucleus", 9.5, 700, anchor="middle"))
    out.append(T(460, 14, "One chromosome", 9.5, 700, anchor="middle"))
    # 1. cell
    rnd = random.Random(3)
    blob = [(72 + 60 * math.cos(t) * rnd.uniform(0.93, 1.04), 80 + 47 * math.sin(t) * rnd.uniform(0.93, 1.04))
            for t in [i * 2 * math.pi / 11 for i in range(11)]]
    out.append('<g class="cell">')
    out.append(f'<path class="membrane" d="{smooth(blob, True)}" fill="{BLUE}" fill-opacity="0.06" stroke="{BLUE}" stroke-width="1.2"/>')
    for (x, y, rot) in ((40, 98, 20), (48, 58, -35), (112, 104, -10), (108, 50, 30)):
        out.append(f'<ellipse cx="{x}" cy="{y}" rx="8" ry="3.6" transform="rotate({rot} {x} {y})" '
                   f'fill="{ORANGE}" fill-opacity="0.2" stroke="{ORANGE}" stroke-width="0.9"/>')
    for (x, y) in ((30, 78), (60, 110), (95, 112), (120, 78), (70, 44), (58, 82), (82, 104)):
        out.append(f'<circle cx="{x}" cy="{y}" r="1.3" fill="{GREEN}"/>')
    out.append(f'<circle class="nucleus" cx="88" cy="76" r="19" fill="{PURPLE}" fill-opacity="0.12" stroke="{PURPLE}" stroke-width="1"/>')
    out.append("</g>")
    out.append(zoom_lines((88, 76), 19, (245, 80), 50))
    # 2. interphase nucleus: territories tile the nucleus
    ring = [(245 + 35 * math.cos(math.radians(a)), 80 + 35 * math.sin(math.radians(a)))
            for a in (-100, -52, -8, 33, 72, 116, 160, 205)]
    seeds = [(239, 70), (259, 88)] + ring
    out.extend(nucleus_detail(245, 80, 50, seeds, (227, 93, 6.5)))
    out.append('<g class="nucleus-labels">')
    out.append(f'<path d="M190 95.8L219.5 93.5" fill="none" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(188, 98.5, "Nucleolus", 7.5, 600, anchor="end"))
    out.append("</g>")
    # 3. one chromosome territory, zoomed
    cells, cols = nucleus_detail.info
    ti = 5  # lower-right edge territory
    tsx, tsy, trays, _ = cells[ti]
    N = len(trays)
    zc, zr = (276, 100), 16  # nucleus callout
    lc, lr = (460, 80), 46  # lens
    sc = lr / zr
    L = lambda x, y: (lc[0] + sc * (x - zc[0]), lc[1] + sc * (y - zc[1]))
    out.append(f'<circle class="callout" cx="{zc[0]}" cy="{zc[1]}" r="{zr}" {CALLOUT.replace("0.7", "1")}/>')
    out.append(zoom_lines(zc, zr, lc, lr))
    out.append(f'<clipPath id="lens-clip"><circle cx="{lc[0]}" cy="{lc[1]}" r="{lr - 0.4}"/></clipPath>')
    out.append('<g class="chromosome-territory" clip-path="url(#lens-clip)">')
    ec, eR = L(245, 80), 50 * sc
    out.append(f'<circle class="envelope" cx="{ec[0]:.2f}" cy="{ec[1]:.2f}" r="{eR:.2f}" fill="{PURPLE}" fill-opacity="0.05" '
               f'stroke="{PURPLE}" stroke-width="1.6"/>')
    for i, ((sx, sy, rays, _), col) in enumerate(zip(cells, cols)):
        poly = [L(sx + r[1] * math.cos(r[0]), sy + r[1] * math.sin(r[0])) for r in rays[::4]]
        out.append(f'<path d="{smooth(poly, True)}" fill="{col}" fill-opacity="{0.2 if i == ti else 0.1}"/>')
    rr = lambda x, y: trays[round(math.atan2(y - tsy, x - tsx) / (2 * math.pi) * N) % N][1]
    def inside(x, y):
        qx, qy = zc[0] + (x - lc[0]) / sc, zc[1] + (y - lc[1]) / sc
        return math.hypot(qx - tsx, qy - tsy) < 0.8 * rr(qx, qy) and math.hypot(x - lc[0], y - lc[1]) < lr - 5
    # envelope-facing face of this territory, as nucleus angles, limited to what the lens shows
    phis = []
    for th, t, kind in trays:
        if kind == "env":
            px, py = tsx + t * math.cos(th), tsy + t * math.sin(th)
            if math.hypot(*(a - b for a, b in zip(L(px, py), lc))) < lr - 3:
                phis.append(math.atan2(py - 80, px - 245))
    p0, p1 = min(phis) + math.radians(2), max(phis) - math.radians(2)
    ks = [p0 + (p1 - p0) * i / 160 for i in range(161)]
    EP = lambda ph, off: (ec[0] + (eR - 1.2 - off) * math.cos(ph), ec[1] + (eR - 1.2 - off) * math.sin(ph))
    band = [EP(ph, 0) for ph in ks] + [EP(ph, 11) for ph in reversed(ks)]
    out.append(f'<path class="dense-band" d="{smooth(band[::4], True)}" fill="{NAVY}" fill-opacity="0.16"/>')
    # one continuous thread: loose (blue) stretches with dense (navy) patches
    rnd = random.Random(8)
    seg = []
    def loose(start, steps, target=None):
        x, y = start
        a = rnd.uniform(0, 6.3)
        pts = [(x, y)]
        for _ in range(steps if target is None else 200):
            if target is not None:
                if math.hypot(target[0] - x, target[1] - y) < 4.5:
                    pts.append(target)
                    break
                want = math.atan2(target[1] - y, target[0] - x)
                a += 0.35 * math.atan2(math.sin(want - a), math.cos(want - a))
            a += rnd.gauss(0, 0.5)
            nx, ny = x + 3.6 * math.cos(a), y + 3.6 * math.sin(a)
            if target is None and not inside(nx, ny):
                a = math.atan2(L(tsx, tsy)[1] - y, L(tsx, tsy)[0] - x) + rnd.gauss(0, 0.4)
                nx, ny = x + 3.6 * math.cos(a), y + 3.6 * math.sin(a)
            x, y = nx, ny
            pts.append((x, y))
        seg.append(("loose", pts))
        return pts[-1]
    def clump(start):
        near = lambda x, y: math.hypot(x - start[0], y - start[1]) < 5.5
        pts = _walk(rnd, start[0], start[1], rnd.uniform(0, 6.3), 80, 1.3, 1.1, near, start)
        seg.append(("dense", pts))
        return pts[-1]
    E0, J = EP(p0, 4), EP(p1, 4)
    seed_l = L(tsx, tsy)
    p = loose((seed_l[0] - 24, seed_l[1] - 18), 22)
    p = clump(p)
    p = loose(p, 20)
    p = clump(p)
    p = loose(p, 14)
    p = loose(p, 0, E0)
    # dense patch along the envelope: the same thread crumples along the edge from E0 to J
    def env_off(x, y):
        return eR - 1.2 - math.hypot(x - ec[0], y - ec[1])
    x, y, a = E0[0], E0[1], 0.0
    edge, phi_t = [E0], p0
    while phi_t < p1 or math.hypot(J[0] - x, J[1] - y) > 3:
        phi_t = min(p1, phi_t + 0.0016)
        tgt = EP(phi_t, 4.5)
        want = math.atan2(tgt[1] - y, tgt[0] - x)
        a += 0.22 * math.atan2(math.sin(want - a), math.cos(want - a)) + rnd.gauss(0, 1.0)
        nx, ny = x + 1.3 * math.cos(a), y + 1.3 * math.sin(a)
        if not 0.6 < env_off(nx, ny) < 9.5:
            a = want + rnd.gauss(0, 0.5)
            nx, ny = x + 1.3 * math.cos(a), y + 1.3 * math.sin(a)
        x, y = nx, ny
        edge.append((x, y))
        if len(edge) > 2000:
            break
    edge.append(J)
    seg.append(("dense", edge))
    p = loose(J, 16)
    p = clump(p)
    p = loose(p, 22)
    p = clump(p)
    loose(p, 18)
    for kind, pts in seg:
        col, w = (BLUE, 1.0) if kind == "loose" else (NAVY, 0.8)
        out.append(f'<path class="{kind}-chromatin" d="{smooth(pts)}" fill="none" stroke="{col}" stroke-width="{w}" '
                   f'stroke-linecap="round" stroke-linejoin="round"/>')
    out.append("</g>")
    out.append(f'<circle class="lens" cx="{lc[0]}" cy="{lc[1]}" r="{lr}" {CALLOUT}/>')
    out.append('<g class="lens-labels">')
    out.append(f'<path d="M407 70L435.5 66M407 91.5L440 93" fill="none" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(405, 72.5, "Open chromatin", 7.5, 600, anchor="end"))
    out.append(T(405, 94, "Dense chromatin", 7.5, 600, anchor="end"))
    out.append("</g>")
    # whole lens -> chromatin close-up: tangents from the box's top corners
    def tangent(P, side):
        d = math.hypot(lc[0] - P[0], lc[1] - P[1])
        base = math.atan2(lc[1] - P[1], lc[0] - P[0])
        ang = base + side * math.asin(lr / d)
        t = math.sqrt(d * d - lr * lr)
        return P[0] + t * math.cos(ang), P[1] + t * math.sin(ang)
    lx, ly = tangent((8, 182), 1)
    rx_, ry_ = tangent((519, 182), 1)
    out.append(f'<path class="zoom" d="M{lx:.2f} {ly:.2f}L8 182M{rx_:.2f} {ry_:.2f}L519 182" {CALLOUT}/>')
    # 4. chromatin close-up
    out.append(f'<rect class="close-up" x="8" y="182" width="511" height="118" rx="8" {CALLOUT}/>')
    out.append(T(18, 199, "Chromatin", 9.5, 700))
    cy = 245
    # tightly packed: regular two-row nucleosome zigzag
    clump = [(24 + i * 11, cy + (6 if i % 2 else -6), 7.5) for i in range(18)]
    loose = [(250, cy), (356, cy), (414, cy), (466, cy), (505, cy)]
    out.append('<g class="dna">')
    out.append(f'<path d="{smooth([(p[0], p[1]) for p in clump] + [(232, 243), (250, cy), (273, 250), (296, cy)])}" '
               f'fill="none" stroke="{BLUE}" stroke-width="1.6"/>')
    out.append(f'<path d="{smooth([(332, cy), (344, 241.5), (356, cy), (385, 250), (414, cy), (440, 240.5), (466, cy), (486, 240), (505, cy), (514, 248)])}" '
               f'fill="none" stroke="{BLUE}" stroke-width="1.6"/>')
    out.append("</g>")
    out.append('<g class="tightly-packed">' + "".join(nucleosome(*p) for p in clump) + "</g>")
    out.append(f'<rect class="gene" x="336" y="230" width="108" height="30" rx="4" fill="{GREEN}" fill-opacity="0.12" '
               f'stroke="{GREEN}" stroke-width="1"/>')
    out.append('<g class="loosely-packed">' + "".join(nucleosome(x, y, 8.5) for x, y in loose) + "</g>")
    # promoter: short nucleosome-free stretch of bare double helix just upstream of the gene
    out.append('<g class="promoter">')
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    seq = "TATAAAGGC"
    for m, b in enumerate(seq):
        x = 298 + 4 * m
        h = 5 * abs(math.sin(2 * math.pi * (x - 296) / 24))
        out.append(f'<path d="M{x:.2f} {cy - h:.2f}V{cy:.2f}" stroke="{NUC_COL[b] if b != "T" else LBLUE}" stroke-width="1.3"/>')
        out.append(f'<path d="M{x:.2f} {cy:.2f}V{cy + h:.2f}" stroke="{NUC_COL[comp[b]] if comp[b] != "T" else LBLUE}" stroke-width="1.3"/>')
    for down in (True, False):
        out.append(f'<path d="{sine_path(296, 332, cy, 5, 24, down)}" fill="none" stroke="{BLUE}" stroke-width="1.4"/>')
    out.append("</g>")
    out.append(T(390, 225, "Gene", 7.5, 700, GREEN, "middle"))
    # labels
    out.append('<g class="labels">')
    for x, y1, t in ((250, 235, "Histone"), (314, 238, "Promoter"), (486, 236, "DNA")):
        out.append(f'<path d="M{x} 228V{y1}" stroke="{DARK}" stroke-width="0.6"/>')
        out.append(T(x, 225, t, 7.5, 600, anchor="middle"))
    out.append(f'<path d="M18 266V270H218V266M236 266V270H512V266" fill="none" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(118, 284, "Tightly packed: less accessible", 7.5, 600, anchor="middle"))
    out.append(T(374, 284, "Loosely packed: more accessible", 7.5, 600, anchor="middle"))
    out.append("</g>")
    out.append(copyright_text(519, 310))
    svg = svg_doc(527, 316, out, "Chromatin: chromosome territories in the nucleus, one chromosome's tangled thread, "
                                 "and DNA wrapped around histones")
    return svg.replace('width="527" height="316" viewBox="0 0 527 316"', 'width="519.5" height="311" viewBox="4 3 519.5 311"')


if __name__ == "__main__":
    main(NAME, fig)
