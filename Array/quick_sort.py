# Quick sort algorithm

def partition(arr, starting_index, ending_index):
    i = starting_index - 1         # index of smaller element
    pivot = arr[ending_index]     # pivot
 
    for j in range(starting_index, ending_index):
        if arr[j] <= pivot: # if current element is <= to pivot
         
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[ending_index] = arr[ending_index], arr[i + 1]
    return (i + 1)
 
def quickSort(arr, starting_index, ending_index):
    if starting_index < ending_index:
        p = partition(arr,starting_index, ending_index)
        quickSort(arr, starting_index, p - 1)
        quickSort(arr, p + 1, ending_index)
