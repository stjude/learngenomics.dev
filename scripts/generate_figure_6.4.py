"""Figure 6.4: BAM files."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, T, main, svg_doc

NAME = "6.4-bam-files"

X0 = 8.0
FS = 12.0
CW = FS * 0.6
LS = 21.0
HEADER = [
    ([("@HD ", DARK), ("SO:coordinate", DARK)], "how the reads are sorted"),
    ([("@SQ ", DARK), ("SN:chr1 LN:80000", DARK)], None),
    ([("@SQ ", DARK), ("SN:chr2 LN:80000", DARK)], None),
    ([("@RG ", DARK), ("ID:", DARK), ("rg1", BLUE), (" SM:sample1", DARK)], "a read group and its sample"),
    ([("@PG ", DARK), ("ID:minimap2", DARK)], "a program that made the file"),
]
COLS = [
    ("1", "QNAME", [("read_1", DARK)]),
    ("2", "FLAG", [("99", DARK)]),
    ("3", "RNAME", [("chr1", DARK)]),
    ("4", "POS", [("1203", DARK)]),
    ("5", "MAPQ", [("60", DARK)]),
    ("6", "CIGAR", [("150M", DARK)]),
    ("7", "RNEXT", [("=", DARK)]),
    ("8", "PNEXT", [("1451", DARK)]),
    ("9", "TLEN", [("398", DARK)]),
    ("10", "SEQ", [("GATTACAGGC\u2026", DARK)]),
    ("11", "QUAL", [("CCCFFFFF?H\u2026", DARK)]),
    ("", "tags", [("NM:i:1 RG:Z:", DARK), ("rg1", BLUE)]),
]
GROUPS = [(0, 1, "which read", "its name and flags"),
          (2, 5, "where it maps", "and how well"),
          (6, 8, "its mate", "and the fragment length"),
          (9, 10, "the read itself", "bases and qualities"),
          (11, 11, "optional tags", "extra details")]


def spans(x, y, parts, out):
    for txt, col in parts:
        lead = len(txt) - len(txt.lstrip(" "))
        out.append(T(x + lead * CW, y, txt.lstrip(" "), FS, 600, col, mono=True))
        x += len(txt) * CW


def bracket(out, xb, ya, yb, xl, lab, sub):
    out.append(f'<path d="M{xb:.2f} {ya:.2f}H{xb + 4:.2f}V{yb:.2f}H{xb:.2f}" fill="none" stroke="{BLUE}" stroke-width="1.3"/>')
    ym = (ya + yb) / 2
    if sub:
        out.append(T(xl, ym - 2, lab, 11, 600, BLUE))
        out.append(T(xl, ym + 12, sub, 11, 400, MUTED))
    else:
        out.append(T(xl, ym + 4, lab, 11, 600, BLUE))


def fig():
    W = 400.0
    out = []
    y = 20.0
    out.append(T(X0, y, "The header comes first", 13, 700))
    out.append(T(X0, y + 17, "Each header line starts with @", 11, 400, MUTED))
    xt = X0 + 4
    y0 = y + 46
    xb, xl = 194.0, 208.0
    for k, (parts, lab) in enumerate(HEADER):
        yy = y0 + k * LS
        spans(xt, yy, parts, out)
        if lab:
            out.append(T(xl, yy, lab, 11, 400, MUTED))
    ya, yb = y0 + LS - 12, y0 + 2 * LS + 3
    out.append(f'<path d="M{xb:.2f} {ya:.2f}H{xb + 4:.2f}V{yb:.2f}H{xb:.2f}" fill="none" stroke="{GREY_LINE}" stroke-width="1.1"/>')
    out.append(T(xl, (ya + yb) / 2 + 4, "the reference\u2019s chromosomes", 11, 400, MUTED))
    y = y0 + (len(HEADER) - 1) * LS + 26
    out.append(f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y += 26
    out.append(T(X0, y, "Then one line per alignment", 13, 700))
    out.append(T(X0, y + 17, "Eleven tab-separated columns, then tags, shown here one per row", 11, 400, MUTED))
    y0 = y + 46
    xn, xc, xv = X0 + 14, X0 + 22, X0 + 68
    for k, (num, name, parts) in enumerate(COLS):
        yy = y0 + k * LS
        out.append(T(xn, yy, num, 11, 400, MUTED, "end", mono=True))
        out.append(T(xc, yy, name, 11, 400, MUTED, mono=True))
        spans(xv, yy, parts, out)
    for a, b, lab, sub in GROUPS:
        ya, yb = y0 + a * LS - 12, y0 + b * LS + 4
        bracket(out, xb, ya, yb, xl, lab, sub if b > a else None)
    H = y0 + (len(COLS) - 1) * LS + 40
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "BAM files: a header of lines starting with @, then one line per alignment, with eleven columns and optional tags", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
