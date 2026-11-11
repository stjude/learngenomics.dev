"""Figure 7.3: A methylated CpG site drawn atom by atom."""

import math

from figures import molecules as m
from figures.core import BLUE, COPYRIGHT, DARK, ORANGE, T, main, svg_doc
from figures.dna_atoms import build_pairs
from figures.molecules import G, TINT

NAME = "7.3-methylated-cpg"
PAIRS = (("C", "G"), ("G", "C"))
METHYL = ("L0", "R1")
METHYL_FILL = "#fbd38a"


def draw():
    """Return (svg fragments, bbox) in raw coordinates."""
    left, right = build_pairs(PAIRS, METHYL)
    a = G["atoms"]
    out, notes = [], []
    base_kind = {"L0": "C", "R0": "G", "L1": "G", "R1": "C"}
    for g, names in G["groups"].items():
        kind, pre = g.split(":")
        if kind == "base":
            m.blob(out, names, TINT[base_kind[pre]])
        elif kind == "sugar":
            m.blob(out, names, TINT["sugar"])
        else:
            m.blob(out, names, TINT["phosphate"], 10)
    for pre in METHYL:
        x, y = a[f"{pre}.C5M"]["p"]
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="17" fill="{METHYL_FILL}" stroke="{ORANGE}" stroke-width="1.5"/>')
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
    names = {"L0": "5-methylcytosine", "R0": "guanine", "L1": "guanine", "R1": "5-methylcytosine"}
    bb = {pre: m.bbox(grp[pre]) for pre in names}
    ytop = min(bb["L0"][1], bb["R0"][1]) - 30
    ybot = max(bb["L1"][3], bb["R1"][3]) + 29
    for pre in ("L0", "R0"):
        x0, y0, x1, y1 = bb[pre]
        notes.append((T((x0 + x1) / 2, ytop, names[pre], 12, 700, DARK, "middle"), ytop - 11))
    # below the lower pair the right label must end before the right strand's sugar
    xr = min(a[n]["p"][0] for n in grp["R1s"]) - 4
    xg = min((bb["L1"][0] + bb["L1"][2]) / 2, xr - len(names["R1"]) * 6.9 - 14 - len(names["L1"]) * 3.45)
    notes.append((T(xg, ybot, names["L1"], 12, 700, DARK, "middle"), ybot + 4))
    notes.append((T(xr, ybot, names["R1"], 12, 700, DARK, "end"), ybot + 4))
    xs = [p["p"][0] for p in a.values()]; ys = [p["p"][1] for p in a.values()]
    X0, X1 = min(xs), max(xs)
    t5 = m.bbox(grp[left[0] + "p"]); b3 = a[f"{left[1]}.O3'"]["p"]
    notes.append((T(X0 - 36, t5[1] - 12, "5\u2032 end", 12, 700, DARK), t5[1] - 23))
    notes.append((T(b3[0] + 4, b3[1] + 28, "3\u2032 end", 12, 700, DARK, "middle"), b3[1] + 33))
    r3 = a[f"{right[0]}.O3'"]["p"]; r5 = m.bbox(grp[right[1] + "p"])
    notes.append((T(r3[0] + 4, r3[1] - 17, "3\u2032 end", 12, 700, DARK, "middle"), r3[1] - 28))
    notes.append((T(r5[2] + 4, r5[3] + 29, "5\u2032 end", 12, 700, DARK, "end"), r5[3] + 33))
    m.arrow(out, X0 - 24, t5[1] + 6, b3[1] + 6)
    m.arrow(out, X1 + 24, r5[3] - 6, r3[1] - 6)
    boxes = []
    for (cx, cy, w) in ((X0 - 36 + 22, t5[1] - 16, 44), (b3[0] + 4, b3[1] + 24, 44),
                        (r3[0] + 4, r3[1] - 21, 44), (r5[2] + 4 - 22, r5[3] + 25, 44)):
        boxes += [(cx + dx, cy + dy) for dx in range(-int(w / 2), int(w / 2) + 1, 5) for dy in (-5, 0, 5)]
    for pre in METHYL:
        x, y = a[f"{pre}.C5M"]["p"]
        boxes += [(x + dx, y + dy) for dx in range(-18, 19, 6) for dy in range(-18, 19, 6)]
    for sg in ("L0s", "R0s", "L1s", "R1s"):
        m.numbers(out, sg, extra=boxes)
    out += [t for t, _ in notes]
    top = min([min(ys) - 18] + [y for _, y in notes]) - 4
    bot = max([max(ys)] + [y for _, y in notes]) + 10
    ly = bot + 14
    leg = [("swatch", TINT["C"], "5-methylcytosine", 0, 0), ("swatch", TINT["G"], "guanine", 1, 0),
           ("methyl", METHYL_FILL, "methyl group", 0, 1), ("hb", BLUE, "hydrogen bond", 1, 1),
           ("swatch", TINT["phosphate"], "phosphate", 0, 2), ("swatch", TINT["sugar"], "deoxyribose", 1, 2)]
    colw = 150
    lx = (X0 + X1) / 2 - colw
    for kind, col, txt, ci, ri in leg:
        x, y = lx + ci * colw + 14, ly + ri * 24
        if kind == "swatch":
            out.append(f'<rect x="{x:.2f}" y="{y - 8:.2f}" width="18" height="14" rx="4" fill="{col}"/>')
        elif kind == "methyl":
            out.append(f'<circle cx="{x + 9:.2f}" cy="{y - 1:.2f}" r="7.5" fill="{col}" stroke="{ORANGE}" stroke-width="1.5"/>')
        else:
            out.append(m.line((x + 1, y - 1), (x + 19, y - 1), 2.0, BLUE, ' stroke-dasharray="0.1 4"'))
        out.append(T(x + 25, y + 3.5, txt, 12, 400, DARK))
    return out, (X0 - 36, top, X1 + 36, ly + 60)


def fig():
    out, (x0, y0, x1, y1) = draw()
    W = x1 - x0
    H = y1 - y0 + 26
    body = [f'<g transform="translate({-x0:.2f} {-y0:.2f})">'] + out + ["</g>"]
    body.append(T(W - 4, H - 6, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(round(W, 2), round(H, 2), body, "A methylated CpG site drawn atom by atom.")


if __name__ == "__main__":
    main(NAME, fig)
