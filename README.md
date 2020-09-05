# bioinformatics
basic functionality for manipulating biological data

in development

CONTENTS:

1. `ori_finder.py`
  The purpose of this file is to provide features to help find the origin of replication (ori) of a genome. It provides features to analyze text for repeated patterns                         and other features that can help locate the ori.

-`PatternCount(text, pattern)` returns number of instances of a certain pattern in the given text. Useful for finding the number of times a given DNA fragment appears in a genome. Inputs: `text`, the genome, and `pattern`, the DNA fragment, such as `"CTGAAAGC"`. Runs in `O(N)` time, where `N` is the size of the dataset.



-`frequency(text, k)` returns a `dict` with keys that are patterns of length `k` from `text` and values that are the amount of times the pattern appears. For example, suppose one had a sequence of `GTGCCTGTTCGGTGGTCGCGGCGCTGATGGCGATGAATGAACAC` and wanted the frequency of every pattern of length 3 in the sequence, the `dict` would contain keys of GTG, TGC, GCC, etc. with values that correspond to each pattern's frequency. Inputs: `text`, a string, and `k`, an int. Runs in `O(N)` time, where `N` is the size of the dataset.


-`max_rep(table)` finds the pattern in a `dict`, such as the one that is the output of `frequency(text, k)`, that has the highest value. Runs in `O(N)` time, where `N` is the size of the table.
