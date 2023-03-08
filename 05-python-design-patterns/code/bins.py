"""
Utility functions and classes for incrementally filling bins during an algorithm.

Author: Erel Segal-Halevi
Since:  2022-02
"""

from abc import ABC, abstractmethod
from typing import Any, Callable


class Bins(ABC):
    """
    An abstract bins class.
    """

    def __init__(self, numbins: int):
        self.num = numbins
        self.valueof = lambda x: x

    def set_valueof(self, new_valueof: Callable):
        self.valueof = new_valueof

    @abstractmethod
    def add_item_to_bin(self, item: float, bin_index: int):
        pass

    @abstractmethod
    def result(self):
        return None


class BinsKeepingSums(Bins):
    """
    A bins structure that keeps track only of the total sum in each bin.
    """

    def __init__(self, numbins: int):
        super().__init__(numbins)
        self.sums = numbins*[0]

    def add_item_to_bin(self, item: float, bin_index: int):
        self.sums[bin_index] += self.valueof(item)

    def result(self):
        return self.sums

class BinsKeepingContents(BinsKeepingSums):
    """
    A bins structure that keeps track of both the sum and the entire contents of each bin.
    """

    def __init__(self, numbins: int):
        super().__init__(numbins)
        self.bins = [[] for _ in range(numbins)]

    def add_item_to_bin(self, item: float, bin_index: int):
        super().add_item_to_bin(item, bin_index)
        self.bins[bin_index].append(item)

    def result(self):
        return self.bins



if __name__ == "__main__":
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
