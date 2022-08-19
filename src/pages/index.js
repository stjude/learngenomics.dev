import React from "react";
import clsx from "clsx";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import styles from "./index.module.css";
import LogoFull from "@site/static/img/learngenomics-logo-full.svg";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header
      className={clsx("hero hero--primary", styles.heroBanner)}
      style={{ padding: "0" }}
    >
      <div
        className="container"
        style={{
          backgroundImage: "url(img/BG-texture.svg)",
          backgroundRepeat: "no-repeat",
          backgroundPosition: "center center",
          backgroundSize: "100vh 100vw",
          height: "100vh",
          width: "100vw",
          minWidth: "100vw",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          flexDirection: "column",
        }}
      >
        <LogoFull height="200" style={{ paddingBottom: "20px" }} />
        <h1 className="hero__title" style={{ paddingBottom: "20px" }}>
          {siteConfig.title}
        </h1>
        {/* <p className="hero__subtitle">{siteConfig.tagline}</p> */}
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/biological-foundations/cells-genomes-dna-chromosomes"
          >
            Start Here
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout title={`${siteConfig.title}`} description={`${siteConfig.title}`}>
      <HomepageHeader />
    </Layout>
  );
}
