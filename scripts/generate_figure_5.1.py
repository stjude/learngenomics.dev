"""Figure 5.1: From reads to variants."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, ORANGE, T, main, svg_doc

NAME = "5.1-reads-to-variants"

X0, X1 = 92.0, 392.0
REF = "GATTACAGGTTACCTGAAGTCCATGAT"   # made up
SNP = 13                              # made-up C>T
CW = (X1 - X0) / len(REF)
HL = "#f6d7b8"


def divider(y):
    return f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>'


def head(y, text, fmt):
    return T(8, y, text, LBL, 700) + T(392, y, fmt, LBL, 600, MUTED, "end", mono=True)


def down_arrow(y0, y1, l1, l2=None):
    x = 20
    s = (f'<path class="step-arrow" d="M{x} {y0:.2f}V{y1 - 7:.2f}" stroke="{DARK}" stroke-width="1.6"/>'
         f'<path d="M{x - 5} {y1 - 8:.2f}L{x} {y1:.2f}L{x + 5} {y1 - 8:.2f}Z" fill="{DARK}"/>')
    ym = (y0 + y1) / 2
    if l2:
        s += T(x + 14, ym - 2, l1, LBL, 600) + T(x + 14, ym + 13, l2, LBL, 400, MUTED)
    else:
        s += T(x + 14, ym + 4.5, l1, LBL, 600)
    return s


def read_bar(x0, x1, y, alt_x=None, dup=False, fade_l=False, fade_r=False):
    h = 7
    if dup:
        s = f'<rect class="read duplicate" x="{x0:.2f}" y="{y - h / 2:.2f}" width="{x1 - x0:.2f}" height="{h}" rx="1.5" fill="none" stroke="{BLUE}" stroke-width="0.9" stroke-dasharray="3 2"/>'
    else:
        s = f'<rect class="read" x="{x0:.2f}" y="{y - h / 2:.2f}" width="{x1 - x0:.2f}" height="{h}" rx="1.5" fill="{BLUE}" fill-opacity="0.55"/>'
    if alt_x is not None:
        s += f'<rect class="mismatch" x="{alt_x - 2:.2f}" y="{y - h / 2 - 1:.2f}" width="4" height="{h + 2}" fill="{ORANGE}"/>'
    return s


def fig():
    W = 400.0
    out = []
    # ---- 1. FASTQ
    y = 20.0
    out.append(head(y, "Reads, in no particular order", "FASTQ"))
    rows = [[(8, 118, 40), (140, 250, None), (272, 382, 95)],
            [(30, 140, None), (162, 272, 22), (294, 392, None)],
            [(8, 118, None), (128, 238, 70), (260, 370, None)]]
    y += 20
    for r in rows:
        for a, b, m in r:
            out.append(read_bar(a, b, y, None if m is None else a + m))
        y += 14
    # ---- arrow 1
    y += 2
    out.append(down_arrow(y, y + 40, "Map to the reference,", "then sort and mark duplicates"))
    y += 66
    # ---- 2. BAM
    out.append(divider(y - 16))
    out.append(head(y, "Reads placed on the reference", "BAM"))
    y += 28
    sx = X0 + CW * (SNP + 0.5)
    out.append(T(sx, y, "Position 1,042", LBL, 400, MUTED, "middle"))
    out.append(f'<rect class="key-mismatch" x="8" y="{y - 9:.2f}" width="4" height="9" fill="{ORANGE}"/>'
               + T(18, y, "Differs from the reference", LBL, 400, MUTED))
    y += 20
    yref = y
    band_top = yref - 10
    out.append(T(8, yref + 4.5, "Reference", LBL, 600))
    for i, b in enumerate(REF):
        out.append(T(X0 + CW * (i + 0.5), yref + 4.5, b, LBL, 600 if i == SNP else 400, None, "middle", mono=True))
    y += 18
    reads = [  # (start cell, end cell, alt, dup)
        (0, 27, False, False), (0, 27, True, False), (0, 21, False, False), (4, 27, True, False),
        (0, 27, True, False), (9, 27, False, False), (0, 27, True, False), (0, 27, True, True),
    ]
    out.append(T(8, y + 4.5, "Reads", LBL, 600))
    for k, (a, b, alt, dup) in enumerate(reads):
        x0 = X0 + CW * a + (0 if a == 0 else 1)
        x1 = X0 + CW * b - (0 if b == 27 else 1)
        if dup:
            out.append(T(8, y + 4.5, "Duplicate", LBL, 400, MUTED))
        out.append(read_bar(x0, x1, y, sx if alt else None, dup))
        y += 13
    band = f'<rect class="variant-column" x="{sx - CW / 2:.2f}" y="{band_top:.2f}" width="{CW:.2f}" height="{y - band_top - 4:.2f}" rx="2" fill="{HL}" fill-opacity="0.75"/>'
    out.insert(len(out) - len(reads) - 1 - len(REF) - 2, band)
    # ---- arrow 2
    y += 2
    out.append(down_arrow(y, y + 34, "Call variants, then filter"))
    y += 60
    # ---- 3. VCF
    out.append(divider(y - 16))
    out.append(head(y, "Variant calls", "VCF"))
    y += 26
    cols = [(8, "Position", "start"), (124, "Ref", "start"), (196, "Alt", "start"), (290, "Genotype", "middle"), (392, "Filter", "end")]
    for x, h, a in cols:
        out.append(T(x, y, h, LBL, 600, None, a))
    out.append(f'<path d="M8 {y + 6:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    rows = [("1,027", "G", "A", "1/1", "PASS", False, False),
            ("1,042", "C", "T", "0/1", "PASS", True, False),
            ("1,115", "ATGCA", "A", "1/1", "PASS", False, False),
            ("1,180", "A", "C", "0/1", "LowQual", False, True)]
    y += 24
    for pos, ref, alt, gt, flt, hl, low in rows:
        if hl:
            out.append(f'<rect class="variant-row" x="4" y="{y - 14:.2f}" width="392" height="20" rx="3" fill="{HL}" fill-opacity="0.75"/>')
        fill = MUTED if low else None
        for (x, _, a), v in zip(cols, (pos, ref, alt, gt, flt)):
            out.append(T(x, y, v, LBL, 400, fill, a, mono=x != 8 and x != 392 or x == 8))
        y += 22
    H = y + 12
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "From reads to variants: unordered reads are mapped to the reference, a heterozygous variant shows in about half the reads, and the calls are listed in a VCF", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
