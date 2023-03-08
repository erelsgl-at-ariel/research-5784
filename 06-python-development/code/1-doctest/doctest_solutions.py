"""
Illustrates some potential problems in doctest.
"""

def div3(n):
    """
    >>> import numpy as np
    >>> np.round(div3(10),4)
    3.3333
    """
    return n/3

def myrange(n):
    """
    >>> list(myrange(3))
    [0, 1, 2]
    """
    return range(n)

def firstthreenumbers():
    """
    >>> sorted(firstthreenumbers())
    [0, 1, 2]
    """
    return [2,1,0]



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
