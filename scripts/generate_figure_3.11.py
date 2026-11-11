"""Figure 3.11: Variant equivalence: one change in a sample described three ways."""

from figures.core import COPYRIGHT, GREY_LINE, LBL, SANS, T, esc, main, svg_doc
from figures.sequences import base_cells, change_box

NAME = "3.11-variant-equivalence"


def fig():
    W, H = 400.0, 360.0
    MUTED = "#4d4d4f"
    X0, CW, RG = 84.0, 22.0, 22.0                     # grid start, column width, ref-to-sample row gap
    out = []
    lab = lambda y, t, w=600, c=None: T(8, y + LBL * 0.36, t, LBL, w, c)

    def pair(y, ref, smp, boxes=(), muted=False):
        s = ""
        w, c = (400, MUTED) if muted else (600, None)
        for c0, c1 in boxes:
            s += change_box(X0, CW, c0, c1, y - 12, y + RG + 12)
        return s + lab(y, "Reference", w, c) + base_cells(X0, CW, y, ref) + lab(y + RG, "Sample", w, c) + base_cells(X0, CW, y + RG, smp)

    SMP = list("TCGAAATC")
    out.append(pair(22, list("TCGG--TC"), SMP))
    blocks = [
        ("SNV + insertion", "G becomes A, then AA inserted", list("TCGG--TC"), SMP, [(3, 4), (4, 6)], None),
        ("Deletion + insertion", "G deleted, then AAA inserted", list("TCGG---TC"), list("TCG-AAATC"), [(3, 4), (4, 7)], None),
        ("One replacement", "G replaced by AAA", ["T", "C", "G", ("G", 3), "T", "C"], SMP, [(3, 6)], ("REF G", "ALT AAA")),
    ]
    y = 84.0
    for i, (name, note, ref, smp, boxes, vcf) in enumerate(blocks):
        out.append(f'<path class="divider" d="M8 {y - 22:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.5"/>')
        out.append(f'<g class="description">')
        out.append(f'<text x="8" y="{y:.2f}" font-family="{SANS}" font-size="{LBL:g}" font-weight="700">{esc(chr(97 + i) + ". " + name)}'
                   f'<tspan dx="8" font-weight="400" fill="{MUTED}">{esc(note)}</tspan></text>')
        out.append(pair(y + 24, ref, smp, boxes, muted=True))
        if vcf:
            xe = X0 + CW * 8 + 14
            out.append(T(xe, y + 24 + 4.5, vcf[0], LBL, 500, MUTED, mono=True) + T(xe, y + 24 + RG + 4.5, vcf[1], LBL, 500, MUTED, mono=True))
        out.append("</g>")
        y += 84
    out.append(T(8, y - 2, "Same sample sequence every time", LBL, 400, MUTED))
    out.append(T(W - 8, y + 22, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, out, "Variant equivalence: one change in a sample described three ways")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="392" height="351.25" viewBox="4 13.25 392 351.25"')


if __name__ == "__main__":
    main(NAME, fig)
