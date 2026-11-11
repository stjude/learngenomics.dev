"""Figure 5.3: Sorting."""

from figures.core import (
    BLUE, COPYRIGHT, DARK, GREEN, GREY_LINE, LBL, MUTED, PURPLE, T, main, svg_doc,
)

NAME = "5.3-sorting"

COL = {"A": BLUE, "B": PURPLE, "C": GREEN}
POS = {"A1": 900, "A2": 1350, "B1": 300, "B2": 750, "C1": 600, "C2": 1050}
RLEN = 150
TX0, TX1, P0, P1 = 128.0, 392.0, 250, 1550
px = lambda p: TX0 + (p - P0) / (P1 - P0) * (TX1 - TX0)
RH = 22.0


def rows(y0, order):
    out = []
    for k, r in enumerate(order):
        y = y0 + RH * k
        c = COL[r[0]]
        out.append(f'<rect class="row" x="8" y="{y - RH / 2 + 1:.2f}" width="384" height="{RH - 2:g}" rx="3" fill="{GREY_LINE}" fill-opacity="{0.07 if k % 2 == 0 else 0}"/>')
        out.append(T(16, y + LBL * 0.36, r, LBL, 700, DARK, mono=True))
        out.append(T(104, y + LBL * 0.36, f"{POS[r]:,}", LBL, 500, DARK, "end", mono=True))
        x0, x1 = px(POS[r]), px(POS[r] + RLEN)
        out.append(f'<rect class="read" x="{x0:.2f}" y="{y - 4:.2f}" width="{x1 - x0:.2f}" height="8" rx="1.5" fill="{c}" fill-opacity="0.6"/>')
    return "".join(out)


def header(y):
    return (T(16, y, "Read", 11, 600, MUTED) + T(104, y, "Position", 11, 600, MUTED, "end")
            + T(TX0, y, "Where it lands on the chromosome", 11, 600, MUTED))


def fig():
    W = 400.0
    out = []
    y = 20.0
    out.append(T(8, y, "Aligner output, in sequencer order", 13, 700))
    out.append(header(y + 22))
    out.append(rows(y + 40, ["A1", "A2", "B1", "B2", "C1", "C2"]))
    ya = y + 40 + RH * 5 + 20
    out.append(f'<path d="M20 {ya:.2f}V{ya + 26:.2f}" stroke="{DARK}" stroke-width="1.8"/>'
               f'<path d="M14.5 {ya + 24:.2f}L20 {ya + 34:.2f}L25.5 {ya + 24:.2f}Z" fill="{DARK}"/>')
    out.append(T(36, ya + 21, "samtools sort", LBL, 600, DARK, mono=True))
    y = ya + 60
    out.append(T(8, y, "Sorted by position", 13, 700))
    out.append(header(y + 22))
    order = sorted(POS, key=POS.get)
    out.append(rows(y + 40, order))
    H = y + 40 + RH * 5 + 36
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Sorting: the aligner writes reads in sequencer order, with mates together; sorting puts them in order of position", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
