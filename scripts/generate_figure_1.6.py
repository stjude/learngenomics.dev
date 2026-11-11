"""Figure 1.6: Starting transcription."""

import math

from figures.core import (
    BLUE, DARK, GREEN, GREY_LINE, LBLUE, ORANGE, T, TEAL, copyright_text, main, svg_doc,
)
from figures.drawing import smooth
from figures.biology import NUC_COL, nucleosome

NAME = "1.6-transcription-start"


def _catmull(pts, n=24):
    """Densely sample a Catmull-Rom spline through pts."""
    ext = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)))
    out.append(pts[-1])
    return out


def _resample(pts, ds=0.5):
    out, acc = [pts[0]], 0.0
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        seg = math.hypot(x1 - x0, y1 - y0)
        t = ds - acc
        while t <= seg:
            out.append((x0 + (x1 - x0) * t / seg, y0 + (y1 - y0) * t / seg))
            t += ds
        acc = seg - (t - ds)
    return out


def helix_along(pts, amp_at, period=20.0, ds=0.5, seed=7, sw=1.4):
    """Double helix (two crossing strands plus coloured base pairs) following a polyline.
    amp_at(s) gives the strand amplitude at arc length s; 0 draws a single linker line."""
    import random
    rnd = random.Random(seed)
    P = _resample(pts, ds)
    s1, s2, ticks = [], [], []
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    next_tick = 0.0
    for i, (x, y) in enumerate(P):
        a, b = P[max(i - 1, 0)], P[min(i + 1, len(P) - 1)]
        tx, ty = b[0] - a[0], b[1] - a[1]
        L = math.hypot(tx, ty) or 1
        nx, ny = -ty / L, tx / L
        s = i * ds
        w = amp_at(s) * math.sin(2 * math.pi * s / period)
        s1.append((x + nx * w, y + ny * w))
        s2.append((x - nx * w, y - ny * w))
        if s >= next_tick and abs(w) > 2.2:
            base = rnd.choice("ACGT")
            col = lambda c: LBLUE if c == "T" else NUC_COL[c]
            ticks.append(f'<path d="M{x + nx * w * 0.85:.2f} {y + ny * w * 0.85:.2f}L{x:.2f} {y:.2f}" stroke="{col(base)}" stroke-width="1.1"/>'
                         f'<path d="M{x:.2f} {y:.2f}L{x - nx * w * 0.85:.2f} {y - ny * w * 0.85:.2f}" stroke="{col(comp[base])}" stroke-width="1.1"/>')
            next_tick = s + 2.6
    pl = lambda q: "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in q[::2] + [q[-1]])
    return ('<g class="dna">' + "".join(ticks)
            + f'<path d="{pl(s1)}" fill="none" stroke="{BLUE}" stroke-width="{sw}" stroke-linejoin="round"/>'
            + f'<path d="{pl(s2)}" fill="none" stroke="{BLUE}" stroke-width="{sw}" stroke-linejoin="round"/></g>'), P


def blob(cx, cy, rx, ry, seed, fill, stroke, op=0.45, wob=0.1, n=7):
    import random
    rnd = random.Random(seed)
    pts = []
    for k in range(n):
        t = 2 * math.pi * k / n + rnd.uniform(-0.15, 0.15)
        f = 1 + rnd.uniform(-wob, wob)
        pts.append((cx + rx * f * math.cos(t), cy + ry * f * math.sin(t)))
    return (f'<path d="{smooth(pts, True)}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" '
            f'stroke-width="0.9" stroke-linejoin="round"/>')


def fig():
    W, H = 400.0, 262.0
    y0 = 112.0
    E0, E1 = 82.0, 136.0          # enhancer
    P0, TSS = 166.0, 226.0        # promoter, gene start
    G1 = 334.0                    # gene end
    MUTED = "#4d4d4f"
    out = []
    # region boxes (behind the DNA), labels inside along the bottom edge like 1.5's exon boxes
    for x0, x1, col, name in ((E0, E1, GREY_LINE, "Enhancer"), (P0, TSS, GREY_LINE, "Promoter"), (TSS, G1, GREEN, "Gene")):
        out.append(f'<rect x="{x0}" y="{y0 - 11}" width="{x1 - x0:g}" height="31" fill="{col}" fill-opacity="0.12" '
                   f'stroke="{col}" stroke-width="1"/>')
    # DNA: linker + nucleosomes, bare helix through the regulatory region, the loop hanging below the neck
    nx = E1 + (P0 - E1) / 2
    path = [(4, y0), (40, y0), (E0 - 4, y0), (E1 - 4, y0), (E1 + 3, y0 + 9), (nx - 14, y0 + 40),
            (nx - 46, y0 + 70), (nx - 36, y0 + 108), (nx, y0 + 120), (nx + 36, y0 + 108), (nx + 46, y0 + 70),
            (nx + 14, y0 + 40), (P0 - 3, y0 + 9), (P0 + 4, y0), (TSS, y0), (G1, y0), (W - 4, y0)]
    dense = _catmull(path)
    total = len(_resample(dense)) * 0.5
    ramp = lambda s, a, b: max(0.0, min(1.0, (s - a) / 8, (b - s) / 8))
    GN = 302.0                    # active genes keep nucleosomes (as in 1.3); only the promoter is bare
    s_gn = total - (W - 4 - GN)
    amp = lambda s: 5.0 * min(ramp(s, 66, total - (W - 4 - (G1 + 6))), 1 - ramp(s, s_gn - 16, s_gn + 16))
    dna, _ = helix_along(dense, amp, period=30.0)
    out.append(dna)
    out.append('<g class="nucleosomes">' + "".join(nucleosome(x, y0, 8.5) for x in (20, 48))
               + "".join(nucleosome(x, y0, 8.5) for x in (GN, 356, 384)) + "</g>")
    for x0, x1, col, name in ((E0, E1, GREY_LINE, "Enhancer"), (P0, TSS, GREY_LINE, "Promoter"), (TSS, G1, GREEN, "Gene")):
        out.append(T((x0 + x1) / 2, y0 + 16.5, name, 8, 700 if name == "Gene" else 600,
                     fill=GREEN if name == "Gene" else None, anchor="middle"))
    # proteins: transcription factors (orange) on enhancer and promoter, meeting above the loop's neck
    tfs = [(E0 + 18, y0 - 12.5, 8.5, 8, 1), (E1 - 6, y0 - 12.5, 9, 8, 2), (nx - 8.5, y0 - 25.5, 8.5, 8, 3),
           (nx + 8.5, y0 - 25.5, 8.5, 8, 4), (P0 + 6, y0 - 12.5, 9, 8, 5), (P0 + 22, y0 - 12.5, 8.5, 8, 6)]
    out.append('<g class="transcription-factors">' + "".join(blob(x, y, rx, ry, s, ORANGE, ORANGE, 0.5, 0.05, 6) for x, y, rx, ry, s in tfs) + "</g>")
    pol = (TSS - 17, y0 - 15)
    out.append('<g class="rna-polymerase">' + blob(pol[0], pol[1], 20, 16, 11, TEAL, TEAL, 0.35, 0.02, 6) + "</g>")
    # transcription start: bent arrow at the gene start
    ay = y0 - 44
    out.append(f'<g class="tss"><path d="M{TSS} {y0 - 11}V{ay}H{TSS + 16}" fill="none" stroke="{DARK}" stroke-width="1.4"/>'
               f'<path d="M{TSS + 15} {ay - 4}L{TSS + 22} {ay}L{TSS + 15} {ay + 4}Z" fill="{DARK}"/></g>')
    out.append(T(TSS + 26, ay + 2.8, "Transcription start", 8, 600))
    # leader labels
    out.append('<g class="labels">')
    ly = 46.0
    tfx = 104.0
    out.append(f'<path d="M{tfx} {ly + 3}L{E0 + 17} {y0 - 20.5}M{tfx} {ly + 3}L{nx - 9} {y0 - 33}M{tfx} {ly + 3}L{nx + 8} {y0 - 33}" '
               f'fill="none" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(tfx, ly, "Transcription factors", 8, 600, anchor="middle"))
    out.append(f'<path d="M{pol[0]} {pol[1] - 17}V{ly + 3}" stroke="{DARK}" stroke-width="0.6"/>')
    out.append(T(pol[0] + 2, ly, "RNA polymerase", 8, 600, anchor="middle"))
    out.append("</g>")
    out.append(T(8, 18, "Starting transcription", 10, 700))
    # loop annotation
    out.append(T(nx + 60, y0 + 80, "The DNA in between loops out,", 7.5, 400, fill=MUTED))
    out.append(T(nx + 60, y0 + 90, "bringing the enhancer to the promoter", 7.5, 400, fill=MUTED))
    out.append(copyright_text(W - 4, H - 6))
    svg = svg_doc(W, H, out, "Starting transcription: transcription factors on an enhancer reach the promoter through a DNA loop")
    # crop to content plus about 4 units of padding
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       'width="400" height="254.5" viewBox="0 6.8 400 254.5"')


if __name__ == "__main__":
    main(NAME, fig)
