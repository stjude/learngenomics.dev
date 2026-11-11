import React from "react";
import clsx from "clsx";
import { ThemeClassNames } from "@docusaurus/theme-common";
import { useDoc } from "@docusaurus/plugin-content-docs/client";
import Heading from "@theme/Heading";
import MDXContent from "@theme/MDXContent";
import DocItemTOCMobile from "@theme/DocItem/TOC/Mobile";

/**
 * Same as the theme's DocItem/Content, plus the collapsible "On this page"
 * placed directly under the title (the theme puts it above the title).
 * Lessons declare their title in front matter so the h1 is rendered here;
 * an authored `# Heading` would land below the collapsible.
 */
export default function DocItemContent({ children }) {
  const { metadata, frontMatter, contentTitle, toc } = useDoc();
  const syntheticTitle =
    !frontMatter.hide_title && typeof contentTitle === "undefined"
      ? metadata.title
      : null;
  const hasTOC = !frontMatter.hide_table_of_contents && toc.length > 0;

  return (
    <div className={clsx(ThemeClassNames.docs.docMarkdown, "markdown")}>
      {syntheticTitle && (
        <header>
          <Heading as="h1">{syntheticTitle}</Heading>
        </header>
      )}
      {hasTOC && (
        <div className="lg-toc-mobile">
          <DocItemTOCMobile />
        </div>
      )}
      <MDXContent>{children}</MDXContent>
    </div>
  );
}
