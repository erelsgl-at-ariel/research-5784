"""
Number partitioning algorithms - naive implementation - accepts dicts as input.

Author: Erel Segal-Halevi
Since: 2022-03
"""

from typing import Dict

def roundrobin(numbins: int, items: Dict[str, float]):
    """
    Partition the given items using the round-robin algorithm.

    >>> roundrobin(numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'e', 'd', 'a'], ['g', 'c', 'b']]
    >>> roundrobin(numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'c', 'a'], ['g', 'd'], ['e', 'b']]
    """
    bins = [[] for _ in range(numbins)]
    ibin = 0
    for item in sorted(items.keys(), key=lambda k: items[k], reverse=True):
        bins[ibin].append(item)
        ibin = (ibin+1) % numbins
    return bins



def greedy(numbins: int, items: Dict[str, float]):
    """
    Partition the given items using the greedy number partitioning algorithm.

    >>> greedy(numbins=2, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'e', 'b'], ['g', 'c', 'd', 'a']]
    >>> greedy(numbins=3, items={"a":1, "b":2, "c":3, "d":3, "e":5, "f":9, "g":9})
    [['f', 'b'], ['g', 'a'], ['e', 'c', 'd']]
    """
    bins = [[] for _ in range(numbins)]
    sums = [0 for _ in range(numbins)]
    for item_name in sorted(items.keys(), key=lambda item_name: items[item_name], reverse=True):
        index_of_least_full_bin = min(range(numbins), key=lambda i: sums[i])
        bins[index_of_least_full_bin].append(item_name)
        sums[index_of_least_full_bin] += items[item_name]
    return bins


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
