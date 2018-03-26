# Insertion sort algorithm

def insertion_sort(arr):

    """
    insertion_sort([7, 4, 9, 5])
    [7, 4, 9, 5]
    [7, 4, 9, 5]
    [4, 7, 9, 5]
    [4, 7, 9, 5]
    [4, 5, 7, 9]

    """

    size = len(arr)

    for i in range(1, size):
        item = arr[i]
        j = i - 1 # previous 
        while 0 <= j and item < arr[j]: # while current is less than previous
            # current item = previous item
            arr[j + 1] = arr[j]
            j -= 1
        # copy the value which was at ith index to its correct sorted position
        arr[j + 1] = item
