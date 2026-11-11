import { useEffect, useMemo, useState } from "react";
import { usePluginData } from "@docusaurus/useGlobalData";

const STORAGE_KEY = "learngenomics:read-pages";
const CHANGE_EVENT = "learngenomics:progress-change";

function loadReadPages() {
  try {
    const stored = JSON.parse(window.localStorage.getItem(STORAGE_KEY));
    return new Set(Array.isArray(stored) ? stored : []);
  } catch (e) {
    return new Set();
  }
}

function saveReadPages(pages) {
  try {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify([...pages]));
  } catch (e) {
    // Storage can be unavailable (private mode, quotas); progress is optional.
  }
  window.dispatchEvent(new Event(CHANGE_EVENT));
}

export function markPageRead(id) {
  const pages = loadReadPages();
  if (pages.has(id)) return;
  pages.add(id);
  saveReadPages(pages);
}

export function clearReadPages() {
  saveReadPages(new Set());
}

/** "25 min" / "1 hr 5 min", and a compact "25m" / "1h 5m" for small screens. */
export function formatMinutes(total) {
  const hours = Math.floor(total / 60);
  const minutes = total % 60;
  if (hours === 0) return { long: `${minutes} min`, short: `${minutes}m` };
  return {
    long: minutes ? `${hours} hr ${minutes} min` : `${hours} hr`,
    short: minutes ? `${hours}h ${minutes}m` : `${hours}h`,
  };
}

/** Page ids the reader has finished, stored only in this browser. */
/** A page's title, led by its section when it has one ("Types of Sequencing: Introduction"). */
export function pageTitle(page) {
  return page.section ? `${page.section}: ${page.title}` : page.title;
}

export function useReadPages() {
  const [readPages, setReadPages] = useState(() => new Set());
  useEffect(() => {
    const sync = () => setReadPages(loadReadPages());
    sync();
    window.addEventListener("storage", sync);
    window.addEventListener(CHANGE_EVENT, sync);
    return () => {
      window.removeEventListener("storage", sync);
      window.removeEventListener(CHANGE_EVENT, sync);
    };
  }, []);
  return readPages;
}

/** The guide's chapters and pages, in reading order, with word counts. */
export function useGuideMap() {
  const data = usePluginData("guide-map");
  return useMemo(() => {
    const chapters = (data && data.chapters) || [];
    const pages = [];
    chapters.forEach((chapter, chapterIndex) =>
      chapter.pages.forEach((page, pageIndex) =>
        pages.push({
          ...page,
          chapterIndex,
          pageIndex,
          number: pages.length + 1,
        })
      )
    );
    const totalWords = pages.reduce((sum, page) => sum + page.words, 0);
    return { chapters, pages, totalWords };
  }, [data]);
}
