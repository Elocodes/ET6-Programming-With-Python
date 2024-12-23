"""
behavior - function returns the lesser number between the two arguments passed.
           if they are equal, return their sum
strategies - a) use the min function. this is straightforward and easy to read
             b) use if, elif, else as below. this takes a lot of iterations
implementation - I will implement a)
"""

# -- before testing --
# def mystery_3(a, b):
#    if a < b:
#        return a
#    elif a > b:
#        return b
#    else:
#       return a + b

def min_or_equal(a: int | float , b: int | float) -> int | float:
    """find the smallest number. sum if both are equal.
    
    parameters:
    a: int
    b: int
    
    Returns: smallest number or sum of both numbers if equal

    >>> min_or_equal(45, 9)
    9

    >>> min_or_equal(0, -38)
    -38

    >>> min_or_equal(2, 2)
    4

    >>> min_or_equal(-2.33, -2.34)
    -2.34
    """

    # assert arguments are int
    assert isinstance(a, int | float)
    assert isinstance(b, int | float)

    if a != b:
        return min(a, b)
    else:
        return a + b
