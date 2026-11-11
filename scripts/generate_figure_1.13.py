"""Figure 1.13: A kinase as an on/off switch."""

from figures.core import (
    BLUE, COPYRIGHT, DARK, DARK_PAGE, GREEN, GREY_LINE, MUTED, NAVY, ORANGE, PURPLE, T, main, svg_doc,
)

NAME = "1.13-kinase-switch"

NFILL, CFILL, LSTROKE = "#e3f1fa", "#b9e2f0", "#4f9fbb"
LOOP = PURPLE
PHOS = ORANGE
ARG = BLUE
W = 400


def chaikin(pts, n=2, closed=True):
    for _ in range(n):
        q = []
        m = len(pts) if closed else len(pts) - 1
        for i in range(m):
            a, b = pts[i], pts[(i + 1) % len(pts)]
            q.append((0.75 * a[0] + 0.25 * b[0], 0.75 * a[1] + 0.25 * b[1]))
            q.append((0.25 * a[0] + 0.75 * b[0], 0.25 * a[1] + 0.75 * b[1]))
        if not closed:
            q = [pts[0]] + q + [pts[-1]]
        pts = q
    return pts


def catmull(p):
    o = f"M{p[0][0]:.2f} {p[0][1]:.2f}"
    for i in range(len(p) - 1):
        p0, p1, p2, p3 = p[max(i - 1, 0)], p[i], p[i + 1], p[min(i + 2, len(p) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        o += f" C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}"
    return o


def closed_path(p):
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in p) + "Z"


N_LOBE = [(-58, -10), (-64, -36), (-46, -72), (-8, -90), (34, -82), (60, -56), (64, -30), (44, -18), (8, -16), (-30, -14)]
C_LOBE = [(-66, 2), (-30, 6), (6, 8), (40, 6), (66, 14), (74, 46), (60, 84), (16, 104), (-34, 100), (-66, 70), (-74, 32)]
SITE = (40, 18)
LOOP_OFF = [(-4, 10), (16, 14), (30, 4), (44, 6), (56, 20), (58, 38), (46, 50)]
LOOP_ON = [(-4, 10), (14, 18), (22, 34), (34, 50), (52, 56), (66, 46)]


class Kin:
    def __init__(self, ox, oy):
        self.ox, self.oy = ox, oy

    def P(self, v):
        return (self.ox + v[0], self.oy + v[1])

    def draw(self, out, on=False):
        hx, hy = self.P((-62, -24))
        out.append(f'<rect x="{hx:.2f}" y="{hy:.2f}" width="15" height="34" rx="3" fill="#d0e9f4" stroke="{LSTROKE}" stroke-width="1"/>')
        for pts, fill in ((C_LOBE, CFILL), (N_LOBE, NFILL)):
            p = chaikin([self.P(v) for v in pts], 4)
            out.append(f'<path d="{closed_path(p)}" fill="{fill}" stroke="{LSTROKE}" stroke-width="1" stroke-linejoin="round"/>')
        sx, sy = self.P(SITE)
        out.append(f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="11" fill="#ffffff" stroke="{NAVY}" stroke-width="1" stroke-dasharray="2.4 2"/>')
        mini_atp(out, *self.P((-16, -3)))
        loop = [self.P(v) for v in (LOOP_ON if on else LOOP_OFF)]
        d = catmull(loop)
        out.append(f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round"/>')
        out.append(f'<path d="{d}" fill="none" stroke="{LOOP}" stroke-width="4" stroke-linecap="round"/>')
        if not on:
            bead(out, *self.P((40, 15)), "Y")
            bead(out, *self.P((57, 30)), "T")
        else:
            for (bx, by), pp, pl in (((22, 34), (8, 44), [(-6, 40), (4, 60)]), ((52, 56), (52, 74), [(36, 80), (66, 82)])):
                X, Y = self.P((bx, by)); PX, PY = self.P(pp)
                for q in pl:
                    QX, QY = self.P(q)
                    out.append(f'<path d="M{PX:.2f} {PY:.2f}L{QX:.2f} {QY:.2f}" stroke="{DARK}" stroke-width="0.9" stroke-dasharray="1.6 1.6"/>')
                out.append(f'<path d="M{X:.2f} {Y:.2f}L{PX:.2f} {PY:.2f}" stroke="{PHOS}" stroke-width="2"/>')
                for q in pl:
                    QX, QY = self.P(q)
                    out.append(f'<circle cx="{QX:.2f}" cy="{QY:.2f}" r="5" fill="{ARG}"/>')
                    out.append(plus(QX, QY, 2.7))
                bead(out, X, Y, "T" if bx < 30 else "Y")
                phosphate(out, PX, PY)


def bead(out, x, y, ch):
    out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="6" fill="#ffffff" stroke="{LOOP}" stroke-width="1.8"/>')
    out.append(T(x, y + 3.4, ch, 9, 700, LOOP, "middle"))


def mini_atp(out, x, y):
    out.append(f'<rect x="{x - 9:.2f}" y="{y - 6.5:.2f}" width="18" height="13" rx="4" fill="{GREEN}"/>')
    for i in range(3):
        out.append(f'<circle cx="{x + 14 + i * 8.5:.2f}" cy="{y:.2f}" r="4" fill="{PHOS}" stroke="#ffffff" stroke-width="0.8"/>')


def plus(x, y, r, col="#ffffff", sw=1.3):
    return (f'<path d="M{x - r:.2f} {y:.2f}H{x + r:.2f}M{x:.2f} {y - r:.2f}V{y + r:.2f}" '
            f'stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>')


def phosphate(out, x, y, r=6.2):
    out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{PHOS}" stroke="#ffffff" stroke-width="1"/>')
    out.append(T(x, y + r * 0.55, "P", r * 1.55, 700, DARK, "middle", dark=DARK_PAGE))


def leader(out, x0, y0, x1, y1, dot=True):
    out.append(f'<path d="M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}" stroke="{GREY_LINE}" stroke-width="0.8" fill="none"/>')
    if dot:
        out.append(f'<circle cx="{x1:.2f}" cy="{y1:.2f}" r="1.8" fill="{GREY_LINE}"/>')


def note(out, x, y, lines, bold=None, lh=15):
    for i, l in enumerate(lines):
        w = 700 if (bold is not None and i == 0) else 400
        c = DARK if w == 700 else MUTED
        out.append(T(x, y + i * lh, l, 12, w, c))
    return y + (len(lines) - 1) * lh


def heading(out, y, n, title, sub, sx):
    out.append(f'<circle cx="19" cy="{y - 4.5:.2f}" r="9" fill="{NAVY}"/>')
    out.append(T(19, y, str(n), 11, 700, "#ffffff", "middle"))
    out.append(T(34, y, title, 13, 700, DARK))
    out.append(T(34 + sx + 8, y, sub, 12, 400, MUTED))


def varrow(out, x, y0, y1, col=DARK):
    d = 1 if y1 > y0 else -1
    out.append(f'<path d="M{x:.2f} {y0:.2f}V{y1 - d * 6:.2f}" stroke="{col}" stroke-width="1.6" fill="none"/>')
    out.append(f'<path d="M{x - 4.5:.2f} {y1 - d * 7:.2f}L{x:.2f} {y1:.2f}L{x + 4.5:.2f} {y1 - d * 7:.2f}Z" fill="{col}"/>')


def harrow(out, x0, x1, y, col=DARK):
    out.append(f'<path d="M{x0:.2f} {y:.2f}H{x1 - 6:.2f}" stroke="{col}" stroke-width="1.6" fill="none"/>')
    out.append(f'<path d="M{x1 - 7:.2f} {y - 4.5:.2f}L{x1:.2f} {y:.2f}L{x1 - 7:.2f} {y + 4.5:.2f}Z" fill="{col}"/>')


def adenosine(out, x, y):
    out.append(f'<rect x="{x - 14:.2f}" y="{y - 10:.2f}" width="28" height="20" rx="6" fill="{GREEN}"/>')
    out.append(T(x, y + 4.3, "A", 12, 700, DARK, "middle", dark=DARK_PAGE))


def chain(out, x0, y, n, gap=17, r=7.2, skip=None):
    out.append(f'<path d="M{x0:.2f} {y:.2f}H{x0 + (n - 1) * gap:.2f}" stroke="{LSTROKE}" stroke-width="1.6"/>')
    for i in range(n):
        cx = x0 + i * gap
        if i == skip:
            out.append(f'<circle cx="{cx:.2f}" cy="{y:.2f}" r="{r + 1:.2f}" fill="#ffffff" stroke="{NAVY}" stroke-width="1.6"/>')
            out.append(T(cx, y + 4, "S", 11, 700, NAVY, "middle"))
        else:
            out.append(f'<circle cx="{cx:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{CFILL}" stroke="{LSTROKE}" stroke-width="1"/>')


def fig():
    out = []
    KX = 86.0
    NX = 184.0

    # ---------------- panel 1: off
    y = 26.0
    heading(out, y, 1, "Off", "loop folded shut", 19)
    oy = y + 16 + 84
    k = Kin(KX, oy)
    k.draw(out)
    out.append(T(KX - 4, oy - 44, "upper lobe", 12, 700, DARK, "middle"))
    out.append(T(KX - 8, oy + 66, "lower lobe", 12, 700, DARK, "middle"))
    ty = oy - 52
    note(out, NX, ty, ["ATP sits in the cleft", "between the two lobes"])
    leader(out, NX - 4, ty - 4, *k.P((-14, -7)))
    ty2 = ty + 44
    ty2 = oy - 16
    note(out, NX, ty2 + 4, ["A hinge joins the lobes"])
    leader(out, NX - 4, ty2, *k.P((-52, -16)))
    ty3 = oy + 26
    note(out, NX, ty3, ["The activation loop folds", "into the opening. A tyrosine", "(Y) plugs the target site", "(dashed circle)."])
    leader(out, NX - 4, ty3 - 4, *k.P((46, 15)))
    bottom1 = oy + 104

    # ---------------- transition
    y = bottom1 + 18
    varrow(out, KX - 12, y, y + 34)
    varrow(out, KX + 12, y + 34, y)
    out.append(T(KX + 30, y + 13, "Another kinase adds two phosphates", 12, 400, DARK))
    out.append(T(KX + 30, y + 29, "A phosphatase can remove them", 12, 400, MUTED))

    # ---------------- panel 2: on
    y = y + 34 + 30
    heading(out, y, 2, "On", "phosphates reshape the loop", 19)
    oy = y + 16 + 84
    k = Kin(KX, oy)
    k.draw(out, on=True)
    beads = [k.P(v) for v in [(40, 18), (56, 10), (72, 5), (88, 4), (104, 6)]]
    out.append(f'<path d="{catmull(beads)}" stroke="{LSTROKE}" stroke-width="1.6" fill="none"/>')
    for i, (bx, by) in enumerate(reversed(beads)):
        if i == len(beads) - 1:
            out.append(f'<circle cx="{bx:.2f}" cy="{by:.2f}" r="7.2" fill="#ffffff" stroke="{NAVY}" stroke-width="1.6"/>')
            out.append(T(bx, by + 4, "S", 11, 700, NAVY, "middle"))
        else:
            out.append(f'<circle cx="{bx:.2f}" cy="{by:.2f}" r="6.4" fill="{CFILL}" stroke="{LSTROKE}" stroke-width="1"/>')
    ty = oy - 52
    gx, gy = k.P((15, -3))
    sx, sy = k.P((40, 18))
    out.append(f'<path d="M{gx + 3:.2f} {gy + 4:.2f}C{gx + 10:.2f} {gy + 16:.2f} {sx - 18:.2f} {sy - 2:.2f} {sx - 10:.2f} {sy - 1:.2f}" stroke="{DARK}" stroke-width="1.3" fill="none"/>')
    out.append(f'<path d="M{sx - 14:.2f} {sy - 4.5:.2f}L{sx - 7.5:.2f} {sy - 0.8:.2f}L{sx - 14:.2f} {sy + 2.5:.2f}Z" fill="{DARK}"/>')
    note(out, NX, ty, ["The target protein docks in", "the open site. Its serine (S)", "is next to ATP, ready to", "take ATP's last phosphate."])
    leader(out, NX - 4, ty - 4, *k.P((96, 0)))
    ty2 = oy + 30
    note(out, NX, ty2, ["Phosphates (P) on T and Y", "are negative. Each pairs", "with positive charges (+),", "pulling the loop into a", "new shape."])
    leader(out, NX - 4, ty2 - 4, *k.P((60, 74)), dot=False)
    bottom2 = oy + 104

    # ---------------- panel 3: at work
    y = bottom2 + 40
    heading(out, y, 3, "At work", "the phosphate moves onto the serine", 48)
    y += 34
    ax0 = 30.0
    adenosine(out, ax0, y)
    for i in range(3):
        phosphate(out, ax0 + 24 + i * 15, y, 6.4)
    out.append(T(ax0 + 22, y - 15, "ATP", 12, 700, DARK, "middle"))
    cy = y + 46
    chain(out, 22, cy, 6, skip=3)
    sx = 22 + 3 * 17
    pxg = ax0 + 24 + 2 * 15
    out.append(f'<path d="M{pxg + 3:.2f} {y + 7:.2f}C{pxg + 14:.2f} {y + 24:.2f} {sx + 10:.2f} {cy - 22:.2f} {sx + 3:.2f} {cy - 12:.2f}" stroke="{DARK}" stroke-width="1.4" fill="none"/>')
    out.append(f'<path d="M{sx - 1.5:.2f} {cy - 15.5:.2f}L{sx + 2:.2f} {cy - 9.5:.2f}L{sx + 6.8:.2f} {cy - 14.6:.2f}Z" fill="{DARK}"/>')
    out.append(T(22 + 2.5 * 17, cy + 25, "target protein, with", 12, 400, MUTED, "middle"))
    out.append(T(22 + 2.5 * 17, cy + 40, "the serine from step 2", 12, 400, MUTED, "middle"))

    harrow(out, 144, 176, y + 23)
    rx = 204.0
    adenosine(out, rx, y)
    for i in range(2):
        phosphate(out, rx + 24 + i * 15, y, 6.4)
    out.append(T(rx + 15, y - 15, "ADP", 12, 700, DARK, "middle"))
    out.append(T(rx + 52, y - 1, "ADP leaves, and a", 12, 400, MUTED))
    out.append(T(rx + 52, y + 14, "new ATP takes its place", 12, 400, MUTED))
    chain(out, 190, cy, 6, skip=3)
    sx2 = 190 + 3 * 17
    out.append(f'<path d="M{sx2:.2f} {cy - 8:.2f}V{cy - 15:.2f}" stroke="{PHOS}" stroke-width="2"/>')
    phosphate(out, sx2, cy - 20, 6.4)
    out.append(T(190 + 2.5 * 17, cy + 25, "target leaves, now", 12, 400, MUTED, "middle"))
    out.append(T(190 + 2.5 * 17, cy + 40, "switched on or off", 12, 400, MUTED, "middle"))
    y = cy + 40

    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "A kinase switched off, switched on by phosphates on its activation loop, and moving a phosphate from ATP onto a target protein.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
