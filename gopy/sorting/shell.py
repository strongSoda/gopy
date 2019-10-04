"""Shell Sort Implementation
Takes in an array & returns the sorted array
"""
def gaps(size):
    # uses the gap sequence 2^k - 1: 1, 3, 7, 15, 31, ...
    length = size.bit_length()
    for k in range(length - 1, 0, -1):
        yield 2**k - 1
 
 
def shell_sort(array):
    def insertion_sort_with_gap(gap):
        for i in range(gap, len(array)):
            temp = array[i]
            j = i - gap
            while (j >= 0 and temp < array[j]):
                array[j + gap] = array[j]
                j = j - gap
            array[j + gap] = temp
 
    for g in gaps(len(array)):
        insertion_sort_with_gap(g)
    
    return array

def sort(array):
    return shell_sort(array)