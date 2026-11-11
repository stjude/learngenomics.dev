"""Figure 6.5: VCF files."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, T, main, svg_doc

NAME = "6.5-vcf-files"

X0 = 8.0
FS = 12.0
CW = FS * 0.6
LS = 21.0
HEADER = [
    ([("##fileformat=VCFv4.2", DARK)], "the VCF version"),
    ([("##contig=<ID=chr1,\u2026>", DARK)], None),
    ([("##contig=<ID=chr2,\u2026>", DARK)], None),
    ([("##INFO=<ID=DP,\u2026>", DARK)], "what an INFO key means"),
    ([("##FORMAT=<ID=GT,\u2026>", DARK)], "what a FORMAT key means"),
    ([("#CHROM POS \u2026 sample2", DARK)], "names the columns"),
]
COLS = [
    ("1", "CHROM", [("chr1", DARK)]),
    ("2", "POS", [("1042", DARK)]),
    ("3", "ID", [(".", DARK)]),
    ("4", "REF", [("C", DARK)]),
    ("5", "ALT", [("T", DARK)]),
    ("6", "QUAL", [("48.2", DARK)]),
    ("7", "FILTER", [("PASS", DARK)]),
    ("8", "INFO", [("DP=22;AC=1;AN=4", DARK)]),
    ("9", "FORMAT", [("GT:DP", DARK)]),
    ("10", "sample1", [("0/1:10", DARK)]),
    ("11", "sample2", [("0/0:12", DARK)]),
]
GROUPS = [(0, 2, "where it is", "and its name, if any"),
          (3, 4, "the change", "reference and alternate"),
          (5, 6, "how far to trust it", "quality and filters"),
          (7, 7, "extra details", "about the variant as a whole"),
          (8, 10, "the samples", "one column each")]


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
    out.append(T(X0, y + 17, "Lines starting with ## describe the file; the last names the columns", 11, 400, MUTED))
    xt = X0 + 4
    y0 = y + 46
    xb, xl = 210.0, 224.0
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
    out.append(T(X0, y, "Then one line per variant", 13, 700))
    out.append(T(X0, y + 17, "Eight fixed columns, then FORMAT and the samples, one per row", 11, 400, MUTED))
    y0 = y + 46
    xn, xc, xv = X0 + 14, X0 + 22, X0 + 80
    for k, (num, name, parts) in enumerate(COLS):
        yy = y0 + k * LS
        out.append(T(xn, yy, num, 11, 400, MUTED, "end", mono=True))
        out.append(T(xc, yy, name, 11, 400, MUTED, mono=True))
        spans(xv, yy, parts, out)
    for a, b, lab, sub in GROUPS:
        ya, yb = y0 + a * LS - 12, y0 + b * LS + 4
        bracket(out, xb, ya, yb, xl, lab, sub)
    H = y0 + (len(COLS) - 1) * LS + 40
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "VCF files: a header of lines starting with ##, a line naming the columns, then one line per variant with eight fixed columns, FORMAT and one column per sample", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
