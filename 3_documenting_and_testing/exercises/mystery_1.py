"""
Behavior - function takes two arguments and returns their sum
strategies - a) you can create a variable and assign the sum of the arguments to it, then return the variable
             b) directly return the sum of the two arguments
implementation - implement strategy b) below as it is simpler and more readable
"""

# -- before documenting and testing --
# def mystery_1(a,b):
#    return a + b

# -- after documenting and testing --

def sum_of_numbers(a: int | float, b: int | float) -> int:
    """ sums the two arguments passed and returns their value.
    
    Parameters:
    a: int or float- positive, negative or zero
    b: int or float- positive, negative or zero

    Returns: a sum of the arguments 
    
    >>> sum_of_numbers(2, 3)
    5
    
    >>> sum_of_numbers(-2, 3)
    1

    >>> sum_of_numbers(2, -3)
    -1

    >>> sum_of_numbers(-2, -3)
    -5
    """
    # assert that argument passed is integer or float
    assert isinstance(a, int | float)
    assert isinstance(b, int | float)

    return a + b