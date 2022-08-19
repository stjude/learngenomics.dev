// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Introduction to Genomics for Engineers",
  tagline:
    "A guided, intuitive introduction to genomics for software engineers.",
  url: "https://learngenomics.dev",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "learngenomics", // Usually your GitHub org/user name.
  projectName: "learngenomics.dev", // Usually your repo name.

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          editUrl:
            "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
        gtag: {
          trackingID: "G-6XD8R1VWBJ",
          anonymizeIP: true,
        },
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: "learngenomics.dev",
        logo: {
          alt: "learngenomics.dev logo: a DNA helix beside five lines of code.",
          src: "img/learngenomics-logo.svg",
        },
        items: [
          {
            type: "doc",
            docId: "biological-foundations/cells-genomes-dna-chromosomes",
            position: "left",
            label: "Guide",
          },
          // { to: "/blog", label: "Blog", position: "left" },
          {
            href: "https://github.com/learngenomics/learngenomics.dev",
            label: "GitHub",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "About",
            items: [
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
                label: "Genomic Variation",
                to: "/docs/genomic-variation",
              },
              {
                label: "Next-generation Sequencing",
                to: "/docs/next-generation-sequencing",
              },
              {
                label: "Engineering Ecosystem",
                to: "/docs/engineering-ecosystem",
              },
              {
                label: "Advanced Topics",
                to: "/docs/advanced-topics",
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
        copyright: `Copyright © ${new Date().getFullYear()} learngenomics.dev and associated contributors. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
