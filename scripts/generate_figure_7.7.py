"""Figure 7.7: How a microRNA is made and how it finds its target."""

from figures.core import COPYRIGHT, DARK, FAINT_BASE, GREY_LINE, LBL, MUTED, NAVY, ORANGE, T, TEAL, main, svg_doc

NAME = "7.7-microrna-path"

K = 5.5                    # px per nucleotide along the stem
GAP = 14                   # distance between the two strands of the stem
TOP0 = 120.0               # 5' end of the microRNA (Drosha cut on the top strand)
TOP1 = TOP0 + 22 * K       # 3' end of the microRNA (Dicer cut on the top strand)
BOT0, BOT1 = TOP0 - 2 * K, TOP1 - 2 * K   # the other strand, offset by the 2-nt 3' overhangs
STEM_END = 262.0           # where the terminal loop starts
FORK = 62.0                # where the single-stranded flanks meet the stem
RNA = FAINT_BASE
MIR16 = "UAGCAGCACGUAAAUAUUGGCG"   # hsa-miR-16-5p, from the MIR16-1 precursor (GRCh38 chr13)
COMP = {"A": "U", "U": "A", "G": "C", "C": "G"}


def line(x0, x1, y, col, w=3.5):
    return f'<path d="M{x0:.2f} {y:.2f}H{x1:.2f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'


def rungs(x0, x1, y):
    out, x = [], x0 + 3
    while x < x1 - 1:
        out.append(f'M{x:.2f} {y + 3:.2f}V{y + GAP - 3:.2f}')
        x += K * 1.6
    return f'<path class="base-pairs" d="{"".join(out)}" stroke="{GREY_LINE}" stroke-width="0.8" stroke-opacity="0.6"/>'


def loop(y):
    r = GAP / 2 + 6
    return (f'<path d="M{STEM_END:.2f} {y:.2f}A{r:.2f} {r:.2f} 0 1 1 {STEM_END:.2f} {y + GAP:.2f}" fill="none" '
            f'stroke="{RNA}" stroke-width="3.5" stroke-linecap="round"/>')


def stem(y, flanks):
    """The hairpin; the microRNA on the top strand and its partner on the bottom strand."""
    out = []
    if flanks:
        out.append(f'<path d="M14 {y - 26:.2f}C40 {y - 26:.2f} 44 {y:.2f} {FORK:.2f} {y:.2f}H{TOP0:.2f}" fill="none" '
                   f'stroke="{RNA}" stroke-width="3.5" stroke-linecap="round"/>')
        out.append(f'<path d="M14 {y + GAP + 26:.2f}C40 {y + GAP + 26:.2f} 44 {y + GAP:.2f} {FORK:.2f} {y + GAP:.2f}H{BOT0:.2f}" '
                   f'fill="none" stroke="{RNA}" stroke-width="3.5" stroke-linecap="round"/>')
        out.append(rungs(FORK, STEM_END, y))
    else:
        out.append(rungs(TOP0, STEM_END, y))
    out.append(line(TOP1, STEM_END, y, RNA) + line(BOT1, STEM_END, y + GAP, RNA) + loop(y))
    out.append(line(TOP0, TOP1, y, TEAL) + line(BOT0, BOT1, y + GAP, ORANGE))
    return "".join(out)


def ends(y, x5, x3):
    """5' and 3' labels for the top strand (left to right) and the bottom strand (right to left)."""
    return (T(x5 - 7, y + 4, "5\u2032", 10, 400, MUTED, "end") + T(x3 - 7, y + GAP + 4, "3\u2032", 10, 400, MUTED, "end"))


def cut(xt, xb, y, name, lx):
    """A staggered cut through both strands and the enzyme that makes it."""
    d = (f'M{xt:.2f} {y - 8:.2f}V{y + GAP / 2:.2f}H{xb:.2f}V{y + GAP + 8:.2f}')
    w = 14 + 7.2 * len(name)
    return (f'<path class="cut" d="{d}" fill="none" stroke="{DARK}" stroke-width="1.3" stroke-dasharray="3 2"/>'
            f'<rect class="enzyme" x="{lx - w / 2:.2f}" y="{y - 33:.2f}" width="{w:.2f}" height="20" rx="10" '
            f'fill="{NAVY}" fill-opacity="0.09" stroke="{NAVY}" stroke-opacity="0.45" stroke-width="1"/>'
            + T(lx, y - 19, name, LBL, 600, DARK, "middle")
            + f'<path d="M{lx:.2f} {y - 13:.2f}L{xt:.2f} {y - 8:.2f}" stroke="{NAVY}" stroke-opacity="0.45" stroke-width="1"/>')


def argonaute(cx, cy, rx, ry):
    return (f'<ellipse class="argonaute" cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" fill="{NAVY}" '
            f'fill-opacity="0.09" stroke="{NAVY}" stroke-opacity="0.45" stroke-width="1"/>')


def divider(y):
    return f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>'


def fig():
    out = []
    # ---- 1
    out.append(T(8, 20, "1. In the nucleus, Drosha cuts the hairpin free", LBL, 700))
    y1 = 82
    out.append(stem(y1, flanks=True))
    out.append(cut(TOP0, BOT0, y1, "Drosha", 86))
    out.append(T(290, y1 + 11, "loop", LBL, 400, MUTED))
    # ---- 2
    y = y1 + GAP + 52
    out.append(divider(y - 18))
    out.append(T(8, y, "2. In the cytoplasm, Dicer cuts off the loop", LBL, 700))
    y2 = y + 50
    out.append(stem(y2, flanks=False))
    out.append(ends(y2, TOP0, BOT0))
    out.append(cut(TOP1, BOT1, y2, "Dicer", 300))
    # ---- 3
    y = y2 + GAP + 44
    out.append(divider(y - 18))
    out.append(T(8, y, "3. Argonaute keeps one strand", LBL, 700))
    y3 = y + 40
    out.append(argonaute((TOP0 + TOP1) / 2, y3 + 2, 82, 22))
    out.append(T(TOP0 - 30, y3 + 5, "Argonaute", LBL, 600, DARK, "end"))
    out.append(line(TOP0, TOP1, y3, TEAL))
    # the other strand, broken into pieces
    xs = BOT0 + 168
    pieces = [(0, 0, 18, -8), (24, 6, 14, 10), (44, -4, 16, -14), (66, 4, 10, 6)]
    for dx, dy, ln, rot in pieces:
        x, yy = xs + dx, y3 + 16 + dy
        out.append(f'<path d="M{x:.2f} {yy:.2f}h{ln:.2f}" stroke="{ORANGE}" stroke-width="3.5" stroke-linecap="round" '
                   f'stroke-opacity="0.75" transform="rotate({rot} {x + ln / 2:.2f} {yy:.2f})"/>')
    out.append(T(xs + 38, y3 - 8, "broken down", LBL, 400, MUTED, "middle"))
    # ---- 4
    y = y3 + 24 + 40
    out.append(divider(y - 18))
    out.append(T(8, y, "4. The seed pairs with a site in an mRNA", LBL, 700))
    ym = y + 44
    # mRNA: cap, coding sequence, 3' UTR, poly-A tail
    cds0, cds1, utr1 = 44, 176, 340
    out.append(f'<g class="mrna">'
               f'<circle cx="22" cy="{ym:.2f}" r="4.2" fill="{NAVY}"/>' + line(26, utr1, ym, RNA, 2.2)
               + f'<rect x="{cds0}" y="{ym - 7:.2f}" width="{cds1 - cds0}" height="14" rx="3" fill="{RNA}" fill-opacity="0.35" '
               f'stroke="{RNA}" stroke-width="1"/>'
               + T(utr1 + 4, ym + 4, "AAAA", 10.5, 600, MUTED) + "</g>")
    out.append(T((cds0 + cds1) / 2, ym + 24, "coding sequence", LBL, 400, MUTED, "middle"))
    out.append(f'<path d="M{cds1 + 2:.2f} {ym - 8:.2f}V{ym - 13:.2f}H{utr1 - 2:.2f}V{ym - 8:.2f}" fill="none" '
               f'stroke="{GREY_LINE}" stroke-width="0.8"/>')
    out.append(T((cds1 + utr1) / 2, ym - 19, "3\u2032 UTR", LBL, 400, MUTED, "middle"))
    ax = 262
    out.append(argonaute(ax, ym + 13, 44, 13))
    out.append(line(ax - 34, ax + 34, ym + 9, TEAL, 3))
    out.append('<path d="' + "".join(f'M{ax + d:.2f} {ym + 2:.2f}V{ym + 7:.2f}' for d in (14, 18.5, 23, 27.5))
               + f'" stroke="{GREY_LINE}" stroke-width="0.9"/>')
    # letter-level view of the site
    ys = ym + 70
    step = 11.0
    x0 = 118.0
    mir = MIR16[::-1]                       # written 3' to 5' so it lines up with the mRNA
    seed = [i for i in range(22) if 2 <= 22 - i <= 7]
    out.append(f'<path d="M{ax - 40:.2f} {ym + 20:.2f}L{x0 - 8:.2f} {ys - 26:.2f}'
               f'M{ax + 40:.2f} {ym + 20:.2f}L{x0 + 21 * step + 8:.2f} {ys - 26:.2f}" stroke="{GREY_LINE}" '
               f'stroke-width="0.6" stroke-dasharray="2 2"/>')
    sx0, sx1 = x0 + seed[0] * step - 5.5, x0 + seed[-1] * step + 5.5
    out.append(f'<rect class="seed" x="{sx0:.2f}" y="{ys - 22:.2f}" width="{sx1 - sx0:.2f}" height="50" rx="4" '
               f'fill="{TEAL}" fill-opacity="0.12"/>')
    out.append(T(8, ys - 8, "mRNA", LBL, 600, DARK) + T(8, ys + 22, "miR-16", LBL, 600, DARK))
    for i, b in enumerate(mir):
        x = x0 + i * step
        if i in seed:
            out.append(T(x, ys - 8, COMP[b], LBL, 600, DARK, "middle", mono=True))
            out.append(f'<path d="M{x:.2f} {ys - 3:.2f}V{ys + 8:.2f}" stroke="{GREY_LINE}" stroke-width="1"/>')
        elif seed[0] - 3 <= i <= seed[-1] + 1:
            out.append(T(x, ys - 8, "\u00b7", LBL, 600, MUTED, "middle", mono=True))
        out.append(T(x, ys + 22, b, LBL, 600 if i in seed else 400, DARK if i in seed else MUTED, "middle", mono=True))
    out.append(T(x0 + (seed[0] - 3) * step - 10, ys - 8, "5\u2032", 10, 400, MUTED, "end"))
    out.append(T(x0 + (seed[-1] + 1) * step + 10, ys - 8, "3\u2032", 10, 400, MUTED))
    out.append(T(x0 - 10, ys + 22, "3\u2032", 10, 400, MUTED, "end"))
    out.append(T(x0 + 21 * step + 10, ys + 22, "5\u2032", 10, 400, MUTED))
    out.append(T((sx0 + sx1) / 2, ys + 44, "seed", LBL, 600, DARK, "middle"))
    # ---- key
    y = ys + 76
    out.append(divider(y - 18))
    k1, k2 = 20, 210
    out.append(line(k1, k1 + 14, y - 4, TEAL) + T(k1 + 22, y + 0.5, "microRNA", LBL, 400, MUTED))
    out.append(line(k2, k2 + 14, y - 4, ORANGE) + T(k2 + 22, y + 0.5, "its partner strand", LBL, 400, MUTED))
    y += 26
    out.append(line(k1, k1 + 14, y - 4, RNA) + T(k1 + 22, y + 0.5, "rest of the RNA", LBL, 400, MUTED))
    out.append(f'<rect x="{k2:.2f}" y="{y - 12:.2f}" width="16" height="14" rx="7" fill="{NAVY}" fill-opacity="0.09" '
               f'stroke="{NAVY}" stroke-opacity="0.45" stroke-width="1"/>' + T(k2 + 22, y + 0.5, "protein", LBL, 400, MUTED))
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(392, H - 7, out, "How a microRNA is made: Drosha and Dicer cut it from a hairpin, Argonaute keeps one strand, "
                   "and its seed pairs with a site in an mRNA", origin=(4, 7))


if __name__ == "__main__":
    main(NAME, fig)
