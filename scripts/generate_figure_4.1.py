"""Figure 4.1: Sequencing by synthesis."""

from figures.core import COPYRIGHT, DARK, FAINT_BASE, GREY_LINE, LBL, PURPLE, T, main, svg_doc
from figures.drawing import arrow, leader, panel_head
from figures.sequences import BASE_C, base_cells
from figures.reads import ADAPT_C

NAME = "4.1-sequencing-by-synthesis"


def vstrand(x, ybot, ins="TGACGTAC", seg=5.5, ad0=16.0, ad1=12.0, sw=2.6):
    """A library strand standing up from ybot: adapter, base-colored insert, adapter."""
    s = f'<g class="strand"><path d="M{x:.2f} {ybot:.2f}V{ybot - ad0:.2f}" stroke="{ADAPT_C}" stroke-width="{sw}"/>'
    y = ybot - ad0
    for b in ins:
        s += f'<path d="M{x:.2f} {y:.2f}V{y - seg:.2f}" stroke="{BASE_C[b]}" stroke-width="{sw}"/>'
        y -= seg
    s += f'<path d="M{x:.2f} {y:.2f}V{y - ad1:.2f}" stroke="{ADAPT_C}" stroke-width="{sw}" stroke-linecap="round"/></g>'
    return s


def fig():
    W, H = 400.0, 380.0
    MUTED = "#4d4d4f"
    out = []
    YS = 136.0                                     # flow cell surface (top edge)

    def surface(x0, x1, anchors, skip=()):
        s = f'<g class="flow-cell"><rect x="{x0:.2f}" y="{YS:.2f}" width="{x1 - x0:.2f}" height="7" rx="2" fill="{GREY_LINE}" fill-opacity="0.35"/>'
        for ax in anchors:
            if any(a <= ax <= b for a, b in skip):
                continue
            s += f'<path d="M{ax:.2f} {YS:.2f}V{YS - 14:.2f}" stroke="{ADAPT_C}" stroke-width="2.2" stroke-linecap="round"/>'
        return s + "</g>"

    # a. loading
    out.append(panel_head(8, 20, "a", "Loading"))
    out.append(surface(8, 192, [11 + 15 * i for i in range(12)]))
    fx = 61.0                                      # fragment, paired with the anchor at x=56
    out.append('<g class="pairing">' + "".join(
        f'<path d="M56.8 {YS - 2.5 - 2.6 * i:.2f}H{fx - 0.8:.2f}" stroke="{GREY_LINE}" stroke-width="0.7"/>' for i in range(5)) + "</g>")
    out.append(vstrand(fx, YS - 1, ad0=17))
    ytop = YS - 1 - 17 - 44 - 12
    out.append(leader(fx + 4, ytop + 5, 88, ytop + 14) + leader(fx + 4, YS - 12, 88, ytop + 24))
    out.append(T(92, ytop + 23, "Adapters", LBL))
    out.append(leader(fx - 4, YS - 40, 46, YS - 52) + T(42, YS - 48, "Insert", LBL, anchor="end"))
    out.append(leader(161, YS - 16, 155, YS - 26) + T(192, YS - 30, "Surface strands", LBL, anchor="end"))
    out.append(T(8, YS + 22, "Flow cell surface", LBL, 400, MUTED))

    # b. clustering
    out.append(panel_head(208, 20, "b", "Clustering"))
    CX0, CN, CS = 230.0, 10, 5.4
    out.append(f'<rect class="cluster-spot" x="{CX0 - 7:.2f}" y="{ytop - 6:.2f}" width="{CS * (CN - 1) + 14:.2f}" height="{YS - ytop + 4:.2f}" rx="8" '
               f'fill="{GREY_LINE}" fill-opacity="0.1"/>')
    out.append(surface(208, 392, [214] + [292 + 15 * i for i in range(7)]))
    out.append('<g class="cluster">' + "".join(vstrand(CX0 + CS * i, YS, ad0=16, sw=2.2) for i in range(CN)) + "</g>")
    lx = CX0 + CS * (CN - 1) + 14
    out.append(T(lx, ytop + 14, "Cluster:", LBL, 600) + T(lx, ytop + 29, "thousands of", LBL) + T(lx, ytop + 44, "identical copies", LBL))

    # c. cycling
    YC = 196.0
    out.append(f'<path class="divider" d="M8 {YC - 22:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.5"/>')
    out.append(panel_head(8, YC, "c", "Cycling", "one strand in the cluster"))
    X0, CW = 84.0, 20.0
    YCOPY, YTMP = YC + 50, YC + 76
    copy, tmpl = "TGAC", "ACTGTAG"
    out.append('<g class="pairing">' + "".join(
        f'<path d="M{X0 + CW * (i + 0.5):.2f} {YCOPY + 8:.2f}V{YTMP - 8:.2f}" stroke="{GREY_LINE}" stroke-width="0.8"/>' for i in range(4)) + "</g>")
    out.append(T(8, YCOPY + LBL * 0.36, "New copy", LBL, 600) + T(8, YTMP + LBL * 0.36, "Template", LBL, 400, MUTED))
    out.append(base_cells(X0, CW, YCOPY, list(copy), size=16))
    out.append('<g class="template">' + "".join(T(X0 + CW * (i + 0.5), YTMP + 5.8, b, 16, 700, FAINT_BASE, "middle", mono=True) for i, b in enumerate(tmpl)) + "</g>")
    nx = X0 + CW * 3.5                             # newest base: dye + cap
    out.append(f'<g class="dye"><path d="M{nx:.2f} {YCOPY - 10:.2f}V{YCOPY - 17:.2f}" stroke="{GREY_LINE}" stroke-width="1"/>'
               f'<circle cx="{nx:.2f}" cy="{YCOPY - 22:.2f}" r="9" fill="{PURPLE}" fill-opacity="0.18"/>'
               f'<circle cx="{nx:.2f}" cy="{YCOPY - 22:.2f}" r="5" fill="{PURPLE}"/></g>')
    out.append(T(nx - 14, YCOPY - 18, "Dye", LBL, anchor="end"))
    cx_ = X0 + CW * 4 + 1
    out.append(f'<rect class="cap" x="{cx_:.2f}" y="{YCOPY - 9:.2f}" width="6" height="18" rx="1.5" fill="{DARK}"/>')
    out.append(T(cx_ + 12, YCOPY + LBL * 0.36, "Cap", LBL))

    # loop of steps
    SX, SY, SG = 268.0, YC + 30, 26.0
    steps = ["Add one base", "Image", "Remove dye and cap", "Repeat"]
    for i, st in enumerate(steps):
        y = SY + SG * i
        out.append(T(SX, y + LBL * 0.36, f"{i + 1}", LBL, 700, MUTED) + T(SX + 12, y + LBL * 0.36, st, LBL, 600 if i < 3 else 400))
        if i < 3:
            out.append(f'<path class="step-arrow" d="M{SX + 3.6:.2f} {y + 8:.2f}V{y + SG - 9:.2f}M{SX + 0.6:.2f} {y + SG - 12:.2f}L{SX + 3.6:.2f} {y + SG - 8:.2f}L{SX + 6.6:.2f} {y + SG - 12:.2f}" '
                       f'stroke="{GREY_LINE}" stroke-width="1.1" fill="none"/>')
    lx_ = SX - 10
    y1, y0 = SY + SG * 3, SY
    out.append(f'<path class="repeat-arrow" d="M{SX - 3:.2f} {y1:.2f}H{lx_ + 4:.2f}Q{lx_:.2f} {y1:.2f} {lx_:.2f} {y1 - 4:.2f}V{y0 + 4:.2f}Q{lx_:.2f} {y0:.2f} {lx_ + 4:.2f} {y0:.2f}H{SX - 6:.2f}" '
               f'stroke="{GREY_LINE}" stroke-width="1.1" fill="none"/>'
               f'<path d="M{SX - 10:.2f} {y0 - 3.5:.2f}L{SX - 4:.2f} {y0:.2f}L{SX - 10:.2f} {y0 + 3.5:.2f}Z" fill="{GREY_LINE}"/>')

    # camera strip
    YN, YQ = YTMP + 34, YTMP + 52
    out.append(T(8, YN + 3.6, "Cycle", LBL, 400, MUTED) + T(8, YQ + LBL * 0.36, "Camera", LBL, 600))
    s = '<g class="camera">'
    for i, b in enumerate(copy):
        x = X0 + CW * i + 2
        s += T(X0 + CW * (i + 0.5), YN + 3.6, str(i + 1), 10, 400, MUTED, "middle")
        s += f'<rect x="{x:.2f}" y="{YQ - 8:.2f}" width="{CW - 4:.2f}" height="16" rx="2" fill="{BASE_C[b]}"/>'
    s += T(X0 + CW * 4.5, YQ + 4.5, "…", LBL, 700, MUTED, "middle") + "</g>"
    out.append(s)
    ax = X0 + CW * 5 + 4
    out.append(arrow(ax, ax + 26, YQ, col=GREY_LINE, sw=1.4, hl=6, hw=7))
    out.append(T(ax + 34, YQ + LBL * 0.36, "Reads", LBL, 400, MUTED) + base_cells(ax + 72, 13, YQ, list(copy), size=14))
    out.append(T(W - 8, YQ + 32, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, out, "Sequencing by synthesis: loading, clustering and cycling on a flow cell")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="392" height="355.5" viewBox="4 6.75 392 355.5"')


if __name__ == "__main__":
    main(NAME, fig)
