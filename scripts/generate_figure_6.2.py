"""Figure 6.2: Binning, one set of bins per chromosome."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, PURPLE, T, main, svg_doc

NAME = "6.2-index-bins"

X0, X1, KB = 8.0, 392.0, 144.0
px = lambda kb: X0 + kb / KB * (X1 - X0)
RH, RG = 36.0, 10.0
LEVELS = [[(0, 0, 144)], [(1, 0, 48), (2, 48, 96), (3, 96, 144)],
          [(4 + k, 16 * k, 16 * k + 16) for k in range(9)]]
RECS = [("C", 40, 49, 0), ("B", 51, 70, 1), ("A", 65, 67, 2), ("D", 95, 98, 0)]
Q0, Q1 = 65, 71
HIT = {0, 2, 8}
LIN = ["\u2013", "\u2013", "C", "C", "B", "D", "D", "\u2013", "\u2013"]
TROWS = [(0, "C", "40\u201349", "before B, skipped"), (2, "B", "51\u201370", "overlaps, kept"), (8, "A", "65\u201367", "overlaps, kept"), (0, "D", "95\u201398", "past 71 kb, stop")]


def fig():
    W = 400.0
    out = []
    y = 20.0
    out.append(T(X0, y, "Each record goes in the smallest bin that holds it whole", 13, 700))
    out.append(T(X0, y + 17, "Each bin splits into three smaller bins", 11, 400, MUTED))
    yt0 = y + 34
    TW, TGAP, TBH = 46.0, 4.0, 20.0
    for k, lab in enumerate(["chr1", "chr2", "chr3", "\u2026"]):
        tx = X0 + k * (TW + TGAP)
        on = k == 0
        out.append(f'<rect class="tab" x="{tx:.2f}" y="{yt0:.2f}" width="{TW:g}" height="{TBH:g}" rx="3" fill="{BLUE if on else GREY_LINE}" fill-opacity="{0.12 if on else 0.07}" stroke="{BLUE if on else GREY_LINE}" stroke-width="{1.4 if on else 1}"/>')
        out.append(T(tx + TW / 2, yt0 + 14, lab, 11, 700 if on else 500, BLUE if on else MUTED, "middle", mono=True))
    out.append(T(X1, yt0 + 14, "one set of bins per chromosome", 11, 400, MUTED, "end"))
    y0 = yt0 + TBH + 12
    ybot = y0 + 3 * RH + 2 * RG
    out.append(f'<rect class="want" x="{px(Q0):.2f}" y="{y0 - 6:.2f}" width="{px(Q1) - px(Q0):.2f}" height="{ybot - y0 + 12:.2f}" fill="{BLUE}" fill-opacity="0.12"/>')
    for lv, bins in enumerate(LEVELS):
        ry = y0 + lv * (RH + RG)
        for b, s, e in bins:
            x0, x1 = px(s) + 1.5, px(e) - 1.5
            hit = b in HIT
            st = f'stroke="{BLUE}" stroke-width="1.4"' if hit else f'stroke="{GREY_LINE}" stroke-width="1"'
            fo = 0.0 if hit else 0.07
            out.append(f'<rect class="bin" x="{x0:.2f}" y="{ry:.2f}" width="{x1 - x0:.2f}" height="{RH:g}" rx="3" fill="{GREY_LINE}" fill-opacity="{fo}" {st}/>')
            out.append(T(x0 + 5, ry + 13, str(b), 10.5, 700 if hit else 500, BLUE if hit else MUTED))
            if lv < 2:
                step = (e - s) / 3
                for k in (1, 2):
                    xt = px(s + k * step)
                    out.append(f'<path d="M{xt:.2f} {ry + 17:.2f}V{ry + RH - 3:.2f}" stroke="{GREY_LINE}" stroke-width="0.8" stroke-dasharray="2 2"/>')
    for name, s, e, lv in RECS:
        ry = y0 + lv * (RH + RG)
        out.append(f'<rect class="read" x="{px(s):.2f}" y="{ry + 21:.2f}" width="{px(e) - px(s):.2f}" height="7" rx="1.5" fill="{PURPLE}" fill-opacity="0.75"/>')
        out.append(T(px(e) + 4, ry + 28.5, name, 11.5, 700, DARK, mono=True))
    ya = ybot + 8
    out.append(f'<path d="M{X0:.2f} {ya:.2f}H{X1:.2f}" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    for kb, lab, anc in ((0, "0", "start"), (48, "48 kb", "middle"), (96, "96 kb", "middle"), (144, "144 kb", "end")):
        out.append(f'<path d="M{px(kb):.2f} {ya:.2f}v4" stroke="{GREY_LINE}" stroke-width="0.8"/>')
        out.append(T(px(kb), ya + 16, lab, 10.5, 400, MUTED, anc))
    out.append(T((px(Q0) + px(Q1)) / 2, ya + 16, "", 10.5))
    yq = ya + 32
    out.append(T((px(Q0) + px(Q1)) / 2, yq, "wanted: 65\u201371 kb", 11, 600, BLUE, "middle"))

    yl = yq + 32
    out.append(T(X0, yl, "Linear index", 12, 700))
    out.append(T(X0, yl + 16, "First record in the file for each 16 kb window", 11, 400, MUTED))
    out.append(T(X1, yl, "file order: C, B, A, D", 11, 400, MUTED, "end"))
    yc = yl + 26
    LH = 24.0
    for k, lab in enumerate(LIN):
        x0, x1 = px(16 * k) + 1.5, px(16 * k + 16) - 1.5
        on = k == 4
        st = f'stroke="{BLUE}" stroke-width="1.4"' if on else f'stroke="{GREY_LINE}" stroke-width="1"'
        out.append(f'<rect class="win" x="{x0:.2f}" y="{yc:.2f}" width="{x1 - x0:.2f}" height="{LH:g}" rx="3" fill="{BLUE if on else GREY_LINE}" fill-opacity="{0.12 if on else 0.07}" {st}/>')
        out.append(T((x0 + x1) / 2, yc + 16, lab, 11.5, 700 if lab != "\u2013" else 400, BLUE if on else (DARK if lab != "\u2013" else MUTED), "middle", mono=True))
    yq = yc + LH

    y = yq + 26
    out.append(f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y += 26
    out.append(T(X0, y, "Looking up chr1, 65\u201371 kb", 13, 700))
    out.append(T(X0, y + 17, "Start reading at B; stop at the first record past 71 kb", 11, 400, MUTED))
    yh = y + 42
    XB, XR, XS, XO = 16, 74, 100, 200
    out.append(T(XB, yh, "Bin", 11, 600, MUTED) + T(XR, yh, "Record", 11, 600, MUTED)
               + T(XO, yh, "Result", 11, 600, MUTED))
    yt = yh + 8
    TH = 24.0
    for k, (b, r, span, kept) in enumerate(TROWS):
        ry = yt + k * TH
        cy = ry + TH / 2 + LBL * 0.36
        out.append(f'<rect class="row" x="8" y="{ry + 1:.2f}" width="384" height="{TH - 2:g}" rx="3" fill="{GREY_LINE}" fill-opacity="{0.07 if k % 2 == 0 else 0}"/>')
        out.append(T(XB, cy, str(b), LBL, 700, BLUE, mono=True))
        out.append(T(XR, cy, r, LBL, 700, DARK, mono=True))
        out.append(T(XS, cy, f"{span} kb", 11.5, 400, MUTED))
        out.append(T(XO, cy, kept, LBL, 700 if kept.endswith("kept") else 400, BLUE if kept.endswith("kept") else MUTED))
    H = yt + len(TROWS) * TH + 36
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Binning, one set of bins per chromosome: each record goes in the smallest bin that holds it; a lookup checks every bin that overlaps the wanted stretch, its linear index lets it skip records before the first one that overlaps, and it stops at the first record past the stretch", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
