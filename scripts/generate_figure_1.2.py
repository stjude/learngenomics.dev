"""Figure 1.2: Human karyotype: 22 pairs of autosomes and the sex chromosomes X and Y."""

import math
import os

from figures.core import BLUE, DATA_DIR, FONT_DIR, NAVY, PURPLE, T, copyright_text, main, svg_doc

NAME = "1.2-karyotype"

_metrics = None


def text_width(s, size):
    """Advance width of s in Source Sans 3 Regular (the variable font instanced at wght 400)."""
    global _metrics
    if _metrics is None:
        from fontTools.ttLib import TTFont
        from fontTools.varLib import instancer
        f = instancer.instantiateVariableFont(TTFont(os.path.join(FONT_DIR, "SourceSans3-VF.ttf")), {"wght": 400})
        _metrics = (f.getBestCmap(), f["hmtx"].metrics, f["head"].unitsPerEm)
    cmap, hmtx, upm = _metrics
    total = 0
    for ch in s:
        g = cmap.get(ord(ch)) or cmap.get(ord("?"))
        total += hmtx[g][0]
    return total * size / upm


STAIN = {"gneg": 0, "gpos25": 0.25, "gpos50": 0.5, "gpos75": 0.75, "gpos100": 0.95, "gvar": 0.6}


def load_cytobands():
    """UCSC hg38 cytoBand table (https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/cytoBand.txt.gz)."""
    path = os.path.join(DATA_DIR, "hg38-cytoBand.txt")
    chroms = {}
    for line in open(path, encoding="utf-8"):
        c, a, b, name, stain = line.rstrip("\n").split("\t")
        chroms.setdefault(c[3:], []).append((int(a) / 1e6, int(b) / 1e6, name, stain))
    return chroms


def chrom_outline(bands, s, w):
    """Closed path for an ideogram: rounded telomeres, pinched centromere, narrow stalks."""
    L = bands[-1][1] * s
    yc = next(b[1] for b in bands if b[2].startswith("p") and b[3] == "acen") * s
    stalks = [(b[0] * s, b[1] * s) for b in bands if b[3] == "stalk"]
    r, t, hw0 = w / 2, 2.2, w / 2

    def hw(y):
        h = hw0
        for a, b in stalks:
            if a - 0.6 < y < b + 0.6:
                d = min(y - (a - 0.6), (b + 0.6) - y, 0.6) / 0.6
                h = min(h, hw0 - (hw0 - w * 0.17) * d)
        if abs(y - yc) < t:
            h = min(h, w * 0.2 + (hw0 - w * 0.2) * (abs(y - yc) / t) ** 1.3)
        for e in (y, L - y):
            if e < r:
                h = min(h, math.sqrt(max(0.0, r * r - (r - e) ** 2)))
        return h

    ys = {0.0, L}
    for k in range(41):
        ys.add(r * k / 40)
        ys.add(L - r * k / 40)
        ys.add(yc - t + 2 * t * k / 40)
    for a, b in stalks:
        for k in range(7):
            ys.update((a - 0.6 + 0.1 * k, b + 0.6 - 0.1 * k))
    ys = sorted(y for y in ys if 0 <= y <= L)
    right = [(hw(y), y) for y in ys]
    pts = right + [(-x, y) for x, y in reversed(right)]
    simp = [pts[0]]
    for i in range(1, len(pts) - 1):
        (x0, y0), (x1, y1), (x2, y2) = simp[-1], pts[i], pts[i + 1]
        if abs((x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)) > 0.02:
            simp.append(pts[i])
    simp.append(pts[-1])
    return "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in simp) + "Z", L, yc


def fig():
    chroms = load_cytobands()
    s, w, gap = 0.47, 10.0, 3.0
    W = 527
    out, defs = [], []
    out.append(T(W / 2, 14, "Human karyotype", 9.5, 700, anchor="middle"))
    info = {}
    for c, bands in chroms.items():
        sex = c in ("X", "Y")
        stroke, tint = (PURPLE, PURPLE) if sex else (BLUE, BLUE)
        d, L, yc = chrom_outline(bands, s, w)
        info[c] = (L, yc)
        merged = []
        for a, b, _, st in bands:
            op = STAIN.get(st, 0)
            if merged and merged[-1][2] == op:
                merged[-1][1] = b
            else:
                merged.append([a, b, op])
        rects = "".join(f'<rect x="{-w / 2:g}" y="{a * s:.2f}" width="{w:g}" height="{(b - a) * s:.2f}" fill-opacity="{op:g}"/>'
                        for a, b, op in merged if op)
        defs.append(f'<clipPath id="chr{c}-clip"><path d="{d}"/></clipPath>')
        defs.append(f'<g id="chr{c}"><path d="{d}" fill="{tint}" fill-opacity="0.1"/>'
                    f'<g clip-path="url(#chr{c}-clip)" fill="{NAVY}">{rects}</g>'
                    f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="0.8" stroke-linejoin="round"/></g>')
    out.append("<defs>" + "".join(defs) + "</defs>")

    def place(c, x, y):
        return f'<use href="#chr{c}" xlink:href="#chr{c}" x="{x:.2f}" y="{y:.2f}"/>'

    rows = [[str(i) for i in range(1, 13)], [str(i) for i in range(13, 23)] + ["XY"]]
    slot, top = (W - 16) / 12, 30
    for row in rows:
        members = [m for k in row for m in (("X", "Y") if k == "XY" else (k,))]
        cen = max(info[m][1] for m in members)
        bottom = max(cen - info[m][1] + info[m][0] for m in members)
        x0 = 8 + (W - 16 - slot * len(row)) / 2
        out.append(f'<g class="row">')
        for i, k in enumerate(row):
            cx = x0 + slot * (i + 0.5)
            pair = (("X", cx - (w + gap) / 2), ("Y", cx + (w + gap) / 2)) if k == "XY" else \
                   ((k, cx - (w + gap) / 2), (k, cx + (w + gap) / 2))
            out.append(f'<g class="chromosome-pair" id="pair-{k}">')
            for c, x in pair:
                out.append(place(c, x, top + cen - info[c][1]))
            out.append("</g>")
            if k == "XY":
                out.append(T(pair[0][1], top + bottom + 9, "X", 7.5, 600, anchor="middle"))
                out.append(T(pair[1][1], top + bottom + 9, "Y", 7.5, 600, anchor="middle"))
            else:
                out.append(T(cx, top + bottom + 9, k, 7.5, 600, anchor="middle"))
        out.append("</g>")
        top += bottom + 22
    # legend
    y = top + 2
    items = [(BLUE, "Autosomes (pairs 1–22)"), (PURPLE, "Sex chromosomes (XY shown; XX is also typical)")]
    widths = [12 + text_width(t, 7.5) for _, t in items]
    x = W / 2 - (sum(widths) + 18) / 2
    out.append('<g class="legend">')
    for (col, t), wd in zip(items, widths):
        out.append(f'<rect x="{x:.2f}" y="{y - 7:.2f}" width="7" height="8" rx="2.5" fill="{col}" fill-opacity="0.1" '
                   f'stroke="{col}" stroke-width="0.8"/>')
        out.append(T(x + 11, y, t, 7.5, 400))
        x += wd + 18
    out.append("</g>")
    H = y + 12
    out.append(copyright_text(W / 2 + 246.25, H - 2))
    svg = svg_doc(W, H, out, "Human karyotype: 22 pairs of autosomes and the sex chromosomes X and Y")
    # crop to content plus about 4 units of padding
    vb = (13.25, 3.25, 500.5, round(H + 3.2 - 3.25, 2))
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       f'width="{vb[2]:g}" height="{vb[3]:g}" viewBox="{vb[0]:g} {vb[1]:g} {vb[2]:g} {vb[3]:g}"')


if __name__ == "__main__":
    main(NAME, fig)
