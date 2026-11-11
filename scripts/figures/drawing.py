"""General drawing helpers: arrows, pills, smooth curves, leader lines and panel headings."""

import math

from figures.core import DARK, DARK_PAGE, GREEN, INK, GREY_LINE, LBL, SANS, T, esc

CALLOUT = 'fill="none" stroke="#6d6e71" stroke-width="0.7" stroke-dasharray="2.5 2"'


def sine_path(x0, x1, cy, amp, period, start_down=True):
    """Sine wave as cubic Beziers, one per quarter period (standard quarter-sine approximation)."""
    sgn = 1 if start_down else -1
    q = period / 4
    sc = q / (math.pi / 2)
    p1, p2 = 0.512286623, 1.002313686
    n = max(1, round((x1 - x0) / q))
    d = [f"M{x0:.2f} {cy:.2f}"]
    for i in range(n):
        xa = x0 + i * q
        ext = cy + sgn * amp * (1 if i % 4 in (0, 1) else -1)
        if i % 2 == 0:  # centre -> extreme
            c1 = (xa + p1 * sc, cy + (ext - cy) * p1)
            c2 = (xa + p2 * sc, ext)
            end = (xa + q, ext)
        else:  # extreme -> centre
            c1 = (xa + q - p2 * sc, ext)
            c2 = (xa + q - p1 * sc, cy + (ext - cy) * p1)
            end = (xa + q, cy)
        d.append(f"C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {end[0]:.2f} {end[1]:.2f}")
    return " ".join(d)


def arrow(x0, x1, y, col=DARK, sw=1.8, hl=8.4, hw=10.2):
    return (f'<g class="arrow"><path d="M{x0:.2f} {y:.2f}H{x1 - hl + 0.5:.2f}" stroke="{col}" stroke-width="{sw}" fill="none"/>'
            f'<path d="M{x1 - hl:.2f} {y - hw / 2:.2f}L{x1:.2f} {y:.2f}L{x1 - hl:.2f} {y + hw / 2:.2f}Z" fill="{col}"/></g>')


def pill(cx, cy, w, h, label, fill=GREEN, size=5.5):
    return (f'<g class="pill"><rect x="{cx - w / 2:.2f}" y="{cy - h / 2:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{h / 2:.2f}" fill="{fill}"/>'
            + T(cx, cy + size * 0.34, label, size, 600, INK, "middle", dark=DARK_PAGE) + "</g>")


def smooth(pts, closed=False):
    """Catmull-Rom spline through pts as cubic Beziers."""
    P = pts
    ext = ([P[-1]] + P + [P[0], P[1]]) if closed else ([P[0]] + P + [P[-1]])
    d = f"M{P[0][0]:.2f} {P[0][1]:.2f}"
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f"C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}"
    return d + ("Z" if closed else "")


def zoom_lines(c1, r1, c2, r2):
    (x1, y1), (x2, y2) = c1, c2
    th = math.atan2(y2 - y1, x2 - x1)
    a = math.acos((r1 - r2) / math.hypot(x2 - x1, y2 - y1))
    d = ""
    for sg in (1, -1):
        g = th + sg * a
        d += (f"M{x1 + r1 * math.cos(g):.2f} {y1 + r1 * math.sin(g):.2f}"
              f"L{x2 + r2 * math.cos(g):.2f} {y2 + r2 * math.sin(g):.2f}")
    return f'<path class="zoom" d="{d}" {CALLOUT}/>'


def leader(x0, y0, x1, y1):
    return f'<path class="leader" d="M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}" stroke="{GREY_LINE}" stroke-width="0.8" fill="none"/>'


def panel_head(x, y, letter, name, note=None):
    s = f'<text x="{x:.2f}" y="{y:.2f}" font-family="{SANS}" font-size="{LBL:g}" font-weight="700">{esc(letter + ". " + name)}'
    if note:
        s += f'<tspan dx="8" font-weight="400" fill="#4d4d4f">{esc(note)}</tspan>'
    return s + "</text>"
