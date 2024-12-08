"""
Behavior - As long as a is not empty, remove its smallest value, add it to b
strategy - remove from a, add it to b.
implementation - argument a can be a list or tuple, containing numbers or strings.
                rename function from mystrey_5 to list_to_list.
                ensure that argument a is iterable, so it has to be either a list or tuple or a str
"""


def list_to_list(a: list | tuple | str, b=None) -> list | tuple | str:
    """while a is not empty, remove its smallest value and add it to b.
    
    parameter:
    a: list | tuple - can contain either numbers or strings.
    
    Returns - list b.
    
    >>> list_to_list([2, 3, 9], b=None)
    [2, 3, 9]

    >>> list_to_list((45, -67, 0), b=None)
    [-67, 0, 45]

    >>> list_to_list(("milk", "strawberry" "zebra", "apple"), b=None)
    ["apple", "milk", "strawberry", "zebra"]
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
