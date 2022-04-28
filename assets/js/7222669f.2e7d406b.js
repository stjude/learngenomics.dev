"use strict";(self.webpackChunklearngenomics_dev=self.webpackChunklearngenomics_dev||[]).push([[8859],{3905:function(e,t,n){n.d(t,{Zo:function(){return u},kt:function(){return h}});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var l=r.createContext({}),c=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},u=function(e){var t=c(e.components);return r.createElement(l.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),d=c(n),h=a,m=d["".concat(l,".").concat(h)]||d[h]||p[h]||o;return n?r.createElement(m,i(i({ref:t},u),{},{components:n})):r.createElement(m,i({ref:t},u))}));function h(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=d;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var c=2;c<o;c++)i[c]=n[c];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},2995:function(e,t,n){n.r(t),n.d(t,{assets:function(){return u},contentTitle:function(){return l},default:function(){return h},frontMatter:function(){return s},metadata:function(){return c},toc:function(){return p}});var r=n(7462),a=n(3366),o=(n(7294),n(3905)),i=["components"],s={title:"Structural Variation",track:"Genomic Variation"},l=void 0,c={unversionedId:"genomic-variation/structural-variation",id:"genomic-variation/structural-variation",title:"Structural Variation",description:"Living cells are remarkably tough in that they can tolerate large scale changes (\\>1,000 bp). These large-scale variants, called structural variants or SVs, can play a role in cancer and other diseases.",source:"@site/docs/02-genomic-variation/04-structural-variation.md",sourceDirName:"02-genomic-variation",slug:"/genomic-variation/structural-variation",permalink:"/docs/genomic-variation/structural-variation",editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/02-genomic-variation/04-structural-variation.md",tags:[],version:"current",sidebarPosition:4,frontMatter:{title:"Structural Variation",track:"Genomic Variation"},sidebar:"tutorialSidebar",previous:{title:"Insertions and Deletions",permalink:"/docs/genomic-variation/insertions-and-deletions"},next:{title:"Copy Number Variation",permalink:"/docs/genomic-variation/copy-number-variation"}},u={},p=[{value:"Gene Fusions",id:"gene-fusions",level:3}],d={toc:p};function h(e){var t=e.components,s=(0,a.Z)(e,i);return(0,o.kt)("wrapper",(0,r.Z)({},d,s,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("p",null,"Living cells are remarkably tough in that they can tolerate large scale changes (",">","1,000 bp). These large-scale variants, called ",(0,o.kt)("strong",{parentName:"p"},"structural variants")," or ",(0,o.kt)("strong",{parentName:"p"},"SVs"),", can play a role in cancer and other diseases."),(0,o.kt)("p",null,"Structural variations take many forms---sequences may be deleted, copied, moved, inverted or exchanged between chromosomes. These changes vary greatly as some SVs are complex rearrangements involving multiple chromosomes while other SVs may only disrupt one part of a single chromosome. SVs are distinguished from indels by their large size, although there is no standard accepted threshold. While SVs are detected computationally, some SVs are large enough to be seen in an ordinary microscope."),(0,o.kt)("p",null,'After an SV event the original genomic sequence is interrupted by another out place of sequence, creating a\xa0"',(0,o.kt)("strong",{parentName:"p"},"breakpoint"),'." Detecting breakpoints in SVs requires specialized computational methods. One strategy is to pull all of the reads that are high quality but do not map to the reference genome as expected, split them in two and remap the pieces. If the read overlaps the breakpoint, the two pieces both map but to different locations. This is called a\xa0"',(0,o.kt)("strong",{parentName:"p"},"split read"),'." If multiple unique split reads map to same locations, on both strands, there may be enough evidence to call breakpoints. Discordant paired end reads, where one read maps to one chromosome and the second to another chromosome, also lend support to breakpoints.'),(0,o.kt)("h3",{id:"gene-fusions"},"Gene Fusions"),(0,o.kt)("p",null,"For SVs what happens at the breakpoint matters. Often DNA breaks interrupt coding regions, separating the exons of specific genes. When multiple chromosomes are broken, the pieces of DNA from different chromosomes are joined together. When the rearranged DNA is translated into RNA, some, or all, of one gene's exons are spliced to the exons of another gene. These novel sequences are called \"",(0,o.kt)("strong",{parentName:"p"},'gene fusions"')," and are potent drivers of cancer. Gene fusions that are translatable will generate hybrid proteins with a combination of the functional sections (or ",(0,o.kt)("strong",{parentName:"p"},"domains)")," from the original genes. Often these hybrids act in ways the cell is not prepared to handle."),(0,o.kt)("p",null,(0,o.kt)("img",{src:n(6987).Z,width:"2000",height:"1737"})),(0,o.kt)("p",null,"Consider the case of the well-studied BCR-ABL1 gene fusion (or ",(0,o.kt)("strong",{parentName:"p"},"Philadelphia chromosome"),"). This effect of this fusion becomes apparent when you look at the distinct functions of the BCR and ABL1 genes in normal cells:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("p",{parentName:"li"},"ABL1 is involved in cell proliferation and replication. The protein has a domain (specifically, the tyrosine kinase domain) that transmits a signal telling the cell to replicate by dividing. When functioning properly, the cell creates ABL1 proteins to drive normal cell growth as needed.")),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("p",{parentName:"li"},"Unfortunately, the function of the BCR protein in normal cells is not well known at the time of writing. What is important is in this case is that the cell will produce BCR at different levels than ABL1 depending on the scenario."))),(0,o.kt)("p",null,"In some leukemias, the front half of the BCR gene is fused to the back half of the ABL1 gene. When the cell machinery attempts to produce the BCR protein, a hybrid protein containing the tyrosine kinase domain is produced instead. This can lead to many copies of the problematic domain floating around than the cell intends, which causes the cell to divide much more than it intends and can ultimately be a driver for cancer."),(0,o.kt)("p",null,"Detecting fusions like BCR-ABL1 is an important part of cancer diagnosis and influences the choice of treatments a patient receives. Like breakpoint discovery, many fusion detection methods rely on finding split reads and discordant read pairs that map to two genes called\xa0",(0,o.kt)("strong",{parentName:"p"},"spanning reads"),". These reads are rare in genomic sequences, so fusions are generally detected using RNA-seq. Fusion detection methods may also enhance their sensitivity by testing for known fusion sequences or by testing against a database of potential fusions based on known exons."))}h.isMDXComponent=!0},6987:function(e,t,n){t.Z=n.p+"assets/images/3.5-Gene-Fusion-6b2b4fdab1f4bf82f15b08593c25a8ce.jpg"}}]);