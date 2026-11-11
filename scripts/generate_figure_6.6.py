"""Figure 6.6: The same four bases counted two ways."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, T, main, svg_doc
from figures.sequences import seq_grid_row

NAME = "6.6-bed-files"

SEQ = "ACGTTGCAAC"
A, B = 2, 6                       # highlighted bases: indices 2..5, BED 2 6, 1-based 3-6
CW = 32.0
X0 = (400.0 - CW * len(SEQ)) / 2


def num(x, y, s, on):
    return T(x, y, s, 11, 700 if on else 400, BLUE if on else MUTED, "middle", mono=True)


def fig():
    W = 400.0
    out = []
    out.append(T(8, 20, "Two ways to count the same bases", 13, 700))
    out.append(T(8, 37, "Both name the four highlighted bases on chr1", 11, 400, MUTED))

    # 1-based: numbers sit on the bases
    out.append(T(X0, 66, "In-base: SAM, VCF and samtools number the bases", 11, 600, DARK))
    yb = 104.0
    for i in range(len(SEQ)):
        cx = X0 + CW * (i + 0.5)
        out.append(num(cx, 84, str(i + 1), A <= i < B))
    out.append(seq_grid_row(X0, CW, yb, SEQ, {i: BLUE for i in range(A, B)}, size=13, ch=26.0))

    # 0-based: numbers sit on the gaps between bases
    yt0, yt1 = yb + 15, yb + 23
    for i in range(len(SEQ) + 1):
        x = X0 + CW * i
        on = i in (A, B)
        out.append(f'<path d="M{x:.2f} {yt0:.2f}V{yt1:.2f}" stroke="{BLUE if on else GREY_LINE}" stroke-width="{1.4 if on else 0.8}"/>')
        out.append(num(x, yt1 + 13, str(i), on))
    out.append(T(X0, yt1 + 40, "Interbase: BED numbers the gaps between bases", 11, 600, DARK))

    # the same region written both ways
    y = yt1 + 70
    out.append(f'<path class="divider" d="M8 {y - 20:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    rows = (("chr1:3-6", "from base 3 to base 6, both included"),
            ("chr1\u00a0\u00a02\u00a0\u00a06", "from gap 2 to gap 6, so 6 \u2212 2 = 4 bases"))
    for k, (code, note) in enumerate(rows):
        yy = y + k * 24
        out.append(T(X0, yy, code, 12, 600, DARK, mono=True))
        out.append(T(X0 + 92, yy, note, 11, 400, MUTED))
    H = y + 24 + 34
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "The same four bases counted two ways: chr1:3-6 in in-base coordinates, numbering the bases, and chr1 2 6 in BED's interbase coordinates, numbering the gaps between bases", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
