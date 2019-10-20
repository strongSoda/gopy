"""
Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data 
into smaller arrays. A large array is partitioned into two arrays one of which holds values 
smaller than the specified value, say pivot, based on which the partition is made and another 
array holds values greater than the pivot value.

Quick sort partitions an array and then calls itself recursively twice to sort the two resulting 
subarrays. This algorithm is quite efficient for large-sized data sets as its average and worst 
case complexity are of Ο(n2), where n is the number of items.

### Quick Sort Algorithm

Using pivot algorithm recursively, we end up with smaller possible partitions. Each partition is 
then processed for quick sort. We define recursive algorithm for quicksort as follows −

```
Step 1 − Make the right-most index value pivot
Step 2 − partition the array using pivot value
Step 3 − quicksort left partition recursively
Step 4 − quicksort right partition recursively
```


### Quick Sort Pivot Algorithm

Based on our understanding of partitioning in quick sort, we will now try to write an algorithm for 
it, which is as follows.

```
Step 1 − Choose the highest index value has pivot

Step 2 − Take two variables to point left and right 
         of the list excluding pivot

Step 3 − left points to the low index

Step 4 − right points to the high

Step 5 − while value at left is less than pivot move 
         right

Step 6 − while value at right is greater than pivot
         move left

Step 7 − if both step 5 and step 6 does not match 
         swap left and right

Step 8 − if left ≥ right, the point where they met 
         is new pivot
```

"""
def quicksort(array, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(array, start, end)
        quicksort(array, start, p)
        quicksort(array, p + 1, end)
    return array 

def partition(array, start, end):
    pivot = array[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and array[i] <= pivot):
            i = i + 1
        while (i <= j and array[j] >= pivot):
            j = j - 1
 
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            array[start], array[j] = array[j], array[start]
            return j

def sort(array):
    return quicksort(array, 0, len(array))