"""Figure 3.12: Two changes in one codon."""

from figures.core import COPYRIGHT, DARK, GREY_LINE, LBL, T, main, svg_doc
from figures.drawing import arrow
from figures.sequences import base_cells, change_box

NAME = "3.12-codon-mnv"


def fig():
    W, H = 400.0, 260.0
    MUTED = "#4d4d4f"
    CW, CX0 = 24.0, 168.0
    rows = [("Reference", "TTT", "Phe", ()), ("First change only", "CTT", "Leu", (0,)),
            ("Second change only", "TAT", "Tyr", (1,)), ("Both, on the same copy", "CAT", "His", (0, 1))]
    out = []
    ys = [24.0, 70.0, 108.0, 154.0]
    for k, ((name, codon, aa, ch), y) in enumerate(zip(rows, ys)):
        last = k == 3
        out.append('<g class="codon-row">')
        if last:
            out.append(f'<rect class="emphasis" x="6" y="{y - 18:.2f}" width="{326 - 6:.2f}" height="36" rx="6" fill="{GREY_LINE}" fill-opacity="0.08" '
                       f'stroke="{DARK}" stroke-width="1.2"/>')
        out.append(T(10, y + LBL * 0.36, name, LBL, 700 if last else 600))
        for c in ch:
            out.append(change_box(CX0, CW, c, c + 1, y - 13, y + 13))
        out.append(base_cells(CX0, CW, y, list(codon), size=16))
        ax = CX0 + 3 * CW + 8
        out.append(arrow(ax, ax + 26, y, col=GREY_LINE, sw=1.4, hl=6, hw=7))
        px = ax + 34
        out.append(f'<rect x="{px:.2f}" y="{y - 12:.2f}" width="44" height="24" rx="12" fill="{GREY_LINE}" fill-opacity="{0.2 if last else 0.1}" '
                   f'stroke="{DARK if last else GREY_LINE}" stroke-width="{1.3 if last else 0.9}"/>')
        out.append(T(px + 22, y + LBL * 0.36, aa, LBL, 700 if last else 600, None, "middle"))
        out.append("</g>")
    # notes
    bx = 336.0
    out.append(f'<path d="M{bx - 4:.2f} {ys[1] - 12:.2f}h4V{ys[2] + 12:.2f}h-4" fill="none" stroke="{GREY_LINE}" stroke-width="1"/>')
    my = (ys[1] + ys[2]) / 2
    out.append(T(bx + 6, my - 2, "Read one", LBL, 400, MUTED) + T(bx + 6, my + 12, "at a time", LBL, 400, MUTED))
    out.append(T(bx + 6, ys[3] - 2, "Read", LBL, 400, MUTED) + T(bx + 6, ys[3] + 12, "together", LBL, 400, MUTED))
    out.append(T(W - 8, ys[3] + 46, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, out, "Two changes in one codon: read one at a time they suggest Leu or Tyr, read together they make His")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="393.5" height="198.75" viewBox="1.75 7.5 393.5 198.75"')


if __name__ == "__main__":
    main(NAME, fig)
