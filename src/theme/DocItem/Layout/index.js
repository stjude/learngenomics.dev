import React from "react";
import { useWindowSize } from "@docusaurus/theme-common";
import { useDoc } from "@docusaurus/plugin-content-docs/client";
import DocItemPaginator from "@theme/DocItem/Paginator";
import DocVersionBanner from "@theme/DocVersionBanner";
import DocVersionBadge from "@theme/DocVersionBadge";
import DocItemFooter from "@theme/DocItem/Footer";
import DocItemTOCDesktop from "@theme/DocItem/TOC/Desktop";
import DocItemContent from "@theme/DocItem/Content";
import DocBreadcrumbs from "@theme/DocBreadcrumbs";
import ContentVisibility from "@theme/ContentVisibility";
import DocSourceLinks from "@site/src/components/DocSourceLinks";

/**
 * One reading column, centered in the space beside the sidebar. On wide
 * screens a rail joins it on the right with "On this page" and the page's
 * source links. The rail renders on every lesson, so the composition doesn't
 * shift between pages with and without section headings. The mobile TOC lives
 * in DocItem/Content so it can sit under the title.
 */
export default function DocItemLayout({ children }) {
  const { metadata, frontMatter, toc } = useDoc();
  const windowSize = useWindowSize();
  const hasTOC = !frontMatter.hide_table_of_contents && toc.length > 0;
  const renderRailTOC =
    hasTOC && (windowSize === "desktop" || windowSize === "ssr");

  return (
    <div className="lg-doc">
      <div className="lg-doc__main">
        <ContentVisibility metadata={metadata} />
        <DocVersionBanner />
        <article>
          <DocBreadcrumbs />
          <DocVersionBadge />
          <DocItemContent>{children}</DocItemContent>
          <DocItemFooter />
        </article>
        <DocItemPaginator />
      </div>
      <aside className="lg-doc__rail" aria-label="Page tools">
        <div className="lg-rail">
          {renderRailTOC && (
            <div className="lg-rail__toc">
              <p className="lg-rail__label">
                On this page
              </p>
              <DocItemTOCDesktop />
            </div>
          )}
          <DocSourceLinks variant="rail" />
        </div>
      </aside>
    </div>
  );
}
