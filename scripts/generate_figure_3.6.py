"""Figure 3.6: Kinds of structural variants."""

from figures.core import (
    BLUE, COPYRIGHT, DARK, GREEN, GREY_LINE, LBLUE, NAVY, ORANGE, PURPLE, RED, T, TEAL, main,
    svg_doc,
)

NAME = "3.6-structural-variant-types"


def fig():
    W, H = 400.0, 640.0
    MUTED = "#4d4d4f"
    BW, BH, GAP, JGAP = 24.0, 18.0, 2.0, 7.0          # block width/height, normal gap, gap at a junction
    TX = 104.0                                        # tracks start here; labels sit to the left
    COLS = {"A": BLUE, "B": TEAL, "C": ORANGE, "D": GREEN, "E": PURPLE, "F": NAVY, "G": LBLUE}
    out = ['<defs><pattern id="unmappable" patternUnits="userSpaceOnUse" width="4" height="4" '
           'patternTransform="rotate(45)"><path d="M0 0V4" stroke="#6d6e71" stroke-width="1.1"/></pattern></defs>']

    def chevron(x, y, w, col, rev=False, dash=False):
        h = BH / 2
        if not rev:
            pts = [(x, y - h), (x + w - 5, y - h), (x + w, y), (x + w - 5, y + h), (x, y + h), (x + 5, y)]
        else:
            pts = [(x + 5, y - h), (x + w, y - h), (x + w - 5, y), (x + w, y + h), (x + 5, y + h), (x, y)]
        d = "M" + "L".join(f"{a:.2f} {b:.2f}" for a, b in pts) + "Z"
        da = ' stroke-dasharray="2.5 1.5"' if dash else ""
        return f'<path d="{d}" fill="{col}" fill-opacity="0.16" stroke="{col}" stroke-width="1.1"{da}/>'

    def tick(x, y):
        return (f'<path class="junction" d="M{x:.2f} {y - BH / 2 - 4:.2f}V{y + BH / 2 + 4:.2f}" stroke="{RED}" '
                f'stroke-width="2.2" stroke-linecap="round"/>')

    def track(x, y, items):
        """items: strings like 'A', 'C~' (reversed), '|D' (junction before D), 'X+' (new), '#' (unmappable)."""
        s = '<g class="track">'
        for k, it in enumerate(items):
            junction = it.startswith("|")
            it = it.lstrip("|")
            if k:
                x += JGAP if junction else GAP
            if junction:
                s += tick(x - JGAP / 2, y)
            if it == "#":
                w = 64.0
                s += (f'<rect class="unmappable" x="{x:.2f}" y="{y - BH / 2:.2f}" width="{w:g}" height="{BH:g}" rx="2" '
                      f'fill="url(#unmappable)" stroke="{GREY_LINE}" stroke-width="1.1"/>')
                x += w
                continue
            rev, new = it.endswith("~"), it.endswith("+")
            L = it.rstrip("~+")
            col = DARK if new else COLS.get(L, GREY_LINE)
            s += chevron(x, y, BW, col, rev, dash=new)
            cx, ty = x + BW / 2 + (0.6 if not rev else -0.6), y + 12.5 * 0.36
            extra = f' transform="matrix(-1 0 0 1 {2 * cx:.2f} 0)"' if rev else ""
            s += T(cx, ty, L, 12.5, 700, DARK, "middle", mono=True, extra=extra)
            x += BW
        return s + "</g>", x

    def label(y, lines):
        s = ""
        for i, (txt, w, c) in enumerate(lines):
            s += T(8, y + 4.5 + i * 14, txt, 12.5, w, c)
        return s

    def note(x, y, lines):
        return "".join(T(x, y + 4.5 + i * 14, t, 12.5, 400, MUTED) for i, t in enumerate(lines))

    ref = list("ABCDE")
    TRK = 24.0                                        # reference to sample spacing
    rows = [
        ("Deletion", ["Unbalanced"], [ref, ["A", "B", "|D", "E"]], ["C lost"]),
        ("Insertion", [], [ref, ["A", "B", "|X+", "|C", "D", "E"]], ["X: new sequence,", "e.g. mobile element"]),
        ("Tandem", ["duplication", "Unbalanced"], [ref, ["A", "B", "C", "|C", "D", "E"]], ["Copy lands right", "after the original"]),
        ("Inversion", ["Balanced"], [ref, ["A", "B", "|C~", "|D", "E"]], ["C reversed", "in place"]),
        ("Translocation", ["Balanced"], None, None),
        ("Single", ["breakend"], [ref, ["A", "B", "C", "|#"]], ["Other side", "can't be placed"]),
        ("Complex", ["(chromothripsis)"], [list("ABCDEFG"), ["A", "|E~", "|C", "|F", "|B~", "|G"]], ["Scrambled, some", "reversed, D lost"]),
    ]
    out.append(T(8, 22, "In each row: reference (top), sample (bottom)", 12.5, 400, MUTED))
    y = 52.0
    for name, sub, tracks, notes in rows:
        out.append(f'<g class="sv-row">')
        out.append(label(y, [(name, 600, None)] + [(t, 400 if t in ("Balanced", "Unbalanced") or name != "Tandem" else 600,
                                                    MUTED if t in ("Balanced", "Unbalanced") else None) for t in sub]))
        if name == "Translocation":
            X2 = TX + 5 * BW + 4 * GAP + 20
            s1, e1 = track(TX, y, list("ABCDE")); s2, _ = track(X2, y, list("VWXYZ"))
            s3, e3 = track(TX, y + TRK, ["A", "B", "C", "|Y", "Z"]); s4, _ = track(X2, y + TRK, ["V", "W", "X", "|D", "E"])
            s5, e5 = track(TX, y + 2 * TRK + 6, ["A", "B", "C", "|Z~", "Y~"])
            out += [s1, s2, s3, s4, s5]
            out.append(T((e1 + X2) / 2, y + 4.5, "+", 12.5, 400, MUTED, "middle"))
            out.append(T((e3 + X2) / 2, y + TRK + 4.5, "+", 12.5, 400, MUTED, "middle"))
            out.append(note(e5 + 10, y + 2 * TRK + 6 - 7, ["Or the moved piece", "arrives reversed"]))
            h = 2 * TRK + 6
        else:
            s1, e1 = track(TX, y, tracks[0]); s2, e2 = track(TX, y + TRK, tracks[1])
            out += [s1, s2]
            out.append(note(max(e1, e2) + 10, y, notes))
            h = TRK
        out.append("</g>")
        y += h + 46
        if name != "Complex":
            out.append(f'<path class="divider" d="M8 {y - 25:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.5"/>')
    # legend
    ly = y - 8
    out.append('<g class="key">')
    out.append(f'<path class="junction" d="M19 {ly - 13:.2f}V{ly + 4:.2f}" stroke="{RED}" stroke-width="2.2" stroke-linecap="round"/>'
               + T(36, ly, "Junction", 12.5, 400, MUTED))
    out.append(f'<rect x="120" y="{ly - 13.5:.2f}" width="22" height="18" rx="2" fill="url(#unmappable)" stroke="{GREY_LINE}" stroke-width="1.1"/>'
               + T(148, ly, "Unmappable sequence", 12.5, 400, MUTED))
    out.append(chevron(8, ly + 24 - 4.5, 22, GREY_LINE, rev=True) + T(36, ly + 24, "Reversed (fold-back) segment", 12.5, 400, MUTED))
    out.append("</g>")
    out.append(T(W - 8, ly + 50, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, out, "Kinds of structural variants: deletion, insertion, tandem duplication, inversion, translocation, single breakend and complex rearrangement")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="392.75" height="612" viewBox="3.25 8.5 392.75 612"')


if __name__ == "__main__":
    main(NAME, fig)
