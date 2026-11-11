"""Figure 5.6: Comparing calls with a truth set."""

from figures.core import BLUE, COPYRIGHT, DARK, GREY_LINE, LBL, MUTED, PURPLE, RED, T, main, svg_doc

NAME = "5.6-truth-set-comparison"

RH = 24.0
XP, XT, XC, XR = 58, 74, 158, 268
RES = {"TP": ("True positive", BLUE), "FP": ("False positive", RED),
       "FN": ("False negative", PURPLE), "NC": ("Not counted", MUTED)}
ROWS = [(1027, "G>A", "G>A", "TP", None),
        (1042, "C>T", "C>T", "TP", None),
        (1115, "ATGCA>A", "ATGCA>A", "TP", None),
        (1236, None, "T>G", "FP", None),
        (1302, "C>CT", "CTTTT>CTTTTT", "TP", "written differently"),
        (1388, "GA>G", None, "FN", None),
        (1450, "A>G", "A>G", "TP", None),
        (1517, "T>C", None, "FN", None)]
OUT = [(1630, None, "G>C", "NC", "nothing to check it against")]


def row(y, k, r, faded=False):
    pos, t, c, res, note = r
    h = RH + (12 if note else 0)
    cy = y + RH / 2
    o = [f'<rect class="row" x="8" y="{y + 1:.2f}" width="384" height="{h - 2:g}" rx="3" fill="{GREY_LINE}" fill-opacity="{0.07 if k % 2 == 0 else 0}"/>']
    col = MUTED if faded else DARK
    o.append(T(XP, cy + LBL * 0.36, f"{pos:,}", LBL, 500, col, "end", mono=True))
    for x, s in ((XT, t), (XC, c)):
        o.append(T(x, cy + LBL * 0.36, s if s else "none", 11.5 if s else 11, 600 if s else 400,
                   col if s else MUTED, mono=bool(s), extra="" if s else ' font-style="italic"'))
    lab, rc = RES[res]
    o.append(T(XR, cy + LBL * 0.36, lab, LBL, 700, rc))
    if note:
        o.append(T(XR, cy + 13 + 10.5 * 0.36, note, 10.5, 400, MUTED))
    return "".join(o), h


def fig():
    W = 400.0
    out = []
    y = 20.0
    out.append(T(8, y, "Your calls compared with the truth set", 13, 700))
    yh = y + 24
    out.append(T(XP, yh, "Position", 11, 600, MUTED, "end") + T(XT, yh, "Truth set", 11, 600, MUTED)
               + T(XC, yh, "Your calls", 11, 600, MUTED) + T(XR, yh, "Result", 11, 600, MUTED))
    y = yh + 16
    out.append(T(8, y + 4, "Inside the benchmark regions", 10.5, 700, DARK))
    y += 10
    for k, r in enumerate(ROWS):
        s, h = row(y, k, r)
        out.append(s)
        y += h
    y += 14
    out.append(T(8, y + 4, "Outside the benchmark regions", 10.5, 700, MUTED))
    y += 10
    s, h = row(y, 0, OUT[0], faded=True)
    out.append(s)
    y += h
    y += 14
    out.append(f'<path class="divider" d="M8 {y:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.7" stroke-opacity="0.5"/>')
    y += 26
    out.append(T(8, y, "5 true positives, 1 false positive, 2 false negatives", LBL, 400, DARK))
    for name, aka, what, frac in (("Precision", "", "Share of your calls that are right", ("5 of 6", "83%")),
                                  ("Recall", "also called sensitivity", "Share of the true variants you found", ("5 of 7", "71%"))):
        y += 40
        out.append(T(8, y - 4, name, 14, 700, DARK))
        if aka:
            out.append(T(62, y - 4, aka, 11, 400, MUTED))
        out.append(T(8, y + 12, what, 11, 400, MUTED))
        out.append(T(330, y + 4, frac[0], LBL, 400, MUTED, "end"))
        out.append(T(390, y + 4 + 0.5, frac[1], 16, 700, DARK, "end"))
    H = y + 40
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "Comparing calls with a truth set: matches are true positives, extra calls are false positives and missed variants are false negatives", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
