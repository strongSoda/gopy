"""Counting Sort Implementation
Takes in an array & returns the sorted array
"""
def counting_sort(array, largest):
    c = [0]*(largest + 1)
    for i in range(len(array)):
        c[array[i]] = c[array[i]] + 1
 
    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(array)
 
    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    for x in reversed(array):
        result[c[x]] = x
        c[x] = c[x] - 1
 
    return result

def sort(array):
    return counting_sort(array, max(array))