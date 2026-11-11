"""Figure 7.6: How long each kind of RNA is, on a log scale, with the 200-nucleotide cutoff."""

import math

from figures.core import COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, TEAL, T, main, svg_doc

NAME = "7.6-rna-lengths"

# Lengths in nucleotides. A range is (low, high, median or None). The microRNA, piRNA and
# tRNA ranges come from Bartel (2018), Ozata et al. (2019) and Berg and Brandl (2021). The
# spliceosomal snRNAs are RNU1-1, RNU2-1, RNU4-1, RNU5A-1 and RNU6-1 in GENCODE release 50.
# snoRNAs, lncRNAs and mRNAs are the middle 90% of GENCODE 50 transcript lengths (exons
# added up), with mRNAs taken from MANE Select transcripts. rRNAs are RefSeq NR_003285,
# NR_003286 and NR_003287 and GENCODE RNA5S1.
ROWS = (
    ("microRNAs", "point", 22),
    ("piRNAs", "range", (21, 35, None)),
    ("tRNAs", "range", (76, 90, None)),
    ("snoRNAs", "range", (68, 213, 118)),
    ("snRNAs", "range", (107, 188, None)),
    ("rRNAs", "rrna", ((119, "5S"), (157, "5.8S"), (1869, "18S"), (5070, "28S"))),
    ("lncRNAs", "range", (369, 2264, 813)),
    ("mRNAs", "range", (760, 9142, 2941)),
)
LO, HI = 10, 10000
X0, X1 = 118, 368
BAR = 9
ROW = 32
SHADE = "#e9f6f8"
REF = "#a7a9ac"   # mRNAs, shown only for comparison


def xs(n):
    return X0 + (X1 - X0) * (math.log10(n) - math.log10(LO)) / (math.log10(HI) - math.log10(LO))


def dot(x, y, fill="#ffffff", line=DARK, r=4.2):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}" stroke="{line}" stroke-width="1.5"/>'


def bar(a, b, y, col):
    x0, x1 = xs(a), xs(b)
    return f'<rect x="{x0:.2f}" y="{y - BAR / 2:.2f}" width="{x1 - x0:.2f}" height="{BAR}" rx="{BAR / 2}" fill="{col}"/>'


def fig():
    out = []
    top = 60
    bottom = top + ROW * len(ROWS)
    x200 = xs(200)
    # small vs long
    out.append(f'<rect x="{X0:.2f}" y="{top - 14:.2f}" width="{x200 - X0:.2f}" height="{bottom - top + 14:.2f}" fill="{SHADE}"/>')
    out.append(T((X0 + x200) / 2, top - 22, "small", LBL, 700, DARK, "middle"))
    out.append(T((x200 + X1) / 2, top - 22, "long", LBL, 700, DARK, "middle"))
    out.append(f'<path d="M{x200:.2f} {top - 34:.2f}V{bottom:.2f}" stroke="{DARK}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    out.append(T(x200 + 4, top - 36, "200 nt", 11, 600, DARK))
    for i, (name, kind, data) in enumerate(ROWS):
        y = top + ROW * i + ROW / 2
        ref = name == "mRNAs"
        col = REF if ref else TEAL
        out.append(T(8, y + 4.5, name, LBL, 600, MUTED if ref else DARK))
        if kind == "point":
            out.append(dot(xs(data), y, col, col))
            out.append(T(xs(data) + 9, y + 4.5, f"about {data}", 11, 400, MUTED))
        elif kind == "range":
            a, b, med = data
            out.append(bar(a, b, y, col))
            if med:
                out.append(dot(xs(med), y))
        else:
            out.append(f'<path d="M{xs(data[0][0]):.2f} {y:.2f}H{xs(data[-1][0]):.2f}" stroke="{col}" stroke-width="1.4" stroke-dasharray="2 3"/>')
            for n, lab in data:
                out.append(dot(xs(n), y, col, col))
            out.append(T(xs(157) + 3, y - 9, "5S, 5.8S", 10.5, 600, MUTED, "end"))
            for n, lab in data[2:]:
                out.append(T(xs(n), y - 9, lab, 10.5, 600, MUTED, "middle"))
    # axis
    ya = bottom + 6
    out.append(f'<path d="M{X0:.2f} {ya:.2f}H{X1:.2f}" stroke="{GREY_LINE}" stroke-width="1"/>')
    for e in range(1, 5):
        for m in range(1, 10):
            n = m * 10 ** e
            if n > HI:
                break
            x = xs(n)
            major = m == 1
            out.append(f'<path d="M{x:.2f} {ya:.2f}V{ya + (6 if major else 3.5):.2f}" stroke="{GREY_LINE}" stroke-width="{1 if major else 0.7}"/>')
            if major:
                out.append(T(x, ya + 19, f"{n:,}", 11, 400, MUTED, "middle"))
    out.append(T((X0 + X1) / 2, ya + 37, "length in nucleotides (log scale)", LBL, 400, MUTED, "middle"))
    # key
    yk = ya + 66
    out.append(f'<path class="divider" d="M8 {yk - 20:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>')
    out.append(f'<rect x="16" y="{yk - BAR / 2 - 4:.2f}" width="28" height="{BAR}" rx="{BAR / 2}" fill="{TEAL}"/>')
    out.append(T(52, yk + 0.5, "typical range", LBL, 400, MUTED))
    out.append(f'<rect x="196" y="{yk - BAR / 2 - 4:.2f}" width="28" height="{BAR}" rx="{BAR / 2}" fill="{TEAL}"/>' + dot(210, yk - 4))
    out.append(T(232, yk + 0.5, "median", LBL, 400, MUTED))
    H = yk + 32
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(392, H - 7, out, "Typical lengths of noncoding RNAs and mRNAs on a log scale, with the 200-nucleotide line that separates small from long noncoding RNAs", origin=(4, 7))


if __name__ == "__main__":
    main(NAME, fig)
