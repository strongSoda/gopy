"""Comb Sort Implementation
Takes in an array & returns the sorted array
"""
def comb_sort(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]
 
    gap = len(array)
    shrink = 1.3
 
    no_swap = False
    while not no_swap:
        gap = int(gap/shrink)
 
        if gap < 1:
            gap = 1
            no_swap = True
        else:
            no_swap = False
 
        i = 0
        while i + gap < len(array):
            if array[i] > array[i + gap]:
                swap(i, i + gap)
                no_swap = False
            i = i + 1
    return array

def sort(array):
    return comb_sort(array)