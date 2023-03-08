"""
Number partitioning algorithms - sending the algorithm as argument - strategy pattern.

Author: Erel Segal-Halevi
Since: 2022-03
"""

from typing import Callable, Any
from bins import *
import outputtypes as out


def partition(algorithm: Callable, numbins: int, items: list, outputtype: out.OutputType=out.Partition, **kwargs):
    """
    >>> partition(algorithm=roundrobin, numbins=2, items=[1,2,3,3,5,9,9])
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9], outputtype=out.Partition)
    [[9, 3, 1], [9, 3], [5, 2]]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9], outputtype=out.Partition, first_bin=1)
    [[5, 2], [9, 3, 1], [9, 3]]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9], outputtype=out.Sums)
    [13, 12, 7]
    >>> partition(algorithm=roundrobin, numbins=3, items=[1,2,3,3,5,9,9], outputtype=out.LargestSum)
    13

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
    bins = outputtype.create_empty_bins(numbins)
    bins.set_valueof(valueof)
    algorithm(bins, item_names, **kwargs)
    return outputtype.extract_output_from_bins(bins)


def roundrobin(bins: Bins, item_names: list, first_bin=0):
    """
    Partition the given items using the round-robin algorithm.
    >>> roundrobin(BinsKeepingContents(2), item_names=[1,2,3,3,5,9,9]).bins
    [[9, 5, 3, 1], [9, 3, 2]]
    >>> roundrobin(BinsKeepingContents(3), item_names=[1,2,3,3,5,9,9]).bins
    [[9, 3, 1], [9, 3], [5, 2]]
    >>> roundrobin(BinsKeepingContents(3), item_names=[1,2,3,3,5,9,9], first_bin=1).bins
    [[5, 2], [9, 3, 1], [9, 3]]
    """
    ibin = first_bin
    for item in sorted(item_names, key=bins.valueof, reverse=True):
        bins.add_item_to_bin(item, ibin)
        ibin = (ibin+1) % bins.num
    return bins


def greedy(bins: Bins, item_names: list):
    """
    Partition the given items using the greedy number partitioning algorithm.

    >>> greedy(BinsKeepingContents(2), item_names=[1,2,3,3,5,9,9]).bins
    [[9, 5, 2], [9, 3, 3, 1]]
    >>> greedy(BinsKeepingContents(3), item_names=[1,2,3,3,5,9,9]).bins
    [[9, 2], [9, 1], [5, 3, 3]]
    """
    for item in sorted(item_names, key=bins.valueof, reverse=True):
        index_of_least_full_bin = min(range(bins.num), key=lambda i: bins.sums[i])
        bins.add_item_to_bin(item, index_of_least_full_bin)
    return bins



##### Extra fun

import numpy as np

def partition_random_items(numitems: int, bitsperitem: int, **kwargs):
    """
    Generates a uniformly-random list of items and partitions them using the given algorithm.
    :param numitems: how many items to generate.
    :param bitsperitem: how many bits in each item.
    :param kwargs: keyword arguments delegated to `partition`.
    >>> partition_random_items(numitems=10, bitsperitem=16, algorithm=greedy, numbins=2, outputtype=out.Sums) # doctest:+ELLIPSIS
    [..., ...]
    """
    items = np.random.randint(1, 2**bitsperitem-1, numitems)
    return partition(items=items, **kwargs)




def compare_algorithms(
    numbins: int, items: Any, outputtype: out.OutputType,
    algorithm1: Callable, kwargs1: dict,
    algorithm2: Callable, kwargs2: dict,
)->bool:
    """
    Compare the output of two algorithms on the given items.

    :param numbins: int - how many parts should be in the partition?
    :param items: what items to partition (as in the `partition` function).
    :param outputtype: what output to return for comparison. See `outputtypes.py'.
    :param algorithm1. algorithm2: algorithms to compare.
    :param kwargs1, kwargs2: keyword arguments to send to algorithms 1 and 2 respectively.

    >>> compare_algorithms(2, [4,5,6,7,8], out.LargestSum, algorithm1=roundrobin, kwargs1={}, algorithm2=greedy, kwargs2={})
    Algorithms differ on input [4, 5, 6, 7, 8]:
        roundrobin:   LargestSum=18
        greedy:   LargestSum=17
    False
    >>> compare_algorithms(5, [4,5,6,7,8], out.LargestSum, algorithm1=roundrobin, kwargs1={}, algorithm2=greedy, kwargs2={})
    True
    >>> compare_algorithms(3, [4,5,6,7,8], out.Sums, algorithm1=roundrobin, kwargs1={'first_bin': 1}, algorithm2=roundrobin, kwargs2={'first_bin': 0})
    Algorithms differ on input [4, 5, 6, 7, 8]:
        roundrobin:   Sums=[6, 13, 11]
        roundrobin:   Sums=[13, 11, 6]
    False
    >>> compare_algorithms(3, [4,5,6,7,8], out.SortedSums, algorithm1=roundrobin, kwargs1={'first_bin': 1}, algorithm2=roundrobin, kwargs2={'first_bin': 0})
    True
    """
    bins1 = partition(algorithm1, numbins, items, outputtype=out.PartitionAndSums, **kwargs1)
    bins2 = partition(algorithm2, numbins, items, outputtype=out.PartitionAndSums, **kwargs2)
    output1 = outputtype.extract_output_from_bins(bins1)
    output2 = outputtype.extract_output_from_bins(bins2)
    if output1 != output2:
        explanation1 = f"{outputtype.__name__}={output1}"
        explanation2 = f"{outputtype.__name__}={output2}"
        print(f"Algorithms differ on input {items}:\n\t{algorithm1.__name__}:   {explanation1}\n\t{algorithm2.__name__}:   {explanation2}")
        return False
    else:
        return True

def compare_algorithms_on_random_items(numitems: int, bitsperitem: int, **kwargs)->bool:
    """
    Compare the output of two algorithms on randomly-generated items.

    :param numitems: how many items to generate.
    :param bitsperitem: how many bits in each item.
    :param kwargs: keyword arguments delegated to `partition`.
    >>> compare_algorithms_on_random_items(10, 16, numbins=2, outputtype=out.SortedSums, algorithm1=greedy, kwargs1={}, algorithm2=roundrobin, kwargs2={})
    Algorithms differ on input [...]:
        greedy:   SortedSums=[...]
        roundrobin:   SortedSums=[...]
    False   
    """
    items = np.random.randint(1, 2**bitsperitem-1, numitems, dtype=np.int64)
    return compare_algorithms(items=items, **kwargs)


if __name__ == "__main__":
    import doctest

    (failures, tests) = doctest.testmod(report=True, optionflags=doctest.NORMALIZE_WHITESPACE+doctest.ELLIPSIS)
    print("{} failures, {} tests".format(failures, tests))

    print(partition_random_items(10, 16, algorithm=greedy, numbins=2, outputtype=out.Partition))
    compare_algorithms_on_random_items(10, 16, numbins=2, outputtype=out.SortedSums, algorithm1=greedy, kwargs1={}, algorithm2=roundrobin, kwargs2={})
