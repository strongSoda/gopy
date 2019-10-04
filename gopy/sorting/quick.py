"""Quick Sort Implementation
Takes in an array & returns the sorted array
"""
def quicksort(array, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(array, start, end)
        quicksort(array, start, p)
        quicksort(array, p + 1, end)
    return array 
 
def partition(array, start, end):
    pivot = array[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and array[i] <= pivot):
            i = i + 1
        while (i <= j and array[j] >= pivot):
            j = j - 1
 
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            array[start], array[j] = array[j], array[start]
            return j

def sort(array):
    return quicksort(array, 0, len(array))