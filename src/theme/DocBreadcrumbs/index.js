import React from "react";
import DocBreadcrumbs from "@theme-original/DocBreadcrumbs";
import GuideLocator from "@site/src/components/GuideLocator";

export default function DocBreadcrumbsWrapper(props) {
  return (
    <GuideLocator>
      <DocBreadcrumbs {...props} />
    </GuideLocator>
  );
}
