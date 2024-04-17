"""
Illustrates solutions to some potential problems in doctest.
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

# 4: expressions
def factorial(n):
    """
    >>> factorial(5)==1*2*3*4*5
    True
    """
    return 1 if n<=1 else n*factorial(n-1)
   


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
