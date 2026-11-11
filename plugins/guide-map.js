/**
 * Builds a map of the guide (chapters, pages, and word counts) from the docs
 * sidebar so the theme can draw the guide "to scale" on the home page and in
 * the locator bar above each doc.
 */
const fs = require("fs");
const path = require("path");

const WORDS_PER_MINUTE = 200;

function countWords(file) {
  const text = fs
    .readFileSync(file, "utf8")
    .replace(/^---[\s\S]*?---/, "")
    .replace(/!\[[^\]]*\]\([^)]*\)/g, "")
    .replace(/<[^>]+>/g, " ");
  return (text.match(/[A-Za-z0-9][\w'’-]*/g) || []).length;
}

module.exports = function guideMap(context) {
  return {
    name: "guide-map",
    injectHtmlTags() {
      return {
        headTags: [
          {
            tagName: "script",
            innerHTML:
              "try{if(localStorage.getItem('learngenomics:band-collapsed')==='1')document.documentElement.dataset.lgBand='collapsed'}catch(e){}",
          },
        ],
      };
    },
    async allContentLoaded({ allContent, actions }) {
      const docsPlugin = allContent["docusaurus-plugin-content-docs"];
      const version = docsPlugin && docsPlugin.default.loadedVersions[0];
      if (!version) return;

      const docsById = new Map(version.docs.map((doc) => [doc.id, doc]));
      const page = ({ id, section }) => {
        const doc = docsById.get(id);
        const file = path.join(
          context.siteDir,
          doc.source.replace(/^@site\//, "")
        );
        const words = countWords(file);
        return {
          id,
          title: doc.title,
          // The nested category a page sits in, if any, such as Types of
          // Sequencing; it tells apart pages that share a title.
          ...(section && { section }),
          permalink: doc.permalink,
          words,
          minutes: Math.max(1, Math.round(words / WORDS_PER_MINUTE)),
        };
      };

      const [sidebar] = Object.values(version.sidebars);
      const chapters = sidebar
        .filter((item) => item.type === "category")
        .map((category) => {
          // Nested categories (such as Types of Sequencing) are flattened
          // into their chapter, in reading order.
          const ids = [];
          const collect = (cat, section) => {
            if (cat.link && cat.link.type === "doc") {
              ids.push({ id: cat.link.id, section });
            }
            cat.items.forEach((item) => {
              if (item.type === "doc") ids.push({ id: item.id, section });
              else if (item.type === "category") collect(item, item.label);
            });
          };
          collect(category, undefined);
          const pages = ids.map(page);
          const words = pages.reduce((sum, p) => sum + p.words, 0);
          return {
            label: category.label,
            pages,
            words,
            // Rounded to 5 minutes; a chapter estimate shouldn't look precise.
            minutes: Math.max(
              5,
              Math.round(words / WORDS_PER_MINUTE / 5) * 5
            ),
          };
        });

      actions.setGlobalData({
        chapters,
        totalPages: chapters.reduce((sum, c) => sum + c.pages.length, 0),
        totalWords: chapters.reduce((sum, c) => sum + c.words, 0),
      });
    },
  };
};
