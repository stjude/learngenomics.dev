// @ts-check
const { expect } = require("@playwright/test");
const fs = require("fs");
const path = require("path");

/*
 * Text contrast inside the SVG figures. Pages show figures as <img>, so axe
 * can't see their text. Each figure is drawn here on the site's page background,
 * as the built site serves it (dark mode serves a recolored copy, made by
 * plugins/figure-dark.js), then measured from pixels in three renders:
 *
 *   A  the figure as readers see it
 *   B  the same, with all text hidden: the background behind each glyph
 *   M  only the text, each run painted a unique color on black: which pixels
 *      belong to which run, and which are fully inside a glyph
 *
 * Every pixel fully inside a glyph pairs its color in A with the color behind
 * it in B. A run's contrast is the median over its pixels. Runs too thin to
 * have a fully covered pixel fail as unmeasured, so nothing passes unseen.
 *
 * Figures sit directly on the page background. None are inside admonitions or
 * other tinted containers; this would need revisiting if one were.
 */

const IMAGES = path.join(__dirname, "..", "..", "docs", "images");
const BUILD = path.join(__dirname, "..", "..", "build");
const SCALE = 6;
const PHONE = { width: 390, height: 844 };

const FIGURES = fs
  .readdirSync(IMAGES)
  .filter((file) => file.endsWith(".svg"))
  .sort();

/** A built page with an SVG figure, to read the figure's real surroundings from. */
function figureRoute() {
  const xml = fs.readFileSync(path.join(BUILD, "sitemap.xml"), "utf8");
  for (const [, loc] of xml.matchAll(/<loc>([^<]+)<\/loc>/g)) {
    const route = new URL(loc).pathname;
    const file = path.join(BUILD, route, "index.html");
    if (
      fs.existsSync(file) &&
      /<img[^>]+src="\/assets\/images\/[^"]+\.svg"/.test(
        fs.readFileSync(file, "utf8"),
      )
    ) {
      return route;
    }
  }
  throw new Error(
    "No built page has an SVG figure. Run `npm run build` first.",
  );
}

/** The built copy of a figure that a theme serves. */
function servedFigure(file, dark) {
  if (!dark) return fs.readFileSync(path.join(IMAGES, file), "utf8");
  const assets = path.join(BUILD, "assets", "images");
  const name = file.replace(/\.svg$/, "");
  const copies = fs
    .readdirSync(assets)
    .filter((asset) =>
      new RegExp(`^${name.replace(/\./g, "\\.")}-dark-[0-9a-f]+\\.svg$`).test(
        asset,
      ),
    );
  if (copies.length !== 1) {
    throw new Error(
      `Expected one dark copy of ${file} in the build, found ${copies.length}.`,
    );
  }
  return fs.readFileSync(path.join(assets, copies[0]), "utf8");
}

/**
 * The page background, figure filter, phone-width figure size, and whether the
 * dark copy is the one shown, from the live site.
 */
async function readSite(browser, project) {
  const context = await browser.newContext({
    baseURL: project.use.baseURL,
    colorScheme: project.use.colorScheme,
    viewport: PHONE,
  });
  const page = await context.newPage();
  await page.addInitScript((theme) => {
    window.localStorage.setItem("theme", theme);
  }, project.use.colorScheme);
  await page.goto(figureRoute());
  const figure = page.locator(".lg-figure--themed").first();
  const img = figure.locator("img:visible");
  await expect(img).toHaveCount(1);
  const site = await img.evaluate((el) => {
    let node = el.parentElement;
    let background = "rgb(255, 255, 255)";
    while (node) {
      const color = getComputedStyle(node).backgroundColor;
      if (color !== "rgba(0, 0, 0, 0)" && color !== "transparent") {
        background = color;
        break;
      }
      node = node.parentElement;
    }
    return {
      background,
      filter: getComputedStyle(el).filter,
      phoneWidth: el.getBoundingClientRect().width,
      dark: el.classList.contains("lg-figure__dark"),
    };
  });
  await context.close();
  return site;
}

/**
 * Draws one SVG and measures every text run in it. Returns one entry per run:
 * its text, display size, required ratio, and measured ratio (null if no pixel
 * was fully inside a glyph).
 */
async function measure(page, svg, site) {
  await page.setViewportSize({ width: 1600, height: 1000 });
  await page.setContent(
    `<!doctype html><body style="margin:0;background:${site.background}">${svg}</body>`,
  );

  const size = await page.evaluate(
    ({ SCALE, site }) => {
      const svg = document.querySelector("svg");
      const width = parseFloat(svg.getAttribute("width"));
      const height = parseFloat(svg.getAttribute("height"));
      svg.setAttribute("width", String(width * SCALE));
      svg.setAttribute("height", String(height * SCALE));
      svg.style.display = "block";
      svg.style.filter = site.filter;

      // Each run remembers the <text> or <tspan> it came from, in document order,
      // so a fix can find it in the file.
      svg.querySelectorAll("text, tspan").forEach((el, i) => {
        el.setAttribute("data-source", String(i));
      });
      // Loose text beside a <tspan> is its own run; wrap it so it can be painted alone.
      for (const text of svg.querySelectorAll("text")) {
        const walker = document.createTreeWalker(text, NodeFilter.SHOW_TEXT);
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        for (const node of nodes) {
          if (!node.textContent.trim()) continue;
          const run = document.createElementNS(
            "http://www.w3.org/2000/svg",
            "tspan",
          );
          run.setAttribute("data-run", "");
          node.replaceWith(run);
          run.append(node);
        }
      }
      return { width: width * SCALE, height: height * SCALE, intrinsic: width };
    },
    { SCALE, site },
  );
  await page.setViewportSize({
    width: Math.ceil(size.width),
    height: Math.ceil(size.height),
  });
  await page.evaluate(() => document.fonts.ready);

  const runs = await page.evaluate(
    ({ SCALE, phoneScale }) => {
      return [...document.querySelectorAll("[data-run]")].map((run, i) => {
        const style = getComputedStyle(run);
        const ctm = run.getScreenCTM();
        const px =
          parseFloat(style.fontSize) *
          (Math.hypot(ctm.a, ctm.b) / SCALE) *
          phoneScale;
        const weight = parseInt(style.fontWeight, 10);
        const large = px >= 24 || (px >= 18.66 && weight >= 700);
        const box = run.getBoundingClientRect();
        // Label colors keep blue at 255, so an edge blended with the black
        // background never matches a label.
        const k = i + 1;
        const label = [(k % 64) * 4, Math.floor(k / 64) * 4, 255];
        let opacity = parseFloat(style.fillOpacity);
        for (let el = run; el && el.tagName !== "svg"; el = el.parentElement) {
          opacity *= parseFloat(getComputedStyle(el).opacity);
        }
        return {
          source: Number(run.parentElement.getAttribute("data-source")),
          fill: style.fill,
          opacity,
          text: run.textContent.trim(),
          px: Math.round(px * 10) / 10,
          weight,
          required: large ? 3 : 4.5,
          label,
          box: { x: box.x, y: box.y, w: box.width, h: box.height },
        };
      });
    },
    { SCALE, phoneScale: site.phoneWidth / size.intrinsic },
  );

  const shoot = async () => (await page.screenshot()).toString("base64");
  const a = await shoot();
  const hide = await page.addStyleTag({
    content: "text, tspan { visibility: hidden !important; }",
  });
  const b = await shoot();
  await hide.evaluate((el) => el.remove());
  await page.addStyleTag({
    content: `
      body { background: #000 !important; }
      svg { filter: none !important; }
      svg * {
        visibility: hidden !important;
        opacity: 1 !important;
        fill-opacity: 1 !important;
        filter: none !important;
        mask: none !important;
        stroke: none !important;
      }
      svg [data-run] { visibility: visible !important; }
    `,
  });
  await page.evaluate(
    (labels) => {
      document.querySelectorAll("[data-run]").forEach((run, i) => {
        run.style.setProperty(
          "fill",
          `rgb(${labels[i].join(",")})`,
          "important",
        );
      });
    },
    runs.map((run) => run.label),
  );
  const m = await shoot();

  return page.evaluate(
    async ({ a, b, m, runs }) => {
      // WCAG relative luminance and contrast ratio, for [r, g, b] in 0–255.
      const lum = (rgb) => {
        const [r, g, b] = rgb.map((v) => {
          v /= 255;
          return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
        });
        return 0.2126 * r + 0.7152 * g + 0.0722 * b;
      };
      const ratio = (p, q) => {
        const [hi, lo] = [lum(p), lum(q)].sort((x, y) => y - x);
        return (hi + 0.05) / (lo + 0.05);
      };
      const decode = async (data) => {
        const blob = await (
          await fetch(`data:image/png;base64,${data}`)
        ).blob();
        const bitmap = await createImageBitmap(blob);
        const canvas = new OffscreenCanvas(bitmap.width, bitmap.height);
        const ctx = canvas.getContext("2d");
        ctx.drawImage(bitmap, 0, 0);
        return ctx.getImageData(0, 0, bitmap.width, bitmap.height);
      };
      const [A, B, M] = await Promise.all([a, b, m].map(decode));
      const hex = (p) =>
        "#" + p.map((v) => v.toString(16).padStart(2, "0")).join("");

      return runs.map((run) => {
        const samples = [];
        const x0 = Math.max(0, Math.floor(run.box.x));
        const y0 = Math.max(0, Math.floor(run.box.y));
        const x1 = Math.min(M.width, Math.ceil(run.box.x + run.box.w));
        const y1 = Math.min(M.height, Math.ceil(run.box.y + run.box.h));
        for (let y = y0; y < y1; y++) {
          for (let x = x0; x < x1; x++) {
            const i = (y * M.width + x) * 4;
            if (
              M.data[i] !== run.label[0] ||
              M.data[i + 1] !== run.label[1] ||
              M.data[i + 2] !== run.label[2]
            ) {
              continue;
            }
            const fg = [A.data[i], A.data[i + 1], A.data[i + 2]];
            const bg = [B.data[i], B.data[i + 1], B.data[i + 2]];
            samples.push({ ratio: ratio(fg, bg), fg, bg });
          }
        }
        samples.sort((p, q) => p.ratio - q.ratio);
        const mid = samples[Math.floor(samples.length / 2)];
        return {
          source: run.source,
          fill: run.fill,
          opacity: run.opacity,
          text: run.text,
          px: run.px,
          weight: run.weight,
          required: run.required,
          pixels: samples.length,
          ratio: mid ? Math.round(mid.ratio * 100) / 100 : null,
          fg: mid ? hex(mid.fg) : null,
          bg: mid ? hex(mid.bg) : null,
        };
      });
    },
    { a, b, m, runs },
  );
}

module.exports = { FIGURES, readSite, servedFigure, measure };
