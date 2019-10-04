"""Gnome Sort Implementation
Takes in an array & returns the sorted array
"""
def gnome_sort(array):
    for pos in range(1, len(array)):
        while (pos != 0 and array[pos] < array[pos - 1]):
            array[pos], array[pos - 1] = array[pos - 1], array[pos]
            pos = pos - 1
    return array
    
def sort(array):
    return gnome_sort(array)