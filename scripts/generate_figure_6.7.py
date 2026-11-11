"""Figure 6.7: A made-up gene, G1, with two transcripts."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, PURPLE, T, main, svg_doc

NAME = "6.7-gtf-gff3-files"

EXONS = {"E1": (1001, 1400), "E2": (2001, 2500), "E3": (3301, 4000)}
L, R = 40.0, 360.0
P0, P1 = 900.0, 4100.0


def X(p):
    return L + (p - P0) / (P1 - P0) * (R - L)


def label(y, kind, attrs):
    return [T(L, y, kind, 11, 600, DARK), T(L + 66, y, attrs, 11, 400, MUTED, mono=True)]


def transcript(y, exons, hl=None):
    s = [f'<path d="M{X(EXONS[a][1]):.2f} {y:.2f}H{X(EXONS[b][0]):.2f}" stroke="{GREY_LINE}" stroke-width="1.1"/>'
         for a, b in zip(exons, exons[1:])]
    for e in exons:
        a, b = EXONS[e]
        on = e == hl
        col = BLUE if on else GREY_LINE
        s.append(f'<rect x="{X(a):.2f}" y="{y - 8:.2f}" width="{X(b) - X(a):.2f}" height="16" rx="2.5" '
                 f'fill="{col}" fill-opacity="{0.18 if on else 0.12}" stroke="{col}" stroke-width="{1.3 if on else 0.9}"/>')
        s.append(T((X(a) + X(b)) / 2, y + 3.8, e, 10, 700 if on else 500, BLUE if on else DARK, "middle", mono=True))
    return s


def fig():
    W = 400.0
    out = []
    out.append(T(8, 20, "One gene, two transcripts", 13, 700))
    out.append(T(8, 37, "In GFF3, each line names its own ID and its parent's", 11, 400, MUTED))

    y = 64
    out += label(y, "gene", "ID=G1")
    out.append(f'<rect x="{X(1001):.2f}" y="{y + 10:.2f}" width="{X(4000) - X(1001):.2f}" height="7" rx="2" fill="{PURPLE}" fill-opacity="0.75"/>')

    y = 108
    out += label(y, "transcript", "ID=T1;Parent=G1")
    out += transcript(y + 20, ["E1", "E2", "E3"], hl="E2")

    y = 160
    out += label(y, "transcript", "ID=T2;Parent=G1")
    out += transcript(y + 20, ["E1", "E3"])

    # ruler
    yr = 204
    out.append(f'<path d="M{X(P0 + 50):.2f} {yr:.2f}H{X(P1 - 50):.2f}" stroke="{GREY_LINE}" stroke-width="0.8"/>')
    for p in (1000, 2000, 3000, 4000):
        out.append(f'<path d="M{X(p):.2f} {yr:.2f}V{yr + 4:.2f}" stroke="{GREY_LINE}" stroke-width="0.8"/>')
        out.append(T(X(p), yr + 16, f"{p:,}", 10, 400, MUTED, "middle"))

    # column 9 of E2 both ways
    y = yr + 44
    out.append(f'<path class="divider" d="M8 {y - 18:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    out.append(T(L, y, "Column 9 of exon E2, written two ways", 11, 600, DARK))
    rows = (("GFF3", "ID=E2;Parent=T1"),
            ("GTF", 'gene_id "G1"; transcript_id "T1";'))
    for k, (fmt, attrs) in enumerate(rows):
        yy = y + 24 + k * 22
        out.append(T(L, yy, fmt, 11, 600, DARK))
        out.append(T(L + 44, yy, attrs, 11, 600, BLUE, mono=True))
    H = y + 24 + 22 + 34
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "A made-up gene, G1, with two transcripts: T1 has exons E1, E2 and E3, and T2 has E1 and E3. In GFF3, exon E2 says ID=E2;Parent=T1; in GTF, it says gene_id \"G1\"; transcript_id \"T1\";", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
