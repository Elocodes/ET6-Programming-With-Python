"""
Behavior - while length of c is less than the value of a, append b to c. increase b by 1
strategy - use a while loop
implementation - rename mystery_6 to append_to_c. add documntation
"""


def append_to_c(a: int, b: int) -> int:
    """append b to c while length of c is less than a.
    
    parameters:
    a: int
    b: int
    
    Returns: list c
    
    >>> append_to_c(0, 90)
    []

    >>> append_to_c(1, 67)
    [67]

    >>> append_to_c(4, 11)
    [11, 12, 13, 14]
    """
    # assert a and b are int
    assert isinstance(a, int)
    assert isinstance(b, int)
    
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
