"""
Behavior - function accepts a list, and for each position,
            if the number is bigger than the value after it,
            swaps the values. in other words, function sorts the
            list from smallest to biggest
implementation - rename function from mystery_9 to sort_values.
                 ensure argument passed is iterable
"""


def sort_values(a: list ) -> list:
    """function sorts the list from smallest to biggest by
    swapping values.
    
    parameters:
    a: list - contains numbers
    
    Returns - the sorted list, a
    
    >>> sort_values([7, 3, 2])
    [2, 3, 7]

    >>> sort_values([1, 2, 3])
    [1, 2, 3]

    >>> sort_values([])
    []

    >>> sort_values(['j', 'a', 'k', 'c'])
    ['a', 'c', 'j', 'k']
    """
    # assert arg is list
    assert isinstance(a, list)


    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
