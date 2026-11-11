// @ts-check
const { test, expect } = require("./scan");
const { FIGURES, readSite, servedFigure, measure } = require("./figures");

// How figures are measured is described in ./figures.js.

test.describe("figure text contrast", () => {
  test.skip(
    ({ isMobile }) => isMobile,
    "Figures are vector; one width covers them.",
  );

  /** @type {{ background: string, filter: string, phoneWidth: number, dark: boolean }} */
  let site;
  test.beforeAll(async ({ browser }, testInfo) => {
    site = await readSite(browser, testInfo.project);
    expect(site.dark).toBe(testInfo.project.use.colorScheme === "dark");
  });

  test("controls measure known colors", async ({ page, colorScheme }) => {
    test.skip(colorScheme !== "light", "One theme covers the controls.");
    const control = `<svg xmlns="http://www.w3.org/2000/svg" width="300" height="60" viewBox="0 0 300 60">
      <rect width="300" height="60" fill="#ffffff"/>
      <text x="4" y="18" font-family="sans-serif" font-size="12" fill="#767676">Passes at 4.54</text>
      <text x="4" y="36" font-family="sans-serif" font-size="12" fill="#777777">Fails at 4.48</text>
      <text x="4" y="54" font-family="sans-serif" font-size="12" fill="#222222">Dark <tspan fill="#cccccc">faint</tspan> dark</text>
    </svg>`;
    const runs = await measure(page, control, { ...site, filter: "none" });
    const by = Object.fromEntries(runs.map((run) => [run.text, run.ratio]));
    expect(by["Passes at 4.54"]).toBeCloseTo(4.54, 1);
    expect(by["Fails at 4.48"]).toBeCloseTo(4.48, 1);
    expect(by["faint"]).toBeLessThan(2);
    expect(by["Dark"]).toBeGreaterThan(14);
    expect(by["dark"]).toBeGreaterThan(14);
  });

  for (const file of FIGURES) {
    test(`figure ${file}`, async ({ page }, testInfo) => {
      const svg = servedFigure(file, site.dark);
      const runs = await measure(page, svg, site);
      await testInfo.attach("runs.json", {
        body: JSON.stringify(runs, null, 2),
        contentType: "application/json",
      });
      const failures = runs.filter(
        (run) => run.ratio === null || run.ratio < run.required,
      );
      expect(
        failures.length,
        failures
          .map((run) =>
            run.ratio === null
              ? `"${run.text}" (${run.px}px): no pixel fully inside a glyph, couldn't measure`
              : `"${run.text}" ${run.ratio}:1, needs ${run.required}:1 (${run.px}px, ${run.fg} on ${run.bg})`,
          )
          .join("\n"),
      ).toBe(0);
    });
  }
});
