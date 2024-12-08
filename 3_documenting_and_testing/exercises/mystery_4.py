"""
Behavior - while length of variable b remains less than the passed argument,
           function adds the value of variable c to b, and increases c by 1
Strategy - use while loop to loop through
implementatioon - rename mystery_4 to increment_list, and add documentation 
"""


def increment_list(a: int) -> int:
    """is length of b lower than a, then add c to b. increase c by 1.
    
    parameters:
    a: int
    
    Returns: list b
    
    >>> increment_list(0)
    []

    >>> increment_list(-1)
    []

    >>> increment_list(1)
    [0]

    >>> increment_list(4)
    [0, 1, 2, 3]
    """
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
