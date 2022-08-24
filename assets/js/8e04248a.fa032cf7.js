"use strict";(self.webpackChunklearngenomics_dev=self.webpackChunklearngenomics_dev||[]).push([[510],{3905:function(e,n,t){t.d(n,{Zo:function(){return u},kt:function(){return g}});var r=t(7294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function o(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function i(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?o(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):o(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,a=function(e,n){if(null==e)return{};var t,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)t=o[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var c=r.createContext({}),p=function(e){var n=r.useContext(c),t=n;return e&&(t="function"==typeof e?e(n):i(i({},n),e)),t},u=function(e){var n=p(e.components);return r.createElement(c.Provider,{value:n},e.children)},l={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},f=r.forwardRef((function(e,n){var t=e.components,a=e.mdxType,o=e.originalType,c=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),f=p(t),g=a,d=f["".concat(c,".").concat(g)]||f[g]||l[g]||o;return t?r.createElement(d,i(i({ref:n},u),{},{components:t})):r.createElement(d,i({ref:n},u))}));function g(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var o=t.length,i=new Array(o);i[0]=f;var s={};for(var c in n)hasOwnProperty.call(n,c)&&(s[c]=n[c]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var p=2;p<o;p++)i[p]=t[p];return r.createElement.apply(null,i)}return r.createElement.apply(null,t)}f.displayName="MDXCreateElement"},6617:function(e,n,t){t.r(n),t.d(n,{assets:function(){return u},contentTitle:function(){return c},default:function(){return g},frontMatter:function(){return s},metadata:function(){return p},toc:function(){return l}});var r=t(7462),a=t(3366),o=(t(7294),t(3905)),i=["components"],s={title:"Read Mapping",track:"Next-Generation Sequencing"},c=void 0,p={unversionedId:"next-generation-sequencing/read-mapping",id:"next-generation-sequencing/read-mapping",title:"Read Mapping",description:"During the next generation sequencing portion of our workflow, it's as if a box",source:"@site/docs/03-next-generation-sequencing/04-read-mapping.md",sourceDirName:"03-next-generation-sequencing",slug:"/next-generation-sequencing/read-mapping",permalink:"/learngenomics.dev/docs/next-generation-sequencing/read-mapping",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/03-next-generation-sequencing/04-read-mapping.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{title:"Read Mapping",track:"Next-Generation Sequencing"},sidebar:"tutorialSidebar",previous:{title:"Types of Sequencing",permalink:"/learngenomics.dev/docs/next-generation-sequencing/types-of-sequencing"},next:{title:"Genomic File Formats",permalink:"/learngenomics.dev/docs/genomic-file-formats/"}},u={},l=[],f={toc:l};function g(e){var n=e.components,t=(0,a.Z)(e,i);return(0,o.kt)("wrapper",(0,r.Z)({},f,t,{components:n,mdxType:"MDXLayout"}),(0,o.kt)("p",null,"During the next generation sequencing portion of our workflow, it's as if a box\nof puzzle pieces were dumped out onto a table. To get a full picture of an\nindividual's genome, we need to put that puzzle back together through a process\ncalled ",(0,o.kt)("strong",{parentName:"p"},"read mapping"),'. As with any puzzle, you need the picture on the front\nof the box that describes what the puzzle should look like. In genomics, this\nproverbial "picture on the front of the box" is called the ',(0,o.kt)("strong",{parentName:"p"},"reference genome"),".\nYou can learn more about the reference genome ",(0,o.kt)("a",{parentName:"p",href:"/learngenomics.dev/docs/genomic-variation/baselines-for-variation"},"here"),"."),(0,o.kt)("p",null,"Before starting your analysis, you'll need to decide on which reference genome\nyou will use as the baseline for your project. Once a reference genome is\ndecided, the next step is to choose a mapping software (frequently referred to\nas a mapper or aligner) to align the reads to that reference genome. The mapping\nsoftware generates a special data structure from a reference genome and then\ngoes through each read pair in the FASTQ files to see if and where they fit in\nthe reference genome. "),(0,o.kt)("p",null,"At the time of writing, the most popular aligner for each type of data\nis\xa0",(0,o.kt)("a",{parentName:"p",href:"https://github.com/lh3/bwa"},"BWA")," for DNA sequencing\nand\xa0",(0,o.kt)("a",{parentName:"p",href:"https://github.com/alexdobin/STAR"},"STAR"),' for RNA sequencing. Each program\nprovides many parameters that can be tweaked depending on the characteristics of\nthe data to achieve the "best" alignment. Once the alignment program has\ncompleted, it creates\na\xa0',(0,o.kt)("a",{parentName:"p",href:"https://samtools.github.io/hts-specs/SAMv1.pdf"},"SAM/BAM"),"\xa0file containing all\nof the read pairs, where the aligner believes they live in the reference genome\n(if anywhere), and many other fields that the aligner computes. This file is\nwidely considered the basis of most modern computational genomic analyses. The\nspecifics of each file type are discussed in the next chapter."),(0,o.kt)("admonition",{type:"info"},(0,o.kt)("p",{parentName:"admonition"},"As an implementation note, the entire analysis is based off of the reference\ngenome used. Generally speaking, analyses that use two different reference\ngenomes are not compatible because the positions of genes and other important\nbiomarkers are updated with each genome build. Once an end-to-end analysis\npipeline is decided on, it is a significant task to update analysis pipelines to\na new reference genome. As such, at the time of writing, many labs are still\nusing the\xa0GRCh37\xa0version of the human genome, which was released in\n2009.")))}g.isMDXComponent=!0}}]);