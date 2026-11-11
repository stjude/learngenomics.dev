"""Atom-level DNA builders shared by figures 7.8 and 7.10 and the chemistry check."""

import math

from figures.molecules import (B, G, add, ang, bond, chain, clear, out_dir, phos, pt, purine,
                               pyrimidine, relax, sub, sugar)

DPAIR = 5.2   # vertical spacing between the two base pairs, in bond lengths
TILT = 9.0    # each base pair is turned this many degrees counterclockwise


def build_pairs(pairs=(("A", "T"), ("G", "C")), methyl=()):
    """Two stacked base pairs on two antiparallel two-nucleotide strands.

    pairs lists (left base, right base) from top to bottom; by default A-T above G-C.
    When the pyrimidine is on the left, that pair's bases are mirrored left to right about
    the midpoint of the glycosidic atoms before the sugars are added (a flat base is the same molecule from either face).
    methyl lists the prefixes (such as "L0") of cytosines that carry a 5-methyl group.
    Returns the sugar prefixes of the left strand (5' to 3', top to bottom) and of the
    right strand (top to bottom, so 3' to 5').
    """
    clear()
    xP, xY = 0.0, 4 * B
    L, R = [], []
    for i, (lb, rb) in enumerate(pairs):
        y = i * DPAIR * B
        lp, rp = f"L{i}", f"R{i}"
        flip = lb in "CT"
        pu, py = (rb, lb) if flip else (lb, rb)
        ppre, ypre = (rp, lp) if flip else (lp, rp)
        before = set(G["atoms"])
        g9 = purine(ppre, (xP, y), pu)
        n1 = pyrimidine(ypre, (xY, y), py)
        if ypre in methyl:
            sub(ypre, "C5", "C5M", "C", 60, label="CH3", group="base:" + ypre)
        cx, cy = (xP + xY) / 2, y
        new = set(G["atoms"]) - before
        if flip:
            # mirror about the midpoint of the two glycosidic atoms, so the sugars land where
            # an unflipped pair would put them
            mx = (G["atoms"][f"{ppre}.N9"]["p"][0] + G["atoms"][f"{ypre}.N1"]["p"][0]) / 2
            for n in new:
                px, py_ = G["atoms"][n]["p"]
                G["atoms"][n]["p"] = (2 * mx - px, py_)
                if G["atoms"][n]["label"] == "CH3":
                    G["atoms"][n]["label"] = "H3C"
            G["bonds"][:] = [(x, z, o, c if c is None or x not in new else (2 * mx - c[0], c[1]))
                             for x, z, o, c in G["bonds"]]
            g9, n1 = 180 - g9, 180 - n1
        th = math.radians(TILT)
        for n in new:
            px, py_ = G["atoms"][n]["p"]
            dx, dy = px - cx, py_ - cy
            G["atoms"][n]["p"] = (cx + dx * math.cos(th) + dy * math.sin(th), cy - dx * math.sin(th) + dy * math.cos(th))
        g9 += TILT; n1 += TILT
        gl, gr = (n1, g9) if flip else (g9, n1)
        al, ar = (f"{lp}.N1", f"{rp}.N9") if flip else (f"{lp}.N9", f"{rp}.N1")
        sugar(lp + "s", pt(G["atoms"][al]["p"], gl), gl)
        bond(al, f"{lp}s.C1'")
        sugar(rp + "s", pt(G["atoms"][ar]["p"], gr), gr)
        bond(ar, f"{rp}s.C1'")
        if pu == "A":
            G["hbonds"] += [(f"{ppre}.H6a", f"{ypre}.O4"), (f"{ypre}.H3", f"{ppre}.N1")]
        else:
            G["hbonds"] += [(f"{ypre}.H4a", f"{ppre}.O6"), (f"{ppre}.H1", f"{ypre}.N3"), (f"{ppre}.H2a", f"{ypre}.O2")]
        L.append(lp + "s"); R.append(rp + "s")
    a = G["atoms"]
    for up, dn, side in ((L[0], L[1], 1), (R[1], R[0], 1)):
        o3, P, o5, c5 = f"{up}.O3'", f"{dn}p.P", f"{dn}.O5'", f"{dn}.C5'"
        add(o3, pt(a[f"{up}.C3'"]["p"], out_dir(f"{up}.C3'", G["centre"][up])), "O")
        bond(f"{up}.C3'", o3)
        chain([P, o5, c5], ["P", "O", "C"], o3, f"{dn}.C4'", -side)
        G["groups"]["sugar:" + dn].append(c5)
        din, dout = ang(P, o3), ang(P, o5)
        mid = math.degrees(math.atan2(math.sin(math.radians(din)) + math.sin(math.radians(dout)),
                                      math.cos(math.radians(din)) + math.cos(math.radians(dout)))) + 180
        phos(f"{dn}p", (mid + 40, mid - 40))
        G["groups"]["phosphate:" + dn + "p"] += [o3, o5]
    for s, rot in ((L[0], 0), (R[1], 180)):
        sub(s, "C4'", "C5'", "C", 120 + rot, group="sugar:" + s)
        o5 = sub(s, "C5'", "O5'", "O", 60 + rot)
        add(f"{s}p.P", pt(a[o5]["p"], 120 + rot), "P")
        bond(o5, f"{s}p.P")
        phos(f"{s}p", (30 + rot, 210 + rot, 120 + rot))
        G["groups"]["phosphate:" + s + "p"].append(o5)
    for s in (L[1], R[0]):
        sub(s, "C3'", "O3'", "O", out_dir(f"{s}.C3'", G["centre"][s]), label="OH", group="sugar:" + s)
    free = set()
    for up, dn in ((L[0], L[1]), (R[1], R[0])):
        free |= {f"{up}.O3'", f"{dn}p.P", f"{dn}.O5'", f"{dn}.C5'", f"{dn}p.O=", f"{dn}p.O-"}
    relax(free)
    return L, R


def build_bases():
    """The four free bases, each prefixed by its letter, all at the origin.

    Returns {letter: (glycosidic atom, direction of its bond to the sugar in degrees)}.
    """
    clear()
    stubs = {}
    for k in "AG":
        stubs[k] = (f"{k}.N9", purine(k, (0, 0), k))
    for k in "CT":
        stubs[k] = (f"{k}.N1", pyrimidine(k, (0, 0), k))
    return stubs
