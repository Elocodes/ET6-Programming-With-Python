"""
Behavior - As long as a is not empty, remove its smallest value, add it to b
strategy - remove from a, add it to b.
implementation - argument a can be a list or tuple, containing numbers or strings.
                rename function from mystrey_5 to list_to_list.
                ensure that argument a is iterable, so it has to be either a list.
                tuple and str are iterable but do not have the ".remove" attribute,
                so will not work for the function below.
"""


def list_to_list(a: list, b=None) -> list:
    """while a is not empty, remove its smallest value and add it to b.
    
    parameter:
    a: list - can contain either numbers or strings but not both.
    
    Returns - list b.
    
    >>> list_to_list([2, 3, 9], b=None)
    [2, 3, 9]

    >>> list_to_list(["food"], b=None)
    ['food']

    >>> list_to_list(["milk", "strawberry", "zebra", "apple"], b=None)
    ['apple', 'milk', 'strawberry', 'zebra']

    >>> list_to_list([[2, 3], [-1, 56]])
    [[-1, 56], [2, 3]]

    >>> list_to_list([3, "dress", -4, 0], b=None)
    Traceback (most recent call last):
    ...
    AssertionError: arg is mixed with numbers and strings
    """
    # assert arg a is iterable - either a list or nested lists
    # assert arg a contains either numbers or str, but not both
    has_num = False
    has_str = False    
    assert isinstance(a, list)
    for item in a:
        if isinstance(item, int | float):
            has_num = True
        elif isinstance(item, str):
            has_str = True
        if has_num and has_str:
            raise AssertionError("arg is mixed with numbers and strings")

    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
