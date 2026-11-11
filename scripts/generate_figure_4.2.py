"""Figure 4.2: Paired-end reads."""

from figures.core import DARK, GREEN, GREY_LINE, LBL, MUTED, SANS, T, big_copyright, esc, main, svg_doc
from figures.drawing import leader
from figures.reads import ADP_C, INS_C, PE_DEFS, R1_C, R2_C, pe_fragment, pe_read

NAME = "4.2-paired-end-reads"

OVL_C = GREEN


def fig():
    X0, K, AD, RL = 12.0, 0.6, 60, 150           # left edge, units per base, adapter bases, read length
    out = [PE_DEFS]
    # key
    ky = 20.0
    out.append('<g class="key">' + pe_read(X0, X0 + 26, ky, R1_C) + T(X0 + 32, ky + 4.5, "Read 1", LBL)
               + pe_read(124, 98, ky, R2_C) + T(130, ky + 4.5, "Read 2", LBL)
               + f'<rect x="196" y="{ky - 4:.2f}" width="22" height="8" fill="{ADP_C}"/>' + T(224, ky + 4.5, "Adapter", LBL)
               + f'<rect x="290" y="{ky - 4:.2f}" width="22" height="8" fill="{INS_C}"/>' + T(318, ky + 4.5, "Insert", LBL) + "</g>")
    xr = X0 + AD * K                              # read 1 start (all rows)
    xg = xr + RL * K
    yg0 = 58.0
    out.append(f'<g class="read-length"><path d="M{xr:.2f} {yg0:.2f}H{xg:.2f}M{xr:.2f} {yg0 - 4:.2f}V{yg0 + 4:.2f}" stroke="{DARK}" stroke-width="1"/>'
               + T((xr + xg) / 2, yg0 - 7, "150 bases", LBL, 600, None, "middle") + "</g>")
    rows = [("Long fragment", "500-base insert", 500), ("Medium fragment", "250-base insert", 250), ("Short fragment", "100-base insert", 100)]
    RY = [92.0, 178.0, 264.0]
    gd = f"M{xg:.2f} {yg0 - 4:.2f}V{RY[0] - 16:.2f}" + "".join(f"M{xg:.2f} {y + 8:.2f}V{y + 58:.2f}" for y in RY)
    out.append(f'<path class="guide" d="{gd}" stroke="{DARK}" stroke-width="1" stroke-dasharray="3 3"/>')
    for (name, sub, ins), y0 in zip(rows, RY):
        y1, yb, y2 = y0 + 18, y0 + 33, y0 + 48
        xi1 = X0 + (AD + ins) * K                  # right adapter starts
        r2e = xi1 - RL * K
        g = '<g class="pair">'
        g += (f'<text x="{X0:.2f}" y="{y0:.2f}" font-family="{SANS}" font-size="{LBL:g}" font-weight="700">{esc(name)}'
              f'<tspan dx="6" font-weight="400" fill="{MUTED}">{esc(sub)}</tspan></text>')
        if ins == 250:
            g += (f'<rect class="overlap" x="{r2e:.2f}" y="{y1 - 7:.2f}" width="{xg - r2e:.2f}" height="{y2 - y1 + 14:.2f}" rx="2" '
                  f'fill="{OVL_C}" fill-opacity="0.3" stroke="{OVL_C}" stroke-width="1"/>')
        g += pe_fragment(X0, AD * K, ins * K, yb)
        g += pe_read(xr, xg, y1, R1_C, hatch=(xi1, xg) if xg > xi1 else None)
        g += pe_read(xi1, r2e, y2, R2_C, hatch=(r2e, xr) if r2e < xr else None)
        if ins == 500:
            g += (f'<path class="gap" d="M{xg + 3:.2f} {y2 - 4:.2f}v4H{r2e - 3:.2f}v-4" fill="none" stroke="{GREY_LINE}" stroke-width="1"/>'
                  + T((xg + r2e) / 2, y2 + 14, "Unread gap", LBL, 400, MUTED, "middle"))
        elif ins == 250:
            g += leader(xg + 1, y1 - 7, xi1 + AD * K + 18, y1 - 7) + T(xi1 + AD * K + 22, y1 - 2.5, "Overlap", LBL, 400, MUTED)
        else:
            tx = xi1 + AD * K + 22
            g += (leader(xg + 2, y1, tx - 4, yb - 4)
                  + T(tx, yb - 3, "Both reads run into", LBL, 400, MUTED) + T(tx, yb + 11, "the adapter (hatched)", LBL, 400, MUTED))
        out.append(g + "</g>")
    out.append(big_copyright(392, 335))
    return svg_doc(392, 335, out, "Paired-end reads: the reads stay the same length while the fragments vary", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
