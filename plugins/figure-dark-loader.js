// Webpack loader: turns an SVG figure into its dark-mode copy.
const { toDark } = require("./figure-dark");

module.exports = function figureDarkLoader(source) {
  return toDark(String(source));
};
