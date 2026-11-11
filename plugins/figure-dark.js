// Makes the dark-mode copy of an SVG figure by remapping its colors.
//
// Each color's contrast with white becomes its contrast with the dark page
// background, so white lands on the page. The WCAG contrast ratio between
// two colors is (Y1 + 0.05) / (Y2 + 0.05), so this map keeps ratios between
// colors close to what they were while swapping which color is lighter: text
// that is readable on paper stays readable in dark mode. Hue is kept, so each
// color keeps its identity.
//
// Bright accents are the exception. On paper they stand out by color, not
// by darkness, so the map would turn them dim (orange into brown). They keep
// their color in dark mode, where they stand out the same way.

const BACKGROUND = "#170d10";

const toLinear = (c) =>
  c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
const fromLinear = (c) =>
  c <= 0.0031308 ? 12.92 * c : 1.055 * Math.pow(c, 1 / 2.4) - 0.055;

const parseHex = (hex) =>
  [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255);

const toHex = (rgb) =>
  "#" +
  rgb
    .map((c) =>
      Math.round(Math.min(1, Math.max(0, c)) * 255)
        .toString(16)
        .padStart(2, "0"),
    )
    .join("");

const luminance = ([r, g, b]) =>
  0.2126 * toLinear(r) + 0.7152 * toLinear(g) + 0.0722 * toLinear(b);

// OKLab, from https://bottosson.github.io/posts/oklab/
function toOklch(rgb) {
  const [r, g, b] = rgb.map(toLinear);
  const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b);
  const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b);
  const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b);
  const L = 0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s;
  const A = 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s;
  const B = 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s;
  return [L, Math.hypot(A, B), Math.atan2(B, A)];
}

function fromOklch([L, C, h]) {
  const A = C * Math.cos(h);
  const B = C * Math.sin(h);
  const l = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3;
  const m = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3;
  const s = (L - 0.0894841775 * A - 1.291485548 * B) ** 3;
  return [
    4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
    -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
    -0.0041960863 * l - 0.7034186147 * m + 1.707614701 * s,
  ].map(fromLinear);
}

const inGamut = (rgb) => rgb.every((c) => c >= -1e-4 && c <= 1 + 1e-4);

// The most saturated in-gamut color with this lightness and hue, up to C.
function clip(L, C, h) {
  if (inGamut(fromOklch([L, C, h]))) return fromOklch([L, C, h]);
  let low = 0;
  let high = C;
  for (let i = 0; i < 24; i++) {
    const mid = (low + high) / 2;
    if (inGamut(fromOklch([L, mid, h]))) low = mid;
    else high = mid;
  }
  return fromOklch([L, low, h]);
}

const TINT_BOOST = 3;

const BG = parseHex(BACKGROUND);
const [BG_L, BG_CHROMA, BG_HUE] = toOklch(BG);

// The color with this hue and chroma whose luminance is the target.
function withLuminance(rgb, target) {
  const [L0, C0, hue] = toOklch(rgb);
  // Greys take the page's warm tint, fading out toward white.
  const grey = C0 < 0.01;
  const h = grey ? BG_HUE : hue;
  // Pale tints get more color, or a pink and a grey panel both turn brown.
  const C = L0 > 0.85 ? C0 * TINT_BOOST : C0;
  const chroma = (L) =>
    grey ? BG_CHROMA * Math.min(1, Math.max(0, (1 - L) / (1 - BG_L))) : C;
  let low = 0;
  let high = 1;
  for (let i = 0; i < 32; i++) {
    const mid = (low + high) / 2;
    if (luminance(clip(mid, chroma(mid), h)) < target) low = mid;
    else high = mid;
  }
  return toHex(clip(low, chroma(low), h));
}

// A color's contrast with white, r, becomes its contrast with the page. Low
// contrasts are lifted a little (r^(1 + 1/r): 1.5 becomes 2, 2 becomes 2.8),
// because pale fills that are clear on paper look dim on a dark page. The
// lift is monotonic, so ramps keep their order, and it fades out by 21:1.
function darkColor(hex) {
  const rgb = parseHex(hex);
  const r = 1.05 / (luminance(rgb) + 0.05);
  const lifted = Math.pow(r, 1 + 1 / r);
  const target = Math.min(1, (luminance(BG) + 0.05) * lifted - 0.05);
  return withLuminance(rgb, target);
}

// In figures marked data-dark-deep, deep colored shapes stay deep so their
// white labels can stay white: they are only lifted enough to stand 3:1
// off the page.
const DEEP_MAX = 0.18;
const DEEP_MIN = 0.13;

function deepColor(hex) {
  const rgb = parseHex(hex);
  const Y = luminance(rgb);
  if (Y > DEEP_MAX || toOklch(rgb)[1] < 0.04) return null;
  return Y >= DEEP_MIN ? hex : withLuminance(rgb, DEEP_MIN);
}

// The figure palette's bright accents. Each would come out darker than it
// started; they also stand out on the dark page as they are.
const ACCENTS = new Set([
  "#fcb025", // orange
  "#75bc43", // green
  "#14adc1", // teal
  "#6acbe0", // light cyan
  "#ff2129", // red
  "#ab86bf", // light purple
  "#6ea6e6", // light blue
  "#4f9fbb", // steel blue
  "#3d89df", // blue
  "#c98200", // amber
  "#0096a2", // dark teal
]);

const NAMED = { white: "#ffffff", black: "#000000" };
const cache = new Map();

// role is "text" or "shape"; deep is set in data-dark-deep figures.
function mapColor(value, role = "shape", deep = false) {
  const hex = (NAMED[value.toLowerCase()] || value).toLowerCase();
  if (!/^#[0-9a-f]{6}$/.test(hex)) return value;
  if (hex === "#ffffff") return deep && role === "text" ? hex : BACKGROUND;
  if (ACCENTS.has(hex)) return hex;
  if (deep && role === "shape") {
    const kept = deepColor(hex);
    if (kept) return kept;
  }
  if (!cache.has(hex)) cache.set(hex, darkColor(hex));
  return cache.get(hex);
}

const COLOR = /(?<![\w-])(fill|stroke|stop-color)="([^"]*)"/g;

// Faded shapes (opacity 0.25 and up, such as dimmed reads or a strand that
// has left the picture) skip the lift that pale solid fills get, so on the
// dark page they look fainter than on paper. Raising their opacity to this
// power gives them about the same lift. Lower opacities and fill-opacity are
// left alone: the figures use those for tint boxes behind text, and a
// brighter box would cost the text its contrast.
const OPACITY_GAMMA = 0.6;
const OPACITY = /(?<![\w-])((?:stroke-)?opacity)="([\d.]+)"/g;
const liftOpacity = (value) => {
  const o = Number(value);
  return o >= 0.25 && o < 1
    ? Number(Math.pow(o, OPACITY_GAMMA).toFixed(3))
    : value;
};

// A shape can name its own dark fill with data-dark-fill, for markers whose
// fill carries meaning (filled means methylated) or text on a kept accent.
function toDark(svg) {
  const deep = /<svg\b[^>]*\sdata-dark-deep\b/.test(svg);
  const recolored = svg.replace(/<([\w-]+)\b[^>]*>/g, (tag, name) => {
    const role = name === "text" || name === "tspan" ? "text" : "shape";
    tag = tag.replace(
      COLOR,
      (_, attr, value) => `${attr}="${mapColor(value, role, deep)}"`,
    );
    tag = tag.replace(
      OPACITY,
      (_, attr, value) => `${attr}="${liftOpacity(value)}"`,
    );
    const own = /\sdata-dark-fill="([^"]*)"/.exec(tag);
    if (!own) return tag;
    return /(?<![\w-])fill="/.test(tag)
      ? tag.replace(/(?<![\w-])fill="[^"]*"/, `fill="${own[1]}"`)
      : tag.replace(/^<[\w-]+/, (open) => `${open} fill="${own[1]}"`);
  });
  // Shapes and text without a fill are black; give them the mapped black.
  return recolored.replace(/<svg\b([^>]*)>/, (tag, attributes) =>
    /\sfill="/.test(attributes)
      ? tag
      : `<svg${attributes} fill="${mapColor("#000000")}">`,
  );
}

module.exports = { BACKGROUND, toDark, mapColor, luminance, parseHex };
