"""
Number partitioning algorithms - sending the algorithm as argument - strategy pattern.

Author: Erel Segal-Halevi
Since: 2022-03
"""

from typing import Callable, Any
from binners import *
import outputtypes2 as out


def partition(algorithm: Callable, numbins: int, items: list, outputtype: out.OutputType=out.Partition, **kwargs):
    """
    >>> partition(algorithm=roundrobin, numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9], outputtype=out.Partition)
    [[9, 3, 1], [9, 3], [5, 2]]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9], outputtype=out.Sums)
    [13.0, 12.0, 7.0]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9], outputtype=out.LargestSum)
    13.0

    >>> partition(algorithm=roundrobin, numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'e', 'd', 'a'], ['g', 'c', 'b']]
    >>> partition(algorithm=roundrobin, numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'c', 'a'], ['g', 'd'], ['e', 'b']]

    >>> partition(algorithm=greedy, numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 2], [9, 3, 3, 1]]
    >>> partition(algorithm=greedy, numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 2], [9, 1], [5, 3, 3]]

    >>> partition(algorithm=greedy, numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'e', 'b'], ['g', 'c', 'd', 'a']]
    >>> partition(algorithm=greedy, numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'b'], ['g', 'a'], ['e', 'c', 'd']]
    """    
    if isinstance(items, dict):  # items is a dict mapping an item to its value.
        item_names = items.keys()
        valueof = items.__getitem__
    else:  # items is a list
        item_names = items
        valueof = lambda item: item
    binner = outputtype.create_binner(valueof)
    bins   = algorithm(binner, numbins, item_names, **kwargs)
    return outputtype.extract_output_from_binsarray(bins)


def roundrobin(binner: Binner, numbins: int, items: List[any]):
    """
    Partition the given items using the roundrobin number partitioning algorithm.

    >>> printbins(roundrobin(BinnerKeepingContents(), 2, items=[1,2,3,3,5,9,9]))
    Bin #0: [9, 5, 3, 1], sum=18.0
    Bin #1: [9, 3, 2], sum=14.0
    >>> printbins(roundrobin(BinnerKeepingContents(), 3, items=[1,2,3,3,5,9,9]))
    Bin #0: [9, 3, 1], sum=13.0
    Bin #1: [9, 3], sum=12.0
    Bin #2: [5, 2], sum=7.0
    >>> list(roundrobin(BinnerKeepingSums(), 3, items=[1,2,3,3,5,9,9]))
    [13.0, 12.0, 7.0]

    >>> partition(algorithm=roundrobin, numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'c', 'a'], ['g', 'd'], ['e', 'b']]
    >>> partition(algorithm=roundrobin, numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9}, outputtype=out.Sums)
    [18.0, 14.0]
    """
    ibin = 0
    bins = binner.new_bins(numbins)
    for item in sorted(items, key=binner.valueof, reverse=True):
        binner.add_item_to_bin(bins, item, ibin)
        ibin = (ibin+1) % numbins
    return bins


def greedy(binner: Binner, numbins: int, items: List[any]):
    """
    Partition the given items using the greedy number partitioning algorithm.

    >>> printbins(greedy(BinnerKeepingContents(), 2, items=[1,2,3,3,5,9,9]))
    Bin #0: [9, 5, 2], sum=16.0
    Bin #1: [9, 3, 3, 1], sum=16.0
    >>> printbins(greedy(BinnerKeepingContents(), 3, items=[1,2,3,3,5,9,9]))
    Bin #0: [9, 2], sum=11.0
    Bin #1: [9, 1], sum=10.0
    Bin #2: [5, 3, 3], sum=11.0
    >>> list(greedy(BinnerKeepingSums(), 3, items=[1,2,3,3,5,9,9]))
    [11.0, 10.0, 11.0]

    >>> partition(algorithm=greedy, numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'b'], ['g', 'a'], ['e', 'c', 'd']]
    >>> partition(algorithm=greedy, numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9}, outputtype=out.Sums)
    [16.0, 16.0]
    """
    bins = binner.new_bins(numbins)
    for item in sorted(items, key=binner.valueof, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=binner.sums(bins).__getitem__)
        binner.add_item_to_bin(bins, item, index_of_least_full_bin)
    return bins





if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True, optionflags=doctest.NORMALIZE_WHITESPACE+doctest.ELLIPSIS)
    print("{} failures, {} tests".format(failures, tests))
