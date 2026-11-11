"""Figure 6.3: FASTQ files."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, PURPLE, T, TEAL, main, svg_doc

NAME = "6.3-fastq-files"

X0 = 8.0
READ_NAME = "@SIM:7:FCX12:2:1101:15329:1045 1:N:0:1"
SEQ = "GATTACAGGCTTACCGTAAC"
QUAL = "CCCFFFFF?HJJJJIJJIG#"
HI = 8
FS = 12.0
CW = FS * 0.6
GROUPS = [(1, 12, "which run"), (13, 30, "where on the flow cell"), (31, 38, "about the read")]


def letter(k, x0):
    return x0 + k * CW


def fig():
    W = 400.0
    out = []
    y = 20.0
    out.append(T(X0, y, "Paired-end reads come in two files", 13, 700))
    out.append(T(X0, y + 17, "The nth record in one file pairs with the nth in the other", 11, 400, MUTED))
    yc = y + 32
    CWD, GAPC = 176.0, 32.0
    RH, HH = 22.0, 28.0
    n = 5
    ch = HH + n * RH + 8
    cards = [(X0, "sample_R1.fastq.gz", "1", TEAL), (X0 + CWD + GAPC, "sample_R2.fastq.gz", "2", PURPLE)]
    for cx, fname, r, col in cards:
        out.append(f'<rect class="file" x="{cx:.2f}" y="{yc:.2f}" width="{CWD:g}" height="{ch:g}" rx="4" fill="{GREY_LINE}" fill-opacity="0.06" stroke="{GREY_LINE}" stroke-width="1"/>')
        out.append(T(cx + 10, yc + 18, fname, 11, 600, DARK, mono=True))
        out.append(f'<path d="M{cx:.2f} {yc + HH - 2:.2f}H{cx + CWD:.2f}" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.6"/>')
        for k in range(n):
            ry = yc + HH + k * RH + 4
            lab = "ABCDE"[k] + r
            bx0, bx1 = cx + 40, cx + CWD - 14
            out.append(T(cx + 12, ry + 12, lab, 11.5, 700, col, mono=True))
            if r == "1":
                out.append(f'<path class="read" d="M{bx0:.2f} {ry + 5:.2f}H{bx1 - 7:.2f}L{bx1:.2f} {ry + 8.5:.2f}L{bx1 - 7:.2f} {ry + 12:.2f}H{bx0:.2f}Z" fill="{col}" fill-opacity="0.8"/>')
            else:
                out.append(f'<path class="read" d="M{bx1:.2f} {ry + 5:.2f}H{bx0 + 7:.2f}L{bx0:.2f} {ry + 8.5:.2f}L{bx0 + 7:.2f} {ry + 12:.2f}H{bx1:.2f}Z" fill="{col}" fill-opacity="0.8"/>')
    for k in range(n):
        ry = yc + HH + k * RH + 4 + 8.5
        out.append(f'<path class="pair" d="M{X0 + CWD + 3:.2f} {ry:.2f}H{X0 + CWD + GAPC - 3:.2f}" stroke="{GREY_LINE}" stroke-width="1" stroke-dasharray="2 2"/>')
    y = yc + ch + 26
    out.append(f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y += 26
    out.append(T(X0, y, "Each record is four lines", 13, 700))
    out.append(T(X0, y + 17, "A made-up record, shortened to 20 bases", 11, 400, MUTED))
    xg, xt = X0 + 4, X0 + 22
    LS = 22.0
    y1 = y + 44
    out.append(T(xg, y1, "1", 11, 400, MUTED, mono=True))
    out.append(T(xt, y1, READ_NAME, FS, 600, DARK, mono=True))
    yb = y1 + 9
    for a, b, lab in GROUPS:
        x0, x1 = letter(a, xt) + 0.8, letter(b, xt) - 0.8
        out.append(f'<path d="M{x0:.2f} {yb:.2f}V{yb + 4:.2f}H{x1:.2f}V{yb:.2f}" fill="none" stroke="{BLUE}" stroke-width="1.3"/>')
        out.append(T((x0 + x1) / 2, yb + 18, lab, 11, 600, BLUE, "middle"))
    xl = letter(len(SEQ), xt) + 22
    y2 = yb + 18 + 26
    out.append(f'<rect class="hi" x="{letter(HI, xt) - 1:.2f}" y="{y2 - 14:.2f}" width="{CW + 2:.2f}" height="{2 * LS + 19:.2f}" rx="2" fill="{BLUE}" fill-opacity="0.16"/>')
    for k, (txt, lab) in enumerate(((SEQ, "the bases"), ("+", "a separator"), (QUAL, "one quality score per base"))):
        yy = y2 + k * LS
        out.append(T(xg, yy, str(k + 2), 11, 400, MUTED, mono=True))
        out.append(T(xt, yy, txt, FS, 600, DARK, mono=True))
        out.append(T(xl, yy, lab, 11, 400, MUTED))
    y4 = y2 + 2 * LS
    xh = letter(HI, xt) + CW / 2
    yd = y4 + 30
    out.append(f'<path d="M{xh:.2f} {y4 + 5:.2f}V{yd - 4:.2f}" stroke="{BLUE}" stroke-width="1.3"/>')
    out.append(T(xh - 4, yd + 12, "?", FS, 700, BLUE, mono=True))
    out.append(T(xh + 8, yd + 12, "character code 63 \u2212 33 = Q30", 11.5, 600, BLUE))
    out.append(T(xh + 8, yd + 29, "a 1 in 1,000 chance this G is wrong", 11, 400, MUTED))
    H = yd + 29 + 34
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "FASTQ files: paired-end reads come in two files in the same order, and each record is four lines: a name, the bases, a plus sign, and one quality character per base", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
