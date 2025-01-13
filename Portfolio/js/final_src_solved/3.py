# Solution 1:
def deviation(seq, pred):
    """Returns the difference between the largest and smallest values in seq for which pred is True.
    If pred evaluates to False on all values in seq, this call returns 0.

    Args:
    seq -- a sequence of numbers
    pred -- a one-parameter function

    Returns:
    the difference between the largest and smallest values in seq for which pred is True.
    If pred evaluates to False on all values in seq, this call returns 0.

    Example:
    >>> seq = [-3, 1, 5, -4, 10]
    >>> pred1 = lambda x: x > 0
    >>> pred2 = lambda x: x % 2 == 0
    >>> pred3 = lambda x: True
    >>> pred4 = lambda x: False
    >>> deviation(seq, pred1)
    9
    >>> deviation(seq, pred2)
    14
    >>> deviation(seq, pred3)
    14
    >>> deviation(seq, pred4)
    0
    """
    if not seq:
        return 0

    mx, mn = float("-inf"), float("inf")

    for a in seq:
        if pred(a):
            if a > mx:
                mx = a
            if a < mn:
                mn = a

    return 0 if mx < mn else mx - mn


# Solution 2:
# def deviation(seq, pred):
#     """Returns the difference between the largest and smallest values in seq for which pred is True.
#     If pred evaluates to False on all values in seq, this call returns 0.

#     Args:
#     seq -- a sequence of numbers
#     pred -- a one-parameter function

#     Returns:
#     the difference between the largest and smallest values in seq for which pred is True.
#     If pred evaluates to False on all values in seq, this call returns 0.

#     Example:
#     >>> seq = [-3, 1, 5, -4, 10]
#     >>> pred1 = lambda x: x > 0
#     >>> pred2 = lambda x: x % 2 == 0
#     >>> pred3 = lambda x: True
#     >>> pred4 = lambda x: False
#     >>> deviation(seq, pred1)
#     9
#     >>> deviation(seq, pred2)
#     14
#     >>> deviation(seq, pred3)
#     14
#     >>> deviation(seq, pred4)
#     0
#     """
#     filtered_seq = filter(pred, seq)

#     try:
#         a = next(filtered_seq)
#     except StopIteration:
#         return 0

#     mx, mn = a, a

#     for a in filtered_seq:
#         if a > mx:
#             mx = a
#         if a < mn:
#             mn = a

#     return mx - mn


# Solution 3, shorter but potentially less efficient:
# def deviation(seq, pred):
#     """Returns the difference between the largest and smallest values in seq for which pred is True.
#     If pred evaluates to False on all values in seq, this call returns 0.

#     Args:
#     seq -- a sequence of numbers
#     pred -- a one-parameter function

#     Returns:
#     the difference between the largest and smallest values in seq for which pred is True.
#     If pred evaluates to False on all values in seq, this call returns 0.

#     Example:
#     >>> seq = [-3, 1, 5, -4, 10]
#     >>> pred1 = lambda x: x > 0
#     >>> pred2 = lambda x: x % 2 == 0
#     >>> pred3 = lambda x: True
#     >>> pred4 = lambda x: False
#     >>> deviation(seq, pred1)
#     9
#     >>> deviation(seq, pred2)
#     14
#     >>> deviation(seq, pred3)
#     14
#     >>> deviation(seq, pred4)
#     0
#     """
#     seq = list(filter(pred, seq))
#     if len(seq) == 0:
#         return 0
#     return max(seq) - min(seq)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)