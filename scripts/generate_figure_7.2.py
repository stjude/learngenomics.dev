"""Figure 7.2: The splice sites around BCL2L1 exon 2."""

from figures.core import BLUE, COPYRIGHT, DARK, FAINT_TEXT, GREY_LINE, MUTED, T, main, svg_doc

NAME = "7.2-bcl2l1-splice-sites"

LIGHT = "#8a8b8e"
COMP = {"A": "T", "C": "G", "G": "C", "T": "A"}
PLUS = "ACCTGTTCAA"  # chr20:31721842-31721851, + strand


def line(x0, y0, x1, y1, col=GREY_LINE, sw=1.0, extra=""):
    return f'<path d="M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}" stroke="{col}" stroke-width="{sw}" fill="none"{extra}/>'


def panel_rc(out, y):
    out.append(T(8, y, "What samtools faidx -i does", 13, 700))
    out.append(T(8, y + 17, "chr20.fa stores the + strand, and -i prints the other strand", 11, 400, MUTED))
    x0, cw = 104.0, 17.0
    cx = lambda i: x0 + i * cw
    yc, yp, ym = y + 48, y + 72, y + 98
    for i, lab in ((0, "31,721,842"), (9, "31,721,851")):
        out.append(T(cx(i), yc, lab, 9, 400, MUTED, "middle", mono=True))
        out.append(line(cx(i), yc + 3, cx(i), yp - 12, LIGHT, 0.8))
    out.append(T(8, yp, "+ strand", 11, 600, DARK))
    out.append(T(8, ym, "\u2212 strand", 11, 600, DARK))
    out.append(T(cx(0) - 13, yp, "5\u2032", 11, 400, MUTED, "end"))
    out.append(T(cx(9) + 13, yp, "3\u2032", 11, 400, MUTED))
    out.append(T(cx(0) - 13, ym, "3\u2032", 11, 400, MUTED, "end"))
    out.append(T(cx(9) + 13, ym, "5\u2032", 11, 400, MUTED))
    for i, b in enumerate(PLUS):
        out.append(T(cx(i), yp, b, 12, 600, DARK, "middle", mono=True))
        hi = i <= 1
        out.append(T(cx(i), ym, COMP[b], 12, 700 if hi else 600, BLUE if hi else DARK, "middle", mono=True))
        out.append(line(cx(i), yp + 5, cx(i), ym - 13, LIGHT, 0.8))
    out.append(T(cx(9) + 30, yp, "stored in chr20.fa", 11, 400, MUTED))
    out.append(T(cx(9) + 30, ym, "the gene\u2019s strand", 11, 400, MUTED))
    yo = ym + 58
    for i in range(9, -1, -1):
        hi = i <= 1
        out.append(line(cx(i), ym + 6, cx(9 - i), yo - 15, BLUE if hi else LIGHT, 1.1 if hi else 0.7))
    out.append(T(cx(9) + 30, (ym + yo) / 2, "-i flips the order", 11, 400, MUTED))
    out.append(T(8, yo, "-i prints", 11, 600, DARK))
    out.append(T(cx(0) - 13, yo, "5\u2032", 11, 400, MUTED, "end"))
    out.append(T(cx(9) + 13, yo, "3\u2032", 11, 400, MUTED))
    rc = "".join(COMP[b] for b in reversed(PLUS))
    for i, b in enumerate(rc):
        col, w = (BLUE, 700) if i >= 8 else (DARK, 600)
        out.append(T(cx(i), yo, b, 12, w, col, "middle", mono=True))
    out.append(T(cx(9) + 30, yo, "the same bases,", 11, 400, MUTED))
    out.append(T(cx(9) + 30, yo + 14, "read 5\u2032 to 3\u2032", 11, 400, MUTED))
    out.append(T(cx(8.5), yo + 17, "Bcl-xS donor", 10, 600, BLUE, "middle"))
    return yo + 17


def seq(out, xj, y, before, after, hi_before, label, coord):
    cw = 6.6
    x = xj - len(before) * cw - 2
    for i, b in enumerate(before):
        hi = hi_before and i >= len(before) - 2
        col = BLUE if hi else (FAINT_TEXT if hi_before else DARK)
        out.append(T(x + (i + 0.5) * cw, y, b, 11, 700 if hi else 600, col, "middle", mono=True))
    x = xj + 2
    for i, b in enumerate(after):
        out.append(T(x + (i + 0.5) * cw, y, b, 11, 700, BLUE, "middle", mono=True))
    out.append(line(xj, y - 13, xj, y + 4, DARK, 1.1))
    out.append(T(xj, y + 18, label, 10.5, 400, MUTED, "middle"))


def box(out, a, b, y, hi=False):
    col = BLUE if hi else GREY_LINE
    out.append(f'<rect x="{a:.2f}" y="{y - 6:.2f}" width="{b - a:.2f}" height="12" fill="{col}" '
               f'fill-opacity="{0.22 if hi else 0.12}" stroke="{col}" stroke-width="{1.3 if hi else 0.9}"/>')


def panel_sites(out, y):
    out.append(T(8, y, "Three splice sites around exon 2", 13, 700))
    out.append(T(8, y + 17, "Read on the gene\u2019s strand, as -i prints them", 11, 400, MUTED))
    L, A, S, E, R = 52.0, 78.0, 286.0, 364.0, 392.0  # 505 and 189 bases to scale
    yt = y + 48
    y1, y2 = yt + 30, yt + 56
    ys = y2 + 58
    dash = ' stroke-dasharray="2.5 2"'
    for x in (A, S, E):
        out.append(line(x, yt + 4, x, ys - 14, GREY_LINE, 0.8, dash))
    out.append(T(A, yt, "31,722,348", 9, 400, MUTED, "middle", mono=True))
    out.append(T(S, yt, "31,721,844", 9, 400, MUTED, "middle", mono=True))
    out.append(T(E, yt, "31,721,655", 9, 400, MUTED, "middle", mono=True))
    out.append(T(8, y1 + 4, "Bcl-xS", 11, 600, DARK))
    out.append(T(8, y2 + 4, "Bcl-xL", 11, 600, DARK))
    for yy, end in ((y1, S), (y2, E)):
        out.append(line(L, yy, A, yy))
        out.append(line(end, yy, R, yy))
        box(out, A, S, yy)
    box(out, S, E, y2, True)
    out.append(T((A + S) / 2, y1 + 4, "exon 2", 10, 600, DARK, "middle"))
    out.append(T((S + E) / 2, y2 + 21, "189 bases", 10, 600, BLUE, "middle"))
    out.append(T(A - 5, y1 - 10, "intron 1", 10, 400, MUTED, "end"))
    out.append(T(S + 5, y1 - 10, "intron 2", 10, 400, MUTED))
    seq(out, A, ys, "TTTCCTGAAG", "", True, "acceptor", None)
    seq(out, S, ys, "TTGAACAG", "GT", False, "Bcl-xS donor", None)
    seq(out, E, ys, "GCGGCTGG", "GT", False, "Bcl-xL donor", None)
    return ys + 20


def fig():
    W = 400.0
    out = []
    y = panel_rc(out, 20)
    y += 26
    out.append(f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y = panel_sites(out, y + 26)
    H = y + 34
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "samtools faidx -i reverse-complements the + strand; the three splice sites around BCL2L1 exon 2.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
