"""
Illustrates some potential problems in doctest.
"""

# 1: accuracy
def div3(n):
    """
    >>> div3(10)
    3.3333333333333333
    """
    return n/3

# 2: string representation
def myrange(n):
    """
    >>> myrange(3)
    [0, 1, 2]
    """
    return range(n)

# 3: order
def firstthreenumbers():
    """
    >>> firstthreenumbers()
    [0, 1, 2]
    """
    return [2,1,0]

# 4: expressions
def factorial(n):
    """
    >>> factorial(5)
    1*2*3*4*5
    """
    return 1 if n<=1 else n*factorial(n-1)


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
