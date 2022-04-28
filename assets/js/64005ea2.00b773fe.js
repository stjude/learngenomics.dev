"use strict";(self.webpackChunklearngenomics_dev=self.webpackChunklearngenomics_dev||[]).push([[94],{3905:function(e,t,n){n.d(t,{Zo:function(){return u},kt:function(){return h}});var i=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,i)}return n}function r(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,i,a=function(e,t){if(null==e)return{};var n,i,a={},o=Object.keys(e);for(i=0;i<o.length;i++)n=o[i],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(i=0;i<o.length;i++)n=o[i],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var c=i.createContext({}),l=function(e){var t=i.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):r(r({},t),e)),n},u=function(e){var t=l(e.components);return i.createElement(c.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},p=i.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,c=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),p=l(n),h=a,m=p["".concat(c,".").concat(h)]||p[h]||d[h]||o;return n?i.createElement(m,r(r({ref:t},u),{},{components:n})):i.createElement(m,r({ref:t},u))}));function h(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,r=new Array(o);r[0]=p;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:a,r[1]=s;for(var l=2;l<o;l++)r[l]=n[l];return i.createElement.apply(null,r)}return i.createElement.apply(null,n)}p.displayName="MDXCreateElement"},8827:function(e,t,n){n.r(t),n.d(t,{assets:function(){return u},contentTitle:function(){return c},default:function(){return h},frontMatter:function(){return s},metadata:function(){return l},toc:function(){return d}});var i=n(7462),a=n(3366),o=(n(7294),n(3905)),r=["components"],s={title:"Single Nucleotide Variation",track:"Genomic Variation"},c=void 0,l={unversionedId:"genomic-variation/single-nucleotide-variation",id:"genomic-variation/single-nucleotide-variation",title:"Single Nucleotide Variation",description:"Single Nucleotide Variants (SNVs) and Single Nucleotide Polymorphisms (SNPs)\xa0are the smallest unit of variation in the genome. Here, just one nucleotide, or base, is substituted at a single position in the genome (such as changing a 'C' to an 'A' on chromosome 5, position 1,485,234). The term\xa0\"SNV\"\xa0is used broadly to describe an event where a single nucleotide substitution, insertion or deletion occurs.\xa0SNPs\xa0are a subset of SNVs where the change is found in some non-trivial percentage of a population (e.g. \\> 1%, though an exact threshold is not universally agreed upon). By contrast, SNVs that are not considered SNPs can be very rare and may cause cancer or other diseases.",source:"@site/docs/02-genomic-variation/02-single-nucleotide-variation.md",sourceDirName:"02-genomic-variation",slug:"/genomic-variation/single-nucleotide-variation",permalink:"/docs/genomic-variation/single-nucleotide-variation",editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/02-genomic-variation/02-single-nucleotide-variation.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{title:"Single Nucleotide Variation",track:"Genomic Variation"},sidebar:"tutorialSidebar",previous:{title:"Types of Variation",permalink:"/docs/genomic-variation/types-of-variation"},next:{title:"Insertions and Deletions",permalink:"/docs/genomic-variation/insertions-and-deletions"}},u={},d=[],p={toc:d};function h(e){var t=e.components,s=(0,a.Z)(e,r);return(0,o.kt)("wrapper",(0,i.Z)({},p,s,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("p",null,(0,o.kt)("a",{parentName:"p",href:"https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism"},"Single Nucleotide Variants (SNVs) and Single Nucleotide Polymorphisms (SNPs)"),"\xa0are the smallest unit of variation in the genome. Here, just one nucleotide, or base, is substituted at a single position in the genome (such as changing a 'C' to an 'A' on chromosome 5, position 1,485,234). The term\xa0\"",(0,o.kt)("strong",{parentName:"p"},'SNV"'),"\xa0is used broadly to describe an event where a single nucleotide substitution, insertion or deletion occurs.\xa0",(0,o.kt)("strong",{parentName:"p"},"SNPs"),"\xa0are a subset of SNVs where the change is found in some non-trivial percentage of a population (e.g. ",">"," 1%, though an exact threshold is not universally agreed upon). By contrast, SNVs that are not considered SNPs can be very rare and may cause cancer or other diseases."),(0,o.kt)("p",null,(0,o.kt)("img",{src:n(9552).Z,width:"1000",height:"273"})),(0,o.kt)("p",null,'In cancer genomics, SNPs are less interesting to researchers than SNVs due to their prevalence within the population. To illustrate, consider a SNP event where 45% of the people have an "A" at the specified position and 55% have a "T" at that position. 45% of the human population does not have cancer, so the variation is highly unlikely to play a major role in oncogenesis. The\xa0',(0,o.kt)("a",{parentName:"p",href:"https://www.ncbi.nlm.nih.gov/snp/"},"dbSNP"),"\xa0database is perhaps the most widely-used population frequency database."),(0,o.kt)("p",null,"Determining which of the hundreds of thousands of possible SNVs are important in a particular disease is done by statistical association or through applying biological knowledge. Genome-wide association studies (",(0,o.kt)("strong",{parentName:"p"},"GWAS"),") collect data from thousands of patient samples with the same disease and statistically compare their SNVs to those in a normal population. GWAS studies work well for common diseases that are well-defined and reliably diagnosed. This is especially true if the number of disease-causing variants is small. However, most diseases have many genetic variants that influence the disease. Importantly, GWAS studies only find variants that are linked to disease more closely than expected by chance. Very often these variants only indicate an interesting genomic location and do not themselves result in disease."),(0,o.kt)("p",null,"One downside of GWAS studies is that they require a relatively large number of samples to gain enough statistical power. In rare diseases like pediatric cancer, GWAS studies are not as practical due to low sample count. Thus, researchers apply biological knowledge ",(0,o.kt)("em",{parentName:"p"},"a priori")," to improve the odds of finding relevant SNVs. Commonly scientists focus their efforts on SNVs that fall within exons of genes that are known be associated with cancer or that are predicted to alter the protein product. Databases such as\xa0",(0,o.kt)("a",{parentName:"p",href:"https://cancer.sanger.ac.uk/cosmic"},"COSMIC"),"\xa0track variants in cancer genomes to help identify genes and genomic locations that are commonly mutated and are, therefore, more likely to be relevant to disease."),(0,o.kt)("p",null,'As an aside, SNVs and SNPs are often both colloquially referred to "snips." Strictly speaking, SNVs are not all SNPs, but it is difficult to imagine an easy pronunciation for "SNVs", so individuals often mix the two concepts in speech (e.g. "we need to look at the called snips"). You\'ll need to use context to delineate whether one is talking about polymorphisms or just single nucleotide variation in general.'),(0,o.kt)("p",null,'Recall that multiple version of nucleotide triplet can code for the same amino acid. This means some single nucleotide substitutions may not change the amino acid that is selected, and thus the protein is unaffected. These variants are called\xa0"',(0,o.kt)("strong",{parentName:"p"},"silent mutations"),'." When codon variants change the amino acid used in a protein, the effect on function runs a range from insignificant to highly significant.'))}h.isMDXComponent=!0},9552:function(e,t,n){t.Z=n.p+"assets/images/3.2-SNV-875bdddefc2495bd57dc9dde98f9b681.jpg"}}]);