"""Figure 4.3: One paired-end fragment up close."""

from figures.core import DARK, GREY_LINE, LBL, MUTED, T, big_copyright, main, svg_doc
from figures.reads import PE_DEFS, R1_C, R2_C, pe_fragment, pe_read

NAME = "4.3-paired-end-read-zoomed"


def fig():
    XL, XR, AD = 34.0, 366.0, 46.0
    IL, IR = XL + AD, XR - AD
    RLEN = 104.0
    R1E, R2E = IL + RLEN, IR - RLEN
    YR1, YB, YR2 = 44.0, 62.0, 80.0
    out = [PE_DEFS]
    out.append(T(XL, 22, "Read 1 adapter", LBL, 600) + T(XR, 22, "Read 2 adapter", LBL, 600, None, "end"))
    out.append(T(R1E + 8, YR1 + 4.5, "Read 1", LBL, 700))
    out.append(pe_fragment(XL, AD, IR - IL, YB, h=10))
    for x, y, t, a in ((XL - 5, YB - 3, "5′", "end"), (XL - 5, YB + 13, "3′", "end"), (XR + 5, YB - 3, "3′", "start"), (XR + 5, YB + 13, "5′", "start")):
        out.append(T(x, y, t, LBL, 400, MUTED, a))
    out.append(pe_read(IL, R1E, YR1, R1_C, h=7))
    out.append(pe_read(IR, R2E, YR2, R2_C, h=7))
    out.append(T((IR + R2E) / 2, YR2 + 22, "Read 2", LBL, 700, None, "middle"))
    dash = lambda x, ya, yb: f'<path d="M{x:.2f} {ya:.2f}V{yb:.2f}" stroke="{GREY_LINE}" stroke-width="1" stroke-dasharray="3 3"/>'

    def bracket(xa, xb, y, label, ty):
        return (f'<g class="measure"><path d="M{xa:.2f} {y - 6:.2f}V{y:.2f}H{xb:.2f}V{y - 6:.2f}" fill="none" stroke="{DARK}" stroke-width="1.2"/>'
                + T((xa + xb) / 2, ty, label, LBL, 600, None, "middle") + "</g>")
    y1, y2, y3 = 132.0, 170.0, 208.0
    out.append(dash(R1E, YR1 + 6, y1 - 6) + dash(R2E, YR2 + 6, y1 - 6) + bracket(R1E, R2E, y1, "Inner distance", y1 + 16))
    out.append(dash(IL, YB + 5, y2 - 6) + dash(IR, YB + 5, y2 - 6) + bracket(IL, IR, y2, "Insert size", y2 + 16))
    out.append(dash(XL, YB + 5, y3 - 6) + dash(XR, YB + 5, y3 - 6) + bracket(XL, XR, y3, "Fragment length", y3 + 16))
    out.append(big_copyright(392, 240))
    return svg_doc(392, 237, out, "One paired-end fragment up close: adapters, reads, inner distance, insert size and fragment length", origin=(4, 9))


if __name__ == "__main__":
    main(NAME, fig)
