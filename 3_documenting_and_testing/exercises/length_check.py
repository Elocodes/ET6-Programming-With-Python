"""
Behavior - function checks the length of argument passed
strategy - a) assign the length of the agrument to a variable, then return the variable
           b) return length of argument directly
implementation - strategy b) because of ease
"""

# before documenting and testing

# def mystery_2(a):
#    if len(a) == 0:
#       return None

#    return len(a)

# -- after documenting and testing

def length_check(a: str | list) -> str | list:
    """calculates the length of argument passed.
    
    parameter:
    a: str or list
    
    Returns: length of argument a

    >>> length_check("christmas")
    9

    >>> length_check([]) is None
    True

    >>> length_check("") is None
    True

    >>> length_check([3, 7, "cat"])
    3

    >>> length_check([[4], [8, 9, 23]])
    2

    >>> length_check(50)
    Traceback (most recent call last):
    ...
    AssertionError
    """

    # assert that argument is str or lis
    assert isinstance(a, str | list)

    if len(a) == 0:
        return None
    return len(a)
