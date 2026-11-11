// @ts-check
const { test, expect, scan, settle } = require("./scan");

const DOC = "/docs/biological-foundations/the-central-dogma";
const PROTEIN = "/docs/biological-foundations/protein-folding-and-modification";

test("mobile menu open", async ({ page, isMobile }, testInfo) => {
  test.skip(!isMobile, "The navbar menu only collapses at mobile widths.");
  await page.goto(DOC);
  await settle(page);
  await page.locator(".navbar__toggle").click();
  await expect(page.locator(".navbar-sidebar")).toBeVisible();
  await scan(page, testInfo, "menu open");
});

test("guide overview expanded and collapsed", async ({ page }, testInfo) => {
  await page.goto(DOC);
  const toggle = page.locator('button[aria-label="Full guide overview"]');
  const before = await toggle.getAttribute("aria-expanded");
  await scan(page, testInfo, `aria-expanded=${before}`);
  await toggle.click();
  const after = before === "true" ? "false" : "true";
  await expect(toggle).toHaveAttribute("aria-expanded", after);
  await scan(page, testInfo, `aria-expanded=${after}`);
});

test("3D protein viewer active", async ({ page }, testInfo) => {
  test.setTimeout(60_000);
  await page.goto(PROTEIN);
  await page.getByRole("button", { name: "View in 3D" }).first().click();
  const done = page.getByRole("button", { name: "Done" }).first();
  const wake = page
    .getByRole("button", { name: /(Click|Tap) to rotate and zoom/ })
    .first();
  const unsupported = page.getByText("WebGL is off or unavailable");
  await expect(done.or(wake).or(unsupported).first()).toBeVisible({
    timeout: 30_000,
  });
  if (await unsupported.isVisible()) {
    throw new Error("The protein viewer reports that WebGL is unavailable.");
  }
  if (await wake.isVisible()) await wake.click();
  await expect(done).toBeVisible();
  await scan(page, testInfo, "viewer active");
});

test("home page with reading progress", async ({ page }, testInfo) => {
  await page.goto("/");
  // Mark the first page of three chapters read. Doc ids are the permalinks
  // without the /docs/ prefix.
  const hrefs = await page
    .locator('[aria-labelledby="guide-map-title"] a[class*="label_"]')
    .evaluateAll((links) => links.slice(0, 3).map((a) => a.getAttribute("href")));
  const ids = hrefs.map((href) => String(href).replace(/^\/docs\//, ""));
  await page.evaluate(
    (read) => localStorage.setItem("learngenomics:read-pages", JSON.stringify(read)),
    ids
  );
  await page.reload();
  await expect(page.getByText(", 1 read")).toHaveCount(3);
  await expect(page.getByRole("link", { name: /^Continue:/ })).toBeVisible();
  await scan(page, testInfo, "progress");
});

test("home page guide map chapter expanded", async ({ page }, testInfo) => {
  await page.goto("/");
  const toggle = page.getByRole("button", { name: "Pages in Next-Generation Sequencing" });
  await toggle.click();
  await expect(toggle).toHaveAttribute("aria-expanded", "true");
  await expect(page.locator("#" + (await toggle.getAttribute("aria-controls")))).toBeVisible();
  await scan(page, testInfo, "chapter expanded");
});
