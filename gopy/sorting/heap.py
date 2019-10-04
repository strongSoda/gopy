"""Heap Sort Implementation
Takes in an array & returns the sorted array
"""
def heapsort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, index=0, size=i)
    return array
    
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(array):
    length = len(array)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(array, index=start, size=length)
        start = start - 1
 
def max_heapify(array, index, size):
    l = left(index)
    r = right(index)
    if (l < size and array[l] > array[index]):
        largest = l
    else:
        largest = index
    if (r < size and array[r] > array[largest]):
        largest = r
    if (largest != index):
        array[largest], array[index] = array[index], array[largest]
        max_heapify(array, largest, size)

def sort(array):
    return heapsort(array)