// Renders static/img/social-card.png, the 1200×630 link-preview image.
// The chapter and page counts come from the guide map, so run `npm run build`
// (or `npm start`) first to refresh .docusaurus/globalData.json.
// Usage, from the repo root: node scripts/generate_social_card.cjs

const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const root = path.join(__dirname, "..");
const out = path.join(root, "static/img/social-card.png");
const map = JSON.parse(
  fs.readFileSync(path.join(root, ".docusaurus/globalData.json"), "utf8")
)["guide-map"].default;
const logo = fs.readFileSync(
  path.join(root, "static/img/learngenomics-logo.svg"),
  "utf8"
);

const pages = map.chapters.reduce((n, c) => n + c.pages.length, 0);

const html = `<!doctype html><html><head>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=block" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; }
  body { width: 1200px; height: 630px; overflow: hidden; background: #3730a3;
    font-family: "Source Sans 3", sans-serif; color: #fff; -webkit-font-smoothing: antialiased; }
  .brand { position: absolute; left: 72px; top: 66px; font-size: 30px; font-weight: 600; letter-spacing: -0.005em; }
  h1 { position: absolute; left: 72px; top: 158px; width: 560px; font-size: 76px; line-height: 1.02;
    font-weight: 600; letter-spacing: -0.018em; }
  p { position: absolute; left: 72px; top: 430px; width: 500px; font-size: 29px; line-height: 1.32; color: #d6d5f2; }
  .meta { position: absolute; left: 72px; bottom: 58px; font-size: 23px; color: #d6d5f2; }
  .mark { position: absolute; left: 718px; top: 125px; width: 380px; height: 380px; }
  .mark svg { width: 100%; height: 100%; }
</style></head><body>
  <div class="brand">learngenomics.dev</div>
  <div class="mark">${logo.replace(/<\?xml[^>]*>/, "")}</div>
  <h1>Introduction to Genomics for Engineers</h1>
  <p>A guided, intuitive introduction to genomics for software engineers.</p>
  <div class="meta">${map.chapters.length} chapters · ${pages} pages · free to read online</div>
</body></html>`;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  await page.setContent(html, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: out });
  await browser.close();
  console.log(`wrote ${path.relative(root, out)}`);
})();
