"use strict";(self.webpackChunklearngenomics_dev=self.webpackChunklearngenomics_dev||[]).push([[518],{3905:function(e,n,t){t.d(n,{Zo:function(){return u},kt:function(){return p}});var o=t(7294);function a(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function r(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);n&&(o=o.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,o)}return t}function i(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?r(Object(t),!0).forEach((function(n){a(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):r(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,o,a=function(e,n){if(null==e)return{};var t,o,a={},r=Object.keys(e);for(o=0;o<r.length;o++)t=r[o],n.indexOf(t)>=0||(a[t]=e[t]);return a}(e,n);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(o=0;o<r.length;o++)t=r[o],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(a[t]=e[t])}return a}var l=o.createContext({}),c=function(e){var n=o.useContext(l),t=n;return e&&(t="function"==typeof e?e(n):i(i({},n),e)),t},u=function(e){var n=c(e.components);return o.createElement(l.Provider,{value:n},e.children)},d={inlineCode:"code",wrapper:function(e){var n=e.children;return o.createElement(o.Fragment,{},n)}},m=o.forwardRef((function(e,n){var t=e.components,a=e.mdxType,r=e.originalType,l=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),m=c(t),p=a,h=m["".concat(l,".").concat(p)]||m[p]||d[p]||r;return t?o.createElement(h,i(i({ref:n},u),{},{components:t})):o.createElement(h,i({ref:n},u))}));function p(e,n){var t=arguments,a=n&&n.mdxType;if("string"==typeof e||a){var r=t.length,i=new Array(r);i[0]=m;var s={};for(var l in n)hasOwnProperty.call(n,l)&&(s[l]=n[l]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var c=2;c<r;c++)i[c]=t[c];return o.createElement.apply(null,i)}return o.createElement.apply(null,t)}m.displayName="MDXCreateElement"},9995:function(e,n,t){t.r(n),t.d(n,{assets:function(){return u},contentTitle:function(){return l},default:function(){return p},frontMatter:function(){return s},metadata:function(){return c},toc:function(){return d}});var o=t(7462),a=t(3366),r=(t(7294),t(3905)),i=["components"],s={title:"Cells, Chromosomes, and Genomes",track:"Biological Foundations"},l=void 0,c={unversionedId:"biological-foundations/cells-genomes-dna-chromosomes",id:"biological-foundations/cells-genomes-dna-chromosomes",title:"Cells, Chromosomes, and Genomes",description:"Introduction",source:"@site/docs/01-biological-foundations/01-cells-genomes-dna-chromosomes.md",sourceDirName:"01-biological-foundations",slug:"/biological-foundations/cells-genomes-dna-chromosomes",permalink:"/learngenomics.dev/docs/biological-foundations/cells-genomes-dna-chromosomes",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/01-biological-foundations/01-cells-genomes-dna-chromosomes.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{title:"Cells, Chromosomes, and Genomes",track:"Biological Foundations"},sidebar:"tutorialSidebar",next:{title:"The Central Dogma",permalink:"/learngenomics.dev/docs/biological-foundations/the-central-dogma"}},u={},d=[{value:"Introduction",id:"introduction",level:2},{value:"Bakery Analogy",id:"bakery-analogy",level:3},{value:"A Mental Model for DNA",id:"a-mental-model-for-dna",level:2},{value:"Physical Structure",id:"physical-structure",level:3},{value:"Conclusion",id:"conclusion",level:2}],m={toc:d};function p(e){var n=e.components,s=(0,a.Z)(e,i);return(0,r.kt)("wrapper",(0,o.Z)({},m,s,{components:n,mdxType:"MDXLayout"}),(0,r.kt)("h2",{id:"introduction"},"Introduction"),(0,r.kt)("admonition",{title:"Disclaimer",type:"info"},(0,r.kt)("p",{parentName:"admonition"},'This Guide is written specifically by and for computer scientists and\nengineers. The underlying biology in cancer genomics can be exceedingly complex\nand requires years of study. Making the content palatable requires drawing\nabstractions around these concepts. This guide should be treated as an\nintroduction to the domain that teaches our audience the material in a\n"broad-strokes" fashion. Please be forgiving if you feel we have glossed over\nyour favorite quirk of cancer genomics. Further, everything within the guide is\npresented within a research context and may not be relied on in making decisions\nabout patients. If you feel anything has been stated incorrectly, you can file\nan issue on the Github repository. Please see ',(0,r.kt)("a",{parentName:"p",href:"https://github.com/stjude/learngenomics.dev/blob/main/LICENSE.md"},"the LICENSE.md"),"\nfor more information.")),(0,r.kt)("admonition",{type:"info"},(0,r.kt)("p",{parentName:"admonition"},"Everything in this guide refers to eukaryotic molecular biology, which is the\nstudy of organisms whose DNA is enclosed within a nucleus. Broadly speaking,\nmost familiar species are eukaryotes, except bacteria which has DNA spread\nthroughout the cell. At times, this document will be geared towards the\nsequencing of human cells specifically.")),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Cells"),"\xa0are the smallest unit of life and are the building blocks of organisms, from a\nsingle-celled bacteria to the\xa0",(0,r.kt)("a",{parentName:"p",href:"https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002533"},"trillions of cells that make up the human\nbody"),".\nCells are complicated organized structures that take a variety of forms, forming tissues\nand organs and completing the body's functions."),(0,r.kt)("p",null,"Within nearly every cell is a\xa0",(0,r.kt)("strong",{parentName:"p"},"genome"),". A genome is the complete inherited instruction\nset for producing, operating and maintaining a living cell or organism. This information\nis physically encoded in a molecule called deoxyribonucleic acid or ",(0,r.kt)("strong",{parentName:"p"},"DNA"),". Among other\nthings, DNA contains instructions for the assembly of tens of thousands of different\nmolecular products. These instructions (or recipes) are called ",(0,r.kt)("strong",{parentName:"p"},"genes"),", and the\nphysical, molecular products genes encode for are called ",(0,r.kt)("strong",{parentName:"p"},"proteins"),". Cells are\nconstantly reading and interpreting genes stored within the DNA in order to assemble\nvarious proteins. Each cell type in the body produces a complex ecosystem of proteins\nthat keep the cell alive and executing its specific function."),(0,r.kt)("h3",{id:"bakery-analogy"},"Bakery Analogy"),(0,r.kt)("p",null,"To illustrate this phenomenon, imagine the cell as a bakery that makes many different\ntypes of cakes. In this analogy, the genome stored within the DNA is the master recipe\nbook containing more than 20,000 different cake recipes (genes). The physical cakes that\nare made from these recipes are the proteins. Notably, there are a limited number of\ncopies of the recipe/gene (two copies in the normal case for humans), but you may make\nthousands or more physical cakes from those recipes. Depending on the type of cell, the\nmixture of different cake flavors, their quantities, and how they interact together will\nbe different."),(0,r.kt)("admonition",{type:"tip"},(0,r.kt)("p",{parentName:"admonition"},"Keep an eye on this analogy\u2014we will refer back to and build upon it a number of times\nduring the course of this guide.")),(0,r.kt)("h2",{id:"a-mental-model-for-dna"},"A Mental Model for DNA"),(0,r.kt)("p",null,"Conceptually, you can think of DNA laid end-to-end as a ~3 billion character long string\nconsisting only of 'A's, 'C's, 'T's and 'G's. This string and any substring contained\nwithin are commonly referred to as genomic\xa0",(0,r.kt)("strong",{parentName:"p"},"sequences"),". These characters represent the\nphysical Adenine, Guanine, Thymine, and Cytosine ",(0,r.kt)("strong",{parentName:"p"},"bases")," (or ",(0,r.kt)("strong",{parentName:"p"},"nucleotides"),")\nrespectively."),(0,r.kt)("p",null,"Importantly, though it's easy to conceptualize DNA as a single, very long\nstring, the reality is more complex. DNA is comprised of two complementary sequences\nknown as\xa0",(0,r.kt)("strong",{parentName:"p"},"strands"),". Each base is actually a member of a ",(0,r.kt)("strong",{parentName:"p"},"base pairs"),", whereby\nnucleotides complement each other uniquely\u2014'A's pair only with 'T's, and 'G's only with\n'C's. Up close, this structure resembles a spiral staircase as seen in the figure below."),(0,r.kt)("p",null,(0,r.kt)("img",{alt:"Figure showing computational model and then physical helix for DNA",src:t(5688).Z,width:"1936",height:"1435"})),(0,r.kt)("p",null,"When cells divide, the spiral unwinds; each base pair is split; and the molecule is\nsplit into two strands, each one containing the information needed to replicate the\noriginal DNA structure. Normal healthy cells then copy the genetic code very accurately,\nrarely introducing variation."),(0,r.kt)("h3",{id:"physical-structure"},"Physical Structure"),(0,r.kt)("p",null,"In plants and animals, DNA is broken up into a number of large sequences\ncalled\xa0",(0,r.kt)("strong",{parentName:"p"},"chromosomes"),"\xa0which are paired and tucked into the nucleus. Each chromosome is\ncomposed of two DNA molecules (one from your father and one from your mother) and\npackaging proteins, or\xa0",(0,r.kt)("strong",{parentName:"p"},"histones"),",\xa0that keep the DNA string neatly wound and help\ncontrol which gene products are made in a given cell. For humans, there are normally\n22\xa0",(0,r.kt)("strong",{parentName:"p"},"autosomes"),"\xa0(chromosomes shared by both sexes) and pair of sex chromosomes (XX for\nfemales or XY for males). Autosomes are numbered from 1 to 22 based on size, arranged\nfrom largest to smallest. The full set of chromosomes makes up the genome."),(0,r.kt)("h2",{id:"conclusion"},"Conclusion"),(0,r.kt)("p",null,"The genome is a vast search space for biological questions. Each genome is a biochemical\ndatabase that, if properly accessed, can inform how our bodies function. Genomes account\nfor the natural differences between individuals, define family traits, and distinguish\nhow cells in tissues and organs vary. When genomes acquire adverse mutation(s), cancer\nas well as other genetic diseases can occur. By examining the relationship between\nphysical traits (e.g. blood pressure or the development of a tumor) and the genome,\nknown as ",(0,r.kt)("strong",{parentName:"p"},"genotype-phenotype relationships"),", clinicians can develop personalized\nmedical treatment based on an individual's genetic makeup."))}p.isMDXComponent=!0},5688:function(e,n,t){n.Z=t.p+"assets/images/1.1-DNA-f00aefafd1a3954fd1b496c2144a7bc0.jpg"}}]);