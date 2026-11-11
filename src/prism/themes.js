// Code themes drawn from the site palette.

const light = {
  plain: { color: "#1f1115", backgroundColor: "#f8f6f7" },
  styles: [
    {
      types: ["comment", "prolog", "doctype", "cdata"],
      style: { color: "#7a6d72", fontStyle: "italic" },
    },
    { types: ["punctuation", "operator"], style: { color: "#65585d" } },
    {
      types: ["keyword", "selector", "important", "atrule", "builtin"],
      style: { color: "#4b4fa0" },
    },
    {
      types: ["string", "char", "attr-value", "regex", "inserted"],
      style: { color: "#23774f" },
    },
    {
      types: ["number", "boolean", "constant", "symbol", "deleted"],
      style: { color: "#b7261e" },
    },
    {
      types: ["function", "class-name", "tag"],
      style: { color: "#1f1115", fontWeight: "600" },
    },
    {
      types: ["variable", "property", "attr-name"],
      style: { color: "#8a4a1c" },
    },
  ],
};

const dark = {
  plain: { color: "#f2edef", backgroundColor: "#22161a" },
  styles: [
    {
      types: ["comment", "prolog", "doctype", "cdata"],
      style: { color: "#9a8c91", fontStyle: "italic" },
    },
    { types: ["punctuation", "operator"], style: { color: "#b7aaaf" } },
    {
      types: ["keyword", "selector", "important", "atrule", "builtin"],
      style: { color: "#b9bbea" },
    },
    {
      types: ["string", "char", "attr-value", "regex", "inserted"],
      style: { color: "#8fd3ae" },
    },
    {
      types: ["number", "boolean", "constant", "symbol", "deleted"],
      style: { color: "#ff8a82" },
    },
    {
      types: ["function", "class-name", "tag"],
      style: { color: "#ffffff", fontWeight: "600" },
    },
    {
      types: ["variable", "property", "attr-name"],
      style: { color: "#f6c35c" },
    },
  ],
};

module.exports = { light, dark };
