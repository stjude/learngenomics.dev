"""Figure 7.4: How DNA methylation is copied when a cell divides."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, LBLUE, MUTED, ORANGE, T, main, svg_doc

NAME = "7.4-methylation-copying"

METHYL_FILL = "#fbd38a"   # the methyl highlight used in figure 7.3
SITES = (0.18, 0.5, 0.82)  # CpG positions along a duplex, as fractions of its length
GAP = 14                   # distance between the two strands of a duplex
STEM = 11                  # lollipop stem length


def mark(x, y, up, methylated):
    """A cytosine at a CpG site: a stem off the strand and a circle, filled when methylated."""
    yc = y - STEM if up else y + STEM
    fill = METHYL_FILL if methylated else "#ffffff"
    # In dark mode a filled marker turns solid orange so it still reads as filled next to an empty one.
    dark = f' data-dark-fill="{ORANGE}"' if methylated else ""
    return (f'<path d="M{x:.2f} {y:.2f}V{yc + (5 if up else -5):.2f}" stroke="{DARK}" stroke-width="1.2"/>'
            f'<circle class="{"methylated" if methylated else "unmethylated"}" cx="{x:.2f}" cy="{yc:.2f}" r="5" '
            f'fill="{fill}" stroke="{ORANGE}"{dark} stroke-width="1.5"/>')


def strand(x0, x1, y, col):
    return f'<path d="M{x0:.2f} {y:.2f}H{x1:.2f}" stroke="{col}" stroke-width="3.5" stroke-linecap="round"/>'


def duplex(x0, x1, y, top, bottom):
    """top and bottom are (colour, methylated) for each strand; y is the top strand."""
    out = [strand(x0, x1, y, top[0]), strand(x0, x1, y + GAP, bottom[0])]
    for f in SITES:
        x = x0 + (x1 - x0) * f
        # the C on the bottom strand pairs with the G next to the top strand's C
        out.append(mark(x - 3, y, True, top[1]))
        out.append(mark(x + 3, y + GAP, False, bottom[1]))
    return "".join(out)


def divider(y):
    return f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.45"/>'


def fig():
    out = []
    old, new = BLUE, LBLUE
    L = (24, 182)
    R = (218, 376)
    C = (121, 279)
    # ---- 1
    out.append(T(8, 20, "1. Both strands carry the marks", LBL, 700))
    y1 = 52
    out.append(duplex(*C, y1, (old, True), (old, True)))
    # ---- 2
    y = y1 + GAP + 40
    out.append(divider(y - 18))
    out.append(T(8, y, "2. Copying makes two half-marked duplexes", LBL, 700))
    y2 = y + 32
    out.append(duplex(*L, y2, (old, True), (new, False)))
    out.append(duplex(*R, y2, (new, False), (old, True)))
    # ---- 3
    y = y2 + GAP + 40
    out.append(divider(y - 18))
    out.append(T(8, y, "3. DNMT1 marks the new strands to match", LBL, 700))
    y3 = y + 32
    out.append(duplex(*L, y3, (old, True), (new, True)))
    out.append(duplex(*R, y3, (new, True), (old, True)))
    # ---- key
    y = y3 + GAP + 40
    out.append(divider(y - 18))
    k1, k2 = 20, 210
    out.append(mark(k1 + 6, y + 6, True, True) + T(k1 + 20, y + 0.5, "methylated cytosine", LBL, 400, MUTED))
    out.append(mark(k2 + 6, y + 6, True, False) + T(k2 + 20, y + 0.5, "unmethylated cytosine", LBL, 400, MUTED))
    y += 26
    out.append(strand(k1, k1 + 14, y - 4, old) + T(k1 + 20, y + 0.5, "old strand", LBL, 400, MUTED))
    out.append(strand(k2, k2 + 14, y - 4, new) + T(k2 + 20, y + 0.5, "new strand", LBL, 400, MUTED))
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(392, H - 7, out, "DNA methylation is copied when a cell divides: each new strand starts unmarked, and DNMT1 adds methyl groups opposite the old strand's marks", origin=(4, 7))


if __name__ == "__main__":
    main(NAME, fig)
