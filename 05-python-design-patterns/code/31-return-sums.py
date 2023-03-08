"""
Number partitioning algorithms - naive implementation - returns only the sums.

Author: Erel Segal-Halevi
Since: 2022-03
"""

from typing import List

def roundrobin_partition(numbins: int, items: List[float]):
    """
    Partition the given items using the round-robin algorithm.

    >>> roundrobin_partition(numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> roundrobin_partition(numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 3, 1], [9, 3], [5, 2]]
    """
    bins = [[] for _ in range(numbins)]
    ibin = 0
    for item in sorted(items, reverse=True):
        bins[ibin].append(item)
        ibin = (ibin+1) % numbins
    return bins


def roundrobin_sums(numbins: int, items: List[float]):
    """
    Partition the given items using the round-robin algorithm.

    >>> roundrobin_sums(numbins=2, items=[1,2,3,3,5,9,9])
    [18, 14]
    >>> roundrobin_sums(numbins=3, items=[1,2,3,3,5,9,9])
    [13, 12, 7]
    """
    sums = [0 for _ in range(numbins)]
    ibin = 0
    for item in sorted(items, reverse=True):
        sums[ibin] += item
        ibin = (ibin+1) % numbins
    return sums


def greedy_partition(numbins: int, items: List[float]):
    """
    Partition the given items using the greedy number partitioning algorithm.
    Return the partition.

    >>> greedy_partition(numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 2], [9, 3, 3, 1]]
    >>> greedy_partition(numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 2], [9, 1], [5, 3, 3]]
    """
    bins = [[] for _ in range(numbins)]
    for item in sorted(items, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=lambda i: sum(bins[i]))
        bins[index_of_least_full_bin].append(item)
    return bins

def greedy_partition_2(numbins: int, items: List[float]):
    """
    Partition the given items using the greedy number partitioning algorithm.
    Return the partition.
    Based on code review by Richard Neumann: https://codereview.stackexchange.com/a/274775/20684

    >>> greedy_partition(numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 2], [9, 3, 3, 1]]
    >>> greedy_partition(numbins=3, items=[1,2,3,3,5,9,9])
    [[9, 2], [9, 1], [5, 3, 3]]
    """
    bins = [[] for _ in range(numbins)]
    sums = [0 for _ in range(numbins)]
    for item in sorted(items, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=sums.__getitem__)
        bins[index_of_least_full_bin].append(item)
        sums[index_of_least_full_bin] += item
    return bins


def greedy_sums(numbins: int, items: List[float]):
    """
    Partition the given items using the greedy number partitioning algorithm.
    Return the sums.

    >>> greedy_sums(numbins=2, items=[1,2,3,3,5,9,9])
    [16, 16]
    >>> greedy_sums(numbins=3, items=[1,2,3,3,5,9,9])
    [11, 10, 11]
    """
    sums = [0 for _ in range(numbins)]
    for item in sorted(items, reverse=True):
        index_of_least_full_bin = min(range(numbins), key=sums.__getitem__)  # faster than key=lambda i: sums[i]
        sums[index_of_least_full_bin] += item
    return sums


def benchmark(numbins: int, numitems: int):
    import numpy as np, time
    items = np.random.randint(1, 1000, numitems)
    t0 = time.time()
    greedy_partition_2(numbins, items)
    t1 = time.time()
    greedy_sums(numbins, items)
    t2 = time.time()
    print(f"{numbins} bins, {numitems} items: greedy_partition={t1-t0}. greedy_sums={t2-t1}.")


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

    numbins=3
    for numitems in map(lambda x: 2**x, range(10,25)):
        benchmark(numbins, numitems)
