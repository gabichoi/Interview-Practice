# Selection sort algorithm

def selection_sort(arr):

    """
    selection_sort([23, 42, 4, 16])
    [23, 42, 4, 16]
    [4, 42, 23, 16]
    [4, 42, 23, 16]
    [4, 16, 23, 42]
    
    """
    
    def selection_sort(arr):
    size = len(arr)
    for i in range(0, size):
        for j in range(i + 1, size):
            if arr[i] > arr[j]: # if the value at i is > value at j 
                arr[i], arr[j] = arr[j], arr[i] # swap


