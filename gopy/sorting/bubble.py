"""
Bubble Sort is a simple algorithm which is used to sort a given set of n elements 
provided in form of an array with n number of elements. Bubble Sort compares all 
the element one by one and sort them based on their values.

If the given array has to be sorted in ascending order, then bubble sort will start 
by comparing the first element of the array with the second element, if the first 
element is greater than the second element, it will swap both the elements, and then 
move on to compare the second and the third element, and so on.

If we have total n elements, then we need to repeat this process for n-1 times.

It is known as bubble sort, because with every complete iteration the largest element 
in the given array, bubbles up towards the last place or the highest index, just like 
a water bubble rises up to the water surface.

Sorting takes place by stepping through all the elements one-by-one and comparing it 
with the adjacent element and swapping them if required.

### Implementing Bubble Sort Algorithm

Following are the steps involved in bubble sort(for sorting a given array in ascending order):

- Starting with the first element(index = 0), compare the current element with the next element of the array.
- If the current element is greater than the next element of the array, swap them.
- If the current element is less than the next element, move to the next element. Repeat Step 1.

### Following are the Time and Space complexity for the Bubble Sort algorithm.

- Worst Case Time Complexity [ Big-O ]: O(n2)
- Best Case Time Complexity [Big-omega]: O(n)
- Average Time Complexity [Big-theta]: O(n2)
- Space Complexity: O(1)

"""
def sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1,i,-1):
            if array[j] < array[j-1]:
                array[j-1], array[j] = array[j], array[j-1]
        
    return array