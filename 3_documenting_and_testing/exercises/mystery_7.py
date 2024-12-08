"""
Behavior - argument a is a list that contains multiple lists.
        function checks for arg b in in each of these lists.
        if found, the list that contains it is appended into c.
strategy - iterate through list a, find variable d, append to c
implementation - rename mystery_7 to list_in_list
"""


def list_in_list(a: list, b):
    """if b is in any of the embedded lists in a, append sublist to c.
    
    parameters:
    a: list - contains embedded lists
    b: any - can be numbers or str
    
    Returns: list c
    
    >>> list_in_list([[9], [23, 8], ["apple"]], "apple")
    [["apple"]]

    >>> list_in_list([[9], [8], [3]], 89)
    []
    """
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
