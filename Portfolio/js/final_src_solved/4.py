# Solution 1:
def every_second(seq):
    """Yields every second element of seq infinitely many times in succession.

    Args:
    seq -- a sequence

    Yields:
    every second element of seq infinitely many times in succession

    Example:
    >>> g = every_second('abcdef')
    >>> [next(g) for _ in range(12)]
    ['a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e']
    >>> g = every_second('abc')
    >>> [next(g) for _ in range(12)]
    ['a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b']
    >>> g = every_second('ab')
    >>> [next(g) for _ in range(12)]
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    >>> g = every_second('')
    >>> list(g)
    []
    """
    if not seq:
        return

    k = 0

    while True:
        for a in seq:
            if k % 2 == 0:
                yield a
            k += 1


# Solution 2:
# def cycle(seq):
#     if not seq:
#         return

#     while True:
#         for a in seq:
#             yield a


# def every_second(seq):
#     """Yields every second element of seq infinitely many times in succession.

#     Args:
#     seq -- a sequence

#     Yields:
#     every second element of seq infinitely many times in succession

#     Example:
#     >>> g = every_second('abcdef')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e']
#     >>> g = every_second('abc')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b']
#     >>> g = every_second('ab')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
#     >>> g = every_second('')
#     >>> list(g)
#     []
#     """
#     it = cycle(seq)
#     k = 0

#     for a in it:
#         if k % 2 == 0:
#             yield a
#         k += 1


# Solution 3:
# from itertools import cycle


# def every_second(seq):
#     """Yields every second element of seq infinitely many times in succession.

#     Args:
#     seq -- a sequence

#     Yields:
#     every second element of seq infinitely many times in succession

#     Example:
#     >>> g = every_second('abcdef')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e']
#     >>> g = every_second('abc')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b']
#     >>> g = every_second('ab')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
#     >>> g = every_second('')
#     >>> list(g)
#     []
#     """
#     it = cycle(seq)
#     k = 0

#     for a in it:
#         if k % 2 == 0:
#             yield a
#         k += 1

# Class version:
# class EverySecond:
#     """Implements the generator protocol to yield every second element of seq infinitely many times in succession.

#     Args:
#     seq -- a sequence

#     Example:
#     >>> g = EverySecond('abcdef')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e', 'a', 'c', 'e']
#     >>> g = EverySecond('abc')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b', 'a', 'c', 'b']
#     >>> g = EverySecond('ab')
#     >>> [next(g) for _ in range(12)]
#     ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
#     >>> g = EverySecond('')
#     >>> list(g)
#     []
#     """
    
#     def __init__(self, seq):
#         self.seq = seq
#         self.k = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if not self.seq:
#             raise StopIteration

#         value = self.seq[self.k]
#         self.k = (self.k + 2) % len(self.seq)
#         return value

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)