import React from "react";
import clsx from "clsx";
import { ThemeClassNames } from "@docusaurus/theme-common";
import { useDoc } from "@docusaurus/plugin-content-docs/client";
import LastUpdated from "@theme/LastUpdated";
import TagsListInline from "@theme/TagsListInline";
import DocSourceLinks from "@site/src/components/DocSourceLinks";

/**
 * Tags and last-updated metadata as before. "Edit this page" moved out of
 * here: it lives in the right rail on wide screens and in the end-of-lesson
 * block (DocSourceLinks variant="end") everywhere else.
 */
export default function DocItemFooter() {
  const { metadata } = useDoc();
  const { lastUpdatedAt, lastUpdatedBy, tags } = metadata;

  return (
    <footer className={clsx(ThemeClassNames.docs.docFooter, "lg-doc-footer")}>
      {tags.length > 0 && (
        <div className={ThemeClassNames.docs.docFooterTagsRow}>
          <TagsListInline tags={tags} />
        </div>
      )}
      {(lastUpdatedAt || lastUpdatedBy) && (
        <div className="lg-doc-footer__updated">
          <LastUpdated
            lastUpdatedAt={lastUpdatedAt}
            lastUpdatedBy={lastUpdatedBy}
          />
        </div>
      )}
      <DocSourceLinks variant="end" />
    </footer>
  );
}
