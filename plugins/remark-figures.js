// Turns a paragraph holding a single titled image into a numbered figure:
//
//   ![alt text](../images/1.3-chromatin.svg "Caption text.")
//
// becomes <figure id="figure-1-2"> with the image and
// <figcaption>Figure 1.2 Caption text.</figcaption>. The number comes from
// the file name, so renaming a figure renumbers its caption.
//
// SVG figures also get a dark-mode copy, made at build time by
// ./figure-dark-loader.js. CSS shows one image or the other by theme.

const fs = require("fs");
const path = require("path");

const NUMBERED = /(?:^|\/)(\d+\.\d+)-[^/]+$/;

// A figure taller than it is wide would fill the screen at full column
// width, so it gets a class that caps its width on large screens.
const TALL = 1.05;

function readSvg(url, file) {
  if (!file || !file.path || !/\.svg$/.test(url)) return null;
  try {
    return fs.readFileSync(path.resolve(path.dirname(file.path), url), "utf8");
  } catch {
    return null;
  }
}

function isTall(svg) {
  const box =
    svg &&
    svg.match(/viewBox="\s*[\d.-]+[\s,]+[\d.-]+[\s,]+([\d.]+)[\s,]+([\d.]+)/);
  return Boolean(box) && box[2] / box[1] > TALL;
}

const FILE_LOADER = require.resolve("file-loader", {
  paths: [require.resolve("@docusaurus/utils")],
});
const DARK_LOADER = require.resolve("./figure-dark-loader");
const loaderPath = (file) => file.replace(/\\/g, "/");

const attribute = (name, value) => ({ type: "mdxJsxAttribute", name, value });

const element = (type, name, attributes, children = []) => ({
  type,
  name,
  attributes: Object.entries(attributes).map(([key, value]) =>
    attribute(key, value),
  ),
  children,
});

// `require(request).default` as an attribute value, with the estree MDX
// needs to compile it.
function requireDefault(request) {
  const raw = JSON.stringify(request);
  return {
    type: "mdxJsxAttributeValueExpression",
    value: `require(${raw}).default`,
    data: {
      estree: {
        type: "Program",
        sourceType: "module",
        comments: [],
        body: [
          {
            type: "ExpressionStatement",
            expression: {
              type: "MemberExpression",
              object: {
                type: "CallExpression",
                callee: { type: "Identifier", name: "require" },
                arguments: [{ type: "Literal", value: request, raw }],
                optional: false,
              },
              property: { type: "Identifier", name: "default" },
              computed: false,
              optional: false,
            },
          },
        ],
      },
    },
  };
}

function darkImage(image, svg) {
  const size = (name) => {
    const value = svg.match(new RegExp(`<svg\\b[^>]*\\s${name}="([\\d.]+)"`));
    return value ? { [name]: value[1] } : {};
  };
  const url = image.url.startsWith(".") ? image.url : `./${image.url}`;
  const request = `!${loaderPath(FILE_LOADER)}?name=assets/images/[name]-dark-[hash].[ext]!${loaderPath(DARK_LOADER)}!${url}`;
  return element("mdxJsxFlowElement", "img", {
    className: "lg-figure__dark",
    src: requireDefault(request),
    alt: image.alt || "",
    ...size("width"),
    ...size("height"),
    loading: "lazy",
    decoding: "async",
  });
}

function toFigure(paragraph, file) {
  const children = paragraph.children.filter(
    (n) => !(n.type === "text" && !n.value.trim()),
  );
  if (children.length !== 1 || children[0].type !== "image") return null;

  const image = children[0];
  const match = image.url && image.url.match(NUMBERED);
  if (!image.title || !match) return null;

  const number = match[1];
  const caption = image.title.trim();
  image.title = null;
  const svg = readSvg(image.url, file);
  const classes = ["lg-figure"];
  if (isTall(svg)) classes.push("lg-figure--tall");
  if (svg) classes.push("lg-figure--themed");

  return element(
    "mdxJsxFlowElement",
    "figure",
    { className: classes.join(" "), id: `figure-${number.replace(".", "-")}` },
    [
      image,
      ...(svg ? [darkImage(image, svg)] : []),
      element("mdxJsxFlowElement", "figcaption", {}, [
        element("mdxJsxTextElement", "span", { className: "lg-figure__number" }, [
          { type: "text", value: `Figure ${number}` },
        ]),
        { type: "text", value: ` ${caption}` },
      ]),
    ],
  );
}

function walk(node, file) {
  if (!Array.isArray(node.children)) return;
  node.children = node.children.flatMap((child) => {
    walk(child, file);
    if (child.type === "paragraph") {
      const figure = toFigure(child, file);
      if (figure) return [figure];
    }
    return [child];
  });
}

module.exports = function remarkFigures() {
  return (tree, file) => walk(tree, file);
};

// Docusaurus 3 runs escape-html on Markdown image alt and title text but
// stores the result in a JSX string, which is never decoded, so screen
// readers hear "&#39;". This runs after the default plugins to undo it.
const ENTITIES = { "&quot;": '"', "&#39;": "'", "&lt;": "<", "&gt;": ">", "&amp;": "&" };
const unescapeHtml = (text) =>
  text.replace(/&(?:quot|#39|lt|gt|amp);/g, (entity) => ENTITIES[entity]);

function unescapeImages(node) {
  if (node.name === "img" && Array.isArray(node.attributes)) {
    for (const attribute of node.attributes) {
      if ((attribute.name === "alt" || attribute.name === "title") && typeof attribute.value === "string") {
        attribute.value = unescapeHtml(attribute.value);
      }
    }
  }
  if (Array.isArray(node.children)) node.children.forEach(unescapeImages);
}

module.exports.unescapeImageText = function remarkUnescapeImageText() {
  return (tree) => unescapeImages(tree);
};
