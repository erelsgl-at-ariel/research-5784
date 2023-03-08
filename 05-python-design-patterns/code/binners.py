"""
A partitioning algorithm usually keeps an array of "bins", and fills it incrementally.
Some algorithms (e.g. branch-and-bound algorithms) keep many arrays of bins simultaneously.

A Binner is a class that manages a collection of bin-arrays.
It can create a new bins-array, fill an existing array, etc.

It uses the FlyWeight design pattern. See: https://refactoring.guru/design-patterns/flyweight

Author: Erel Segal-Halevi
Since:  2022-07
"""

from abc import ABC, abstractmethod

import numpy as np, itertools
from typing import Any, Callable, List, Tuple, Iterator

BinsArray = Any

def bins2str(bins: BinsArray)->str:
    try:
        # bins is a tuple (sums,lists):
        sums, lists = bins
        numbins = len(sums)
        bins_str = [f"Bin #{i}: {lists[i]}, sum={sums[i]}" for i in range(numbins)]
    except:
        # bins is an array of sums:
        numbins = len(bins)
        bins_str = [f"Bin #{i}: sum={bins[i]}" for i in range(numbins)]
    return "\n".join(bins_str)

def printbins(bins:BinsArray):
    print(bins2str(bins))

class Binner(ABC):
    """
    An abstract bins-array manager.
    
    All arrays created by the same binner share the following two variables:
     * numbins - the total number of bins.
     * valueof - a function that maps an item to its value.
    """

    def __init__(self, valueof: Callable = lambda x:x):
        self.valueof = valueof

    @abstractmethod
    def new_bins(self, numbins:int)->BinsArray:
        '''
        Create a new bins-array with numbins bins.
        '''
        return None

    @abstractmethod
    def add_item_to_bin(self, bins:BinsArray, item: Any, bin_index: int)->BinsArray:
        """
        Add the given item to the given bin in the given array.
        Return the bins after the addition.
        """
        return bins

    @abstractmethod
    def sums(self, bins: BinsArray) -> Tuple[float]:
        """
        Return only the current sums. 
        """
        return None


class BinnerKeepingSums(Binner):
    """
    A binner that creates bin-arrays that keep track only of the total sum in each bin.

    >>> values = {"a":3, "b":4, "c":5, "d":5, "e":5}
    >>> binner = BinnerKeepingSums(lambda x: values[x])
    >>> bins = binner.new_bins(3)
    >>> printbins(binner.add_item_to_bin(bins, item="a", bin_index=0))
    Bin #0: sum=3.0
    Bin #1: sum=0.0
    Bin #2: sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="b", bin_index=1)
    >>> printbins(bins)
    Bin #0: sum=3.0
    Bin #1: sum=4.0
    Bin #2: sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="c", bin_index=1)
    >>> printbins(bins)
    Bin #0: sum=3.0
    Bin #1: sum=9.0
    Bin #2: sum=0.0
    """
    def __init__(self, valueof: Callable = lambda x:x):
        super().__init__(valueof)

    BinsArray = np.ndarray    # Here, the bins-array is simply an array of the sums.

    def new_bins(self, numbins)->BinsArray:
        bins = np.zeros(numbins)   # similar to numbins*[0]
        return bins

    def add_item_to_bin(self, bins: BinsArray, item: Any, bin_index: int)->BinsArray:
        bins[bin_index] += self.valueof(item)
        return bins

    def sums(self, bins: BinsArray) -> Tuple[float]:
        return bins


class BinnerKeepingContents(BinnerKeepingSums):
    """
    A binner that creates bin-arrays that keep track of the entire contents of each bin.

    >>> values = {"a":3, "b":4, "c":5, "d":5, "e":5}
    >>> binner = BinnerKeepingContents(lambda x: values[x])
    >>> bins = binner.new_bins(3)
    >>> printbins(binner.add_item_to_bin(bins, item="a", bin_index=0))
    Bin #0: ['a'], sum=3.0
    Bin #1: [], sum=0.0
    Bin #2: [], sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="b", bin_index=1)
    >>> printbins(bins)
    Bin #0: ['a'], sum=3.0
    Bin #1: ['b'], sum=4.0
    Bin #2: [], sum=0.0
    >>> _=binner.add_item_to_bin(bins, item="c", bin_index=1);
    >>> printbins(bins)
    Bin #0: ['a'], sum=3.0
    Bin #1: ['b', 'c'], sum=9.0
    Bin #2: [], sum=0.0
    """

    def __init__(self, valueof: Callable = lambda x:x):
        super().__init__(valueof)

    BinsArray = Tuple[np.ndarray, List[List]]  # Here, each bins-array is a tuple: sums,lists. sums is an array of sums; lists is a list of lists of items.

    def new_bins(self, numbins:int)->BinsArray:
        sums  = np.zeros(numbins)
        lists = [[] for _ in range(numbins)]
        return (sums, lists)

    def add_item_to_bin(self, bins:BinsArray, item: Any, bin_index: int)->BinsArray:
        sums, lists = bins
        value = self.valueof(item)
        sums[bin_index] += value
        lists[bin_index].append(item)
        return bins

    def sums(self, bins: BinsArray) -> Tuple[float]:
        return bins[0]

if __name__ == "__main__":
    import doctest, sys
    (failures, tests) = doctest.testmod(report=True, optionflags=doctest.FAIL_FAST)
    print("{} failures, {} tests".format(failures, tests))
    if failures>0:
        sys.exit(1)
