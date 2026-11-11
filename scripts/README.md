# Figure scripts

Python scripts that draw the SVG figures in `docs/images/`.

- `generate_figure_<N.M>.py` draws figure N.M and writes `docs/images/<N.M>-<slug>.svg`.
- `figures/` is the shared package: SVG basics, font embedding, and helpers used by
  more than one figure. It also holds the fonts (`figures/fonts/`, SIL OFL 1.1, see
  `OFL.txt`) and input data (`figures/data/`).
- `check_figure_chemistry.py` checks the atom-level drawings in figures 7.3, 7.8, 7.10 and
  7.11 against PubChem structures with RDKit.

## Setup

```sh
python3 -m venv scripts/.venv
scripts/.venv/bin/pip install -r scripts/requirements.txt
```

For the chemistry check, also install `scripts/requirements-checks.txt`.

## Regenerate figures

One figure:

```sh
scripts/.venv/bin/python scripts/generate_figure_7.9.py
```

All figures:

```sh
for f in scripts/generate_figure_*.py; do scripts/.venv/bin/python "$f" || break; done
```

Add `--out-dir DIR` to write somewhere other than `docs/images/`, for example to compare
with the published files. Output is deterministic: an unchanged script produces a
byte-identical SVG.

## Check the chemistry

```sh
scripts/.venv/bin/python scripts/check_figure_chemistry.py
```

It prints a line per check and exits with status 1 if any fails.

## Figures without scripts

These figures were exported from the original Illustrator files. Edit their SVGs in
`docs/images/` directly:

- 1.4-central-dogma
- 3.3-snv
- 3.5-indels
- 3.7-gene-fusion
- 4.7-whole-genome-sequencing
- 4.8-whole-exome-sequencing
- 4.9-rna-sequencing
- 4.10-targeted-sequencing

## Conventions

- The figure number comes from the filename prefix. Each script sets `NAME`, the output
  file name without `.svg`. To renumber a figure, rename the script, its `NAME`, the SVG,
  and every reference in `docs/`.
- Each script defines `fig()`, which returns the SVG text, and calls
  `figures.core.main(NAME, fig)`. `main` embeds the fonts and writes the file.
- SVGs shown with `<img>` cannot use the page's fonts, so each file embeds a subset of
  Source Sans 3 and Source Code Pro (WOFF2) covering only the characters it uses. Text
  stays as editable `<text>`.
- Every figure carries the copyright line (`figures.core.COPYRIGHT`).
- Code used by one figure lives in its script. Code used by two or more lives in
  `figures/`, because script filenames contain dots and cannot import each other.

## Text colors

Text must reach 4.5:1 against what's behind it, which the accessibility suite checks.
The bright palette colors are too light for that, so each has a darker text variant in
`figures.core` (`BLUE_TEXT`, `ORANGE_TEXT` and so on, listed in `TEXT_FILL`). `T()` swaps
a palette color for its text variant on its own, so `T(..., fill=ORANGE)` draws readable
orange text. The text variants reach 6:1 on white, which keeps them readable on pale
tints too.

For text on a mid-tone accent fill, such as a letter inside a colored bead, use `INK`
with `dark=DARK_PAGE`. Accents keep their color in dark mode, so the letter must stay dark
in both themes.

To fade part of a figure, put `opacity` on its shapes. A faded group that also holds
labels fades them too, and they lose contrast.

## Dark mode

The build makes the dark-mode copy of each figure in `plugins/figure-dark.js`. Each
color's contrast with white becomes its contrast with the dark page, so light and dark
swap while hues stay. Bright accents keep their color. Faded shapes (`opacity` or
`stroke-opacity` of 0.25 and up) are made a little more opaque.

Two attributes steer the dark copy:

- `data-dark-fill="#hex"` on an element sets its dark fill. `T(..., dark=...)` writes it.
  Use it for text on an accent and for markers whose fill carries meaning.
- `data-dark-deep` on the root `<svg>` keeps deep colored shapes deep, so their white
  labels can stay white.

Check a change in both themes with `npm run build` and the figure contrast test:

```sh
npx playwright test tests/a11y/figures.spec.js --project light-desktop --project dark-desktop
```
