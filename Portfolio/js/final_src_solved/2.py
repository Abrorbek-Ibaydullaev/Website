def is_arithmetic(seq):
    """Returns True if the sequence of integers is an arithmetic sequence; otherwise, False

    Args:
    seq -- a list of integers

    Returns:
    True if the sequence is an arithmetic sequence; otherwise, False

    Example:
    >>> is_arithmetic([])
    True
    >>> is_arithmetic([2])
    True
    >>> is_arithmetic([5, -1])
    True
    >>> is_arithmetic([1, 2, 3])
    True
    >>> is_arithmetic(range(100, -1000, -7))
    True
    >>> is_arithmetic((2, 5, 8, 10, 13))
    False
    """    
    if len(seq) < 3:
        return True

    a, b = seq[:2]
    diff = b - a
    a = b

    for b in seq[2:]:
        if b - a != diff:
            return False
        a = b

    return True


# Another solution, do not use list slicing:
# def is_arithmetic(seq):
#     """Returns True if the sequence of integers is an arithmetic sequence; otherwise, False

#     Args:
#     seq -- a list of integers

#     Returns:
#     True if the sequence is an arithmetic sequence; otherwise, False

#     Example:
#     >>> is_arithmetic([])
#     True
#     >>> is_arithmetic([2])
#     True
#     >>> is_arithmetic([5, -1])
#     True
#     >>> is_arithmetic([1, 2, 3])
#     True
#     >>> is_arithmetic(range(100, -1000, -7))
#     True
#     >>> is_arithmetic((2, 5, 8, 10, 13))
#     False
#     """    
#     if len(seq) < 3:
#         return True

#     diff = seq[1] - seq[0]

#     for i in range(2, len(seq)):
#         if seq[i] - seq[i - 1] != diff:
#             return False

#     return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)