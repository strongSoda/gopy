"""
Binary search is the most popular Search algorithm. It is efficient and also 
one of the most commonly used techniques that is used to solve problems.

If all the names in the world are written down together in order and you want 
to search for the position of a specific name, binary search will accomplish 
this in a maximum of 35 iterations.

Binary search works only on a sorted set of elements. To use binary search on 
a collection, the collection must first be sorted.

When binary search is used to perform operations on a sorted set, the number 
of iterations can always be reduced on the basis of the value that is being 
searched.

### Time complexity

As we dispose off one part of the search case during every step of binary search, 
and perform the search operation on the other half, this results in a worst case 
time complexity of O(log2N).

"""
def search(item,array):
    beg = 0
    end = len(array)
    while(end >= beg):
        mid = beg + ((end - beg)//2)
        # if mid goes out of bound report element not present
        if mid >= len(array):
            break
        if array[mid] > item:
            end = mid - 1
        elif array[mid] < item:
            beg = mid + 1
        else:
            return mid
    return "Not Found"