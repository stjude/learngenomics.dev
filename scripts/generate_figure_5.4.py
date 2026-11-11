"""Figure 5.4: Marking duplicates."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, ORANGE, T, main, svg_doc

NAME = "5.4-duplicates"

RL, H8 = 64.0, 8


def bar(x0, x1, y, dup=False):
    if dup:
        return (f'<rect class="read duplicate" x="{x0 + 0.45:.2f}" y="{y - H8 / 2 + 0.45:.2f}" width="{x1 - x0 - 0.9:.2f}" '
                f'height="{H8 - 0.9}" rx="1.5" fill="none" stroke="{BLUE}" stroke-width="0.9" stroke-dasharray="3 2"/>')
    return f'<rect class="read" x="{x0:.2f}" y="{y - H8 / 2:.2f}" width="{x1 - x0:.2f}" height="{H8}" rx="1.5" fill="{BLUE}" fill-opacity="0.55"/>'


def pair(s, e, y, dup=False, err=None):
    out = f'<g class="read-pair"><path d="M{s + RL:.2f} {y:.2f}H{e - RL:.2f}" stroke="{GREY_LINE}" stroke-width="0.9" stroke-dasharray="1.5 2.5"/>'
    out += bar(s, s + RL, y, dup) + bar(e - RL, e, y, dup)
    if err is not None:
        out += f'<rect class="mismatch" x="{err - 2:.2f}" y="{y - H8 / 2 - 1:.2f}" width="4" height="{H8 + 2}" fill="{ORANGE}"/>'
    return out + "</g>"


def fig():
    W = 400.0
    out = []
    S, E, E2, ERR = 140.0, 384.0, 336.0, 176.0
    y = 20.0
    out.append(T(8, y, "Reference", LBL, 700))
    yref = y + 14
    out.append(f'<path class="reference" d="M8 {yref:.2f}H392" stroke="{DARK}" stroke-width="2"/>')
    ylab = yref + 24
    out.append(T((S + E) / 2, ylab, "Both outer ends match", LBL, 600, MUTED, "middle"))
    rows = [yref + 44 + 24 * k for k in range(6)]
    # guides at the shared outer ends
    for gx in (S, E):
        out.append(f'<path class="guide" d="M{gx:.2f} {ylab + 6:.2f}V{rows[3] + 8:.2f}" stroke="{GREY_LINE}" stroke-width="0.8" stroke-dasharray="2 2"/>')
    labels = [("Kept", 600, DARK), ("Duplicate", 400, MUTED), ("Duplicate", 400, MUTED), ("Different end", 400, MUTED)]
    for k, (txt, w, c) in enumerate(labels):
        out.append(T(8, rows[k] + LBL * 0.36, txt, LBL, w, c))
    out.append(pair(S, E, rows[0], err=ERR))
    out.append(pair(S, E, rows[1], dup=True, err=ERR))
    out.append(pair(S, E, rows[2], dup=True, err=ERR))
    out.append(pair(S, E2, rows[3]))
    out.append(T(8, rows[4] + LBL * 0.36, "Other pairs", LBL, 400, MUTED))
    out.append(pair(100, 312, rows[4]))
    out.append(pair(180, 392, rows[5]))
    # key
    ky = rows[5] + 34
    out.append(f'<path d="M8 {ky - 22:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    out.append(f'<rect x="8" y="{ky - 9:.2f}" width="4" height="9" fill="{ORANGE}"/>' + T(18, ky, "Differs from the reference", LBL, 400, MUTED))
    H = ky + 24
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Marking duplicates: read pairs that share both outer ends are copies of one fragment, so one is kept and the rest are marked", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
