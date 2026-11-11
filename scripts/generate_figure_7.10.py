"""Figure 7.10: Two DNA base pairs drawn atom by atom."""

import math

from figures import molecules as m
from figures.core import BLUE, COPYRIGHT, DARK, T, main, svg_doc
from figures.dna_atoms import build_pairs
from figures.molecules import G, TINT

NAME = "7.10-dna-base-pairs"


def draw():
    """Return (svg fragments, bbox) in raw coordinates."""
    left, right = build_pairs()
    a = G["atoms"]
    out, notes = [], []
    base_kind = {"L0": "A", "R0": "T", "L1": "G", "R1": "C"}
    for g, names in G["groups"].items():
        kind, pre = g.split(":")
        if kind == "base":
            m.blob(out, names, TINT[base_kind[pre]])
        elif kind == "sugar":
            m.blob(out, names, TINT["sugar"])
        else:
            m.blob(out, names, TINT["phosphate"], 10)
    for h, acc in G["hbonds"]:
        p, q = a[h]["p"], a[acc]["p"]
        dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        out.append(m.line((p[0] + ux * 6.5, p[1] + uy * 6.5), (q[0] - ux * 8, q[1] - uy * 8), 2.0, BLUE, ' stroke-dasharray="0.1 4"'))
    for x, y, o, c in G["bonds"]:
        m.draw_bond(out, x, y, o, c)
    for n in a:
        m.label(out, n)
    grp = {k.split(":")[1]: v for k, v in G["groups"].items()}
    # base names
    names = {"L0": "adenine (A)", "R0": "thymine (T)", "L1": "guanine (G)", "R1": "cytosine (C)"}
    bb = {pre: m.bbox(grp[pre]) for pre in names}
    ytop = min(bb["L0"][1], bb["R0"][1]) - 19
    ybot = max(bb["L1"][3], bb["R1"][3]) + 29
    for pre, nm in names.items():
        x0, y0, x1, y1 = bb[pre]
        yy = ytop if pre.endswith("0") else ybot
        notes.append((T((x0 + x1) / 2, yy, nm, 12, 700, DARK, "middle"), yy - 11 if pre.endswith("0") else yy + 4))
    # strand ends
    xs = [p["p"][0] for p in a.values()]; ys = [p["p"][1] for p in a.values()]
    X0, X1 = min(xs), max(xs)
    t5 = m.bbox(grp[left[0] + "p"]); b3 = a[f"{left[1]}.O3'"]["p"]
    notes.append((T(t5[0] - 4, t5[1] - 19, "5\u2032 end", 12, 700, DARK), t5[1] - 30))
    notes.append((T(b3[0] + 4, b3[1] + 28, "3\u2032 end", 12, 700, DARK, "middle"), b3[1] + 33))
    r3 = a[f"{right[0]}.O3'"]["p"]; r5 = m.bbox(grp[right[1] + "p"])
    notes.append((T(r3[0] + 4, r3[1] - 17, "3\u2032 end", 12, 700, DARK, "middle"), r3[1] - 28))
    notes.append((T(r5[2] + 4, r5[3] + 29, "5\u2032 end", 12, 700, DARK, "end"), r5[3] + 33))
    m.arrow(out, X0 - 24, t5[1] + 6, b3[1] + 6)
    m.arrow(out, X1 + 24, r5[3] - 6, r3[1] - 6)
    boxes = []
    for (cx, cy, w) in ((t5[0] - 4 + 20, t5[1] - 23, 44), (b3[0] + 4, b3[1] + 24, 44),
                        (r3[0] + 4, r3[1] - 21, 44), (r5[2] + 4 - 22, r5[3] + 25, 44)):
        boxes += [(cx + dx, cy + dy) for dx in range(-int(w / 2), int(w / 2) + 1, 5) for dy in (-5, 0, 5)]
    for sg in ("L0s", "R0s", "L1s", "R1s"):
        m.numbers(out, sg, extra=boxes)
    out += [t for t, _ in notes]
    top = min([min(ys)] + [y for _, y in notes]) - 4
    bot = max([max(ys)] + [y for _, y in notes]) + 10
    # legend
    lx, ly = (X0 + X1) / 2 - 163, bot + 14
    leg = [("swatch", TINT["phosphate"], "phosphate"), ("swatch", TINT["sugar"], "deoxyribose"), ("hb", BLUE, "hydrogen bond")]
    x = lx
    for kind, col, txt in leg:
        if kind == "swatch":
            out.append(f'<rect x="{x:.2f}" y="{ly - 8:.2f}" width="18" height="14" rx="4" fill="{col}"/>')
        else:
            out.append(m.line((x + 1, ly - 1), (x + 19, ly - 1), 2.0, BLUE, ' stroke-dasharray="0.1 4"'))
        out.append(T(x + 25, ly + 3.5, txt, 12, 400, DARK))
        x += 25 + len(txt) * 6.6 + 22
    return out, (X0 - 36, top, X1 + 36, ly + 12)


def fig():
    out, (x0, y0, x1, y1) = draw()
    W = x1 - x0
    H = y1 - y0 + 26
    body = [f'<g transform="translate({-x0:.2f} {-y0:.2f})">'] + out + ["</g>"]
    body.append(T(W - 4, H - 6, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(round(W, 2), round(H, 2), body, "Two DNA base pairs drawn atom by atom.")


if __name__ == "__main__":
    main(NAME, fig)
