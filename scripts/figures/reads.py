"""Sequencing reads: adapter color and the paired-end read and fragment glyphs."""

from figures.core import FAINT_BASE, GREY_LINE, ORANGE, PURPLE, TEAL

ADAPT_C = FAINT_BASE
R1_C, R2_C, ADP_C, INS_C = TEAL, PURPLE, ORANGE, GREY_LINE
PE_DEFS = ('<defs>' + "".join(
    f'<pattern id="hatch-{c[1:]}" patternUnits="userSpaceOnUse" width="4" height="4" patternTransform="rotate(45)">'
    f'<rect width="4" height="4" fill="{c}" fill-opacity="0.18"/><path d="M0 0V4" stroke="{c}" stroke-width="2"/></pattern>'
    for c in (R1_C, R2_C)) + '</defs>')


def pe_read(xs, xe, y, col, hatch=None, h=6.0, hl=7.0):
    """Read from xs to xe (either direction); hatch=(xa, xb) marks the stretch that reads into adapter."""
    d = 1 if xe > xs else -1
    xb = xe - d * hl
    a, b = sorted((xs, xb))
    s = f'<g class="read"><rect x="{a:.2f}" y="{y - h / 2:.2f}" width="{b - a:.2f}" height="{h:.2f}" fill="{col}"/>'
    if hatch:
        ha, hb = sorted(hatch)
        ha, hb = max(ha, a), min(hb, b)
        s += (f'<rect class="into-adapter" x="{ha:.2f}" y="{y - h / 2:.2f}" width="{hb - ha:.2f}" height="{h:.2f}" '
              f'fill="#ffffff"/><rect x="{ha:.2f}" y="{y - h / 2:.2f}" width="{hb - ha:.2f}" height="{h:.2f}" '
              f'fill="url(#hatch-{col[1:]})" stroke="{col}" stroke-width="0.8"/>')
    s += f'<path d="M{xb:.2f} {y - h / 2 - 2.5:.2f}L{xe:.2f} {y:.2f}L{xb:.2f} {y + h / 2 + 2.5:.2f}Z" fill="{col}"/></g>'
    return s


def pe_fragment(x0, ad, ins, y, h=8.0):
    return (f'<g class="fragment"><rect class="adapter" x="{x0:.2f}" y="{y - h / 2:.2f}" width="{ad:.2f}" height="{h:.2f}" fill="{ADP_C}"/>'
            f'<rect class="insert" x="{x0 + ad:.2f}" y="{y - h / 2:.2f}" width="{ins:.2f}" height="{h:.2f}" fill="{INS_C}"/>'
            f'<rect class="adapter" x="{x0 + ad + ins:.2f}" y="{y - h / 2:.2f}" width="{ad:.2f}" height="{h:.2f}" fill="{ADP_C}"/></g>')
