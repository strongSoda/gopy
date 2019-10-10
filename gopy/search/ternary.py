"""What is ternary search ?

Similarly like linear search and binary search, ternary search is a searching technique that is used to find the index or position of a particular value in collection of elements.
Ternary search is used only on a sorted collection of elements.

Ternary search, like binary search, is based on divide-and-conquer algorithm.

It is divided into 3 parts (where in binary search 2 parts) and then determines in which part the element exists.
"""

import cProfile
import re

def ternary_search(left_index, right_index, search_key, array):
    if left_index <= right_index:
        mid_index1 = left_index + (right_index - left_index)//3
        mid_index2 = right_index - (right_index - left_index)//3
        # print(mid_index2, mid_index1, left_index, right_index)
        if array[mid_index1] == search_key:
            return mid_index1
        if array[mid_index2] == search_key:
            return mid_index2
        if search_key < array[mid_index1]:
            return ternary_search(left_index, mid_index1-1, search_key, array)
        elif search_key > array[mid_index2]:
            return ternary_search(mid_index2+1, right_index, search_key, array)
        else:
            return ternary_search(mid_index1+1, mid_index2-1, search_key, array)
    return "Not Found"

def search(item,array):
    left_index = 0
    right_index = len(array) - 1
    return ternary_search(left_index, right_index, item, array)

def profile():
    '''profiling input 
    search(10,[0,1,2,3,4,5,6,7,8,9,10])
    '''
    cProfile.run('search(10,[0,1,2,3,4,5,6,7,8,9,10])')
    