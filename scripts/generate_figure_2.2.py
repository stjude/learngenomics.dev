"""Figure 2.2: The eight hallmarks of cancer."""

from figures.core import (
    BLUE, COPYRIGHT, DARK, GREY_LINE, MUTED, ORANGE, PURPLE, T, TEAL, main, svg_doc,
)

NAME = "2.2-hallmarks"

X0, X1, GAP = 10.0, 390.0, 8.0
CW = (X1 - X0 - GAP) / 2
GROUPS = [
    ("Growing when they shouldn\u2019t", BLUE, "#1460b8", [
        (["Sustaining proliferative", "signaling"], ["divides without an outside", "signal to grow"]),
        (["Evading growth", "suppressors"], ["ignores signals to stop", "dividing"])]),
    ("Refusing to die", PURPLE, PURPLE, [
        (["Resisting cell death"], ["survives damage that should", "trigger self-destruction"]),
        (["Enabling replicative", "immortality"], ["divides past the normal", "limit"])]),
    ("Supplying the tumor", ORANGE, "#a8650a", [
        (["Inducing or accessing", "vasculature"], ["gets a blood supply"]),
        (["Reprogramming cellular", "metabolism"], ["uses nutrients to build", "new cells"])]),
    ("Spreading and hiding", TEAL, "#0b7a88", [
        (["Activating invasion", "and metastasis"], ["invades nearby tissue", "and spreads"]),
        (["Avoiding immune", "destruction"], ["escapes the immune", "system"])]),
]


def card(out, x, y, w, h, col, title, desc, dashed=False):
    if dashed:
        out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="6" fill="none" '
                   f'stroke="{GREY_LINE}" stroke-width="0.9" stroke-dasharray="3 2.5"/>')
    else:
        out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="6" fill="{col}" fill-opacity="0.13" '
                   f'stroke="{col}" stroke-width="1"/>')
        out.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="5" height="{h:.2f}" rx="2" fill="{col}"/>')
    ty = y + 18
    for ln in title:
        out.append(T(x + 13, ty, ln, 12.5, 700, DARK))
        ty += 15
    ty += 2
    for ln in desc:
        out.append(T(x + 13, ty, ln, 11.5, 400, MUTED))
        ty += 14


def fig():
    W = 400.0
    out = []
    y = 22
    out.append(T(X0, y, "The eight hallmarks", 14, 700, DARK))
    y += 20
    CH = 78
    for name, col, lab, cards in GROUPS:
        out.append(T(X0, y, name, 11.5, 700, lab))
        y += 7
        for j, (t, d) in enumerate(cards):
            card(out, X0 + j * (CW + GAP), y, CW, CH, col, t, d)
        y += CH + 20
    y += 6
    out.append(T(X0, y, "Enabling characteristics", 14, 700, DARK))
    out.append(T(X0, y + 16, "processes that help cells gain the hallmarks", 11.5, 400, MUTED))
    y += 26
    EH = 76
    card(out, X0, y, CW, EH, GREY_LINE, ["Genome instability", "and mutation"], ["supplies the changes"])
    card(out, X0 + CW + GAP, y, CW, EH, GREY_LINE, ["Tumor-promoting", "inflammation"], ["immune responses that", "help the tumor"])
    y += EH + 26
    out.append(T(X0, y, "Proposed in 2022", 14, 700, DARK))
    y += 9
    PH = 44
    props = [(["Unlocking phenotypic", "plasticity"]), (["Nonmutational epigenetic", "reprogramming"]),
             (["Polymorphic", "microbiomes"]), (["Senescent cells"])]
    for i, t in enumerate(props):
        r, c = divmod(i, 2)
        x, yy = X0 + c * (CW + GAP), y + r * (PH + GAP)
        card(out, x, yy, CW, PH, GREY_LINE, t, [], dashed=True)
    y += 2 * PH + GAP
    H = y + 30
    out.append(T(392, H - 7, COPYRIGHT, 10, 400, anchor="end"))
    return svg_doc(W - 8, H - 6, out, "The eight hallmarks of cancer, two enabling characteristics and four proposals from 2022.", origin=(4, 6))


if __name__ == "__main__":
    main(NAME, fig)
