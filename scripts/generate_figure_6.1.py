"""Figure 6.1: Gzip versus BGZF."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, T, main, svg_doc

NAME = "6.1-gzip-vs-bgzf"

X0, X1 = 8.0, 392.0
NB, GAP = 6, 4.0
BW = (X1 - X0 - GAP * (NB - 1)) / NB
BH = 30.0
WANT = 3
RH = 22.0
INDEX = [("1", "2,400"), ("2,401", "4,900"), ("4,901", "7,300"),
         ("7,301", "9,800"), ("9,801", "12,200"), ("12,201", "14,700")]
bx = lambda k: X0 + k * (BW + GAP)
WX0 = bx(WANT) + BW * 0.28
WX1 = bx(WANT) + BW * 0.42


def arrow_down(x, y0, y1, col=DARK):
    return (f'<path d="M{x:.2f} {y0:.2f}V{y1 - 8:.2f}" stroke="{col}" stroke-width="1.8"/>'
            f'<path d="M{x - 5.5:.2f} {y1 - 10:.2f}L{x:.2f} {y1:.2f}L{x + 5.5:.2f} {y1 - 10:.2f}Z" fill="{col}"/>')


def bracket(x0, x1, y, label, col):
    return (f'<path d="M{x0:.2f} {y - 5:.2f}V{y:.2f}H{x1:.2f}V{y - 5:.2f}" fill="none" stroke="{col}" stroke-width="1.4"/>'
            + T((x0 + x1) / 2, y + 16, label, 11, 600, col, "middle"))


def wanted(y):
    return f'<rect class="want" x="{WX0:.2f}" y="{y + 4:.2f}" width="{WX1 - WX0:.2f}" height="{BH - 8:g}" rx="1.5" fill="{BLUE}" fill-opacity="0.75"/>'


def fig():
    W = 400.0
    out = []
    y = 20.0
    out.append(T(X0, y, "Wanted: the records for positions 8,000 to 8,200", 13, 700))

    y += 34
    out.append(T(X0, y, "Gzip: one long stream", 13, 700))
    out.append(T(X0, y + 17, "Everything before the wanted records is decompressed too", 11, 400, MUTED))
    yb = y + 32
    out.append(f'<rect class="file" x="{X0:.2f}" y="{yb:.2f}" width="{X1 - X0:g}" height="{BH:g}" rx="3" fill="none" stroke="{GREY_LINE}" stroke-width="1"/>')
    out.append(f'<rect class="read" x="{X0 + 0.5:.2f}" y="{yb + 0.5:.2f}" width="{WX1 - X0 - 0.5:.2f}" height="{BH - 1:g}" rx="2.5" fill="{BLUE}" fill-opacity="0.18"/>')
    out.append(wanted(yb))
    out.append(bracket(X0, WX1, yb + BH + 8, "decompressed", BLUE))

    y = yb + BH + 62
    out.append(T(X0, y, "BGZF: many small blocks, plus an index", 13, 700))
    out.append(T(X0, y + 17, "The index says which block to open; only that block is decompressed", 11, 400, MUTED))
    yh = y + 42
    out.append(T(X0 + 8, yh, "Index", 11, 600, MUTED) + T(150, yh, "Positions", 11, 600, MUTED, "end")
               + T(208, yh, "Block", 11, 600, MUTED, "middle"))
    ytab = yh + 8
    for k, (a, b) in enumerate(INDEX):
        ry = ytab + k * RH
        hit = k == WANT
        fill = f'fill="{BLUE}" fill-opacity="0.18"' if hit else f'fill="{GREY_LINE}" fill-opacity="{0.07 if k % 2 == 0 else 0}"'
        out.append(f'<rect class="row" x="{X0:.2f}" y="{ry + 1:.2f}" width="226" height="{RH - 2:g}" rx="3" {fill}/>')
        cy = ry + RH / 2 + LBL * 0.36
        col = DARK
        out.append(T(150, cy, f"{a}\u2013{b}", 11.5, 600 if hit else 500, col, "end", mono=True))
        out.append(T(208, cy, str(k + 1), 11.5, 700 if hit else 500, col, "middle", mono=True))
    hy = ytab + WANT * RH + RH / 2
    out.append(T(244, hy + LBL * 0.36, "8,000 falls here", 11, 600, BLUE))
    yb = ytab + NB * RH + 34
    xa = bx(WANT) + BW / 2
    out.append(f'<path d="M234 {hy:.2f}H{xa + 60:.2f}" stroke="none"/>')
    out.append(arrow_down(xa, ytab + NB * RH + 6, yb - 2, BLUE))
    for k in range(NB):
        x = bx(k)
        if k == WANT:
            out.append(f'<rect class="read" x="{x:.2f}" y="{yb:.2f}" width="{BW:.2f}" height="{BH:g}" rx="3" fill="{BLUE}" fill-opacity="0.18" stroke="{BLUE}" stroke-width="1.2"/>')
            out.append(wanted(yb))
        else:
            out.append(f'<rect class="block" x="{x:.2f}" y="{yb:.2f}" width="{BW:.2f}" height="{BH:g}" rx="3" fill="{GREY_LINE}" fill-opacity="0.07" stroke="{GREY_LINE}" stroke-width="1"/>')
            out.append(T(x + BW / 2, yb + BH / 2 + 4, f"Block {k + 1}", 11, 500, MUTED, "middle"))
    out.append(bracket(bx(WANT), bx(WANT) + BW, yb + BH + 8, "decompressed", BLUE))
    out.append(T(X0, yb + BH + 24, "skipped", 11, 600, MUTED))
    out.append(T(X1, yb + BH + 24, "skipped", 11, 600, MUTED, "end"))
    H = yb + BH + 60
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Gzip versus BGZF: to reach records in the middle of a gzip file, everything before them is decompressed; with BGZF, the index points to the one block that holds them", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
