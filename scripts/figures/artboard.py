"""Artwork exported from the original Illustrator file, used as the base layer of figures 1.1 and 1.5.

data/dna-artboard.svg and data/dna-to-mrna-artboard.svg are artboards 28 and 29 of the
course's Illustrator source, exported with PyMuPDF; their text is already converted to
Source Sans 3 <text>. Edit those files directly if the artwork needs to change.
"""

import os

from figures.core import DATA_DIR


def load_artboard(name):
    with open(os.path.join(DATA_DIR, f"{name}-artboard.svg"), encoding="utf-8") as fh:
        return fh.read()


def lines_of(svg):
    return svg.split("\n")


def inner(svg):
    """Return the lines between <defs> end and the closing tags, plus the defs block."""
    ls = lines_of(svg)
    d0 = ls.index("<defs>"); d1 = ls.index("</defs>")
    return ls[d0:d1 + 1], ls[d1 + 1:]
