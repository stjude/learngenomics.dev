"""Copy-number colors and noisy depth dots."""

from figures.core import BLUE, RED

GAIN_C, LOSS_C = RED, BLUE


def cn_dots(rnd, x0, x1, n, y_of, level, sd, col, r=1.9):
    s = ""
    for i in range(n):
        x = x0 + (i + 0.5) * (x1 - x0) / n
        s += f'<circle cx="{x:.2f}" cy="{y_of(level + rnd.gauss(0, sd)):.2f}" r="{r:g}" fill="{col}" fill-opacity="0.75"/>'
    return s
