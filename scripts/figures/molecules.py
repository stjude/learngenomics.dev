"""Atom-level molecule drawing engine used by figures 7.8, 7.10 and 7.11.

Builders add atoms and bonds to the shared graph `G` (positions in SVG units, y down),
then the drawing helpers turn it into SVG fragments. scripts/check_figure_chemistry.py
converts the same graph to RDKit molecules to check the chemistry.
"""

import math

from figures.core import BLUE, DARK, T

B = 25.0                     # bond length
HR = 0.62 * B                # N-H drawn shorter
RP = B / (2 * math.sin(math.radians(36)))   # five-membered sugar ring radius
NUM = BLUE
TINT = {"A": "#e6d9ec", "T": "#d5f0f6", "U": "#d5f0f6", "G": "#e1f0d6", "C": "#feeccb",
        "sugar": "#e6e8ec", "phosphate": "#fbe0e1"}

# ---------------------------------------------------------------- graph
# The molecule being drawn. Builders clear and refill it; drawing helpers read it.
G = {"atoms": {}, "bonds": [], "hbonds": [], "groups": {}, "centre": {}}


def clear():
    for v in G.values():
        v.clear()


def pt(c, ang, r=B):
    a = math.radians(ang)
    return (c[0] + r * math.cos(a), c[1] - r * math.sin(a))


def add(name, p, el, label=None, charge=0, group=None, show=True):
    G["atoms"][name] = dict(p=p, el=el, label=label or el, charge=charge, show=show)
    if group:
        G["groups"].setdefault(group, []).append(name)
    return name


def bond(a, b, order=1, inner=None):
    G["bonds"].append((a, b, order, inner))


def ang(a, b):
    pa, pb = G["atoms"][a]["p"], G["atoms"][b]["p"]
    return math.degrees(math.atan2(-(pb[1] - pa[1]), pb[0] - pa[0]))


def out_dir(atom, center):
    p = G["atoms"][atom]["p"]
    return math.degrees(math.atan2(-(p[1] - center[1]), p[0] - center[0]))


def ring(prefix, center, names, start, step, group, r=None):
    r = r or B / (2 * math.sin(math.pi / len(names)))
    for i, n in enumerate(names):
        el = n.rstrip("0123456789'")
        add(f"{prefix}.{n}", pt(center, start + i * step, r), el, group=group)
    for i in range(len(names)):
        bond(f"{prefix}.{names[i]}", f"{prefix}.{names[(i + 1) % len(names)]}", 1, center)


def set_order(prefix, a, b, order):
    for i, (x, y, o, c) in enumerate(G["bonds"]):
        if {x, y} == {f"{prefix}.{a}", f"{prefix}.{b}"}:
            G["bonds"][i] = (x, y, order, c)
            return
    raise KeyError((a, b))


def sub(prefix, parent, name, el, direction, order=1, label=None, group=None, r=B, charge=0):
    p = pt(G["atoms"][f"{prefix}.{parent}"]["p"], direction, r)
    add(f"{prefix}.{name}", p, el, label, charge, group)
    bond(f"{prefix}.{parent}", f"{prefix}.{name}", order)
    return f"{prefix}.{name}"


def purine(prefix, c, kind):
    g = "base:" + prefix
    ring(prefix, c, ["N1", "C6", "C5", "C4", "N3", "C2"], 0, 60, g, B)
    a = G["atoms"]
    c4, c5 = a[f"{prefix}.C4"]["p"], a[f"{prefix}.C5"]["p"]
    m = ((c4[0] + c5[0]) / 2, (c4[1] + c5[1]) / 2)
    nx, ny = m[0] - c[0], m[1] - c[1]
    L = math.hypot(nx, ny)
    q = (m[0] + nx / L * 0.688 * B, m[1] + ny / L * 0.688 * B)
    R = B / (2 * math.sin(math.radians(36)))
    a4 = out_dir(f"{prefix}.C4", q)
    a5 = out_dir(f"{prefix}.C5", q)
    d = 72 if abs(((a4 + 72) - a5 + 180) % 360 - 180) > 1 else -72
    for i, n in enumerate(["N9", "C8", "N7"], 1):
        add(f"{prefix}.{n}", pt(q, a4 + d * i, R), n[0], group=g)
    bond(f"{prefix}.C4", f"{prefix}.N9", 1, q)
    bond(f"{prefix}.N9", f"{prefix}.C8", 1, q)
    bond(f"{prefix}.C8", f"{prefix}.N7", 1, q)
    bond(f"{prefix}.N7", f"{prefix}.C5", 1, q)
    set_order(prefix, "C4", "C5", 2)
    set_order(prefix, "N7", "C8", 2)
    set_order(prefix, "C2", "N3", 2)
    if kind == "A":
        set_order(prefix, "N1", "C6", 2)
        sub(prefix, "C6", "N6", "N", 60, group=g)
        sub(prefix, "N6", "H6a", "H", 0, group=g, r=HR)
        sub(prefix, "N6", "H6b", "H", 120, group=g, r=HR)
    else:
        sub(prefix, "C6", "O6", "O", 60, 2, group=g)
        sub(prefix, "N1", "H1", "H", 0, group=g, r=HR)
        sub(prefix, "C2", "N2", "N", 300, group=g)
        sub(prefix, "N2", "H2a", "H", 0, group=g, r=HR)
        sub(prefix, "N2", "H2b", "H", 240, group=g, r=HR)
    return out_dir(f"{prefix}.N9", q)


def pyrimidine(prefix, c, kind):
    g = "base:" + prefix
    ring(prefix, c, ["N3", "C4", "C5", "C6", "N1", "C2"], 180, -60, g, B)
    set_order(prefix, "C5", "C6", 2)
    sub(prefix, "C2", "O2", "O", 240, 2, group=g)
    if kind == "T":
        sub(prefix, "C4", "O4", "O", 120, 2, group=g)
        sub(prefix, "N3", "H3", "H", 180, group=g, r=HR)
        sub(prefix, "C5", "C7", "C", 60, label="CH3", group=g)
    else:
        set_order(prefix, "C4", "N3", 2)
        sub(prefix, "C4", "N4", "N", 120, group=g)
        sub(prefix, "N4", "H4a", "H", 180, group=g, r=HR)
        sub(prefix, "N4", "H4b", "H", 60, group=g, r=HR)
    return 300.0


def sugar(prefix, c1, g):
    """Flat deoxyribose whose centre lies along the glycosidic direction g from C1'.
    Ring order C1', O4', C4', C3', C2' runs counterclockwise on both strands (the right
    strand is an in-plane 180 degree rotation of the left, so no mirror image is drawn)."""
    grp = "sugar:" + prefix
    s = pt(c1, g, RP)
    for k, n in enumerate(("C1'", "O4'", "C4'", "C3'", "C2'")):
        add(f"{prefix}.{n}", pt(s, g + 180 + 72 * k, RP), n[0], group=grp)
    for x, y in (("C1'", "O4'"), ("O4'", "C4'"), ("C4'", "C3'"), ("C3'", "C2'"), ("C2'", "C1'")):
        bond(f"{prefix}.{x}", f"{prefix}.{y}", 1, s)
    sub(prefix, "C2'", "H2'", "H", out_dir(f"{prefix}.C2'", s), group=grp, r=HR)
    G["centre"][prefix] = s
    return s


def phos(name, dirs):
    """Add =O and O- (and an optional terminal O-) around an existing P atom."""
    grp = "phosphate:" + name
    G["groups"].setdefault(grp, []).append(f"{name}.P")
    sub(name, "P", "O=", "O", dirs[0], 2, group=grp)
    sub(name, "P", "O-", "O", dirs[1], group=grp, charge=-1, label="O\u2212")
    if len(dirs) > 2:
        sub(name, "P", "Ot", "O", dirs[2], group=grp, charge=-1, label="O\u2212")


def chain(names, els, start, end, side):
    """Zigzag of atoms between two existing atoms, bulging toward `side` (+1 = left of travel)."""
    p, q = G["atoms"][start]["p"], G["atoms"][end]["p"]
    n = len(names) + 1
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = uy * side, -ux * side
    step = L / n
    h = math.sqrt(max(B * B - step * step, 0)) / 2
    for k, (nm, el) in enumerate(zip(names, els), 1):
        off = h if k % 2 else -h
        add(nm, (p[0] + ux * step * k + nx * off, p[1] + uy * step * k + ny * off), el)
    seq = [start] + names + [end]
    for x, y in zip(seq, seq[1:]):
        bond(x, y)
    return step


# ---------------------------------------------------------------- layout
def relax(free, iters=4000):
    """Spring relaxation of `free` atoms: bonds -> B, angle (1-3) springs, soft repulsion from everything else."""
    a = G["atoms"]
    nb = {n: set() for n in a}
    for x, y, *_ in G["bonds"]:
        nb[x].add(y); nb[y].add(x)
    springs = [(x, y, B, 1.0) for x, y, *_ in G["bonds"] if x in free or y in free]
    for c in a:
        ns = sorted(nb[c])
        if not (set(ns) | {c}) & free:
            continue
        rest = 1.414 * B if len(ns) == 4 else (1.732 * B if len(ns) <= 3 else 1.6 * B)
        for i in range(len(ns)):
            for j in range(i + 1, len(ns)):
                if ns[i] in free or ns[j] in free:
                    springs.append((ns[i], ns[j], rest, 0.35))
    near = {n: nb[n] | {m for k in nb[n] for m in nb[k]} for n in free}
    P = {n: list(a[n]["p"]) for n in a}
    for it in range(iters):
        F = {n: [0.0, 0.0] for n in free}
        for x, y, r0, k in springs:
            dx, dy = P[y][0] - P[x][0], P[y][1] - P[x][1]
            d = math.hypot(dx, dy) or 1e-6
            f = k * (d - r0) / d
            if x in F: F[x][0] += f * dx; F[x][1] += f * dy
            if y in F: F[y][0] -= f * dx; F[y][1] -= f * dy
        for n in free:
            for m in a:
                if m == n or m in near[n]:
                    continue
                dx, dy = P[n][0] - P[m][0], P[n][1] - P[m][1]
                d = math.hypot(dx, dy) or 1e-6
                lim = 1.9 * B
                if d < lim:
                    f = 0.6 * (lim - d) / d
                    F[n][0] += f * dx; F[n][1] += f * dy
        step = 0.25 if it < iters * 0.8 else 0.08
        for n in free:
            P[n][0] += step * F[n][0]; P[n][1] += step * F[n][1]
    for n in free:
        a[n]["p"] = tuple(P[n])


# ---------------------------------------------------------------- drawing
RAD = {"H": 5.5, "C": 6.5, "N": 6.5, "O": 6.5, "P": 7.5}


def rad(n):
    at = G["atoms"][n]
    if not at["show"]:
        return 0
    if at["label"] in ("CH3", "H3C"):
        return 8
    return RAD.get(at["el"], 6.5)


def line(p, q, sw=1.5, col=DARK, extra=""):
    return f'<line x1="{p[0]:.2f}" y1="{p[1]:.2f}" x2="{q[0]:.2f}" y2="{q[1]:.2f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"{extra}/>'


def draw_bond(out, a, b, order, inner):
    pa, pb = G["atoms"][a]["p"], G["atoms"][b]["p"]
    dx, dy = pb[0] - pa[0], pb[1] - pa[1]
    L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    ra, rb = rad(a), rad(b)
    p = (pa[0] + ux * ra, pa[1] + uy * ra); q = (pb[0] - ux * rb, pb[1] - uy * rb)
    if order == 1:
        out.append(line(p, q)); return
    nx, ny = -uy, ux
    if inner is not None:
        mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
        if (inner[0] - mx) * nx + (inner[1] - my) * ny < 0:
            nx, ny = -nx, -ny
        out.append(line(p, q))
        s = 3.8
        shrink = 1.5
        p2 = (p[0] + nx * s + ux * shrink, p[1] + ny * s + uy * shrink)
        q2 = (q[0] + nx * s - ux * shrink, q[1] + ny * s - uy * shrink)
        out.append(line(p2, q2, 1.3))
    else:
        s = 2.1
        out.append(line((p[0] + nx * s, p[1] + ny * s), (q[0] + nx * s, q[1] + ny * s), 1.3))
        out.append(line((p[0] - nx * s, p[1] - ny * s), (q[0] - nx * s, q[1] - ny * s), 1.3))


def label(out, n):
    at = G["atoms"][n]
    if not at["show"]:
        return
    x, y = at["p"]
    lab = at["label"]
    col = DARK
    if lab == "CH3":
        out.append(T(x + 2, y + 4.3, "CH", 12, 600, col, "middle"))
        out.append(T(x + 11.5, y + 8, "3", 8.5, 600, col, "middle"))
        return
    if lab == "H3C":
        out.append(T(x + 0.5, y + 4.3, "C", 12, 600, col, "middle"))
        out.append(T(x - 7, y + 8, "3", 8.5, 600, col, "middle"))
        out.append(T(x - 13.5, y + 4.3, "H", 12, 600, col, "middle"))
        return
    if lab == "O\u2212":
        out.append(T(x, y + 4.3, "O", 12, 600, col, "middle"))
        nbr = [y_ if x_ == n else x_ for x_, y_, *_ in G["bonds"] if n in (x_, y_)][0]
        q = G["atoms"][nbr]["p"]
        sx = 1 if q[0] <= x + 2 else -1
        out.append(T(x + 7.5 * sx, y - 3, "\u2212", 9, 600, col, "middle"))
        return
    if lab == "OH":
        out.append(T(x + 3, y + 4.3, "OH", 12, 600, col, "middle"))
        return
    size = 13 if lab == "P" else (10.5 if lab == "H" else 12)
    out.append(T(x, y + size * 0.36, lab, size, 700 if lab == "P" else 600, col, "middle"))


def hull(points):
    pts = sorted(set((round(x, 2), round(y, 2)) for x, y in points))
    if len(pts) < 3:
        return pts
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def blob(out, names, fill, pad=11):
    h = hull([G["atoms"][n]["p"] for n in names])
    d = "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in h) + "Z"
    out.append(f'<path d="{d}" fill="{fill}" stroke="{fill}" stroke-width="{2 * pad}" stroke-linejoin="round"/>')


def arrow(out, x, y0, y1):
    d = 1 if y1 > y0 else -1
    out.append(line((x, y0), (x, y1 - 9 * d), 1.6))
    out.append(f'<path d="M{x - 5:.2f} {y1 - 10 * d:.2f}L{x:.2f} {y1:.2f}L{x + 5:.2f} {y1 - 10 * d:.2f}Z" fill="{DARK}"/>')


def bbox(names):
    ps = [G["atoms"][n]["p"] for n in names]
    return (min(p[0] for p in ps), min(p[1] for p in ps), max(p[0] for p in ps), max(p[1] for p in ps))


def numbers(out, s, r=13.5, extra=()):
    """Blue 1'-5' labels beside the carbons of sugar `s`, each placed in the emptiest direction."""
    a = G["atoms"]
    obst = [v["p"] for v in a.values()]
    for x, y, *_ in G["bonds"]:
        p, q = a[x]["p"], a[y]["p"]
        obst += [(p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t) for t in (0.25, 0.5, 0.75)]
    obst += list(extra)
    placed = []
    for k in "12345":
        n = f"{s}.C{k}'"
        if n not in a:
            continue
        c = a[n]["p"]; best = None
        for d in range(0, 360, 10):
            q = pt(c, d, r)
            sc = min(math.hypot(q[0] - o[0], q[1] - o[1]) for o in obst + placed if o != c)
            if best is None or sc > best[0] + 0.01:
                best = (sc, q)
        q = best[1]; placed.append(q)
        out.append(T(q[0], q[1] + 3.4, f"{k}\u2032", 9.5, 700, NUM, "middle"))