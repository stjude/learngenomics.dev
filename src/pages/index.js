import React from "react";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import GuideMap from "@site/src/components/GuideMap";
import {
  formatMinutes,
  useGuideMap,
  useReadPages,
} from "@site/src/components/GuideMap/progress";
import styles from "./index.module.css";

function Hero() {
  const { siteConfig } = useDocusaurusContext();
  const { chapters, pages, totalWords } = useGuideMap();
  const readPages = useReadPages();
  const first = pages[0];
  const start = "/docs/before-you-begin";
  const next = pages.find((page) => !readPages.has(page.id));
  const started = readPages.size > 0 && next;
  const minutes = Math.round(totalWords / 200 / 5) * 5;

  return (
    <header className={styles.band}>
      <div className={styles.hero}>
        <div className={styles.intro}>
          <h1 className={styles.title}>{siteConfig.title}</h1>
          <p className={styles.lede}>{siteConfig.tagline}</p>
          <div className={styles.actions}>
            {started ? (
              <>
                <Link className={styles.primary} to={next.permalink}>
                  Continue: {next.title} →
                </Link>
                <Link className={styles.secondary} to={start}>
                  Start from the beginning
                </Link>
              </>
            ) : (
              <Link className={styles.primary} to={start}>
                Start reading →
              </Link>
            )}
          </div>
          <p className={styles.meta}>
            {chapters.length} chapters · {pages.length} pages · about{" "}
            {formatMinutes(minutes).long}
          </p>
          <p className={styles.invite}>
            Spot something unclear? Every page has an edit link.{" "}
            <Link href="https://github.com/learngenomics/learngenomics.dev">
              Contribute on GitHub →
            </Link>
          </p>
        </div>
        <div className={styles.side}>
          <div className={styles.panel}>
            <GuideMap nextPageId={started ? next.id : first.id} />
          </div>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout title={siteConfig.title} description={siteConfig.tagline}>
      <main className={styles.stage}>
        <Hero />
      </main>
    </Layout>
  );
}
