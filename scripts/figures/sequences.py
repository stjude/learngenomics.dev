"""Rows of bases: colored base letters, change boxes, sequence grids and coordinate rulers."""

from figures.core import DARK, FAINT_BASE, GREEN, GREY_LINE, LBL, ORANGE, PURPLE, RED, TEAL, T


def seq_grid_row(x0, cw, cy, bases, marks=None, plain_fill=DARK, size=12.5, ch=22.0):
    """One row of monospace bases in cells. marks: {index: colour} for highlighted (differing) bases."""
    marks = marks or {}
    s = '<g class="bases">'
    for i, b in enumerate(bases):
        x = x0 + cw * i
        col = marks.get(i)
        if col:
            s += (f'<rect x="{x + 1:.2f}" y="{cy - ch / 2:.2f}" width="{cw - 2:g}" height="{ch:g}" rx="3" '
                  f'fill="{col}" fill-opacity="0.16" stroke="{col}" stroke-width="1.1"/>')
        else:
            s += (f'<rect x="{x + 1:.2f}" y="{cy - ch / 2:.2f}" width="{cw - 2:g}" height="{ch:g}" rx="3" '
                  f'fill="{GREY_LINE}" fill-opacity="0.07"/>')
        s += T(x + cw / 2, cy + size * 0.36, b, size, 700 if col else 500, col or plain_fill, "middle", mono=True)
    return s + "</g>"


def ruler(x0, cw, y, chrom, first, n, muted):
    s = '<g class="ruler">' + T(x0 - 5, y, chrom, 10, 600, muted, "end")
    for i in range(n):
        cx = x0 + cw * (i + 0.5)
        s += T(cx, y, str(first + i), 10, 400, muted, "middle")
        s += f'<path d="M{cx:.2f} {y + 3:.2f}V{y + 7:.2f}" stroke="{GREY_LINE}" stroke-width="0.7"/>'
    return s + "</g>"


def two_line_label(x, y, l1, l2, w1=600, w2=400, c2=None):
    """Label centred on row centre y: one or two lines."""
    if not l2:
        return T(x, y + LBL * 0.36, l1, LBL, w1)
    return T(x, y - 2, l1, LBL, w1) + T(x, y + 11.5, l2, LBL, w2, c2)


BASE_C = {"T": ORANGE, "C": PURPLE, "G": TEAL, "A": GREEN}
CHANGE_C = RED


def base_cells(x0, cw, y, seq, size=14.0):
    """Mono bold bases centred in cells; '-' is a muted gap. seq may contain multi-column items as (text, ncols)."""
    s = '<g class="bases">'
    x = x0
    for it in seq:
        txt, n = it if isinstance(it, tuple) else (it, 1)
        cx = x + cw * n / 2
        if txt == "-":
            s += T(cx, y + size * 0.36, "–", size, 400, FAINT_BASE, "middle", mono=True)
        else:
            s += T(cx, y + size * 0.36, txt, size, 700, BASE_C.get(txt, DARK), "middle", mono=True)
        x += cw * n
    return s + "</g>"


def change_box(x0, cw, c0, c1, y0, y1, pad=2.0):
    return (f'<rect class="changed" x="{x0 + cw * c0 + 1:.2f}" y="{y0:.2f}" width="{cw * (c1 - c0) - 2:.2f}" height="{y1 - y0:.2f}" rx="4" '
            f'fill="{CHANGE_C}" fill-opacity="0.1" stroke="{CHANGE_C}" stroke-width="1.1"/>')
