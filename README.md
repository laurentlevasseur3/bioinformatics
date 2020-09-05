# bioinformatics
basic functionality for manipulating biological data

in development


FUNCTIONS:

-`PatternCount(text, pattern)` returns number of instances of a certain pattern in the given text. Useful for finding the number of times a given DNA fragment appears in a genome. Inputs: `text`, the genome, and `pattern`, the DNA fragment, such as `"CTGAAAGC"`.



-`frequency(text, k)` returns a `dict` with keys that are patterns of length `k` from `text` and values that are the amount of times the pattern appears. For example, suppose one had a sequence of `GTGCCTGTTCGGTGGTCGCGGCGCTGATGGCGATGAATGAACAC` and wanted the frequency of every pattern of length 3 in the sequence, the `dict` would contain keys of GTG, TGC, GCC, etc. with values that correspond to each pattern's frequency.
