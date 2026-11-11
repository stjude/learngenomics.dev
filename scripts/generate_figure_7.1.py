"""Figure 7.1: Seven kinds of alternative transcript events."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, T, main, svg_doc

NAME = "7.1-alternative-splicing-events"

L, R = 122.0, 390.0  # diagram span


def X(p):  # p in 0..100
    return L + p / 100.0 * (R - L)


def track(y, exons):
    """exons: list of (a, b, alt) in 0..100; alt pieces are highlighted."""
    s = []
    # merge touching pieces into one block for intron lines
    blocks = []
    for a, b, alt in exons:
        if blocks and abs(blocks[-1][1] - a) < 1e-9:
            blocks[-1][1] = b
        else:
            blocks.append([a, b])
    for (a0, b0), (a1, b1) in zip(blocks, blocks[1:]):
        s.append(f'<path d="M{X(b0):.2f} {y:.2f}H{X(a1):.2f}" stroke="{GREY_LINE}" stroke-width="1.1"/>')
    for a, b, alt in exons:
        col = BLUE if alt else GREY_LINE
        s.append(f'<rect x="{X(a):.2f}" y="{y - 5.5:.2f}" width="{X(b) - X(a):.2f}" height="11" '
                 f'fill="{col}" fill-opacity="{0.22 if alt else 0.12}" stroke="{col}" stroke-width="{1.3 if alt else 0.9}"/>')
    return s


E1, E2, E3 = (0, 18), (41, 59), (82, 100)
c = lambda e, alt=False: (e[0], e[1], alt)
ROWS = [
    ("Exon skipping", None,
     [c(E1), c(E2, True), c(E3)],
     [c(E1), c(E3)]),
    ("Intron retention", None,
     [c((0, 30)), c((70, 100))],
     [c((0, 30)), (30, 70, True), c((70, 100))]),
    ("Alternative", "5\u2032 splice site",
     [c((0, 30)), c((70, 100))],
     [c((0, 30)), (30, 45, True), c((70, 100))]),
    ("Alternative", "3\u2032 splice site",
     [c((0, 30)), c((70, 100))],
     [c((0, 30)), (55, 70, True), c((70, 100))]),
    ("Mutually exclusive", "exons",
     [c(E1), c((30, 46), True), c(E3)],
     [c(E1), c((54, 70), True), c(E3)]),
]
ENDS = [
    ("Alternative first", "exon",
     [c((0, 16), True), c((48, 66)), c(E3)],
     [c((22, 38), True), c((48, 66)), c(E3)]),
    ("Alternative last", "exon",
     [c(E1), c((34, 52)), c((62, 78), True)],
     [c(E1), c((34, 52)), c((84, 100), True)]),
]


def row(y, name, name2, a, b):
    out = []
    if name2:
        out.append(T(8, y - 2, name, 11, 600, DARK))
        out.append(T(8, y + 11, name2, 11, 600, DARK))
    else:
        out.append(T(8, y + 4.5, name, 11, 600, DARK))
    out += track(y - 7, a)
    out += track(y + 9, b)
    return out


def fig():
    W = 400.0
    out = [T(8, 20, "Seven ways one gene can make two transcripts", 13, 700),
           T(8, 37, "In each row, the part that differs is highlighted", 11, 400, MUTED)]
    y = 70
    step = 44
    for r in ROWS:
        out += row(y, *r)
        y += step
    yd = y - step / 2 - 2
    out.append(f'<path class="divider" d="M8 {yd:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    out.append(T(8, yd + 18, "Related changes at the start and end of the transcript", 11, 400, MUTED))
    y = yd + 18 + 30
    for r in ENDS:
        out += row(y, *r)
        y += step
    H = y - step + 24 + 22
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Seven kinds of alternative transcript events, each shown as two transcripts of a made-up gene.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
