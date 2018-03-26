# Given a list, returns it sorted. Merge sort algorithm

def mergesort(seq):

    """
    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]

    """ 
    if seq == []:
        return []
    elif len(seq) == 1:
        return seq 
    else:
        mid = (len(seq) // 2)
        first_half = seq[0 : mid]
        second_half = seq[mid : len(seq)]
        return merge (mergesort(first_half), mergesort(second_half))
