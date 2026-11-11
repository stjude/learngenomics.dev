import React, { useEffect, useRef, useState } from "react";
import clsx from "clsx";
import styles from "./styles.module.css";

// Rows of short "reads" for the poster, in fixed positions so server and
// client render the same thing.
const READS = [
  [0, 4, 18], [0, 26, 14], [0, 44, 20], [0, 70, 16],
  [1, 10, 22], [1, 36, 12], [1, 52, 18], [1, 76, 14],
  [2, 0, 12], [2, 16, 20], [2, 40, 16], [2, 60, 22], [2, 86, 10],
  [3, 6, 16], [3, 28, 18], [3, 50, 14], [3, 68, 20],
  [4, 2, 20], [4, 26, 12], [4, 42, 22], [4, 70, 18],
  [5, 12, 14], [5, 30, 20], [5, 56, 16], [5, 78, 16],
];

function Reads() {
  return (
    <svg
      className={styles.reads}
      viewBox="0 0 100 36"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      {READS.map(([row, x, w], i) => (
        <rect key={i} x={x} y={row * 6 + 1} width={w} height="2.4" rx="1.2" />
      ))}
    </svg>
  );
}

/**
 * A YouTube video behind a click-to-play poster. Nothing loads from YouTube,
 * not even a thumbnail, until the reader presses play, and then only from the
 * privacy-enhanced youtube-nocookie.com domain.
 */
export default function YouTube({ id, title, provider, duration, start, children }) {
  const [playing, setPlaying] = useState(false);
  const frameRef = useRef(null);

  useEffect(() => {
    if (playing) frameRef.current?.focus();
  }, [playing]);

  const params = new URLSearchParams({ autoplay: "1", rel: "0" });
  if (start) params.set("start", String(start));
  const watchUrl = `https://www.youtube.com/watch?v=${id}${start ? `&t=${start}s` : ""}`;

  return (
    <figure className={clsx("lg-figure", styles.figure)}>
      <div className={styles.frame}>
        {playing ? (
          <iframe
            ref={frameRef}
            className={styles.player}
            src={`https://www.youtube-nocookie.com/embed/${id}?${params}`}
            title={`${title} (${provider})`}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerPolicy="strict-origin-when-cross-origin"
            allowFullScreen
          />
        ) : (
          <button
            type="button"
            className={styles.poster}
            onClick={() => setPlaying(true)}
          >
            {/* The accessible name comes from the visible text, so voice control
                users can say what they see; the hidden words fill in the rest. */}
            <Reads />
            <span className={styles.srOnly}>Play: </span>
            <span className={styles.provider}>{provider}</span>
            <span className={styles.srOnly}>, </span>
            <span className={styles.title}>{title}</span>
            <span className={styles.srOnly}>, </span>
            <span className={styles.play} aria-hidden="true">
              <svg viewBox="0 0 24 24">
                <path d="M8 5.5v13l10.5-6.5z" />
              </svg>
            </span>
            <span className={styles.duration}>{duration}</span>
            <span className={styles.srOnly}>. Loads the video from YouTube.</span>
          </button>
        )}
      </div>
      <p className={styles.note}>
        {playing ? "Playing from YouTube. " : "Nothing loads from YouTube until you press play. "}
        <a href={watchUrl} target="_blank" rel="noopener noreferrer">
          Watch on YouTube
        </a>
      </p>
      {children && (
        <figcaption>
          <span className="lg-figure__number">Video</span> {children}
        </figcaption>
      )}
    </figure>
  );
}
