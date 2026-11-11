// @ts-check
const fs = require("fs");
const path = require("path");
const base = require("@playwright/test");
const { default: AxeBuilder } = require("@axe-core/playwright");

const TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"];

// Third-party embeds are out of scope, and blocking them keeps runs deterministic.
const BLOCKED =
  /youtube|ytimg|proteinpaint\.stjude\.org|googletagmanager\.com|google-analytics\.com/;

// GuideBand slices and the home page's guide map pills are left out of target-size
// only. WCAG 2.5.8 exempts small targets when an equivalent control meets the size:
// every slice's page is also linked from the sidebar or the mobile menu, and every
// pill's page from its chapter's expandable page list.
const SLICES = [
  'nav[aria-label="Guide overview"] [class*="ideogram_"] a',
  '[aria-labelledby="guide-map-title"] [class*="pills_"] a',
];

const SITEMAP = path.join(__dirname, "..", "..", "build", "sitemap.xml");

/** Every route in the built site, as a path. */
function routes() {
  if (!fs.existsSync(SITEMAP)) {
    throw new Error("build/sitemap.xml not found. Run `npm run build` first.");
  }
  const xml = fs.readFileSync(SITEMAP, "utf8");
  return [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map(
    (m) => new URL(m[1]).pathname
  );
}

/** Page fixture that forces the project's theme and blocks third-party requests. */
const test = base.test.extend({
  page: async ({ page, colorScheme }, use) => {
    await page.addInitScript((theme) => {
      try {
        window.localStorage.setItem("theme", theme);
      } catch (e) {}
    }, colorScheme);
    await page.route(BLOCKED, (route) => route.abort());
    await use(page);
  },
});

async function settle(page) {
  await page.waitForLoadState("networkidle");
  await page.evaluate(() => document.fonts.ready);
  // Menus and toggles animate; scanning mid-transition reports false contrast
  // failures. Looping animations, such as loading pulses, never finish.
  await page.waitForFunction(() =>
    document
      .getAnimations()
      .every(
        (a) =>
          a.playState !== "running" ||
          a.effect?.getTiming().iterations === Infinity
      )
  );
}

/** Scans the page as it is now and fails with one line per violating node. */
async function scan(page, testInfo, label = "") {
  const theme = testInfo.project.use.colorScheme;
  await base
    .expect(page.locator("html"))
    .toHaveAttribute("data-theme", String(theme));
  await settle(page);

  const builder = () =>
    new AxeBuilder({ page }).withTags(TAGS).exclude("iframe");
  const main = await builder().disableRules(["target-size"]).analyze();
  const size = await SLICES.reduce(
    (axe, selector) => axe.exclude(selector),
    builder().withRules(["target-size"])
  ).analyze();
  const violations = [...main.violations, ...size.violations];

  const where = new URL(page.url()).pathname + (label ? ` [${label}]` : "");
  await testInfo.attach(`axe ${where}`, {
    body: JSON.stringify(violations, null, 2),
    contentType: "application/json",
  });

  const lines = violations.flatMap((v) =>
    v.nodes.map(
      (n) =>
        `${testInfo.project.name} ${where} ${v.id} (${v.impact}): ${v.help} — ${n.target.join(" ")}`
    )
  );
  base.expect(lines, lines.join("\n")).toEqual([]);
}

module.exports = { test, expect: base.expect, scan, settle, routes };
