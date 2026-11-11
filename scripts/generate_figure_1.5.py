"""Figure 1.5: Transformation from DNA to mRNA. The artwork comes from the Illustrator artboard in figures/data."""

import re

from figures.core import BLUE, DARK, GREEN, LBLUE, NAVY, ORANGE, PURPLE, T, main, svg_doc
from figures.artboard import inner, load_artboard

NAME = "1.5-dna-to-mrna"

NUM_RE = re.compile(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?")


def path_bbox(line):
    """Approximate bbox (page coords) of a single PyMuPDF <path> line (absolute commands)."""
    m = re.search(r'\sd="([^"]*)"', line)
    if not m:
        return None
    t = re.search(r'transform="matrix\(([^)]*)\)"', line)
    a, b, c, d, e, f = [float(v) for v in t.group(1).split(",")] if t else (1, 0, 0, 1, 0, 0)
    pts, cx, cy = [], 0.0, 0.0
    for cmd, args in re.findall(r"([MLCHVZmlchvz])([^MLCHVZmlchvz]*)", m.group(1)):
        nums = [float(v) for v in NUM_RE.findall(args)]
        if cmd in "ML":
            for i in range(0, len(nums) - 1, 2):
                cx, cy = nums[i], nums[i + 1]; pts.append((cx, cy))
        elif cmd == "C":
            for i in range(0, len(nums) - 5, 6):
                pts += [(nums[i], nums[i + 1]), (nums[i + 2], nums[i + 3])]
                cx, cy = nums[i + 4], nums[i + 5]; pts.append((cx, cy))
        elif cmd == "H":
            for v in nums:
                cx = v; pts.append((cx, cy))
        elif cmd == "V":
            for v in nums:
                cy = v; pts.append((cx, cy))
    if not pts:
        return None
    tp = [(a * x + c * y + e, b * x + d * y + f) for x, y in pts]
    xs, ys = zip(*tp)
    return min(xs), min(ys), max(xs), max(ys)


def strip_empty_groups(lines):
    txt = "\n".join(lines)
    while True:
        new = re.sub(r"<g[^>]*>\s*</g>\n?", "", txt)
        if new == txt:
            return new.split("\n")
        txt = new


def flatten(line, steps=24):
    """Polyline segments (page coords) of one artboard <path> line with absolute M/L/C/H/V/Z commands."""
    m = re.search(r'\sd="([^"]*)"', line)
    t = re.search(r'transform="matrix\(([^)]*)\)"', line)
    a, b, c, d, e, f = [float(v) for v in t.group(1).split(",")] if t else (1, 0, 0, 1, 0, 0)
    tf = lambda p: (a * p[0] + c * p[1] + e, b * p[0] + d * p[1] + f)
    segs, cur, start = [], (0.0, 0.0), (0.0, 0.0)
    for cmd, args in re.findall(r"([MLCHVZ])([^MLCHVZ]*)", m.group(1)):
        nums = [float(v) for v in NUM_RE.findall(args)]
        pts = []
        if cmd == "M":
            cur = start = (nums[0], nums[1])
            pts = [(nums[i], nums[i + 1]) for i in range(2, len(nums) - 1, 2)]
        elif cmd == "L":
            pts = [(nums[i], nums[i + 1]) for i in range(0, len(nums) - 1, 2)]
        elif cmd == "H":
            pts = [(v, cur[1]) for v in nums]
        elif cmd == "V":
            pts = [(cur[0], v) for v in nums]
        elif cmd == "Z":
            pts = [start]
        elif cmd == "C":
            for i in range(0, len(nums) - 5, 6):
                p1, p2, p3 = (nums[i], nums[i + 1]), (nums[i + 2], nums[i + 3]), (nums[i + 4], nums[i + 5])
                p0 = cur
                for s in range(1, steps + 1):
                    u = s / steps
                    q = [(1 - u) ** 3 * p0[k] + 3 * (1 - u) ** 2 * u * p1[k] + 3 * (1 - u) * u * u * p2[k] + u ** 3 * p3[k]
                         for k in (0, 1)]
                    segs.append((tf(cur), tf(q)))
                    cur = tuple(q)
                cur = p3
            continue
        for p in pts:
            segs.append((tf(cur), tf(p)))
            cur = p
    return segs


def extend_ticks(body, strand="#1874dc", reach=15.0):
    """Lengthen each nucleotide tick so its strand-side end meets the backbone, as the guide's own figures do."""
    segs = [s for l in body if l.startswith("<path") and (f'stroke="{strand}"' in l or f'fill="{strand}"' in l)
            for s in flatten(l)]
    tick_re = re.compile(r'transform="matrix\(1,0,0,-1,([-\d.]+),([-\d.]+)\)"(.*)d="M0 0V([-\d.]+)"')
    out = []
    for l in body:
        m = tick_re.search(l) if l.startswith("<path") and 'stroke-linecap="round"' in l else None
        if not m:
            out.append(l)
            continue
        x, f, ln = float(m.group(1)), float(m.group(2)), float(m.group(4))
        top, bot = sorted((f, f - ln))
        hits = []
        for (x0, y0), (x1, y1) in segs:
            if min(x0, x1) <= x <= max(x0, x1) and x0 != x1:
                hits.append(y0 + (y1 - y0) * (x - x0) / (x1 - x0))
        if any(top - 0.05 <= y <= bot + 0.05 for y in hits):
            out.append(l)
            continue
        above, below = [y for y in hits if y < top], [y for y in hits if y > bot]
        da = top - max(above) if above else float("inf")
        db = min(below) - bot if below else float("inf")
        if min(da, db) > reach:
            out.append(l)
            continue
        # Run into the strand's centre line (midway across its outline) so the strand covers the tick's end.
        if da < db:
            near = sorted(above, reverse=True)
            top = (near[0] + near[1]) / 2 if len(near) > 1 and near[0] - near[1] < 2.5 else near[0]
        else:
            near = sorted(below)
            bot = (near[0] + near[1]) / 2 if len(near) > 1 and near[1] - near[0] < 2.5 else near[0]
        out.append(l[:m.start()] + f'transform="matrix(1,0,0,-1,{x:g},{bot:.3f})"{m.group(3)}d="M0 0V{bot - top:.3f}"' + l[m.end():])
    return ticks_behind_strands(out, strand)


def ticks_behind_strands(body, strand):
    """Draw each run of ticks before the strand run it follows, so the backbone sits on top."""
    is_tick = lambda l: l.startswith("<path") and 'stroke-linecap="round"' in l
    is_strand = lambda l: l.startswith("<path") and strand in l and not is_tick(l)
    out, i = [], 0
    while i < len(body):
        if is_strand(body[i]):
            j = i
            while j < len(body) and is_strand(body[j]):
                j += 1
            k = j
            while k < len(body) and is_tick(body[k]):
                k += 1
            out += body[j:k] + body[i:j]
            i = k
        else:
            out.append(body[i])
            i += 1
    return out


CAP_AT = (134.0, 373.8)


def fig():
    svg = load_artboard("dna-to-mrna")
    defs, body = inner(svg)
    body = extend_ticks(body)
    DY, W, H = 55.2, 672.4, 442.2
    cols_dna = [(84.4, 152.6, GREEN), (182.4, 224.5, ORANGE), (252.7, 378.0, LBLUE), (439.3, 540.4, PURPLE)]
    cols_mrna = [(144.6, 211.5, GREEN), (211.5, 257.6, ORANGE), (257.6, 393.1, LBLUE), (393.1, 503.0, PURPLE)]
    rows = [(cols_dna, 71.9, 144.2), (cols_dna, 195.0, 250.0), (cols_mrna, 289.1, 346.3)]
    keep, title, boxes_at = [], None, None
    for l in body:
        if l.startswith("<path") and 'fill="#' in l:
            bb = path_bbox(l)
            if bb and bb[2] - bb[0] > 30 and bb[3] - bb[1] > 30:
                if boxes_at is None:
                    boxes_at = len(keep)
                continue
        if l.startswith("<text") and "Introns and Exons" in l:
            title = l; continue
        if l.startswith("<text") and ">Exon<" in l:
            spans = re.findall(r'<tspan y="([^"]*)" x="([^"]*)"([^>]*)>([^<]*)</tspan>', l)
            dna = [sp for sp in spans if float(sp[0]) < -290]
            out = []
            for word in ("Exon", "Intron"):
                ws = sorted([sp for sp in dna if sp[3] == word], key=lambda sp: float(sp[1]))
                for n, (y, x, rest, _) in enumerate(ws, 1):
                    out.append(f'<tspan y="{y}" x="{x}"{rest}>{word} {n}</tspan>')
            l = re.sub(r"(<text[^>]*>).*(</text>)", lambda m: m.group(1) + "".join(out) + m.group(2), l)
        if l.startswith("<text") and ">Immature<" in l:
            l = re.sub(r'<tspan y="[^"]*" x="([^"]*)"([^>]*)>Immature</tspan><tspan y="[^"]*" x="[^"]*"[^>]*>RNA</tspan>',
                       r'<tspan y="-173.65" x="\1"\2>Pre-mRNA</tspan>', l)
        if l.startswith("<text") and ">mRNA<" in l:
            l = re.sub(r'<tspan y="[^"]*" x="[^"]*"([^>]*)>mRNA</tspan>',
                       r'<tspan y="-74.2" x="25.21"\1>Mature</tspan><tspan y="-62.2" x="25.21"\1>mRNA</tspan>', l)
            l = l.replace('x="25.21" text-anchor="middle"', 'x="25.21"')
        if l in ("<g>", '<g id="layer-2">', "</svg>"):
            continue
        # the guide draws the poly-A tail in purple
        if l.startswith("<path") and GREEN in l:
            bb = path_bbox(l)
            if bb and bb[0] > 505 and bb[1] > 300 and bb[3] < 335:
                l = l.replace(GREEN, PURPLE)
        if l.startswith("<text") and 'font-size="5.4"' in l and ">A<" in l:
            l = l.replace(GREEN, PURPLE)
        keep.append(l)
    # drop the two closing </g> of the wrappers we skipped
    for _ in range(2):
        idx = max(i for i, l in enumerate(keep) if l == "</g>")
        keep.pop(idx)
    rects = ['<g id="exon-boxes">']
    for cols, y0, y1 in rows:
        for x0, x1, col in cols:
            rects.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0:.1f}" height="{y1 - y0:.1f}" fill="{col}" '
                         f'fill-opacity="0.1" stroke="{col}" stroke-width="1"/>')
    rects.append("</g>")
    # untranslated regions: hatched ends of exon 1 (5' UTR) and exon 4 (3' UTR) in every row
    hatch = []
    for col in (GREEN, PURPLE):
        hatch.append(f'<pattern id="utr-{col[1:]}" patternUnits="userSpaceOnUse" width="3.6" height="3.6" '
                     f'patternTransform="rotate(45)"><path d="M0 0V3.6" stroke="{col}" stroke-width="0.9" '
                     f'stroke-opacity="0.55"/></pattern>')
    rects.insert(0, "<defs>" + "".join(hatch) + "</defs>")
    rects.append('<g id="utrs">')
    for cols, y0, y1 in rows:
        (a0, a1, _), (b0, b1, _) = cols[0], cols[-1]
        for x0, x1, col in ((a0, a0 + (a1 - a0) / 3, GREEN), (b1 - (b1 - b0) / 3, b1, PURPLE)):
            rects.append(f'<rect x="{x0:.1f}" y="{y0}" width="{x1 - x0:.1f}" height="{y1 - y0:.1f}" '
                         f'fill="url(#utr-{col[1:]})"/>')
    rects.append("</g>")
    keep[0:0] = rects
    keep = strip_empty_groups(keep)
    out = defs[:]
    out.append(title.replace("Introns and Exons in DNA, RNA, and mRNA", "Transformation from DNA to mRNA"))
    out.append(T(315.0, 61.2, "Example gene", 13.7, 300, anchor="middle"))
    out.append('<path id="gene-brace" d="M84.4 113.5C84.4 96 94 89 118 89L282 89C300 89 310.5 82 313.4 70'
               'C316.3 82 326.8 89 344.8 89L508.8 89C532.8 89 540.4 96 540.4 113.5" fill="none" '
               'stroke="#000000" stroke-width="1.6" stroke-dasharray="3.2 2.2"/>')
    out.append(T(554.8, 335.6, "Poly-A tail", 12.7, 300, anchor="middle"))
    out.append(f'<g id="rows" transform="translate(0,{DY})">')
    out += keep
    out.append("</g>")
    # 5' cap on the front of the mature mRNA
    cx, cy = CAP_AT
    out.append(f'<g id="five-prime-cap"><path d="M{cx + 4.6:.2f} {cy:.2f}H144.6" stroke="{BLUE}" stroke-width="1.6"/>'
               f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="4.6" fill="{NAVY}"/>'
               f'<path d="M{cx:.2f} 340V{cy - 7:.2f}" stroke="{DARK}" stroke-width="0.6"/></g>')
    out.append(T(cx, 335.6, "5\u2032 cap", 12.7, 300, anchor="middle"))
    # UTR labels under the mature mRNA
    (a0, a1, _), (b0, b1, _) = cols_mrna[0], cols_mrna[-1]
    yb = 346.3 + DY
    out.append('<g id="utr-labels">')
    for x0, x1, name in ((a0, a0 + (a1 - a0) / 3, "5\u2032 UTR"), (b1 - (b1 - b0) / 3, b1, "3\u2032 UTR")):
        out.append(f'<path d="M{x0:.1f} {yb + 3}V{yb + 6}H{x1:.1f}V{yb + 3}" fill="none" stroke="{DARK}" stroke-width="0.6"/>')
        out.append(T((x0 + x1) / 2, yb + 18.5, name, 12.7, 300, anchor="middle"))
    out.append("</g>")
    # transition arrows, labelled with the molecules that do the work
    ax, MUTED = 300.0, "#4d4d4f"

    def down_arrow(y0, y1):
        return (f'<path d="M{ax} {y0}V{y1 - 5}" stroke="{MUTED}" stroke-width="1.3"/>'
                f'<path d="M{ax - 4} {y1 - 6}L{ax} {y1}L{ax + 4} {y1 - 6}Z" fill="{MUTED}"/>')
    out.append('<g id="transitions">')
    out.append(down_arrow(207, 243))
    out.append(T(ax + 10, 229.3, "RNA polymerase copies the gene", 12, 400, fill=MUTED))
    out.append(down_arrow(311, 339))
    out.append(T(ax + 10, 321.8, "Spliceosome removes introns", 12, 400, fill=MUTED))
    out.append(T(ax + 10, 335.6, "Enzymes add 5\u2032 cap and poly-A tail", 12, 400, fill=MUTED))
    out.append("</g>")
    svg = svg_doc(W, H, out, "Transformation from DNA to mRNA")
    # crop used in the guide
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       'width="647.45" height="419.97" viewBox="20.82 19.06 647.45 419.97"')


if __name__ == "__main__":
    main(NAME, fig)
