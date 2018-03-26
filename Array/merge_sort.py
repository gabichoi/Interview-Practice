# Merge sort algorithm

def merge_sort(arr):

    """
    >>> merge_sort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> merge_sort([])     # sorting an empty list
    []
    >>> merge_sort([1])   # sorting a one-element list
    [1]

    """ 
    if arr == []:
        return []
    elif len(arr) == 1:
        return arr 
    else:
        mid = (len(arr) // 2)
        first_half = arr[0 : mid]
        second_half = arr[mid : len(arr)]
        return merge (mergesort(first_half), mergesort(second_half))
