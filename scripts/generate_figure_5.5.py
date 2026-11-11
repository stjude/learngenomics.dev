"""Figure 5.5: Genotype likelihoods."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, RED, T, main, svg_doc

NAME = "5.5-genotype-likelihoods"

X0, CW, CH, RS = 84.0, 22.0, 22.0, 24.0
SITE = 5
REF = "AGTCACGTTAG"


# (first cell, last cell, base at the site, low quality?)
READS = [(0, 7, "C", 0), (1, 9, "T", 0), (2, 10, "C", 0), (0, 6, "T", 0), (3, 10, "C", 0),
         (1, 8, "T", 1), (4, 10, "C", 0), (0, 8, "T", 0), (2, 9, "C", 0), (3, 10, "C", 0)]

# A faded red for a difference the model discounts. Solid, not translucent, so it keeps 4.5:1.
LOW_QUALITY = "#9f625b"


def cell(i, y, base, kind):
    x = X0 + CW * i
    r = f'x="{x + 1:.2f}" y="{y - CH / 2:.2f}" width="{CW - 2:g}" height="{CH:g}" rx="3"'
    if kind == "ref":
        box, col, w = f'<rect {r} fill="{GREY_LINE}" fill-opacity="0.07"/>', DARK, 500
    elif kind == "read":
        box, col, w = f'<rect {r} fill="{BLUE}" fill-opacity="0.14" stroke="{BLUE}" stroke-width="0.9"/>', DARK, 500
    elif kind == "diff":
        box, col, w = f'<rect {r} fill="{RED}" fill-opacity="0.16" stroke="{RED}" stroke-width="1.1"/>', RED, 700
    else:  # low-quality difference
        box, col, w = (f'<rect {r} fill="none" stroke="{RED}" stroke-width="1" stroke-dasharray="2.5 2"/>',
                       LOW_QUALITY, 500)
    return box + T(x + CW / 2, y + 12.5 * 0.36, base, 12.5, w, col, "middle", mono=True)


def label(y, s):
    return T(8, y + LBL * 0.36, s, LBL, 600)


def fig():
    W = 400.0
    out = []
    y = 20.0
    out.append(T(8, y, "Reads covering one position", 13, 700))
    sx = X0 + CW * (SITE + 0.5)
    yr = y + 40
    out.append(T(sx, yr - 18, "1,042", 10.5, 600, MUTED, "middle", mono=True))
    y_last = yr + 14 + RS * len(READS)
    out.append(f'<rect class="site" x="{sx - CW / 2 - 1:.2f}" y="{yr - CH / 2 - 3:.2f}" width="{CW + 2:g}" height="{y_last - yr + CH + 6:.2f}" rx="4" fill="none" stroke="{GREY_LINE}" stroke-width="1" stroke-opacity="0.8"/>')
    out.append(label(yr, "Reference"))
    out.append("".join(cell(i, yr, b, "ref") for i, b in enumerate(REF)))
    for k, (a, b, base, lowq) in enumerate(READS):
        yy = yr + 14 + RS * (k + 1)
        if k == 0:
            out.append(label(yy, "Reads"))
        for i in range(a, b + 1):
            if i == SITE:
                kind = "read" if base == REF[i] else ("lowq" if lowq else "diff")
                out.append(cell(i, yy, base, kind))
            else:
                out.append(cell(i, yy, REF[i], "read"))
        if lowq:
            out.append(T(X0 + CW * (b + 1) + 6, yy + 10.5 * 0.36, "low quality", 10.5, 400, MUTED))
    yn = y_last + CH / 2 + 26
    out.append(T(8, yn, "6 reads show C and 4 show T, one of them low quality.", LBL, 400, MUTED))

    out.append(f'<path class="divider" d="M8 {yn + 16:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y = yn + 40
    out.append(T(8, y, "How well each genotype explains them", 13, 700))
    yh = y + 24
    out.append(T(8, yh, "Genotype", 11, 600, MUTED) + T(392, yh, "PL", 11, 600, MUTED, "end"))
    rows = [("C/C", "0/0", "Needs all 4 T's to be errors", None, "70"),
            ("C/T", "0/1", "About half the reads show T, as expected", "Best fit to the reads", "0"),
            ("T/T", "1/1", "Needs all 6 C's to be errors", None, "150")]
    yy = yh + 14
    RH = 44.0
    for g, code, why, note, pl in rows:
        cy = yy + RH / 2
        if note:
            out.append(f'<rect class="best" x="2" y="{yy + 2:.2f}" width="396" height="{RH - 4:g}" rx="5" fill="{BLUE}" fill-opacity="0.08" stroke="{BLUE}" stroke-width="1.1"/>')
        out.append(T(10, cy - 2, g, 14, 700, DARK, mono=True))
        out.append(T(10, cy + 13, code, 10.5, 500, MUTED, mono=True))
        if note:
            out.append(T(72, cy - 2, why, LBL, 400, DARK))
            out.append(T(72, cy + 13, note, 10.5, 700, BLUE))
        else:
            out.append(T(72, cy + LBL * 0.36, why, LBL, 400, DARK))
        out.append(T(390, cy + 14 * 0.36, pl, 14, 700, DARK, "end", mono=True))
        yy += RH
    H = yy + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Genotype likelihoods: ten reads cover a position where the reference has C; six show C and four show T, so C/T explains them best", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
