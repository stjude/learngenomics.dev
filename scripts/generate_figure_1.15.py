"""Figure 1.15: Same genotype, different haplotypes."""

from figures.core import BLUE, DARK, GREEN, GREY_LINE, RED, T, copyright_text, main, svg_doc
from figures.drawing import arrow

NAME = "1.15-same-genotype-different-haplotypes"


def fig():
    W, H = 400.0, 240.0
    MUTED = "#4d4d4f"
    YS = (88.0, 124.0)                      # strand centre lines: copy from parent 1, parent 2
    VX = (66.0, 112.0)                      # F508del, G542X positions (panel-relative)
    out = [T(8, 18, "Same genotype, different haplotypes", 10, 700)]

    def channel(cx, cy, ok):
        d = ""
        for x0 in (cx - 9, cx + 1.5):
            d += f'<rect x="{x0:.2f}" y="{cy - 11:.2f}" width="7.5" height="22" rx="3.5"/>'
        if ok:
            return f'<g class="channel working" fill="{BLUE}" fill-opacity="0.45" stroke="{BLUE}" stroke-width="1">{d}</g>'
        return (f'<g class="channel not-working"><g fill="{GREY_LINE}" fill-opacity="0.08" stroke="{GREY_LINE}" '
                f'stroke-opacity="0.6" stroke-width="0.8" stroke-dasharray="2 1.5">{d}</g>'
                f'<path d="M{cx - 7:.2f} {cy - 7:.2f}L{cx + 7:.2f} {cy + 7:.2f}M{cx + 7:.2f} {cy - 7:.2f}L{cx - 7:.2f} {cy + 7:.2f}" '
                f'stroke="{MUTED}" stroke-width="1.6" stroke-linecap="round"/></g>')

    panels = ((6.0, "Both on one copy", ((True, True), (False, False)), "Carrier, no cystic fibrosis", GREEN),
              (204.0, "One on each copy", ((True, False), (False, True)), "Cystic fibrosis", RED))
    for px, title, hits, outcome, ocol in panels:
        cls = "panel-" + title.lower().replace(" ", "-")
        out.append(f'<g class="{cls}">')
        out.append(T(px + 95, 44, title, 9, 700, anchor="middle"))
        # position guides and column labels
        for vx, name in zip(VX, ("F508del", "G542X")):
            out.append(f'<path d="M{px + vx:.2f} {68:.2f}V{YS[1] + 9:.2f}" stroke="{GREY_LINE}" stroke-width="0.6" stroke-dasharray="1.5 1.5"/>')
            out.append(T(px + vx, 64, name, 8, 600, anchor="middle"))
        out.append(T(px + 170, 64, "Protein", 8, 600, MUTED, "middle"))
        for (y, (h1, h2), who) in zip(YS, hits, ("1", "2")):
            out.append(T(px + 1, y - 1.5, "Copy from", 8, 400))
            out.append(T(px + 1, y + 7.5, f"parent {who}", 8, 400))
            out.append(f'<rect class="strand" x="{px + 42:.2f}" y="{y - 2.5:.2f}" width="96" height="5" rx="1" fill="{BLUE}"/>')
            for vx, hit in zip(VX, (h1, h2)):
                if hit:
                    out.append(f'<circle class="variant" cx="{px + vx:.2f}" cy="{y:.2f}" r="5" fill="{RED}" stroke="#ffffff" stroke-width="1"/>')
                else:
                    out.append(f'<circle class="typical" cx="{px + vx:.2f}" cy="{y:.2f}" r="3" fill="#ffffff" stroke="{GREY_LINE}" stroke-width="0.8"/>')
            out.append(arrow(px + 143, px + 156, y, col=GREY_LINE, sw=1, hl=4.5, hw=5))
            out.append(channel(px + 170, y, not (h1 or h2)))
        # outcome
        out.append(f'<rect class="outcome" x="{px + 30:.2f}" y="{146:.2f}" width="130" height="19" rx="9.5" '
                   f'fill="{ocol}" fill-opacity="0.14" stroke="{ocol}" stroke-width="1"/>')
        out.append(T(px + 95, 158.8, outcome, 9, 700, anchor="middle"))
        # genotype calls: identical in both panels
        out.append(f'<rect class="genotype-calls" x="{px + 30:.2f}" y="178" width="130" height="40" rx="3" '
                   f'fill="{GREY_LINE}" fill-opacity="0.07" stroke="{GREY_LINE}" stroke-width="0.8"/>')
        out.append(T(px + 95, 189.5, "Genotype calls", 7.5, 600, MUTED, "middle"))
        out.append(T(px + 95, 201, "F508del: heterozygous", 8, 400, anchor="middle"))
        out.append(T(px + 95, 211.5, "G542X: heterozygous", 8, 400, anchor="middle"))
        out.append("</g>")
    out.append(f'<path class="divider" d="M200 34V168" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.6"/>')
    out.append(T(200, 202.5, "=", 14, 700, DARK, "middle"))
    ky = H - 8
    out.append(f'<g class="key"><circle cx="12" cy="{ky - 2.6:.2f}" r="3.6" fill="{RED}" stroke="#ffffff" stroke-width="0.8"/>'
               + T(19, ky, "Variant", 7.5, 400, MUTED)
               + f'<circle cx="56" cy="{ky - 2.6:.2f}" r="3" fill="#ffffff" stroke="{GREY_LINE}" stroke-width="0.8"/>'
               + T(62, ky, "Typical", 7.5, 400, MUTED) + "</g>")
    out.append(copyright_text(W - 6, H - 8))
    svg = svg_doc(W, H, out, "Same genotype, different haplotypes: the same genotype calls give a healthy carrier or cystic fibrosis")
    # crop to content plus about 4 units of padding
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"',
                       'width="394.75" height="231" viewBox="3.25 6.75 394.75 231"')


if __name__ == "__main__":
    main(NAME, fig)
