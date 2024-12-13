"""
Behavior - arg a is a list of lists. if arg b is found in the first list,
            that list is appended to c. for each loop, the first list is
            removed from a, regardless of if it weas appended to c or not.
implementation - rename mystery_8 to loop_through_lists. add documentation
"""


def loop_through_lists(a: list, b):
    """check for b in the first sublist. if found, append the sublist to c.
    with each loop, remove the first sublist from the lists in arg a.
    
    parameters:
    a: list - contains other lists
    b: any - can be numbers or str
    
    Returns: the new list of lists, arg c
    
    >>> loop_through_lists([[2, 9, 8], [56, 3], [4]], 9)
    [[2, 9, 8]]

    >>> loop_through_lists([[2, 9, 8], [56, 3], [4, 9]], 9)
    [[2, 9, 8], [4, 9]]

    >>> loop_through_lists([[2, 9, 8], [56, 3], [4, 9]], 10)
    []
    """
    # asser that arg a is a list and its sublists are lists
    assert isinstance(a, list)
    for nested in a:
        assert isinstance(nested, list)
        
    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
