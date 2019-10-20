"""
Counting sort is an efficient algorithm for sorting an array of elements that each have 
a nonnegative integer key, for example, an array, sometimes called a list, of positive 
integers could have keys that are just the value of the integer as the key, or a list 
of words could have keys assigned to them by some scheme mapping the alphabet to 
integers (to sort in alphabetical order, for instance). 

Unlike other sorting algorithms, 
such as mergesort, counting sort is an integer sorting algorithm, not a comparison based 
algorithm. 

While any comparison based sorting algorithm requires Omega(nlgn)Ω(nlgn) 
comparisons, counting sort has a running time of Theta(n)Θ(n) when the length of the 
input list is not much smaller than the largest key value, kk, in the list. Counting 
sort can be used as a subroutine for other, more powerful, sorting algorithms such as 
radix sort

### Complexity of Counting Sort

Counting sort has a O(k+n)O(k+n) running time.

The first loop goes through A, which has n elements. This step has a O(n)O(n) running 
time. The second loop iterates over k, so this step has a running time of O(k)O(k). The 
third loop iterates through AA, so again, this has a running time of O(n)O(n). Therefore, 
the counting sort algorithm has a running time of O(k+n)O(k+n).

Counting sort is efficient if the range of input data, kk, is not significantly greater 
than the number of objects to be sorted, nn.

Counting sort is a stable sort with a space complexity of **O(k + n)O(k+n).**
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