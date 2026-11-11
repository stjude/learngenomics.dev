// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const codeThemes = require("./src/prism/themes");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Introduction to Genomics for Engineers",
  tagline:
    "A guided, intuitive introduction to genomics for software engineers.",
  url: "https://learngenomics.dev",
  baseUrl: "/",
  onBrokenLinks: "throw",
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: "warn",
    },
  },
  favicon: "img/favicon.ico",
  organizationName: "learngenomics", // Usually your GitHub org/user name.
  projectName: "learngenomics.dev", // Usually your repo name.

  plugins: [
    require.resolve("./plugins/guide-map"),
    function googleFonts() {
      return {
        name: "google-fonts",
        injectHtmlTags() {
          return {
            headTags: [
              {
                tagName: "link",
                attributes: {
                  rel: "preconnect",
                  href: "https://fonts.googleapis.com",
                },
              },
              {
                tagName: "link",
                attributes: {
                  rel: "preconnect",
                  href: "https://fonts.gstatic.com",
                  crossorigin: "anonymous",
                },
              },
              {
                tagName: "link",
                attributes: {
                  rel: "stylesheet",
                  href: "https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400..700;1,400..700&display=swap",
                },
              },
            ],
          };
        },
      };
    },
  ],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          beforeDefaultRemarkPlugins: [require("./plugins/remark-figures")],
          remarkPlugins: [require("./plugins/remark-figures").unescapeImageText],
          // Please change this to your repo.
          editUrl:
            "https://github.com/stjude/learngenomics.dev/tree/main/",
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            "https://github.com/stjude/learngenomics.dev/tree/main/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
        gtag: {
          trackingID: "G-6XD8R1VWBJ",
        },
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: "img/social-card.png",
      metadata: [
        { property: "og:site_name", content: "learngenomics.dev" },
        { property: "og:image:width", content: "1200" },
        { property: "og:image:height", content: "630" },
        {
          property: "og:image:alt",
          content:
            "The learngenomics.dev logo beside the title Introduction to Genomics for Engineers.",
        },
        {
          name: "twitter:image:alt",
          content:
            "The learngenomics.dev logo beside the title Introduction to Genomics for Engineers.",
        },
      ],
      navbar: {
        title: "learngenomics.dev",
        logo: {
          alt: "learngenomics.dev logo: a DNA helix beside five lines of code.",
          src: "img/learngenomics-logo.svg",
        },
        items: [
          // { to: "/blog", label: "Blog", position: "left" },
          {
            href: "https://github.com/learngenomics/learngenomics.dev",
            position: "right",
            className: "header-github-link",
            "aria-label": "GitHub repository",
          },
        ],
      },
      footer: {
        style: "light",
        links: [
          {
            title: "About",
            items: [
              {
                label: "Before You Begin",
                to: "/docs/before-you-begin",
              },
              {
                label: "License",
                to: "https://github.com/stjude/learngenomics.dev/blob/main/LICENSE.md",
              },
            ],
          },
          {
            title: "Guide",
            items: [
              {
                label: "Biological Foundations",
                to: "/docs/biological-foundations/cells-genomes-dna-chromosomes",
              },
              {
                label: "Cancer Biology",
                to: "/docs/cancer-biology/introduction",
              },
              {
                label: "Genomic Variation",
                to: "/docs/genomic-variation/introduction",
              },
              {
                label: "Next-Generation Sequencing",
                to: "/docs/next-generation-sequencing/introduction",
              },
              {
                label: "From Reads to Variants",
                to: "/docs/from-reads-to-variants/introduction",
              },
              {
                label: "Genomic File Formats",
                to: "/docs/genomic-file-formats/introduction",
              },
              {
                label: "Advanced Topics",
                to: "/docs/advanced-topics/alternative-splicing",
              },
            ],
          },
          {
            title: "Socials",
            items: [
              // {
              //   label: "Blog",
              //   to: "/blog",
              // },
              {
                label: "GitHub",
                href: "https://github.com/learngenomics/learngenomics.dev",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} St. Jude Children's Research Hospital. Built with Docusaurus.`,
      },
      prism: {
        theme: codeThemes.light,
        darkTheme: codeThemes.dark,
      },
    }),
};

module.exports = config;
