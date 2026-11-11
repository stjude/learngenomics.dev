import React, { useState } from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import {
  clearReadPages,
  formatMinutes,
  pageTitle,
  useGuideMap,
  useReadPages,
} from "@site/src/components/GuideMap/progress";
import styles from "./styles.module.css";

/**
 * A map of the guide: one track per chapter, one pill per page, each
 * sized by word count. Pages the reader has finished fill in. Each pill links
 * to its page and shows the page's title on hover or focus.
 *
 * Pills are narrower than the 24 px minimum target size in WCAG 2.5.8. Each
 * chapter expands into a full-size list of its page links, which meets the
 * criterion's "equivalent" exception. The accessibility tests skip pills for
 * the target-size rule only.
 */
export default function GuideMap({ nextPageId }) {
  const { chapters, pages, totalWords } = useGuideMap();
  const readPages = useReadPages();
  const [open, setOpen] = useState(() => new Set());
  const toggle = (label) =>
    setOpen((was) => {
      const next = new Set(was);
      if (next.has(label)) next.delete(label);
      else next.add(label);
      return next;
    });
  const longest = Math.max(...chapters.map((chapter) => chapter.words), 1);
  const readWords = pages
    .filter((page) => readPages.has(page.id))
    .reduce((sum, page) => sum + page.words, 0);
  const percent = Math.round((readWords / Math.max(totalWords, 1)) * 100);

  return (
    <section className={styles.map} aria-labelledby="guide-map-title">
      <div className={styles.heading}>
        <h2 id="guide-map-title" className={styles.title}>
          The guide
        </h2>
        {readPages.size > 0 && (
          <p className={styles.percent}>You're {percent}% through</p>
        )}
      </div>

      <div className={styles.ruler} aria-hidden="true" />

      <ol className={styles.tracks}>
        {chapters.map((chapter, index) => {
          const read = chapter.pages.filter((page) => readPages.has(page.id));
          const expanded = open.has(chapter.label);
          const listId = `guide-map-pages-${index + 1}`;
          return (
            <li
              key={chapter.label}
              className={styles.track}
              style={{ "--chapter-color": `var(--lg-chapter-${index + 1})` }}
            >
              <button
                type="button"
                className={styles.expand}
                aria-expanded={expanded}
                aria-controls={listId}
                aria-label={`Pages in ${chapter.label}`}
                onClick={() => toggle(chapter.label)}
              >
                <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true">
                  <path
                    d="M6 3.5 10.5 8 6 12.5"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.75"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
              </button>
              <Link to={chapter.pages[0].permalink} className={styles.label}>
                <span className={styles.number}>
                  {String(index + 1).padStart(2, "0")}
                </span>
                {chapter.label}
                <span className={styles.srOnly}>
                  {`, ${chapter.pages.length} pages, about ${formatMinutes(chapter.minutes).long}`}
                  {readPages.size > 0 ? `, ${read.length} read` : ""}
                </span>
              </Link>
              <ol
                className={styles.pills}
                style={{ width: `${(chapter.words / longest) * 100}%` }}
              >
                {chapter.pages.map((page, pageIndex) => {
                  const pageRead = readPages.has(page.id);
                  const next = page.id === nextPageId;
                  // Where the pill's middle falls across the widest track, so
                  // tips near either end open inward and stay in the panel.
                  const before = chapter.pages
                    .slice(0, pageIndex)
                    .reduce((sum, other) => sum + other.words, 0);
                  const middle = (before + page.words / 2) / longest;
                  return (
                    <li key={page.id} style={{ flexGrow: page.words }}>
                      <Link
                        to={page.permalink}
                        className={clsx(
                          styles.pill,
                          pageRead && styles.read,
                          next && styles.next,
                          middle < 0.2 && styles.tipStart,
                          middle > 0.8 && styles.tipEnd
                        )}
                        aria-label={`${pageTitle(page)}, ${page.minutes} min${
                          pageRead ? ", read" : ""
                        }${next ? ", up next" : ""}`}
                      >
                        <span className={styles.tip} aria-hidden="true">
                          {pageTitle(page)}{" "}
                          <span className={styles.tipMinutes}>
                            {page.minutes} min
                          </span>
                        </span>
                      </Link>
                    </li>
                  );
                })}
              </ol>
              <ol id={listId} className={styles.pageList} hidden={!expanded}>
                {chapter.pages.map((page, pageIndex) => {
                  const pageRead = readPages.has(page.id);
                  const startsSection =
                    page.section &&
                    page.section !== chapter.pages[pageIndex - 1]?.section;
                  return (
                    <li key={page.id}>
                      {startsSection && (
                        <span className={styles.section} aria-hidden="true">
                          {page.section}
                        </span>
                      )}
                      <Link
                        to={page.permalink}
                        className={clsx(styles.pageLink, pageRead && styles.read)}
                      >
                        <span className={styles.pageTitle}>
                          {page.section && (
                            <span className={styles.srOnly}>
                              {page.section}:{" "}
                            </span>
                          )}
                          {page.title}
                        </span>
                        <span className={styles.pageMinutes}>
                          {page.minutes} min
                          {pageRead && (
                            <span className={styles.srOnly}>, read</span>
                          )}
                        </span>
                      </Link>
                    </li>
                  );
                })}
              </ol>
            </li>
          );
        })}
      </ol>

      <div className={styles.legend}>
        <span>
          <i className={styles.keyRead} />
          Read
        </span>
        <span>
          <i className={styles.keyNext} />
          Up next
        </span>
        <span>
          <i className={styles.keyUnread} />
          Not yet
        </span>
        <p className={styles.note}>
          Each bar is one page, sized by its word count. Progress is saved only
          in this browser.
          {readPages.size > 0 && (
            <>
              {" "}
              <button
                type="button"
                className={styles.reset}
                onClick={clearReadPages}
              >
                Reset progress
              </button>
            </>
          )}
        </p>
      </div>
    </section>
  );
}
