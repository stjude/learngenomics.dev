"use strict";(self.webpackChunklearngenomics_dev=self.webpackChunklearngenomics_dev||[]).push([[501],{3905:function(e,n,t){t.d(n,{Zo:function(){return u},kt:function(){return f}});var r=t(7294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function i(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function o(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?i(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):i(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},i=Object.keys(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)t=i[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var c=r.createContext({}),l=function(e){var n=r.useContext(c),t=n;return e&&(t="function"==typeof e?e(n):o(o({},n),e)),t},u=function(e){var n=l(e.components);return r.createElement(c.Provider,{value:n},e.children)},m={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},p=r.forwardRef((function(e,n){var t=e.components,a=e.mdxType,i=e.originalType,c=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),p=l(t),f=a,h=p["".concat(c,".").concat(f)]||p[f]||m[f]||i;return t?r.createElement(h,o(o({ref:n},u),{},{components:t})):r.createElement(h,o({ref:n},u))}));function f(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var i=t.length,o=new Array(i);o[0]=p;var s={};for(var c in n)hasOwnProperty.call(n,c)&&(s[c]=n[c]);s.originalType=e,s.mdxType="string"==typeof e?e:a,o[1]=s;for(var l=2;l<i;l++)o[l]=t[l];return r.createElement.apply(null,o)}return r.createElement.apply(null,t)}p.displayName="MDXCreateElement"},1776:function(e,n,t){t.r(n),t.d(n,{assets:function(){return u},contentTitle:function(){return c},default:function(){return f},frontMatter:function(){return s},metadata:function(){return l},toc:function(){return m}});var r=t(7462),a=t(3366),i=(t(7294),t(3905)),o=["components"],s={},c="Baselines for Variation",l={unversionedId:"genomic-variation/baselines-for-variation",id:"genomic-variation/baselines-for-variation",title:"Baselines for Variation",description:"Introduction",source:"@site/docs/02-genomic-variation/01-baselines-for-variation.md",sourceDirName:"02-genomic-variation",slug:"/genomic-variation/baselines-for-variation",permalink:"/learngenomics.dev/docs/genomic-variation/baselines-for-variation",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/02-genomic-variation/01-baselines-for-variation.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Genomic Variation",permalink:"/learngenomics.dev/docs/genomic-variation/"},next:{title:"Single Nucleotide Variation",permalink:"/learngenomics.dev/docs/genomic-variation/single-nucleotide-variation"}},u={},m=[{value:"Introduction",id:"introduction",level:2},{value:"Reference Genome",id:"reference-genome",level:2},{value:"The Analysis of Tumors vs. Germline Mutations",id:"the-analysis-of-tumors-vs-germline-mutations",level:2}],p={toc:m};function f(e){var n=e.components,t=(0,a.Z)(e,o);return(0,i.kt)("wrapper",(0,r.Z)({},p,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"baselines-for-variation"},"Baselines for Variation"),(0,i.kt)("h2",{id:"introduction"},"Introduction"),(0,i.kt)("p",null,"Before we can dive into the types of changes that can occur within a particular\nindividual's genome, we must first answer the question \"changes ",(0,i.kt)("em",{parentName:"p"},"in reference to\nwhat"),'?" After all, there is no "average" human\'s DNA to compare against\u2014genetic\ncode is diverging within individuals and larger geographical populations all the\ntime. How can we compare a single organism\'s genetic code against a baseline\nthat is more accurately represented as a graph that is constantly evolving?'),(0,i.kt)("h2",{id:"reference-genome"},"Reference Genome"),(0,i.kt)("p",null,'At least for the moment, the answer is "we don\'t". The current solution chooses\npracticality over the ideal state of things: there is, in fact, a single model\nknown as the ',(0,i.kt)("strong",{parentName:"p"},"reference genome")," that attempts to recapitulate a consensus\nrepresentation for the human genome. This consensus model is curated by the\n",(0,i.kt)("a",{parentName:"p",href:"https://www.ncbi.nlm.nih.gov/grc"},"Genome Reference Consortium (GRC)"),", and ",(0,i.kt)("strong",{parentName:"p"},"patches")," to the genome are released\non a regular basis to further improve the model as we learn more about the human\ngenome."),(0,i.kt)("p",null,"Genomes for multiple species are maintained by the GRC, and you can view them on\nthe ",(0,i.kt)("a",{parentName:"p",href:"https://www.ncbi.nlm.nih.gov/grc/data"},"GRC's website"),". In the past, the\nnaming conventions were more confusing and versions differed based on where you\ngot the data. However, the academic world has now helpfully synced on the\nversioning."),(0,i.kt)("p",null,"For example, the current version of the human genome is ",(0,i.kt)("inlineCode",{parentName:"p"},"GRCh38")," where ",(0,i.kt)("inlineCode",{parentName:"p"},"GRC"),"\nstands for the Genome Reference Consortium, ",(0,i.kt)("inlineCode",{parentName:"p"},"h")," stands for human, and ",(0,i.kt)("inlineCode",{parentName:"p"},"38"),"\nstands for version 38. The UCSC nomenclature (",(0,i.kt)("inlineCode",{parentName:"p"},"hg38"),") is also used\ninterchangeably with this version. Unfortunately, previous versions of the\ngenome versions did not match up on versioning or nomenclature (e.g., ",(0,i.kt)("inlineCode",{parentName:"p"},"hg19")," is\nequivalent to ",(0,i.kt)("inlineCode",{parentName:"p"},"GRCh37")," or sometimes ",(0,i.kt)("inlineCode",{parentName:"p"},"GRCh37-lite")," depending on the context), so\nyou'll need to be careful when using non-current versions of the human genome.\nIf you find yourself using an older version of the reference genome, the\n",(0,i.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/Reference_genome"},"Wikipedia page")," has a helpful\ntable for comparing these historical genome versions."),(0,i.kt)("admonition",{type:"info"},(0,i.kt)("p",{parentName:"admonition"},"One of the criticisms of the approach outlined above is the lack of accounting\nfor the diversity amongst the world's populations. For example, ",(0,i.kt)("a",{parentName:"p",href:"https://www.theatlantic.com/science/archive/2018/11/human-genome-300-million-missing-letters-dna/576481/"},"~70% of the\nmaterial for the Human Genome Project (the foundation for the reference genome)\ncame from an anonymous, white male from Buffalo, NY known only as RP11"),".\nUsing this linear, haploid reference genome to quantify variation across diverse\npopulations is far from perfect, but (from a scientific perspective) the\ninternational genomics community has come up with several strategies for\ncontextualizing genomic variation within this framework (e.g. population\nfrequency databases)."),(0,i.kt)("p",{parentName:"admonition"},"Note that in the next version of the reference genome (hg39), the preferred\napproach appears to be a graph-based structure that can define variation in a\nmuch wider variety of populations. Clearly this is a step forward, but it also\nintroduces significant computational challenges to the processing of data. As\nsuch, the correct way to define the next iteration of the reference genome is\ncurrently being discussed, and the release is ",(0,i.kt)("a",{parentName:"p",href:"https://www.ncbi.nlm.nih.gov/grc"},"indefinitely on\nhold")," per the notice on the Genome Reference\nConsortium's website.")),(0,i.kt)("h2",{id:"the-analysis-of-tumors-vs-germline-mutations"},"The Analysis of Tumors vs. Germline Mutations"),(0,i.kt)("p",null,"Having a matched pair of tumor and germline data is especially valuable in\nvariant detection because germline data acts as a precise control. The analyst\nuses the paring to sort out common but irrelevant SNVs found in the normal\ngermline tissue from the new cancer driving mutations in the tumor."),(0,i.kt)("p",null,"Studies that consist only of tumor samples are useful in diagnosing subtypes of\nthe disease. Cancer subtypes often differ in their rate of progression and\nrequire distinct treatments. Subtyping helps clinicians provide the precise\ncourse of treatment most suited for a given tumor."),(0,i.kt)("p",null,"Studies that consist only of germline samples are general useful for discovering\ngenes and variations that are associated with disease. Germline studies are\nbasic research studies where hundreds of thousands of candidate variations are\nsystematically filtered to find a few significant variants. Disease associated\nvariants could be markers for elevated risk or causative mutations that\npredispose the subject to disease."))}f.isMDXComponent=!0}}]);