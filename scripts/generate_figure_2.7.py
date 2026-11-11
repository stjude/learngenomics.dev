"""Figure 2.7: The RB and p53 brakes and the ways tumors break them."""

from figures.core import COPYRIGHT, DARK, GREY_LINE, MUTED, ORANGE, T, main, svg_doc

NAME = "2.7-two-brakes"

X0 = 10.0
NH = 26.0
GO = ("#a9dcec", "#4f9fbb")
STOP = ("#ffffff", GREY_LINE)


def node(out, cx, cy, label, kind, w=72.0, h=NH):
    fill, stroke = kind
    out.append(f'<rect x="{cx - w / 2:.2f}" y="{cy - h / 2:.2f}" width="{w:.2f}" height="{h:.2f}" rx="7" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    out.append(T(cx, cy + 4.5, label, 13, 700, DARK, "middle"))


def arrow(out, x0, y0, x1, y1):
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    ux, uy = math.cos(a), math.sin(a)
    bx, by = x1 - 7 * ux, y1 - 7 * uy
    out.append(f'<path d="M{x0:.2f} {y0:.2f}L{bx + ux:.2f} {by + uy:.2f}" stroke="{DARK}" stroke-width="1.6" fill="none"/>')
    px, py = -uy * 4.5, ux * 4.5
    out.append(f'<path d="M{bx + px:.2f} {by + py:.2f}L{x1:.2f} {y1:.2f}L{bx - px:.2f} {by - py:.2f}Z" fill="{DARK}"/>')


def block(out, x0, y0, x1, y1):
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy * 6, ux * 6
    out.append(f'<path d="M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}" stroke="{GREY_LINE}" stroke-width="1.6" fill="none"/>')
    out.append(f'<path d="M{x1 + px:.2f} {y1 + py:.2f}L{x1 - px:.2f} {y1 - py:.2f}" stroke="{GREY_LINE}" stroke-width="2" fill="none"/>')


def badge(out, x, y, r=6.5):
    out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{ORANGE}" stroke="#a8650a" stroke-width="1"/>')
    out.append(f'<path d="M{x:.2f} {y - 3.4:.2f}V{y + 0.6:.2f}" stroke="{DARK}" stroke-width="1.6" stroke-linecap="round"/>')
    out.append(f'<circle cx="{x:.2f}" cy="{y + 3.1:.2f}" r="0.95" fill="{DARK}"/>')


def hit(out, x, y, title, desc):
    badge(out, x + 6.5, y - 4)
    out.append(T(x + 17, y, title, 12, 700, DARK))
    out.append(T(x + 17, y + 15, desc, 12, 400, MUTED))


def note(out, x, y, text, anchor=None):
    out.append(T(x, y, text, 12, 400, MUTED, anchor))


def fig():
    W = 400.0
    out = []
    y = 20
    kx = X0
    for kind, lab, adv in ((GO, "pushes toward division", 140), (STOP, "holds division back", 118)):
        out.append(f'<rect x="{kx:.2f}" y="{y - 11:.2f}" width="18" height="14" rx="4" fill="{kind[0]}" stroke="{kind[1]}" stroke-width="1"/>')
        out.append(T(kx + 23, y, lab, 12, 400, MUTED))
        kx += 23 + adv + 14
    y += 22
    badge(out, X0 + 6.5, y - 4)
    out.append(T(X0 + 18, y, "ways tumors break the brake", 12, 400, MUTED))

    # ---------------------------------------------------------------- RB
    y += 40
    out.append(T(X0, y, "The RB brake", 13, 700, DARK))
    note(out, X0, y + 16, "RB holds E2F, which switches on the genes for dividing.")
    a, b, c = 52.0, 202.0, 338.0
    top = y + 50
    node(out, a, top, "p16", STOP, w=52)
    hit(out, a + 36, top + 4.5, "CDKN2A", "deleted")
    row = top + 64
    node(out, a, row, "", GO, w=76, h=40)
    out.append(T(a, row - 3, "cyclin D +", 13, 700, DARK, "middle"))
    out.append(T(a, row + 13, "CDK4/6", 13, 700, DARK, "middle"))
    block(out, a, top + NH / 2 + 1, a, row - 20 - 3)
    node(out, b, row - 9, "RB", STOP, w=56)
    node(out, b, row + 13, "E2F", GO, w=44, h=22)
    arrow(out, a + 39, row, b - 29, row)
    m = (a + 38 + b - 28) / 2
    note(out, m, row - 22, "adds", "middle")
    note(out, m, row - 8, "phosphates", "middle")
    node(out, c, row, "E2F", GO, w=44, h=22)
    arrow(out, b + 29, row, c - 23, row)
    note(out, (b + 28 + c - 22) / 2, row - 8, "RB lets go", "middle")
    note(out, c, row + 30, "genes for", "middle")
    note(out, c, row + 45, "dividing", "middle")
    note(out, c, row + 60, "switch on", "middle")
    hy = row + 46
    hit(out, a - 38, hy, "cyclin D1", "too much made")
    hit(out, a - 38, hy + 40, "CDK4 or CDK6", "extra copies")
    hit(out, b - 28, hy, "RB1", "lost")
    y = hy + 55

    # ---------------------------------------------------------------- p53
    y += 44
    out.append(T(X0, y, "The p53 brake", 13, 700, DARK))
    note(out, X0, y + 16, "p53 stops or removes cells in trouble.")
    a, b, c = 38.0, 148.0, 256.0
    row = y + 90
    note(out, X0, row - 50, "oncogene signals")
    arrow(out, a, row - 44, a, row - NH / 2 - 1)
    node(out, a, row, "ARF", STOP, w=50)
    note(out, b, row - 50, "DNA damage", "middle")
    block(out, b, row - 44, b, row - NH / 2 - 3)
    node(out, b, row, "MDM2", GO, w=64)
    block(out, a + 26, row, b - 32 - 3, row)
    node(out, c, row, "p53", STOP, w=52)
    block(out, b + 33, row, c - 26 - 3, row)
    arrow(out, c + 27, row, c + 50, row)
    note(out, c + 56, row - 3, "dividing stops")
    note(out, c + 56, row + 12, "or the cell dies")
    hy = row + 40
    hit(out, a - 24, hy, "CDKN2A", "deleted")
    hit(out, b - 32, hy, "MDM2", "amplified")
    hit(out, c - 26, hy, "TP53", "mutated")
    y = hy + 15

    H = y + 34
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "The RB and p53 brakes and the ways tumors break them.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
