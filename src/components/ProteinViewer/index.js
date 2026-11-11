import React, { useCallback, useEffect, useRef, useState } from "react";
import clsx from "clsx";
import useBrokenLinks from "@docusaurus/useBrokenLinks";
import useBaseUrl from "@docusaurus/useBaseUrl";
import { useColorMode } from "@docusaurus/theme-common";
import prepareStructure from "./prepareStructure";
import styles from "./styles.module.css";

const DOMAINS = [
  { key: "tmd1", resi: "1-388" },
  { key: "nbd1", resi: "389-637" },
  { key: "tmd2", resi: "845-1173" },
  { key: "nbd2", resi: "1202-1451" },
];

const FOCUS_RESIDUE = 508;

// Chain A of the RCSB file, trimmed to its backbone plus Phe508 and turned so
// the membrane domains stand at the top, matching the poster images.
const STRUCTURE = {
  chain: "A",
  keepResidues: [FOCUS_RESIDUE],
  rotation: [
    [-0.319307, -0.947635, 0.005611],
    [0.013686, 0.001309, 0.999905],
    [-0.947552, 0.319354, 0.012551],
  ],
  translation: [195.6083, -135.1624, 93.6661],
};

const PALETTES = {
  light: {
    tmd1: "#4b4fa0",
    tmd2: "#8a8dc8",
    nbd1: "#2f7d57",
    nbd2: "#7cc29c",
    focus: "#e0322a",
    label: "#ffffff",
  },
  dark: {
    tmd1: "#9a9dd2",
    tmd2: "#c4c6ea",
    nbd1: "#63b98d",
    nbd2: "#a6dcbf",
    focus: "#ff6a5f",
    label: "#170d10",
  },
};

function hasWebGL() {
  try {
    const canvas = document.createElement("canvas");
    return Boolean(canvas.getContext("webgl2") || canvas.getContext("webgl"));
  } catch (error) {
    return false;
  }
}

function motionMs(ms) {
  return window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : ms;
}

function paint(viewer, palette, focused) {
  viewer.setStyle({}, {});
  DOMAINS.forEach(({ key, resi }) => {
    viewer.setStyle({ resi }, { cartoon: { color: palette[key] } });
  });
  viewer.setStyle(
    { resi: FOCUS_RESIDUE },
    {
      cartoon: { color: palette.focus },
      sphere: { color: palette.focus, scale: 0.95 },
    },
  );
  viewer.removeAllLabels();
  if (focused) {
    viewer.addLabel("Phe508", {
      position: { resi: FOCUS_RESIDUE, atom: "CZ" },
      backgroundColor: palette.focus,
      backgroundOpacity: 1,
      fontColor: palette.label,
      fontSize: 14,
      font: "Source Sans 3, system-ui, sans-serif",
      borderThickness: 0,
      inFront: true,
      screenOffset: { x: 16, y: -16 },
    });
  }
  viewer.render();
}

/**
 * A click-to-load 3Dmol.js viewer for one protein structure. Until the
 * reader asks for it, the figure is a static poster, so the library and the
 * structure file, fetched from `src`, cost nothing. Once loaded, the viewer only takes pointer
 * input while active, so it never traps page scrolling.
 */
export default function ProteinViewer({
  src,
  poster,
  description,
  number,
  children,
}) {
  const { colorMode } = useColorMode();
  const stageRef = useRef(null);
  const hostRef = useRef(null);
  const viewerRef = useRef(null);
  const homeViewRef = useRef(null);
  const [status, setStatus] = useState("idle");
  const [active, setActive] = useState(false);
  const [focused, setFocused] = useState(false);
  const [coarse, setCoarse] = useState(false);

  const id = `figure-${number.replace(".", "-")}`;
  useBrokenLinks().collectAnchor(id);
  const posterUrl = useBaseUrl(`${poster}-${colorMode}.webp`);
  const palette = PALETTES[colorMode] ?? PALETTES.light;

  useEffect(() => {
    setCoarse(window.matchMedia("(pointer: coarse)").matches);
  }, []);

  const load = useCallback(async () => {
    if (status === "loading" || status === "ready") return;
    if (!hasWebGL()) {
      setStatus("unsupported");
      return;
    }
    setStatus("loading");
    try {
      const [module, response] = await Promise.all([
        import("3dmol/build/3Dmol-min.js"),
        fetch(src),
      ]);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const pdb = prepareStructure(await response.text(), STRUCTURE);
      const $3Dmol = module.default ?? module;
      const viewer = $3Dmol.createViewer(hostRef.current, {
        backgroundAlpha: 0,
        antialias: true,
      });
      viewer.addModel(pdb, "pdb");
      viewer.zoomTo();
      viewerRef.current = viewer;
      homeViewRef.current = viewer.getView();
      setStatus("ready");
      setActive(true);
    } catch (error) {
      setStatus("error");
    }
  }, [status, src]);

  useEffect(() => {
    const viewer = viewerRef.current;
    if (status !== "ready" || !viewer) return;
    paint(viewer, palette, focused);
  }, [status, palette, focused]);

  useEffect(() => {
    const viewer = viewerRef.current;
    if (status !== "ready" || !viewer) return undefined;
    const observer = new ResizeObserver(() => {
      viewer.resize();
      viewer.render();
    });
    observer.observe(hostRef.current);
    return () => observer.disconnect();
  }, [status]);

  useEffect(
    () => () => {
      viewerRef.current?.clear();
      viewerRef.current = null;
    },
    [],
  );

  useEffect(() => {
    if (!active) return undefined;
    const onKey = (event) => {
      if (event.key === "Escape") setActive(false);
    };
    const onPointer = (event) => {
      if (!stageRef.current?.contains(event.target)) setActive(false);
    };
    document.addEventListener("keydown", onKey);
    document.addEventListener("pointerdown", onPointer);
    return () => {
      document.removeEventListener("keydown", onKey);
      document.removeEventListener("pointerdown", onPointer);
    };
  }, [active]);

  const reset = () => {
    const viewer = viewerRef.current;
    if (!viewer) return;
    setFocused(false);
    viewer.setView(homeViewRef.current);
    viewer.render();
  };

  const findFocus = () => {
    const viewer = viewerRef.current;
    if (!viewer) return;
    setFocused(true);
    viewer.zoomTo({ resi: FOCUS_RESIDUE }, motionMs(700));
    viewer.zoom(0.2, motionMs(700));
  };

  const ready = status === "ready";
  const failed = status === "unsupported" || status === "error";

  return (
    <figure className={clsx("lg-figure", styles.figure)} id={id}>
      <div
        ref={stageRef}
        className={clsx(
          styles.stage,
          ready && styles.isReady,
          active && styles.isActive,
        )}
      >
        <img
          className={styles.poster}
          src={posterUrl}
          alt=""
          width="1200"
          height="900"
          decoding="async"
          loading="lazy"
        />
        <div ref={hostRef} className={styles.host} aria-hidden="true" />

        {!ready && (
          <div className={styles.launch}>
            {failed ? (
              <p className={styles.message} role="status">
                {status === "unsupported"
                  ? "Your browser can't show 3D graphics here because WebGL is off or unavailable. The picture shows the same structure."
                  : "The 3D structure didn't load. Check your connection and try again."}
                {status === "error" && (
                  <button
                    type="button"
                    className={styles.retry}
                    onClick={load}
                  >
                    Try again
                  </button>
                )}
              </p>
            ) : (
              <>
                <button
                  type="button"
                  className={styles.launchButton}
                  onClick={load}
                  disabled={status === "loading"}
                  aria-describedby={`${id}-size`}
                >
                  <CubeIcon spinning={status === "loading"} />
                  {status === "loading" ? "Loading…" : "View in 3D"}
                </button>
                <span id={`${id}-size`} className={styles.launchNote}>
                  Loads about 0.4 MB
                </span>
              </>
            )}
          </div>
        )}

        {ready && !active && (
          <button
            type="button"
            className={styles.wake}
            onClick={() => setActive(true)}
          >
            <span className={styles.pill}>
              {coarse ? "Tap to rotate and zoom" : "Click to rotate and zoom"}
            </span>
          </button>
        )}

        {ready && active && (
          <div className={styles.activeBar}>
            <span className={styles.hint}>
              {coarse
                ? "Drag to rotate, pinch to zoom"
                : "Drag to rotate, scroll to zoom"}
            </span>
            <button
              type="button"
              className={styles.pillButton}
              onClick={() => setActive(false)}
            >
              Done
            </button>
          </div>
        )}
      </div>

      <div className={styles.toolbar}>
        <ul className={styles.legend} aria-label="Color key">
          <li>
            <span className={styles.swatches} aria-hidden="true">
              <i style={{ background: palette.tmd1 }} />
              <i style={{ background: palette.tmd2 }} />
            </span>
            Membrane domains
          </li>
          <li>
            <span className={styles.swatches} aria-hidden="true">
              <i style={{ background: palette.nbd1 }} />
              <i style={{ background: palette.nbd2 }} />
            </span>
            ATP-binding domains
          </li>
          <li>
            <span className={styles.swatches} aria-hidden="true">
              <i className={styles.dot} style={{ background: palette.focus }} />
            </span>
            Phe508
          </li>
        </ul>
        {ready && (
          <div className={styles.actions}>
            <button
              type="button"
              className={styles.toolButton}
              onClick={findFocus}
              aria-pressed={focused}
            >
              Find Phe508
            </button>
            <button type="button" className={styles.toolButton} onClick={reset}>
              Reset view
            </button>
          </div>
        )}
      </div>

      <p className={styles.srOnly}>{description}</p>

      <figcaption>
        <span className="lg-figure__number">Figure {number}</span> {children}
      </figcaption>
    </figure>
  );
}

function CubeIcon({ spinning }) {
  return (
    <svg
      viewBox="0 0 20 20"
      aria-hidden="true"
      className={clsx(styles.icon, spinning && styles.spinning)}
    >
      <path
        d="M10 2.2 16.8 6v8L10 17.8 3.2 14V6L10 2.2Z M3.2 6 10 9.9 16.8 6 M10 9.9v7.9"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinejoin="round"
      />
    </svg>
  );
}
