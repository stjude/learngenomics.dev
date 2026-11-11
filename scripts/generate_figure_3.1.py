"""Figure 3.1: The reference and variant calls."""

from figures.core import DARK, FAINT_BASE, GREY_LINE, LBL, RED, T, big_copyright, main, svg_doc
from figures.sequences import ruler, seq_grid_row, two_line_label

NAME = "3.1-reference-and-variant-calls"


def fig():
    W, H = 400.0, 360.0
    MUTED = "#4d4d4f"
    X0, CW = 84.0, 22.0
    REF = "ATCAGTCAGTCATG"
    VA, VB = 4, 10                                   # positions 105 and 111
    cx = lambda i: X0 + CW * (i + 0.5)
    out = [T(8, 22, "The reference and variant calls", 14, 700)]
    out.append(ruler(X0, CW, 50, "chr7:", 101, len(REF), MUTED))
    YR, Y1, Y2 = 76.0, 136.0, 174.0
    out.append(two_line_label(8, YR, "Reference", None))
    out.append(seq_grid_row(X0, CW, YR, REF))
    out.append(T(8, 112, "This person's two copies", LBL, 400, MUTED))
    copies = (("parent 1", Y1, {VA: "A", VB: "T"}), ("parent 2", Y2, {VB: "T"}))
    for who, y, alts in copies:
        seq = "".join(alts.get(i, b) for i, b in enumerate(REF))
        out.append(two_line_label(8, y, "Copy from", who, 400, 400))
        out.append(seq_grid_row(X0, CW, y, seq, {i: RED for i in alts}, plain_fill=FAINT_BASE))
    # notes on the dotted guides
    YT = 252.0                                       # table top
    for vi, l1, l2 in ((VA, "Only copy 1", "differs"), (VB, "Both copies", "differ")):
        out.append(f'<path class="guide" d="M{cx(vi):.2f} {Y2 + 12:.2f}V{YT - 3:.2f}" stroke="{GREY_LINE}" '
                   f'stroke-width="0.8" stroke-dasharray="2 2"/>')
        out.append(f'<path d="M{cx(vi) - 3:.2f} {YT - 6:.2f}L{cx(vi):.2f} {YT - 1:.2f}L{cx(vi) + 3:.2f} {YT - 6:.2f}Z" fill="{GREY_LINE}"/>')
        out.append(T(cx(vi) + 6, 207, l1, LBL, 400, MUTED) + T(cx(vi) + 6, 221, l2, LBL, 400, MUTED))
    # variant calls table: full width
    out.append(T(8, 230, "Variant calls", 13, 700))
    TX, TW = 8.0, 384.0
    cols = ((TX, 104.0, "Position"), (TX + 104, 60.0, "REF"), (TX + 164, 60.0, "ALT"), (TX + 224, 160.0, "Genotype"))
    out.append(f'<rect class="variant-calls" x="{TX:g}" y="{YT:g}" width="{TW:g}" height="72" rx="3.5" '
               f'fill="{GREY_LINE}" fill-opacity="0.07" stroke="{GREY_LINE}" stroke-width="0.9"/>')
    out.append(f'<path d="M{TX:g} {YT + 24:g}H{TX + TW:g}" stroke="{GREY_LINE}" stroke-width="0.7"/>')
    for x, w, name in cols:
        out.append(T(x + w / 2, YT + 16.5, name, LBL, 600, MUTED, "middle"))
    rows = (("chr7:105", "G", "A", "Heterozygous"), ("chr7:111", "C", "T", "Homozygous (alt)"))
    for r, vals in enumerate(rows):
        ry = YT + 36 + r * 24
        for k, ((x, w, _), val) in enumerate(zip(cols, vals)):
            if k in (1, 2):
                out.append(T(x + w / 2, ry + 4.5, val, 13, 700, RED if k == 2 else DARK, "middle", mono=True))
            else:
                out.append(T(x + w / 2, ry + 4.5, val, LBL, 400, anchor="middle"))
    out.append(big_copyright(W - 8, YT + 92))
    svg = svg_doc(W, H, out, "The reference and variant calls: each place a copy differs from the reference becomes a variant call")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="393" height="342.5" viewBox="3.5 7.75 393 342.5"')


if __name__ == "__main__":
    main(NAME, fig)
