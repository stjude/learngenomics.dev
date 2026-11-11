// @ts-check
const { defineConfig, devices } = require("@playwright/test");

const PORT = 3100;

const desktop = { viewport: { width: 1280, height: 800 } };
const mobile = {
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 3,
  isMobile: true,
  hasTouch: true,
};

module.exports = defineConfig({
  testDir: "tests/a11y",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: [["list"], ["html", { open: "never" }]],
  use: {
    ...devices["Desktop Chrome"],
    baseURL: `http://localhost:${PORT}`,
    launchOptions: {
      // SwiftShader gives headless Chromium software WebGL for the 3D protein viewer.
      args: ["--use-angle=swiftshader", "--enable-unsafe-swiftshader"],
    },
  },
  projects: [
    { name: "light-desktop", use: { ...desktop, colorScheme: "light" } },
    { name: "dark-desktop", use: { ...desktop, colorScheme: "dark" } },
    { name: "light-mobile", use: { ...mobile, colorScheme: "light" } },
    { name: "dark-mobile", use: { ...mobile, colorScheme: "dark" } },
  ],
  webServer: {
    command: `npm run serve -- --port ${PORT} --no-open`,
    url: `http://localhost:${PORT}`,
    reuseExistingServer: !process.env.CI,
    timeout: 60_000,
  },
});
