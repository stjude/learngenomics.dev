"use strict";(self.webpackChunklearngenomics_dev=self.webpackChunklearngenomics_dev||[]).push([[307],{3905:function(e,t,n){n.d(t,{Zo:function(){return u},kt:function(){return f}});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},i=Object.keys(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(r=0;r<i.length;r++)n=i[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var c=r.createContext({}),l=function(e){var t=r.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},u=function(e){var t=l(e.components);return r.createElement(c.Provider,{value:t},e.children)},m={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,i=e.originalType,c=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),d=l(n),f=a,p=d["".concat(c,".").concat(f)]||d[f]||m[f]||i;return n?r.createElement(p,o(o({ref:t},u),{},{components:n})):r.createElement(p,o({ref:t},u))}));function f(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var i=n.length,o=new Array(i);o[0]=d;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:a,o[1]=s;for(var l=2;l<i;l++)o[l]=n[l];return r.createElement.apply(null,o)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},7019:function(e,t,n){n.r(t),n.d(t,{assets:function(){return u},contentTitle:function(){return c},default:function(){return f},frontMatter:function(){return s},metadata:function(){return l},toc:function(){return m}});var r=n(7462),a=n(3366),i=(n(7294),n(3905)),o=["components"],s={},c="Genomic Variation",l={unversionedId:"genomic-variation/index",id:"genomic-variation/index",title:"Genomic Variation",description:"Introduction",source:"@site/docs/02-genomic-variation/index.md",sourceDirName:"02-genomic-variation",slug:"/genomic-variation/",permalink:"/docs/genomic-variation/",editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/02-genomic-variation/index.md",tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Genotype, Phenotype and Haplotype",permalink:"/docs/biological-foundations/genotype-phenotype-haplotype"},next:{title:"Variant Equivalence",permalink:"/docs/genomic-variation/variant-equivalence"}},u={},m=[{value:"Introduction",id:"introduction",level:2},{value:"Reference Genome",id:"reference-genome",level:2},{value:"The Analysis of Tumors vs. Germline Mutations",id:"the-analysis-of-tumors-vs-germline-mutations",level:2}],d={toc:m};function f(e){var t=e.components,n=(0,a.Z)(e,o);return(0,i.kt)("wrapper",(0,r.Z)({},d,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"genomic-variation"},"Genomic Variation"),(0,i.kt)("h2",{id:"introduction"},"Introduction"),(0,i.kt)("p",null,"During the course of an organism's life, changes to its underlying genetic code will be introduced by a variety of processes. Many of these changes are harmless and are the underlying current driving a species' evolution. Rarely, variation within the genome or combinations thereof will cause adverse phenotypes in individuals that carry the variation(s) ","[","e.g. cancer","]",". The replicate-and-branch nature of the cell lifecycle means that genetic code within different parts of one's body evolve separately and slowly diverge from on another. This phenomenon can be observed more starkly when considering the difference in genetic code from humans separated by large geographic regions."),(0,i.kt)("h2",{id:"reference-genome"},"Reference Genome"),(0,i.kt)("p",null,"Before one can detect mutations that have occurred in a particular individual's genome, there must be a baseline genome to compare against. As stated above, there underlying DNA in humans across the world varies greatly. Importantly, there exists no way to capture an \"average\" human's DNA to create the aforementioned baseline to compare against. Biologists across the world use a common ",(0,i.kt)("strong",{parentName:"p"},"reference genome"),", which is curated by the Genome Reference Consortium, as the foundation for calling variation in an individual",(0,i.kt)("strong",{parentName:"p"},".")," The reference genome is a combination of different individuals DNA collected during the Human Genome Project (and refined since that time)."),(0,i.kt)("p",null,"One of the criticisms of this approach is the lack of accounting for the diversity amongst the world's populations. For example, ",(0,i.kt)("a",{parentName:"p",href:"https://www.theatlantic.com/science/archive/2018/11/human-genome-300-million-missing-letters-dna/576481/"},"~70% of the material for the Human Genome Project came from an anonymous, white male from Buffalo, NY known only as RP11"),". Using this linear, haploid reference genome to quantify variation across diverse populations is far from perfect, but the international genomics community has come up with several strategies for mitigating its negative effects (e.g. population frequency databases). Note that in the next version of the reference genome (hg39), the preferred approach appears to be a graph-based structure that can define variation in a much wider variety of populations."),(0,i.kt)("p",null,(0,i.kt)("em",{parentName:"p"},"Note:")," The results of any genomic analysis depend the version and source of reference sequence\u2014results generated from different versions of a reference genome typically cannot be compared."),(0,i.kt)("h2",{id:"the-analysis-of-tumors-vs-germline-mutations"},"The Analysis of Tumors vs. Germline Mutations"),(0,i.kt)("p",null,"Having a matched pair of tumor and germline data is especially valuable in variant detection because germline data acts as a precise control. The analyst uses the paring to sort out common but irrelevant SNVs found in the normal germline tissue from the new cancer driving mutations in the tumor."),(0,i.kt)("p",null,"Studies that consist only of tumor samples are useful in diagnosing subtypes of the disease. Cancer subtypes often differ in their rate of progression and require distinct treatments. Subtyping helps clinicians provide the precise course of treatment most suited for a given tumor."),(0,i.kt)("p",null,"Studies that consist only of germline samples are general useful for discovering genes and variations that are associated with disease. Germline studies are basic research studies where hundreds of thousands of candidate variations are systematically filtered to find a few significant variants. Disease associated variants could be markers for elevated risk or causative mutations that predispose the subject to disease."))}f.isMDXComponent=!0}}]);