"""Figure 3.8: The BCR-ABL1 fusion protein: domain maps of BCR, ABL1 and the fusion."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, ORANGE, RED, SANS, T, esc, main, svg_doc

NAME = "3.8-bcr-abl1-protein"


def fig():
    BCRC, ABLC = BLUE, ORANGE
    out = ['<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
           f'<path d="M0 0L10 5L0 10Z" fill="{GREY_LINE}"/></marker>'
           '<marker id="ahs" viewBox="0 0 10 10" refX="2" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
           f'<path d="M10 0L0 5L10 10Z" fill="{GREY_LINE}"/></marker></defs>']
    BH, G, BRK = 26.0, 1.5, 3.5                      # bar height, gap between domains, half-gap at a break/junction

    def seg(x, y, w, col, label, strong=False, lost=False):
        if lost:
            s = (f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{BH:g}" rx="3" fill="{GREY_LINE}" fill-opacity="0.06" '
                 f'stroke="{GREY_LINE}" stroke-width="1" stroke-dasharray="3 2"/>')
        else:
            s = (f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{BH:g}" rx="3" fill="{col}" '
                 f'fill-opacity="{0.42 if strong else 0.13}" stroke="{col}" stroke-width="{1.4 if strong else 0.9}"/>')
        cx, cy = x + w / 2, y + BH / 2
        lines = label.split("\n")
        size, wt, fill = (LBL, 600, DARK) if strong else (10, 400, MUTED)
        for i, t in enumerate(lines):
            s += T(cx, cy + size * 0.36 + (i - (len(lines) - 1) / 2) * 10.5, t, size, wt, fill, "middle")
        return s

    def bar(x, y, parts):
        """parts: (width, colour, label, kind) with kind in '', 'strong', 'lost'; returns svg and end x."""
        s = ""
        for k, (w, col, lab, kind) in enumerate(parts):
            s += seg(x, y, w, col, lab, kind == "strong", kind == "lost")
            x += w + G
        return s, x - G

    def name(x, y, title, sub):
        return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{LBL:g}" font-weight="700">{esc(title)}'
                f'<tspan dx="5" font-weight="400" fill="{MUTED}">{esc(sub)}</tspan></text>')

    X0, XR = 8.0, 392.0
    bcr_kept = [(74, BCRC, "Coiled coil", "strong"), (44, BCRC, "Ser/Thr\nkinase", ""), (46, BCRC, "Rho-GEF", "")]
    J = X0 + sum(p[0] for p in bcr_kept) + G * (len(bcr_kept) - 1) + BRK
    abl_kept = [(30, ABLC, "SH3", ""), (30, ABLC, "SH2", ""), (74, ABLC, "Kinase", "strong")]
    tail_w = XR - (J + BRK) - sum(p[0] for p in abl_kept) - G * len(abl_kept)
    abl_kept.append((tail_w, ABLC, "Tail", ""))
    CAPW = 40.0
    Y1, Y2, Y3 = 32.0, 88.0, 150.0
    out.append('<g class="domain-maps">')
    # guides from the parents' kept parts down to the fusion
    gd = f'stroke="{GREY_LINE}" stroke-width="0.8" stroke-dasharray="1.5 2.5"'
    out.append(f'<path class="guide" d="M{X0:.2f} {Y1 + BH:.2f}V{Y3:.2f}" {gd}/>')
    out.append(f'<path class="guide" d="M{XR:.2f} {Y2 + BH:.2f}V{Y3:.2f}" {gd}/>')
    out.append(f'<path class="break" d="M{J:.2f} {Y1 - 5:.2f}V{Y2 + BH + 5:.2f}" stroke="{GREY_LINE}" stroke-width="1.1" stroke-dasharray="4 3"/>')
    out.append(f'<path class="guide" d="M{J:.2f} {Y2 + BH + 5:.2f}V{Y3 - 4:.2f}" {gd}/>')
    # BCR
    out.append(name(X0, Y1 - 8, "BCR", "chromosome 22"))
    s, _ = bar(X0, Y1, bcr_kept); out.append(s)
    s, _ = bar(J + BRK, Y1, [(150, None, "Rest of BCR", "lost")]); out.append(s)
    # ABL1
    xa = J - BRK - CAPW
    out.append(name(xa, Y2 - 8, "ABL1", "chromosome 9"))
    out.append(seg(xa, Y2, CAPW, ABLC, "Cap", strong=True))
    s, _ = bar(J + BRK, Y2, abl_kept); out.append(s)
    # fusion
    out.append(name(X0, Y3 - 8, "BCR-ABL1", "fusion (P210)"))
    s, _ = bar(X0, Y3, bcr_kept); out.append(s)
    s, _ = bar(J + BRK, Y3, abl_kept); out.append(s)
    out.append(f'<path class="junction" d="M{J:.2f} {Y3 - 4:.2f}V{Y3 + BH + 4:.2f}" stroke="{RED}" stroke-width="2.2" stroke-linecap="round"/>')
    out.append("</g>")

    # key
    yk = Y3 + BH + 28
    out.append('<g class="key">'
               + f'<path class="junction" d="M10 {yk - 13:.2f}V{yk + 4:.2f}" stroke="{RED}" stroke-width="2.2" stroke-linecap="round"/>'
               + T(20, yk, "Fusion junction", LBL, 400, MUTED) + "</g>")
    out.append(T(XR, yk + 22, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(392.75, 220.75, out, "The BCR-ABL1 fusion protein: domain maps of BCR, ABL1 and the fusion",
                   origin=(3.25, 11.25), fmt=".2f")


if __name__ == "__main__":
    main(NAME, fig)
