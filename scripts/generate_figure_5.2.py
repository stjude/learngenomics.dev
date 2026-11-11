"""Figure 5.2: Read mapping."""

from figures.core import (
    BLUE, COPYRIGHT, DARK, FAINT_BASE, GREY_LINE, LBL, MUTED, RED, T, main, svg_doc,
)

NAME = "5.2-read-mapping"

X0, CW, CH = 84.0, 22.0, 22.0
cx = lambda i: X0 + CW * (i + 0.5)


def cell(i, y, base, kind):
    x = X0 + CW * i
    r = f'x="{x + 1:.2f}" y="{y - CH / 2:.2f}" width="{CW - 2:g}" height="{CH:g}" rx="3"'
    if kind == "ref":
        box, col, w = f'<rect {r} fill="{GREY_LINE}" fill-opacity="0.07"/>', DARK, 500
    elif kind == "read":
        box, col, w = f'<rect {r} fill="{BLUE}" fill-opacity="0.14" stroke="{BLUE}" stroke-width="0.9"/>', DARK, 500
    elif kind == "diff":
        box, col, w = f'<rect {r} fill="{RED}" fill-opacity="0.16" stroke="{RED}" stroke-width="1.1"/>', RED, 700
    else:  # ghost: clipped or the other equally good place
        box, col, w = (f'<rect {r} fill="none" stroke="{GREY_LINE}" stroke-width="0.9" stroke-dasharray="2.5 2"/>',
                       FAINT_BASE, 500)
    return box + T(x + CW / 2, y + 12.5 * 0.36, base, 12.5, w, col, "middle", mono=True)


def row(y, start, bases, kinds):
    return "".join(cell(start + k, y, b, kinds[k] if isinstance(kinds, list) else kinds) for k, b in enumerate(bases))


def label(y, s):
    return T(8, y + LBL * 0.36, s, LBL, 600)


def bracket(i0, i1, y, text, below=True):
    x0, x1 = X0 + CW * i0 + 2, X0 + CW * (i1 + 1) - 2
    d = 4 if below else -4
    s = f'<path d="M{x0:.2f} {y:.2f}v{d}H{x1:.2f}v{-d}" fill="none" stroke="{GREY_LINE}" stroke-width="0.9"/>'
    ty = y + d + (12 if below else -4)
    return s + T((x0 + x1) / 2, ty, text, 10.5, 400, MUTED, "middle")


def panel_head(y, title, mapq):
    return T(8, y, title, 13, 700) + T(392, y, mapq, LBL, 700, MUTED, "end", mono=True)


def fig():
    W = 400.0
    out = []
    # 1. one place, one difference
    y = 20.0
    out.append(panel_head(y, "Fits one place", "MAPQ 60"))
    REF1 = "GATTCCGATACAGG"
    READ1 = "TTCCGTTACA"
    yr, yd = y + 24, y + 50
    out += [label(yr, "Reference"), row(yr, 0, REF1, "ref"), label(yd, "Read")]
    out.append(row(yd, 2, READ1, ["diff" if READ1[k] != REF1[2 + k] else "read" for k in range(len(READ1))]))
    out.append(T(8, yd + 30, "One base differs, but no other place fits better.", LBL, 400, MUTED))
    # 2. two places equally well
    out.append(f'<path class="divider" d="M8 {yd + 44:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y = yd + 66
    out.append(panel_head(y, "Fits two places equally well", "MAPQ 0"))
    REF2 = "TACGTAGCACGTAG"
    yr, yd = y + 38, y + 64
    out.append(bracket(1, 5, yr - 15, "copy 1", below=False) + bracket(8, 12, yr - 15, "copy 2", below=False))
    out += [label(yr, "Reference"), row(yr, 0, REF2, "ref"), label(yd, "Read")]
    out.append(row(yd, 1, "ACGTA", "read") + row(yd, 8, "ACGTA", "ghost"))
    out.append(T(cx(6.5), yd + 4.5, "or?", LBL, 600, MUTED, "middle"))
    out.append(T(8, yd + 30, "It matches both copies, so the aligner can't choose.", LBL, 400, MUTED))
    # 3. soft clip
    out.append(f'<path class="divider" d="M8 {yd + 44:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y = yd + 66
    out.append(panel_head(y, "End doesn't fit", "MAPQ 60"))
    REF3 = "CTGACCATGGTCAA"
    READ3 = "GACCATGGAGTT"
    yr, yd = y + 24, y + 50
    out += [label(yr, "Reference"), row(yr, 0, REF3, "ref"), label(yd, "Read")]
    out.append(row(yd, 2, READ3, ["read"] * 8 + ["ghost"] * 4))
    out.append(bracket(10, 13, yd + 14, "soft-clipped"))
    out.append(T(8, yd + 46, "The last bases don't match, so they're left out", LBL, 400, MUTED))
    out.append(T(8, yd + 61, "of the alignment but kept in the file.", LBL, 400, MUTED))
    H = yd + 88
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Read mapping: a read that fits one place gets a high mapping quality, a read that matches two copies of a repeat gets mapping quality 0, and a read whose end does not match is soft-clipped", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
