// @ts-check
const { test, scan, routes } = require("./scan");

for (const route of routes()) {
  test(`page ${route}`, async ({ page }, testInfo) => {
    await page.goto(route);
    await scan(page, testInfo);
  });
}
