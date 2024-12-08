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

def sum_of_numbers(a: int, b: int) -> int:
    """ sums the two arguments passed and returns their value.
    
    Parameters:
    a: int - positive, negative or zero
    b: int - positive, negative or zero

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

    if (a or b) is not int:
        return "argument must be an int"
    return a + b