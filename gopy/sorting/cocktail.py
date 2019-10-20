"""
Cocktail sort is the variation of Bubble Sort which traverses the list in both 
directions alternatively. It is different from bubble sort in the sense that, 
bubble sort traverses the list in forward direction only, while this algorithm 
traverses in forward as well as backward direction in one iteration.

### Algorithm

In cocktail sort, one iteration consists of two stages:

- The first stage loop through the array like bubble sort from left to right. The adjacent elements are compared and if left element is greater than the right element, then we swap those elements. The largest element of the list is placed at the end of the array in the forward pass.
- The second stage loop through the array from the right most unsorted element to the left. The adjacent elements are compared and if right element is smaller than the left element then, we swap those elements. The smallest element of the list is placed at the beginning of the array in backward pass.

The process continues until the list becomes unsorted.

### Complexity

#### Best Case	
**Time Complexity**	        O(n2)

#### Average Case
**Time Complexity**	        O(n2)

#### Worst Case
**Time Complexity**	        O(n2)

**Space Complexity**	    O(1) 

"""
def cocktail_shaker_sort(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]
 
    upper = len(array) - 1
    lower = 0
 
    no_swap = False
    while (not no_swap and upper - lower > 1):
        no_swap = True
        for j in range(lower, upper):
            if array[j + 1] < array[j]:
                swap(j + 1, j)
                no_swap = False
        upper = upper - 1
 
        for j in range(upper, lower, -1):
            if array[j - 1] > array[j]:
                swap(j - 1, j)
                no_swap = False
        lower = lower + 1
    return array

def sort(array):
    return cocktail_shaker_sort(array)