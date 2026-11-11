import React from "react";
import clsx from "clsx";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useDoc } from "@docusaurus/plugin-content-docs/client";
import styles from "./styles.module.css";

function PencilIcon() {
  return (
    <svg viewBox="0 0 16 16" aria-hidden="true" className={styles.icon}>
      <path
        d="M10.9 2.6a1.5 1.5 0 0 1 2.1 0l.4.4a1.5 1.5 0 0 1 0 2.1L6 12.5 2.5 13.5l1-3.5 7.4-7.4Z"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.4"
        strokeLinejoin="round"
      />
      <path d="M9.5 4l2.5 2.5" stroke="currentColor" strokeWidth="1.4" />
    </svg>
  );
}

function IssueIcon() {
  return (
    <svg viewBox="0 0 16 16" aria-hidden="true" className={styles.icon}>
      <circle
        cx="8"
        cy="8"
        r="5.8"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.4"
      />
      <path d="M8 4.8v3.8" stroke="currentColor" strokeWidth="1.5" />
      <circle cx="8" cy="11" r="0.9" fill="currentColor" />
    </svg>
  );
}

/**
 * "Edit this page" and "Report an issue" for the current doc. The rail
 * variant sits under "On this page" on wide screens; the end variant closes
 * the lesson on narrower screens. CSS shows exactly one of them.
 */
export default function DocSourceLinks({ variant }) {
  const { siteConfig } = useDocusaurusContext();
  const { metadata } = useDoc();
  const { editUrl, permalink, title } = metadata;
  if (!editUrl) return null;

  const repository = editUrl.split("/tree/")[0];
  const pageUrl = new URL(permalink, siteConfig.url).toString();
  const issueParams = new URLSearchParams({
    title: `${title}: `,
    body: `Page: ${pageUrl}\n\n`,
  });
  const issueUrl = `${repository}/issues/new?${issueParams.toString()}`;

  return (
    <nav
      aria-label="Improve this page"
      className={clsx("lg-source", `lg-source--${variant}`, styles[variant])}
    >
      {variant === "end" && (
        <p className={styles.prompt}>
          Spotted a mistake or something to improve?
        </p>
      )}
      <ul className={styles.links}>
        <li>
          <a
            href={editUrl}
            target="_blank"
            rel="noreferrer noopener"
            className={clsx("theme-edit-this-page", styles.link)}
          >
            <PencilIcon />
            Edit this page
          </a>
        </li>
        <li>
          <a
            href={issueUrl}
            target="_blank"
            rel="noreferrer noopener"
            className={styles.link}
          >
            <IssueIcon />
            Report an issue
          </a>
        </li>
      </ul>
    </nav>
  );
}
