"""Figure 4.6: Coverage and depth."""

from figures.core import DARK, FAINT_BASE, GREY_LINE, LBL, MUTED, ORANGE, PURPLE, T, TEAL, big_copyright, main, svg_doc
from figures.drawing import leader

NAME = "4.6-coverage-and-depth"


def fig():
    N, L = 48, 10
    X0, CW = 66.0, 6.75
    # reads may run off either edge (clipped, as in a genome browser); depth counts only the shown region
    STARTS = [-7, -6, -5, -4, 2, 3, 4, 4, 6, 9, 10, 11, 13, 15, 16, 16, 17, 17, 32, 32, 32, 36, 36, 38, 42, 43, 43, 45, 45]
    GAP = (27, 32)                                 # positions with no reads (half-open)
    VAR, BAND, ERR = 11, 20, 43
    import random
    rnd = random.Random(5)
    depth = [sum(s <= p < s + L for s in STARTS) for p in range(N)]
    assert all(depth[p] == 0 for p in range(*GAP))
    mean = sum(depth) / N
    # pack reads into rows, leaving at least one empty position between reads in a row
    rows_end, place = [], []
    for s in sorted(STARTS):
        free = [r for r, e in enumerate(rows_end) if e + 1 < s]
        if free:
            r = rnd.choice(free[:3]); rows_end[r] = s + L - 1; place.append((s, r))
        else:
            rows_end.append(s + L - 1); place.append((s, len(rows_end) - 1))
    xc = lambda p: X0 + CW * (p + 0.5)
    YREF, RY0, RP, RH = 62.0, 76.0, 7.5, 5.0
    nrows = len(rows_end)
    yreads_end = RY0 + RP * (nrows - 1) + RH
    DB, DK = yreads_end + 58, 4.4                  # depth baseline, units per read
    yd = lambda d: DB - d * DK
    out = []
    # bands
    out.append(f'<rect class="no-reads" x="{X0 + CW * GAP[0]:.2f}" y="{RY0 - 4:.2f}" width="{CW * (GAP[1] - GAP[0]):.2f}" height="{DB - RY0 + 4:.2f}" '
               f'fill="none" stroke="{FAINT_BASE}" stroke-width="0.9" stroke-dasharray="3 2.5" rx="2"/>')
    out.append(f'<rect class="depth-band" x="{X0 + CW * BAND:.2f}" y="{YREF - 6:.2f}" width="{CW:.2f}" height="{DB - YREF + 6:.2f}" '
               f'fill="{FAINT_BASE}" fill-opacity="0.28"/>')
    # reference
    out.append(T(8, YREF + 4.5, "Reference", LBL, 600))
    out.append('<g class="reference">' + "".join(
        f'<rect x="{X0 + CW * p + 0.6:.2f}" y="{YREF - 3:.2f}" width="{CW - 1.2:.2f}" height="6" fill="{GREY_LINE}"/>' for p in range(N)) + "</g>")
    # reads
    out.append(T(8, (RY0 + yreads_end) / 2 + 4.5, "Reads", LBL, 600))
    var_reads = [(s, r) for s, r in place if s <= VAR < s + L]
    unmarked = {var_reads[2], var_reads[-2]}       # reads that carry the reference base here
    g = '<g class="reads">'
    for s, r in place:
        y = RY0 + RP * r
        a, b = max(s, 0), min(s + L, N)
        g += f'<rect x="{X0 + CW * a + 0.6:.2f}" y="{y:.2f}" width="{CW * (b - a) - 1.2:.2f}" height="{RH:g}" rx="1" fill="{TEAL}"/>'
    g += "</g>"
    out.append(g)
    m = '<g class="variant">'
    for s, r in var_reads:
        if (s, r) not in unmarked:
            m += f'<rect x="{X0 + CW * VAR + 0.6:.2f}" y="{RY0 + RP * r - 0.5:.2f}" width="{CW - 1.2:.2f}" height="{RH + 1:g}" fill="{ORANGE}"/>'
    out.append(m + "</g>")
    err_read = sorted(r for s, r in place if s <= ERR < s + L)[2]
    out.append(f'<rect class="error" x="{X0 + CW * ERR + 0.6:.2f}" y="{RY0 + RP * err_read - 0.5:.2f}" width="{CW - 1.2:.2f}" height="{RH + 1:g}" fill="{PURPLE}"/>')
    # callouts
    for p, y, text, anchor in ((VAR, 16, "Real variant: seen in many reads", "start"),
                               (BAND, 32, f"Depth = {depth[BAND]} at this base", "start"),
                               (ERR, 48, "Error: seen in one read", "end")):
        x = xc(p)
        tx = x - 3 if anchor == "start" else x + 3
        out.append(leader(x, y + 3, x, YREF - 7) + T(tx, y, text, LBL, 400, None, anchor))
    # depth track
    out.append(T(8, DB - 14, "Depth", LBL, 600))
    d = f"M{X0:.2f} {DB:.2f}"
    for p in range(N):
        d += f"V{yd(depth[p]):.2f}H{X0 + CW * (p + 1):.2f}"
    d += f"V{DB:.2f}Z"
    out.append(f'<path class="depth" d="{d}" fill="{TEAL}" fill-opacity="0.35" stroke="{TEAL}" stroke-width="1" stroke-linejoin="round"/>')
    out.append(f'<path class="axis" d="M{X0:.2f} {DB:.2f}H{X0 + CW * N:.2f}" stroke="{GREY_LINE}" stroke-width="1"/>')
    out.append(f'<path class="mean" d="M{X0:.2f} {yd(mean):.2f}H{X0 + CW * N:.2f}" stroke="{DARK}" stroke-width="1.1" stroke-dasharray="4 3"/>')
    out.append(f'<g class="mean-key"><path d="M{X0:.2f} {DB + 12:.2f}h22" stroke="{DARK}" stroke-width="1.1" stroke-dasharray="4 3"/>'
               + T(X0 + 28, DB + 16, f"Mean coverage = {round(mean)}x", LBL, 600) + "</g>")
    out.append(T(X0 + CW * (GAP[0] + GAP[1]) / 2, DB + 16, "No reads", LBL, 400, MUTED, "middle"))
    out.append(big_copyright(392, 231))
    return svg_doc(392, 234, out, "Coverage and depth: a pileup of reads over a reference with the depth at each position", origin=(4, 3))


if __name__ == "__main__":
    main(NAME, fig)
