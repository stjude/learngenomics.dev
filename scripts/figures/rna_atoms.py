"""Atom-level RNA strand 5'-pApU-3'OH for figure 7.11 and the chemistry check."""

import math

from figures import molecules as m
from figures.core import DARK, T
from figures.dna_atoms import DPAIR
from figures.molecules import (B, G, TINT, add, ang, bond, chain, clear, out_dir, phos, pt, purine,
                               pyrimidine, relax, sub, sugar)


def xform(names, f):
    for n in names:
        G["atoms"][n]["p"] = f(G["atoms"][n]["p"])
    for i, (x, y, o, c) in enumerate(G["bonds"]):
        if x in names and y in names and c is not None:
            G["bonds"][i] = (x, y, o, f(c))


def ribose(prefix, c1, g):
    s = sugar(prefix, c1, g)
    h = f"{prefix}.H2'"
    del G["atoms"][h]
    G["bonds"] = [b for b in G["bonds"] if h not in b[:2]]
    G["groups"]["sugar:" + prefix].remove(h)
    sub(prefix, "C2'", "O2'", "O", out_dir(f"{prefix}.C2'", s), label="OH", group="sugar:" + prefix)
    return s


def build():
    """Adenosine (L0) linked 3'-5' to uridine (L1) below it."""
    clear()
    g9 = purine("L0", (0.0, 0.0), "A")
    ribose("L0s", pt(G["atoms"]["L0.N9"]["p"], g9), g9)
    bond("L0.N9", "L0s.C1'")
    before = set(G["atoms"])
    pyrimidine("L1", (0.0, 0.0), "T")
    G["atoms"].pop("L1.C7")
    G["bonds"] = [b for b in G["bonds"] if "L1.C7" not in b[:2]]
    G["groups"]["base:L1"].remove("L1.C7")
    new = set(G["atoms"]) - before
    xform(new, lambda p: (-p[0], p[1]))
    a1 = out_dir("L1.N1", (0.0, 0.0))
    th = math.radians(g9 - a1)
    xform(new, lambda p: (p[0] * math.cos(th) + p[1] * math.sin(th), -p[0] * math.sin(th) + p[1] * math.cos(th)))
    n9, n1 = G["atoms"]["L0.N9"]["p"], G["atoms"]["L1.N1"]["p"]
    dx, dy = n9[0] - n1[0], n9[1] + DPAIR * B - n1[1]
    xform(new, lambda p: (p[0] + dx, p[1] + dy))
    ribose("L1s", pt(G["atoms"]["L1.N1"]["p"], g9), g9)
    bond("L1.N1", "L1s.C1'")
    a = G["atoms"]
    up, dn = "L0s", "L1s"
    o3, P, o5, c5 = f"{up}.O3'", f"{dn}p.P", f"{dn}.O5'", f"{dn}.C5'"
    add(o3, pt(a[f"{up}.C3'"]["p"], out_dir(f"{up}.C3'", G["centre"][up])), "O")
    bond(f"{up}.C3'", o3)
    chain([P, o5, c5], ["P", "O", "C"], o3, f"{dn}.C4'", -1)
    G["groups"]["sugar:" + dn].append(c5)
    din, dout = ang(P, o3), ang(P, o5)
    mid = math.degrees(math.atan2(math.sin(math.radians(din)) + math.sin(math.radians(dout)),
                                  math.cos(math.radians(din)) + math.cos(math.radians(dout)))) + 180
    phos(f"{dn}p", (mid + 40, mid - 40))
    G["groups"]["phosphate:" + dn + "p"] += [o3, o5]
    sub(up, "C4'", "C5'", "C", 120, group="sugar:" + up)
    o5_top = sub(up, "C5'", "O5'", "O", 60)
    add(f"{up}p.P", pt(a[o5_top]["p"], 120), "P")
    bond(o5_top, f"{up}p.P")
    phos(f"{up}p", (30, 210, 120))
    G["groups"]["phosphate:" + up + "p"].append(o5_top)
    sub(dn, "C3'", "O3'", "O", out_dir(f"{dn}.C3'", G["centre"][dn]), label="OH", group="sugar:" + dn)
    # The published figure relaxes the top strand's O5' rather than the linker's O5'.
    relax({o3, P, o5_top, c5, f"{dn}p.O=", f"{dn}p.O-"})


def panel():
    """Return (svg fragments, bbox) in raw coordinates."""
    build()
    a = G["atoms"]
    out, notes = [], []
    for g, names in G["groups"].items():
        kind, pre = g.split(":")
        fill = TINT["A"] if pre == "L0" else TINT["U"] if pre == "L1" else TINT["sugar"] if kind == "sugar" else TINT["phosphate"]
        m.blob(out, names, fill, 10 if kind == "phosphate" else 11)
    for x, y, o, c in G["bonds"]:
        m.draw_bond(out, x, y, o, c)
    for n in a:
        m.label(out, n)
    grp = {k.split(":")[1]: v for k, v in G["groups"].items()}
    for pre, nm in (("L0", "adenine (A)"), ("L1", "uracil (U)")):
        x0, y0, x1, y1 = m.bbox(grp[pre])
        notes.append((x1 + 22, (y0 + y1) / 2 + 4, nm, "start", 700))
    t5 = m.bbox(grp["L0sp"]); b3 = a["L1s.O3'"]["p"]
    notes.append((t5[0] - 4, t5[1] - 19, "5\u2032 end", "start", 700))
    notes.append((b3[0] + 4, b3[1] + 28, "3\u2032 end", "middle", 700))
    boxes = []
    for x, y, txt, anc, _ in notes:
        w = len(txt) * 6.8
        x0 = x if anc == "start" else x - w / 2
        boxes += [(x0 + k, y - 4 + dy) for k in range(0, int(w) + 1, 5) for dy in (-5, 0, 5)]
    for sg in ("L0s", "L1s"):
        m.numbers(out, sg, extra=boxes)
    for x, y, txt, anc, wt in notes:
        out.append(T(x, y, txt, 12, wt, DARK, anc))
    xs = [p["p"][0] for p in a.values()]; ys = [p["p"][1] for p in a.values()]
    X0 = min(xs)
    m.arrow(out, X0 - 24, t5[1] + 6, b3[1] + 6)
    X1 = max(max(xs), max(n[0] + len(n[2]) * 6.8 for n in notes if n[3] == "start"))
    return out, (X0 - 36, min(ys + [t5[1] - 30]), X1, max(ys + [b3[1] + 33]))
