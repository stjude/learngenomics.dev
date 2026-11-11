"""Figure 1.1: Deoxyribonucleic acid (DNA). The helix and legend come from the Illustrator artboard in figures/data."""

from figures.core import BLUE, RED, T, copyright_text, main, svg_doc
from figures.biology import base_path
from figures.artboard import inner, load_artboard

NAME = "1.1-dna"


def fig():
    svg = load_artboard("dna")
    defs, body = inner(svg)
    # body lines: helix = clip_1 group, 3'/5' text, clip_2 group; then DNA title,
    # legend text, "base pairs", clip_3 group (pointer + legend bars), copyright.
    helix, legend = [], []
    in_legend = False
    for l in body:
        if l.startswith("<text"):
            if ">DNA<" in l or "base pairs" in l or "\u00a9" in l:
                continue
            (legend if "Adenine" in l else helix).append(l)
        elif l.startswith('<g clip-path="url(#clip_3)'):
            in_legend = True; legend.append(l)
        elif l.startswith("<path") and 'stroke="#000000"' in l:
            continue
        elif l.startswith("<g clip-path") or l.startswith("<path"):
            (legend if in_legend else helix).append(l)
        elif l == "</g>":
            if in_legend:
                legend.append(l); in_legend = None
            elif in_legend is False:
                helix.append(l)
    s, tx, ty = 0.86, 207.9, 33.25
    out = defs[:]
    out.append(T(35.25, 34.5, "Deoxyribonucleic Acid (DNA)", 16.5, 700))
    out.append(T(35.25, 60.5, "Computational Abstraction", 14, 300))
    out.append(T(259.25, 60.5, "Physical Reality", 14, 300))
    # computational abstraction: one strand
    out.append('<g id="computational-strand">')
    out.append(f'<rect x="85.75" y="79.5" width="5.75" height="211.75" fill="{BLUE}"/>')
    for k, b in enumerate("AACTCGAGACTGG"):
        cy = 84.0 + k * 16.96
        out.append(base_path(b, 91.5, cy, 30.25, 3.5))
        out.append(T(71.75, cy + 4.6, b, 13.5, 300, anchor="middle"))
    out.append("</g>")
    # physical reality: helix from artboard 28, scaled
    out.append(f'<g id="helix" transform="matrix({s},0,0,{s},{tx},{ty})">')
    out += helix
    sw = 1.2 / s
    # red outlines in helix coordinates: "base" (purple base of rung 2), "base pair" (rung 3)
    out.append(f'<rect x="85.7" y="100.4" width="38" height="5.8" rx="2" fill="none" stroke="{RED}" stroke-width="{sw:.3f}"/>')
    out.append(f'<rect x="65.6" y="110.0" width="68" height="6.1" rx="2" fill="none" stroke="{RED}" stroke-width="{sw:.3f}"/>')
    out.append("</g>")
    bx, by = 123.7 * s + tx, 103.3 * s + ty
    px, py = 133.6 * s + tx, 113.05 * s + ty
    out.append(f'<path d="M{bx:.2f} {by:.2f}L345.75 93.75" fill="none" stroke="{RED}" stroke-width="1.1" stroke-linecap="round"/>')
    out.append(f'<path d="M{px:.2f} {py:.2f}L346.25 110.25" fill="none" stroke="{RED}" stroke-width="1.1" stroke-linecap="round"/>')
    out.append(T(350.5, 96.0, "base", 8.7, 400))
    out.append(T(350.5, 110.5, "base pair", 8.7, 400))
    out.append('<g id="legend" transform="translate(183,0)">')
    out += legend
    out.append("</g>")
    out.append(copyright_text(469.25, 351.25))
    return svg_doc(441.98, 343.74, out, "Deoxyribonucleic acid (DNA)", origin=(31.26, 13.5), fmt=".2f")


if __name__ == "__main__":
    main(NAME, fig)
