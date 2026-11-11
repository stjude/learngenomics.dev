"""Shared basics for every figure: palette, text, the SVG wrapper, font embedding and the CLI."""

import argparse
import base64
import html
import io
import os
import re

YEAR = 2026
COPYRIGHT = f"\u00a9 Copyright {YEAR} St. Jude Children's Research Hospital"

BLUE, NAVY, PURPLE, LBLUE, TEAL, ORANGE, GREEN = "#1874dc", "#002856", "#7f3e98", "#6acbe0", "#14adc1", "#fcb025", "#75bc43"
RED, DARK = "#ff2129", "#333333"
MUTED = "#4d4d4f"
GREY_LINE = "#6d6e71"
FAINT_BASE = "#9a9b9e"
LBL = 12.5  # row labels, notes, table and key: about 11 px on a 390 px phone

# Text in a palette color uses a darker variant of the same hue with 6:1 contrast on white,
# so it keeps WCAG AA 4.5:1 on the pale tints (down to about #e5e5e5) behind base letters.
# Orange shifts toward red so it stays orange instead of turning olive. T() applies this map.
BLUE_TEXT, TEAL_TEXT, ORANGE_TEXT, GREEN_TEXT, RED_TEXT = "#0061c3", "#006d7b", "#a04a00", "#3a7000", "#c90015"
FAINT_TEXT = "#626366"  # faded letters: lighter than DARK, still 4.5:1 on tints
TEXT_FILL = {BLUE: BLUE_TEXT, TEAL: TEAL_TEXT, ORANGE: ORANGE_TEXT, GREEN: GREEN_TEXT, RED: RED_TEXT,
             FAINT_BASE: FAINT_TEXT}

# The dark theme's page color. plugins/figure-dark.js keeps bright accents (ORANGE, GREEN,
# LBLUE, ...) unchanged in dark mode, so dark ink on an accent passes dark=DARK_PAGE to stay dark.
DARK_PAGE = "#170d10"
INK = "#1a1a1a"  # labels on mid-tone accent fills, where DARK falls short of 4.5:1

SANS = "'Source Sans 3', 'Source Sans Pro', sans-serif"
MONO = "'Source Code Pro', monospace"

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
DATA_DIR = os.path.join(HERE, "data")
REPO = os.path.dirname(os.path.dirname(HERE))
IMAGES = os.path.join(REPO, "docs", "images")


def esc(s):
    return html.escape(s, quote=False)


def T(x, y, s, size, weight=400, fill=None, anchor=None, mono=False, extra="", dark=None):
    """Text element. dark sets data-dark-fill, the fill used in the dark-mode copy."""
    a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
    f = f' fill="{TEXT_FILL.get(fill, fill)}"' if fill else ""
    if dark:
        f += f' data-dark-fill="{dark}"'
    fam = MONO if mono else SANS
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-size="{size:g}" '
            f'font-weight="{weight}"{f}{a}{extra}>{esc(s)}</text>')


def copyright_text(x_right, y):
    return T(x_right, y, COPYRIGHT, 5.4, 400, anchor="end")


def big_copyright(x_right, y):
    return T(x_right, y, COPYRIGHT, 10, 400, anchor="end")


def svg_doc(w, h, body, title, origin=(0, 0), fmt="g"):
    """Wrap body lines in an <svg> root. origin and fmt set the viewBox corner and number format."""
    x, y = origin
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'version="1.1" width="{w:{fmt}}" height="{h:{fmt}}" viewBox="{x:{fmt}} {y:{fmt}} {w:{fmt}} {h:{fmt}}">\n'
            f"<title>{esc(title)}</title>\n" + "\n".join(body) + "\n</svg>\n")


# ---------------------------------------------------------------- font embedding
# SVGs shown via <img> cannot use page fonts, so each file carries a subset of the
# (OFL-licensed) variable fonts it uses. Text stays as editable <text>.
FONTS = {"sans": ("Source Sans 3", "SourceSans3-VF.ttf"),
         "mono": ("Source Code Pro", "SourceCodePro-VF.ttf")}


def _subset_woff2(path, chars):
    from fontTools import subset
    from fontTools.ttLib import TTFont
    # recalcTimestamp=False keeps head.modified from the source font, so output is reproducible.
    f = TTFont(os.path.join(FONT_DIR, path), recalcTimestamp=False)
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern", "liga", "calt", "ccmp", "locl", "mark", "mkmk", "tnum", "lnum"]
    opts.name_IDs = ["*"]
    opts.notdef_outline = True
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=sorted({ord(c) for c in chars} | {32}))
    sub.subset(f)
    buf = io.BytesIO()
    f.flavor = "woff2"
    f.save(buf)
    return base64.b64encode(buf.getvalue()).decode()


def embed_fonts(svg):
    chars = {"sans": set(), "mono": set()}
    for m in re.finditer(r"<text\b([^>]*)>(.*?)</text>", svg, re.S):
        attrs, body = m.groups()
        kind = "mono" if "Source Code Pro" in attrs else "sans"
        chars[kind] |= set(html.unescape(re.sub(r"<[^>]+>", "", body)))
    rules = []
    for kind, cs in chars.items():
        if not cs - {" ", "\n"}:
            continue
        fam, path = FONTS[kind]
        rules.append(f"@font-face{{font-family:'{fam}';font-weight:200 900;"
                     f"src:url(data:font/woff2;base64,{_subset_woff2(path, cs)}) format('woff2')}}")
    if not rules:
        return svg
    style = "<defs><style>/* Source Sans 3 / Source Code Pro, SIL Open Font License 1.1 */\n" + "\n".join(rules) + "</style></defs>\n"
    i = svg.index("</title>") + len("</title>\n")
    return svg[:i] + style + svg[i:]


# ---------------------------------------------------------------- command line
def main(name, fig):
    """Write <out-dir>/<name>.svg (default: docs/images in this repository)."""
    ap = argparse.ArgumentParser(description=f"Generate {name}.svg")
    ap.add_argument("--out-dir", default=IMAGES, help="output directory (default: docs/images)")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    svg = embed_fonts(fig())
    path = os.path.join(args.out_dir, name + ".svg")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    print(path)
