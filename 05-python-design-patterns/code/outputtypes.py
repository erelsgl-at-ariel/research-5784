"""
Define the various available output formats for a partition algorithm.
"""

from abc import ABC
from typing import Any, List
from bins import Bins, BinsKeepingContents, BinsKeepingSums


class OutputType(ABC):
    @classmethod
    def create_empty_bins(cls, numbins: int) -> Bins:
        """
        Construct and return a Bins structure. Used at the initialization phase of an algorithm.
        """
        pass

    @classmethod
    def extract_output_from_bins(cls, bins: Bins) -> Any:
        """
        Return the required output from the given list of filled bins.
        """
        pass


class Sums(OutputType):
    @classmethod
    def create_empty_bins(cls, numbins: int) -> List:
        return BinsKeepingSums(numbins)

    # Output the sums of all the bins (but not the bins contents).
    @classmethod
    def extract_output_from_bins(cls, bins: Bins) -> List:
        return cls.extract_output_from_sums(bins.sums)

    @classmethod
    def extract_output_from_sums(cls, sums: List[float]) -> List:
        return sums


class SortedSums(Sums):
    @classmethod
    def extract_output_from_sums(cls, sums: List[float]) -> List:
        return sorted(sums)


class LargestSum(Sums):
    # Output the largest bin sum.
    @classmethod
    def extract_output_from_sums(cls, sums: List[float]) -> List:
        return max(sums)


class SmallestSum(Sums):
    # Output the smallest bin sum.
    @classmethod
    def extract_output_from_sums(cls, sums: List[float]) -> List:
        return min(sums)


class Difference(Sums):
    # Output the difference between the largest and smallest sum.
    @classmethod
    def extract_output_from_sums(cls, sums: List[float]) -> List:
        return max(sums) - min(sums)


class Partition(OutputType):
    @classmethod
    def create_empty_bins(cls, numbins: int) -> List:
        return BinsKeepingContents(numbins)

    # Output the set of all bins.
    @classmethod
    def extract_output_from_bins(cls, bins: Bins) -> List:
        return bins.bins


class PartitionAndSums(Partition):
    # Output the set of all bins.
    @classmethod
    def extract_output_from_bins(cls, bins: Bins) -> List:
        return bins
