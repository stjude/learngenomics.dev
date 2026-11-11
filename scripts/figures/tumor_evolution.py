"""Shared layout and line helper for the tumor-evolution figures 2.8 and 2.9."""

from figures.core import GREY_LINE, ORANGE

X0, X1 = 10.0, 390.0
CA = ORANGE


def ln(x0, y0, x1, y1, col=GREY_LINE, sw=0.8, extra=""):
    return f'<path d="M{x0:.2f} {y0:.2f}L{x1:.2f} {y1:.2f}" stroke="{col}" stroke-width="{sw}" fill="none" stroke-linecap="round"{extra}/>'
