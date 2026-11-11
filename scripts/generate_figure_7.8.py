"""Figure 7.8: The four DNA bases."""

from figures import molecules as m
from figures.core import COPYRIGHT, DARK, GREY_LINE, MUTED, T, main, svg_doc
from figures.dna_atoms import build_bases
from figures.molecules import B, G, TINT

NAME = "7.8-dna-bases"

STUB = 0.9 * B   # length of the stub bond toward the (undrawn) sugar

RINGS = {"A": [["N1", "C6", "C5", "C4", "N3", "C2"], ["C4", "N9", "C8", "N7", "C5"]],
         "C": [["N3", "C4", "C5", "C6", "N1", "C2"]]}
RINGS["G"] = RINGS["A"]; RINGS["T"] = RINGS["C"]


def shift(k, dx, dy):
    for n in G["groups"]["base:" + k]:
        p = G["atoms"][n]["p"]
        G["atoms"][n]["p"] = (p[0] + dx, p[1] + dy)


def extent(k, stubs):
    n, g = stubs[k]
    ps = [G["atoms"][a]["p"] for a in G["groups"]["base:" + k]]
    ps.append(m.pt(G["atoms"][n]["p"], g, STUB + 22))
    return min(p[0] for p in ps), min(p[1] for p in ps), max(p[0] for p in ps), max(p[1] for p in ps)


def fig():
    stubs = build_bases()
    a = G["atoms"]
    cols = (106.0, 294.0)
    out, y = [], 30.0
    rows = (("Purines", "two rings: a six-membered ring fused to a five-membered ring", "AG"),
            ("Pyrimidines", "one ring: a single six-membered ring", "CT"))
    plan = []
    for r, (title, sub, ks) in enumerate(rows):
        if r:
            out.append(f'<line x1="16" y1="{y - 34:.2f}" x2="384" y2="{y - 34:.2f}" stroke="#d9dbe0" stroke-width="1"/>')
        out.append(T(16, y, title, 15, 700, DARK))
        out.append(T(16, y + 19, sub, 11.5, 400, MUTED))
        top = y + 44
        ex = {k: extent(k, stubs) for k in ks}
        h = max(e[3] - e[1] for e in ex.values())
        for k, cx in zip(ks, cols):
            x0, y0, x1, y1 = ex[k]
            shift(k, cx - (x0 + x1) / 2, top + (h - (y1 - y0)) / 2 - y0)
        plan.append((ks, top + h + 26))
        y = top + h + 26 + 70
    grp = {k.split(":")[1]: v for k, v in G["groups"].items()}
    for k, names in grp.items():
        m.blob(out, names, TINT[k])
        for ring in RINGS[k]:
            pts = " ".join(f"{a[f'{k}.{n}']['p'][0]:.2f},{a[f'{k}.{n}']['p'][1]:.2f}" for n in ring)
            out.append(f'<polygon points="{pts}" fill="#000000" fill-opacity="0.07"/>')
    for x, y_, o, c in G["bonds"]:
        m.draw_bond(out, x, y_, o, c)
    for n in a:
        m.label(out, n)
    for k, (n, g) in stubs.items():
        p = a[n]["p"]
        out.append(m.line(m.pt(p, g, 7), m.pt(p, g, STUB), 1.5, GREY_LINE))
        t = m.pt(p, g, STUB + 11)
        out.append(T(t[0], t[1] + 4, "sugar", 10.5, 400, MUTED, "middle"))
    names = {"A": "adenine (A)", "G": "guanine (G)", "C": "cytosine (C)", "T": "thymine (T)"}
    for ks, yn in plan:
        for k, cx in zip(ks, cols):
            out.append(T(cx, yn, names[k], 12.5, 700, DARK, "middle"))
    H = plan[-1][1] + 34
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(392, round(H, 2) - 6, out, "The four DNA bases: purines adenine and guanine, pyrimidines cytosine and thymine.",
                   origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
