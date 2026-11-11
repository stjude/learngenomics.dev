import React, { useEffect, useState } from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import { useLocation } from "@docusaurus/router";
import {
  formatMinutes,
  pageTitle,
  useGuideMap,
  useReadPages,
} from "@site/src/components/GuideMap/progress";
import styles from "./styles.module.css";

const COLLAPSED_KEY = "learngenomics:band-collapsed";

const trimSlash = (path) => path.replace(/\/+$/, "") || "/";

/**
 * The saved collapsed state lives on <html data-lg-band> so an inline head
 * script (see plugins/guide-map.js) can apply it before the first paint.
 */
function useCollapsed() {
  const [collapsed, setCollapsed] = useState(false);
  useEffect(() => {
    setCollapsed(document.documentElement.dataset.lgBand === "collapsed");
  }, []);
  const toggle = () => {
    const next = document.documentElement.dataset.lgBand !== "collapsed";
    if (next) document.documentElement.dataset.lgBand = "collapsed";
    else delete document.documentElement.dataset.lgBand;
    try {
      window.localStorage.setItem(COLLAPSED_KEY, next ? "1" : "0");
    } catch (e) {
      // Storage can be unavailable; the choice then lasts for this page only.
    }
    setCollapsed(next);
  };
  return [collapsed, toggle];
}

/**
 * The whole guide drawn as one chromosome across the top of every doc page:
 * chapters are segments sized by length, pages are slices you can jump to,
 * and an ink box marks the page you're on.
 */
export default function GuideBand() {
  const { pathname } = useLocation();
  const { chapters, pages } = useGuideMap();
  const readPages = useReadPages();
  const [collapsed, toggleCollapsed] = useCollapsed();
  const current = pages.find(
    (page) => trimSlash(page.permalink) === trimSlash(pathname)
  );

  if (chapters.length === 0) return null;

  const last = chapters.length - 1;

  return (
    <nav className={styles.band} aria-label="Guide overview">
      <div className={styles.inner}>
        <div className={styles.chromosome}>
          <div className={styles.ideogram}>
            {chapters.map((chapter, index) => (
              <span
                key={chapter.label}
                className={clsx(
                  styles.chapter,
                  index === 0 && styles.first,
                  index === last && styles.last
                )}
                style={{
                  flexGrow: chapter.words,
                  "--chapter-color": `var(--lg-chapter-${index + 1})`,
                }}
              >
                {/*
                  Slices are narrower than the 24 px minimum target size in
                  WCAG 2.5.8. They rely on its "equivalent" exception: every
                  page is also linked, at full size, from the sidebar and the
                  mobile menu. The accessibility tests skip slices for the
                  target-size rule only.
                */}
                {chapter.pages.map((page) => {
                  const read = readPages.has(page.id);
                  const here = current && page.id === current.id;
                  return (
                    <Link
                      key={page.id}
                      to={page.permalink}
                      className={clsx(
                        styles.slice,
                        read && styles.read,
                        here && styles.current
                      )}
                      style={{ flexGrow: Math.max(page.words, 1) }}
                      aria-label={`${pageTitle(page)}, ${page.minutes} min${
                        read ? ", read" : ""
                      }`}
                      aria-current={here ? "page" : undefined}
                    >
                      <span className={styles.tip} aria-hidden="true">
                        {pageTitle(page)}{" "}
                        <span className={styles.tipMinutes}>
                          {page.minutes} min
                        </span>
                      </span>
                    </Link>
                  );
                })}
              </span>
            ))}
          </div>

          <ol id="guide-band-labels" className={styles.labels}>
            {chapters.map((chapter, index) => {
              const here = current && current.chapterIndex === index;
              const time = formatMinutes(chapter.minutes);
              return (
                <li
                  key={chapter.label}
                  style={{
                    flexGrow: chapter.words,
                    "--chapter-color": `var(--lg-chapter-${index + 1})`,
                  }}
                >
                  <Link
                    to={chapter.pages[0].permalink}
                    className={clsx(styles.label, here && styles.here)}
                    title={`${chapter.label}, about ${time.long}`}
                    aria-current={here ? "location" : undefined}
                  >
                    <span className={styles.heading}>
                      <span className={styles.number}>
                        {String(index + 1).padStart(2, "0")}
                      </span>
                      <span className={styles.name}>{chapter.label}</span>
                    </span>
                    <span className={styles.time}>
                      <span className={styles.timeLong}>{time.long}</span>
                      <span className={styles.timeShort} aria-hidden="true">
                        {time.short}
                      </span>
                    </span>
                  </Link>
                </li>
              );
            })}
          </ol>
        </div>

        <div className={styles.aside}>
          {current && (
            <p className={styles.position}>
              <span className={styles.long}>
                Page {current.number} of {pages.length}
              </span>
              <span className={styles.short} aria-hidden="true">
                {current.number}/{pages.length}
              </span>
              <span className={styles.minutes}>{current.minutes} min read</span>
            </p>
          )}
          <button
            type="button"
            className={styles.toggle}
            onClick={toggleCollapsed}
            aria-expanded={!collapsed}
            aria-controls="guide-band-labels"
            aria-label="Full guide overview"
            title={
              collapsed
                ? "Expand the guide overview"
                : "Collapse the guide overview"
            }
          >
            <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true">
              <path
                d="M3.5 10l4.5-4.5 4.5 4.5"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.75"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </div>
      </div>
    </nav>
  );
}
