# Variant Equivalence

A common problem in calling genomic variation is the multitude of ways a
variation can be annotated. Two different variant callers might describe the
same genomic alternations in two different ways. For example, consider the
variation that occurs in the figure below: either notation captures the event
correctly, but one considers there to be an SNV then insertion while the other
considers the event a deletion and subsequent insertion. These differences make
comparisons across data sets more difficult. To alleviate the problem, there are
standards emerging that tools can adhere to and software to help normalize
notation of variants, but the problem still exists.

![Figure depicting two variants that are equivalent but called in different ways.](../images/2.5-Variant-Equivalence.jpg)
