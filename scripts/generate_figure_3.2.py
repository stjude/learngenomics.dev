"""Figure 3.2: Reference, matched normal and tumor."""

from figures.core import (
    DARK, FAINT_BASE, GREY_LINE, LBL, PURPLE, RED, T, big_copyright, main, svg_doc,
)
from figures.sequences import ruler, seq_grid_row, two_line_label

NAME = "3.2-reference-normal-tumor"


def fig():
    W, H = 400.0, 400.0
    MUTED = "#4d4d4f"
    GERM, SOM = PURPLE, RED
    X0, CW = 84.0, 22.0
    REF = "TGCATGACGGTCAA"
    G_ALT = {5: "A", 11: "T"}                        # germline (106 G>A, 112 C>T): in the normal and the tumor
    S_ALT = {2: "T", 8: "T"}                         # somatic (103 C>T, 109 G>T): tumor only
    cx = lambda i: X0 + CW * (i + 0.5)
    out = [T(8, 22, "Reference, matched normal and tumor", 14, 700)]
    out.append(ruler(X0, CW, 50, "chr17:", 101, len(REF), MUTED))
    YR, YN, YT, YC = 76.0, 144.0, 212.0, 268.0
    normal = "".join(G_ALT.get(i, b) for i, b in enumerate(REF))
    tumor = "".join(S_ALT.get(i, b) for i, b in enumerate(normal))
    for i in G_ALT:                                  # germline variants carry straight down into the tumor
        out.append(f'<path class="inherited" d="M{cx(i):.2f} {YN + 11:.2f}V{YT - 11:.2f}" stroke="{GERM}" '
                   f'stroke-width="1" stroke-dasharray="2 2"/>')
    rows = ((YR, "Reference", "(GRCh38)", REF, {}, DARK),
            (YN, "Normal", "(blood)", normal, {i: GERM for i in G_ALT}, FAINT_BASE),
            (YT, "Tumor", None, tumor, {**{i: GERM for i in G_ALT}, **{i: SOM for i in S_ALT}}, FAINT_BASE))
    for y, name, sub, seq, marks, plain in rows:
        out.append(two_line_label(8, y, name, sub, c2=MUTED))
        out.append(seq_grid_row(X0, CW, y, seq, marks, plain_fill=plain))

    def compare(y0, y1, col, title, l2):
        x = 13.0
        s = (f'<g class="comparison"><path d="M{x:.2f} {y0 + 19:.2f}V{y1 - 23:.2f}" stroke="{col}" stroke-width="1.3"/>'
             f'<path d="M{x - 3.2:.2f} {y1 - 23.5:.2f}L{x:.2f} {y1 - 17:.2f}L{x + 3.2:.2f} {y1 - 23.5:.2f}Z" fill="{col}"/>')
        ym = (y0 + y1) / 2
        s += T(x + 9, ym - 2.5, title, LBL, 700, col) + T(x + 9, ym + 11, l2, LBL, 400, MUTED)
        return s + "</g>"
    out.append(compare(YR, YN, GERM, "Germline: normal differs", "from the reference"))
    out.append(compare(YN, YT, SOM, "Somatic: tumor differs", "from the normal"))
    # tumor against the reference alone: four differences, no way to tell which is which
    out.append(f'<path class="divider" d="M8 {YT + 21:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-dasharray="3 2"/>')
    out.append(two_line_label(8, YC, "Tumor vs.", "reference", 600, 600))
    out.append(seq_grid_row(X0, CW, YC, tumor, {i: MUTED for i in {**G_ALT, **S_ALT}}, plain_fill=FAINT_BASE))
    out.append(T(X0, YC + 29, "4 differences: germline or somatic?", LBL, 600, MUTED))
    ky = 332.0
    for k, (col, text) in enumerate(((GERM, "Germline: inherited, in every cell"), (SOM, "Somatic: arose in the tumor"))):
        y = ky + k * 18
        out.append(f'<g class="key"><rect x="8" y="{y - 9.5:.2f}" width="11" height="11" rx="2" fill="{col}" fill-opacity="0.16" stroke="{col}" stroke-width="1.1"/>'
                   + T(25, y, text, LBL, 400, MUTED) + "</g>")
    out.append(big_copyright(W - 8, ky + 42))
    svg = svg_doc(W, H, out, "Reference, matched normal and tumor: germline variants differ from the reference, somatic variants differ from the normal")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="392.5" height="372.25" viewBox="3.25 8 392.5 372.25"')


if __name__ == "__main__":
    main(NAME, fig)
