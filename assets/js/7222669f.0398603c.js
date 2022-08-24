"use strict";(self.webpackChunklearngenomics_dev=self.webpackChunklearngenomics_dev||[]).push([[859],{3905:function(e,n,t){t.d(n,{Zo:function(){return u},kt:function(){return m}});var r=t(7294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function o(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function i(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?o(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var l=r.createContext({}),c=function(e){var n=r.useContext(l),t=n;return e&&(t="function"==typeof e?e(n):i(i({},n),e)),t},u=function(e){var n=c(e.components);return r.createElement(l.Provider,{value:n},e.children)},p={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},d=r.forwardRef((function(e,n){var t=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),d=c(t),m=a,h=d["".concat(l,".").concat(m)]||d[m]||p[m]||o;return t?r.createElement(h,i(i({ref:n},u),{},{components:t})):r.createElement(h,i({ref:n},u))}));function m(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var o=t.length,i=new Array(o);i[0]=d;var s={};for(var l in n)hasOwnProperty.call(n,l)&&(s[l]=n[l]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var c=2;c<o;c++)i[c]=t[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,t)}d.displayName="MDXCreateElement"},2995:function(e,n,t){t.r(n),t.d(n,{assets:function(){return u},contentTitle:function(){return l},default:function(){return m},frontMatter:function(){return s},metadata:function(){return c},toc:function(){return p}});var r=t(7462),a=t(3366),o=(t(7294),t(3905)),i=["components"],s={title:"Structural Variation",track:"Genomic Variation"},l=void 0,c={unversionedId:"genomic-variation/structural-variation",id:"genomic-variation/structural-variation",title:"Structural Variation",description:"Living cells are remarkably tough in that they can tolerate large scale changes",source:"@site/docs/02-genomic-variation/04-structural-variation.md",sourceDirName:"02-genomic-variation",slug:"/genomic-variation/structural-variation",permalink:"learngenomics.dev/docs/genomic-variation/structural-variation",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/02-genomic-variation/04-structural-variation.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{title:"Structural Variation",track:"Genomic Variation"},sidebar:"tutorialSidebar",previous:{title:"Insertions and Deletions",permalink:"learngenomics.dev/docs/genomic-variation/insertions-and-deletions"},next:{title:"Copy Number Variation",permalink:"learngenomics.dev/docs/genomic-variation/copy-number-variation"}},u={},p=[{value:"Gene Fusions",id:"gene-fusions",level:3}],d={toc:p};function m(e){var n=e.components,s=(0,a.Z)(e,i);return(0,o.kt)("wrapper",(0,r.Z)({},d,s,{components:n,mdxType:"MDXLayout"}),(0,o.kt)("p",null,"Living cells are remarkably tough in that they can tolerate large scale changes\n(>1,000 bp). These large-scale variants, called ",(0,o.kt)("strong",{parentName:"p"},"structural variants")," or\n",(0,o.kt)("strong",{parentName:"p"},"SVs"),", can play a role in cancer and other diseases."),(0,o.kt)("p",null,"Structural variations take many forms\u2014sequences may be deleted, copied, moved,\ninverted or exchanged between chromosomes. These changes vary greatly as some\nSVs are complex rearrangements involving multiple chromosomes while other SVs\nmay only disrupt one part of a single chromosome. SVs are distinguished from\nindels by their large size, although there is no standard accepted threshold.\nWhile SVs are detected computationally, some SVs are large enough to be seen in\nan ordinary microscope."),(0,o.kt)("p",null,"After an SV event the original genomic sequence is interrupted by another out\nplace of sequence, creating a\xa0",(0,o.kt)("strong",{parentName:"p"},"breakpoint"),". Detecting breakpoints in SVs\nrequires specialized computational methods. One strategy is to pull all of the\nreads that are high quality but do not map to the reference genome as expected,\nsplit them in two and remap the pieces. If the read overlaps the breakpoint, the\ntwo pieces both map but to different locations. This is called a ",(0,o.kt)("strong",{parentName:"p"},"split\nread"),". If multiple unique split reads map to same locations, on both strands,\nthere may be enough evidence to call breakpoints. Discordant paired end reads,\nwhere one read maps to one chromosome and the second to another chromosome, also\nlend support to breakpoints."),(0,o.kt)("h3",{id:"gene-fusions"},"Gene Fusions"),(0,o.kt)("p",null,"For SVs, what happens at the breakpoint matters. Often DNA breaks interrupt\ncoding regions, separating the exons of specific genes. When multiple\nchromosomes are broken, the pieces of DNA from different chromosomes are joined\ntogether. When the rearranged DNA is translated into RNA, some, or all, of one\ngene's exons are spliced to the exons of another gene. These novel sequences are\ncalled ",(0,o.kt)("strong",{parentName:"p"},"gene fusions")," and are potent drivers of cancer. Gene fusions that\nare translatable will generate hybrid proteins with a combination of the\nfunctional sections (or ",(0,o.kt)("strong",{parentName:"p"},"domains"),") from the original genes. Often these\nhybrids act in ways the cell is not prepared to handle."),(0,o.kt)("p",null,(0,o.kt)("img",{alt:"Figure depicting the BCR-ABL1 fusion.",src:t(134).Z,width:"2467",height:"2145"})),(0,o.kt)("p",null,"Consider the case of the well-studied BCR-ABL1 gene fusion (or ",(0,o.kt)("strong",{parentName:"p"},"Philadelphia\nchromosome"),"). This effect of this fusion becomes apparent when you look at the\ndistinct functions of the BCR and ABL1 genes in normal cells:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("p",{parentName:"li"},"ABL1 is involved in cell proliferation and replication. The protein has a\ndomain (specifically, the tyrosine kinase domain) that transmits a signal\ntelling the cell to replicate by dividing. When functioning properly, the cell\ncreates ABL1 proteins to drive normal cell growth as needed.")),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("p",{parentName:"li"},"Unfortunately, the function of the BCR protein in normal cells is not well\nknown at the time of writing. What is important is in this case is that the\ncell will produce BCR at different levels than ABL1 depending on the scenario."))),(0,o.kt)("p",null,"In some leukemias, the front half of the BCR gene is fused to the back half of\nthe ABL1 gene. When the cell machinery attempts to produce the BCR protein, a\nhybrid protein containing the tyrosine kinase domain is produced instead. This\ncan lead to many copies of the problematic domain floating around than the cell\nintends, which causes the cell to divide much more than it intends and can\nultimately be a driver for cancer."),(0,o.kt)("p",null,"Detecting fusions like BCR-ABL1 is an important part of cancer diagnosis and\ninfluences the choice of treatments a patient receives. Like breakpoint\ndiscovery, many fusion detection methods rely on finding split reads and\ndiscordant read pairs that map to two genes called\xa0",(0,o.kt)("strong",{parentName:"p"},"spanning reads"),". These\nreads are rare in genomic sequences, so fusions are generally detected using\nRNA-seq. Fusion detection methods may also enhance their sensitivity by testing\nfor known fusion sequences or by testing against a database of potential fusions\nbased on known exons."))}m.isMDXComponent=!0},134:function(e,n,t){n.Z=t.p+"assets/images/2.3-Gene-Fusion-2cb90311e13f6871e1783f09e4251563.jpg"}}]);