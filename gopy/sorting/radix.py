"""Radix Sort Implementation
Takes in an array & returns the sorted array
"""
def radix_sort(array, base=10):
    if array == []:
        return
 
    def key_factory(digit, base):
        def key(array, index):
            return ((array[index]//(base**digit)) % base)
        return key
    largest = max(array)
    exp = 0
    while base**exp <= largest:
        array = counting_sort(array, base - 1, key_factory(exp, base))
        exp = exp + 1
    return array
 
def counting_sort(array, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(array)):
        c[key(array, i)] = c[key(array, i)] + 1
 
    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(array)
    for i in range(len(array) - 1, -1, -1):
        result[c[key(array, i)]] = array[i]
        c[key(array, i)] = c[key(array, i)] - 1
 
    return result

def sort(array):
    return radix_sort(array)