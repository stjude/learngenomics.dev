import React, { useEffect, useRef, useState } from "react";
import useBrokenLinks from "@docusaurus/useBrokenLinks";
import MDXComponents from "@theme-original/MDXComponents";

/**
 * A Markdown table that joins the tab order only when it scrolls sideways, so
 * keyboard users can scroll it with the arrow keys.
 */
function Table(props) {
  const ref = useRef(null);
  const [scrolls, setScrolls] = useState(false);

  useEffect(() => {
    const table = ref.current;
    if (!table) return undefined;
    const check = () => setScrolls(table.scrollWidth > table.clientWidth + 1);
    check();
    const observer = new ResizeObserver(check);
    observer.observe(table);
    return () => observer.disconnect();
  }, []);

  return <table ref={ref} tabIndex={scrolls ? 0 : undefined} {...props} />;
}

/** A numbered figure (see plugins/remark-figures.js) that links can target. */
function Figure(props) {
  useBrokenLinks().collectAnchor(props.id);
  return <figure {...props} />;
}

export default { ...MDXComponents, table: Table, figure: Figure };
