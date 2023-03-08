"""
Number partitioning algorithms - sending the algorithm as argument - strategy pattern.

Author: Erel Segal-Halevi
Since: 2022-03
"""

from typing import Callable, Any


def partition(algorithm: Callable, numbins: int, items: Any):
    """
    >>> partition(algorithm=roundrobin, numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 3, 1], [9, 3], [5, 2]]

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
    return algorithm(numbins, item_names, valueof)


def roundrobin(numbins: int, item_names: list, valueof: Callable[[Any], float] = lambda x:x):
    """
    Partition the given items using the round-robin algorithm.
    >>> roundrobin(numbins=2, item_names=[1,2,3,3,5,9,9])
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> roundrobin(numbins=3, item_names=[1,2,3,3,5,9,9])
    [[9, 3, 1], [9, 3], [5, 2]]
    """
    bins = [[] for _ in range(numbins)]
    ibin = 0
    for item in sorted(item_names, key=valueof, reverse=True):
        bins[ibin].append(item)
        ibin = (ibin+1) % numbins
    return bins


def greedy(numbins: int, item_names: list, valueof: Callable[[Any], float] = lambda x:x):
    """
    Partition the given items using the greedy number partitioning algorithm.

    >>> greedy(numbins=2, item_names=[1,2,3,3,5,9,9])
    [[9, 5, 2], [9, 3, 3, 1]]
    >>> greedy(numbins=3, item_names=[1,2,3,3,5,9,9])
    [[9, 2], [9, 1], [5, 3, 3]]
    """
    bins = [[] for _ in range(numbins)]
    sums = [0 for _ in range(numbins)]
    for item in sorted(item_names, key=valueof, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=lambda i: sums[i])
        bins[index_of_least_full_bin].append(item)
        sums[index_of_least_full_bin] += valueof(item)
    return bins


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
