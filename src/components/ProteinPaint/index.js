import React, { useCallback, useEffect, useRef, useState } from "react";
import clsx from "clsx";
import useBrokenLinks from "@docusaurus/useBrokenLinks";
import styles from "./styles.module.css";

const HOST = "https://proteinpaint.stjude.org";
const SCRIPT = `${HOST}/bin/proteinpaint.js`;

// Copy-number classes add whole-gene bars that crowd out the point mutations
// this figure is about.
const HIDDEN_CLASSES = [
  "CNV_amp",
  "CNV_loss",
  "CNV_amplification",
  "CNV_homozygous_deletion",
  "CNV_loh",
];

const MIN_PANEL_WIDTH = 360;

let scriptPromise = null;

function loadScript() {
  if (window.runproteinpaint) return Promise.resolve();
  if (scriptPromise) return scriptPromise;
  scriptPromise = new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = SCRIPT;
    script.async = true;
    script.onload = () =>
      window.runproteinpaint
        ? resolve()
        : reject(new Error("ProteinPaint did not initialise"));
    script.onerror = () => {
      script.remove();
      scriptPromise = null;
      reject(new Error("ProteinPaint failed to load"));
    };
    document.head.appendChild(script);
  });
  return scriptPromise;
}

function mainSvg(holder) {
  let widest = null;
  holder.querySelectorAll("svg").forEach((svg) => {
    if (!widest || svg.getBoundingClientRect().width > widest.getBoundingClientRect().width) widest = svg;
  });
  return widest;
}

// ProteinPaint's gene view never draws narrower than 800 px on its own, so
// resize the main panel to the room the column actually has. Returns true if
// that triggered a re-render.
function fitBlock(block, holder) {
  const svg = mainSvg(holder);
  if (!svg) return false;
  const stage = holder.parentElement;
  let overflow =
    svg.getBoundingClientRect().right - holder.getBoundingClientRect().right;
  const scrollExtra = stage.scrollWidth - stage.clientWidth;
  if (scrollExtra > 0) overflow = Math.max(overflow, scrollExtra);
  const width = Math.max(MIN_PANEL_WIDTH, Math.floor(block.width - overflow - 2));
  if (Math.abs(width - block.width) < 4) return false;
  block.zoomedin = false;
  block.pannedpx = undefined;
  block.resized = true;
  block.width = width;
  block.block_coord_updated();
  return true;
}

// On narrow screens the plot scrolls sideways; start with the most
// recurrent variant in view rather than the empty left margin.
function centreHotspot(stage) {
  if (stage.scrollWidth <= stage.clientWidth) return;
  let biggest = null;
  stage.querySelectorAll("circle").forEach((c) => {
    const r = c.r?.baseVal?.value ?? 0;
    if (!biggest || r > biggest.r) biggest = { c, r };
  });
  if (!biggest) return;
  const box = biggest.c.getBoundingClientRect();
  const frame = stage.getBoundingClientRect();
  stage.scrollLeft +=
    box.left + box.width / 2 - (frame.left + frame.width / 2);
}

function foldLegend(holder) {
  const toggle = [...holder.querySelectorAll(".sja_clb")].find(
    (el) => el.textContent.trim() === "LEGEND",
  );
  toggle?.click();
}

/**
 * A live ProteinPaint lollipop plot. The library loads when the figure nears
 * the viewport, so readers who never scroll this far don't download it.
 */
export default function ProteinPaint({
  gene,
  dslabel = "GDC",
  genome = "hg38",
  description,
  number,
  children,
}) {
  const holderRef = useRef(null);
  const stageRef = useRef(null);
  const blockRef = useRef(null);
  const [status, setStatus] = useState("idle");
  const [overflowing, setOverflowing] = useState(false);

  const figureRef = useRef(null);
  const id = `figure-${number.replace(".", "-")}`;
  useBrokenLinks().collectAnchor(id);

  const load = useCallback(async () => {
    if (status === "loading" || status === "ready") return;
    setStatus("loading");
    const holder = holderRef.current;
    holder.innerHTML = "";
    blockRef.current = null;
    try {
      await loadScript();
      let settled = false;
      let attempts = 0;
      await window.runproteinpaint({
        host: HOST,
        holder,
        noheader: true,
        nobox: true,
        hide_dsHandles: true,
        genome,
        gene,
        tracks: [
          {
            type: "mds3",
            dslabel,
            legend: { mclass: { hiddenvalues: new Set(HIDDEN_CLASSES) } },
            callbackOnRender: (tk, block) => {
              if (settled) return;
              if (!blockRef.current) {
                blockRef.current = block;
                foldLegend(holder);
              }
              attempts += 1;
              if (attempts < 4 && fitBlock(block, holder)) return;
              settled = true;
              // Let ProteinPaint's label animation finish before revealing.
              setTimeout(() => setStatus("ready"), 1200);
            },
          },
        ],
      });
    } catch (error) {
      setStatus("error");
    }
  }, [status, gene, dslabel, genome]);

  useEffect(() => {
    if (status !== "idle") return undefined;
    if (!("IntersectionObserver" in window)) {
      load();
      return undefined;
    }
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries.some((entry) => entry.isIntersecting)) {
          observer.disconnect();
          load();
        }
      },
      { rootMargin: "600px 0px" },
    );
    observer.observe(figureRef.current);
    return () => observer.disconnect();
  }, [status, load]);

  useEffect(() => {
    if (status !== "ready") return undefined;
    const holder = holderRef.current;
    const stage = stageRef.current;
    centreHotspot(stage);
    setOverflowing(stage.scrollWidth > stage.clientWidth);
    let frame = 0;
    const observer = new ResizeObserver(() => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        if (blockRef.current) fitBlock(blockRef.current, holder);
        setOverflowing(stage.scrollWidth > stage.clientWidth);
      });
    });
    observer.observe(holder);
    return () => {
      cancelAnimationFrame(frame);
      observer.disconnect();
    };
  }, [status]);

  useEffect(() => {
    const holder = holderRef.current;
    return () => {
      if (holder) holder.innerHTML = "";
    };
  }, []);

  const ready = status === "ready";

  return (
    <figure
      className={clsx("lg-figure", styles.figure)}
      id={id}
      ref={figureRef}
    >
      <div className={styles.card} data-pp-done={ready ? "" : undefined}>
        {!ready && (
          <div className={styles.placeholder}>
            {status === "error" ? (
              <p className={styles.message} role="status">
                The interactive view didn't load. Check your connection and
                try again.
                <button type="button" className={styles.retry} onClick={load}>
                  Try again
                </button>
              </p>
            ) : (
              <p className={styles.loading} role="status">
                <LollipopIcon spinning />
                <span>
                  Loading <em>{gene}</em> variants from ProteinPaint…
                </span>
              </p>
            )}
          </div>
        )}
        {/* Kept in layout while loading so ProteinPaint can measure it. */}
        <div
          ref={stageRef}
          className={clsx(styles.stage, !ready && styles.offstage)}
        >
          <div ref={holderRef} />
        </div>
      </div>

      {ready && (
        <p className={styles.hint}>
          {overflowing && "Scroll sideways to see the whole protein. "}
          Click a circle to list its variants and samples. Drag along the
          ruler to zoom into a region.
        </p>
      )}

      <p className={styles.srOnly}>{description}</p>

      <figcaption>
        <span className="lg-figure__number">Figure {number}</span> {children}
      </figcaption>
    </figure>
  );
}

function LollipopIcon({ spinning }) {
  return (
    <svg
      viewBox="0 0 20 20"
      aria-hidden="true"
      className={clsx(styles.icon, spinning && styles.pulsing)}
    >
      <path
        d="M3 17.5h14M6 17.5V11M10 17.5V6.5M14 17.5v-5"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
      <circle cx="6" cy="9.25" r="1.75" fill="currentColor" />
      <circle cx="10" cy="4.25" r="2.25" fill="currentColor" />
      <circle cx="14" cy="10.75" r="1.75" fill="currentColor" />
    </svg>
  );
}
