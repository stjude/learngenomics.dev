"""Figure 4.4: PacBio HiFi sequencing."""

import math

from figures.core import BLUE, COPYRIGHT, DARK, GREEN, GREY_LINE, LBL, LBLUE, T, main, svg_doc
from figures.drawing import leader, panel_head
from figures.sequences import BASE_C, base_cells, change_box
from figures.reads import ADAPT_C

NAME = "4.4-pacbio-hifi"


def fig():
    W, H = 400.0, 420.0
    MUTED = "#4d4d4f"
    out = []
    # a. library molecule
    out.append(panel_head(8, 20, "a", "Library molecule"))
    L, R, YT, YB = 44.0, 156.0, 74.0, 100.0
    rr = (YB - YT) / 2
    ins_top, ins_bot = "GATCCTAGGTCAGTCATGCA", "CTAGGATCCAGTCAGTACGT"
    seg = (R - L) / len(ins_top)
    s = '<g class="insert">'
    for i in range(len(ins_top)):
        x = L + seg * i
        s += f'<path d="M{x + seg * 0.5:.2f} {YT + 2.5:.2f}V{YB - 2.5:.2f}" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.7"/>'
    for i, (a, b) in enumerate(zip(ins_top, ins_bot)):
        x = L + seg * i
        s += f'<path d="M{x:.2f} {YT:.2f}H{x + seg:.2f}" stroke="{BASE_C[a]}" stroke-width="3"/>'
        s += f'<path d="M{x:.2f} {YB:.2f}H{x + seg:.2f}" stroke="{BASE_C[b]}" stroke-width="3"/>'
    out.append(s + "</g>")
    out.append(f'<g class="hairpins" fill="none" stroke="{ADAPT_C}" stroke-width="3">'
               f'<path d="M{L:.2f} {YT:.2f}A{rr:.2f} {rr:.2f} 0 0 0 {L:.2f} {YB:.2f}"/>'
               f'<path d="M{R:.2f} {YT:.2f}A{rr:.2f} {rr:.2f} 0 0 1 {R:.2f} {YB:.2f}"/></g>')
    mx = (L + R) / 2
    out.append(leader(mx, YT - 3, mx, YT - 12) + T(mx, YT - 17, "Insert", LBL, anchor="middle"))
    out.append(leader(L - rr * 0.7, YB - 2, mx - 14, YB + 22) + leader(R + rr * 0.7, YB - 2, mx + 14, YB + 22))
    out.append(T(mx, YB + 36, "Hairpin adapters", LBL, anchor="middle"))

    # b. one well
    out.append(panel_head(208, 20, "b", "One well, side view"))
    WL, WR, WT, WB = 236.0, 284.0, 40.0, 140.0
    out.append(f'<defs><linearGradient id="hifi-glow" x1="0" y1="1" x2="0" y2="0">'
               f'<stop offset="0" stop-color="{LBLUE}" stop-opacity="0.75"/><stop offset="1" stop-color="{LBLUE}" stop-opacity="0"/></linearGradient></defs>')
    out.append(f'<g class="well"><rect x="212" y="{WT:.2f}" width="{WL - 212:.2f}" height="{WB - WT:.2f}" fill="{GREY_LINE}" fill-opacity="0.35"/>'
               f'<rect x="{WR:.2f}" y="{WT:.2f}" width="{308 - WR:.2f}" height="{WB - WT:.2f}" fill="{GREY_LINE}" fill-opacity="0.35"/>'
               f'<rect x="212" y="{WB:.2f}" width="96" height="9" fill="{LBLUE}" fill-opacity="0.3"/>'
               f'<rect class="lit-zone" x="{WL:.2f}" y="{WB - 24:.2f}" width="{WR - WL:.2f}" height="24" fill="url(#hifi-glow)"/></g>')
    PX, PY = (WL + WR) / 2, WB - 9
    out.append(f'<g class="loop" fill="none" stroke="{DARK}" stroke-width="1.3"><ellipse cx="{PX:.2f}" cy="{PY - 30:.2f}" rx="15" ry="26"/>'
               f'<ellipse cx="{PX:.2f}" cy="{PY - 30:.2f}" rx="11" ry="22"/></g>')
    out.append(f'<ellipse class="polymerase" cx="{PX:.2f}" cy="{PY:.2f}" rx="12" ry="8.5" fill="{BLUE}"/>')
    fx_, fy_ = PX + 10, PY - 9
    rays = "".join(f'M{fx_ + 4 * math.cos(a):.2f} {fy_ + 4 * math.sin(a):.2f}L{fx_ + 8.5 * math.cos(a):.2f} {fy_ + 8.5 * math.sin(a):.2f}'
                   for a in [k * math.pi / 4 for k in range(8)])
    out.append(f'<g class="flash"><path d="{rays}" stroke="{GREEN}" stroke-width="1.6" stroke-linecap="round"/>'
               f'<circle cx="{fx_:.2f}" cy="{fy_:.2f}" r="3" fill="{GREEN}"/></g>')
    TX = 316.0
    out.append(leader(fx_ + 9, fy_ - 6, TX - 4, 76) + T(TX, 72, "Flash as", LBL) + T(TX, 86, "a base is", LBL) + T(TX, 100, "added", LBL))
    out.append(leader(PX + 12, PY + 2, TX - 4, 118) + T(TX, 122, "Polymerase", LBL))
    out.append(leader(WR - 3, WB - 4, TX - 4, 146) + T(TX, 150, "Light is seen", LBL) + T(TX, 164, "only here", LBL))

    # c. passes to consensus
    YC = 200.0
    out.append(f'<path class="divider" d="M8 {YC - 22:.2f}H392" stroke="{GREY_LINE}" stroke-width="0.6" stroke-opacity="0.5"/>')
    out.append(panel_head(8, YC, "c", "Passes to consensus", "around and around the loop"))
    X0, CW, RG = 70.0, 19.0, 21.0
    SEQ = "GATCCTAGGTCA"
    errs = [{2: "G", 9: "-"}, {5: "C"}, {0: "A", 7: "-"}, {10: "G"}, {4: "T"}]
    y = YC + 26
    for p, e in enumerate(errs):
        row = [e.get(i, b) for i, b in enumerate(SEQ)]
        s = '<g class="pass">'
        for c in e:
            s += change_box(X0, CW, c, c + 1, y - 9.5, y + 9.5)
        s += T(8, y + LBL * 0.36, f"Pass {p + 1}", LBL) + base_cells(X0, CW, y, row, size=14) + "</g>"
        out.append(s)
        y += RG
    out.append(f'<path class="rule" d="M8 {y - 7:.2f}H{X0 + CW * 12:.2f}" stroke="{DARK}" stroke-width="1"/>')
    y += 8
    out.append(T(8, y + LBL * 0.36, "HiFi read", LBL, 700) + base_cells(X0, CW, y, list(SEQ), size=14))
    NX = X0 + CW * 12 + 12
    ny = YC + 26 + RG * 2
    out.append(T(NX, ny - 10, "Errors land", LBL, 400, MUTED) + T(NX, ny + 4, "in different", LBL, 400, MUTED) + T(NX, ny + 18, "places", LBL, 400, MUTED))
    out.append(T(NX, y + LBL * 0.36, "Consensus", LBL, 400, MUTED))
    out.append(T(W - 8, y + 34, COPYRIGHT, 10, 400, anchor="end"))
    svg = svg_doc(W, H, out, "PacBio HiFi sequencing: a looped molecule, one well and passes combined into a consensus read")
    return svg.replace(f'width="{W:g}" height="{H:g}" viewBox="0 0 {W:g} {H:g}"', 'width="392" height="372.75" viewBox="4 6.75 392 372.75"')


if __name__ == "__main__":
    main(NAME, fig)
