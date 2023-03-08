"""
Illustrates some potential problems in doctest.
"""

def div3(n):
    """
    >>> div3(10)
    3.3333333333333333
    """
    return n/3

def myrange(n):
    """
    >>> myrange(3)
    [0, 1, 2]
    """
    return range(n)

def firstthreenumbers():
    """
    >>> firstthreenumbers()
    [0, 1, 2]
    """
    return [2,1,0]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
