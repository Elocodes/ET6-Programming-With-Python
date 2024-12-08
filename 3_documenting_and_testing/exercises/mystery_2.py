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

def length_check(a: str) -> str:
    """calculates the length of argument passed.
    
    parameter:
    a: str
    
    Returns: length of argument a

    >>> length_check("christmas")
    9

    >>> length_check()
    None

    >>> length_check(50)
    argument must be be str 
    """

    if len(a) == 0:
        return None
    return len(a)
