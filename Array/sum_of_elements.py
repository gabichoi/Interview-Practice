Returns True if any two non identical elements in lst add up to n

def add_up(n, lst):
    
    """
    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    >>> add_up(151, range(0, 200000, 2))
    False
    >>> timeit(lambda: add_up(151, range(0, 200000, 2))) < 1.0
    True
    >>> add_up(50002, range(0, 200000, 2))
    True

    """

    new_lst = set(lst)
    if len(new_lst) == 1 and n not in new_lst:
        return False 
    else:
        i = 0
        while i in range (len(lst)):
            if (n - lst[i]) in new_lst:
                return True
            i += 1
        return False
