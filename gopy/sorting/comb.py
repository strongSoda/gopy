"""
The basic idea of comb sort and the bubble sort is same. In other words, 
comb sort is an improvement on the bubble sort. In the bubble sorting 
technique, the items are compared with the next item in each phase. But 
for the comb sort, the items are sorted in a specific gap. After completing 
each phase, the gap is decreased. The decreasing factor or the shrink factor 
for this sort is 1.3. It means that after completing each phase the gap is 
divided by 1.3.

### The complexity of Comb Sort Technique

- Time Complexity: O(n log n) for the best case. O(n^2/2^p) (p is a number of increment) 
for average case and O(n^2) for the worst case.

- Space Complexity: O(1)

### Input and Output

```
Input:
A list of unsorted data: 108 96 23 74 12 56 85 42 13 47

Output:
Array before Sorting: 108 96 23 74 12 56 85 42 13 47
Array after Sorting: 12 13 23 42 47 56 74 85 96 108
```

### Algorithm

```
CombSort(array, size)
Input: An array of data, and the total number in the array

Output: The sorted Array

Begin
   gap := size
   flag := true
   while the gap ≠ 1 OR flag = true do
      gap = floor(gap/1.3) //the the floor value after division
      if gap < 1 then
         gap := 1
      flag = false

      for i := 0 to size – gap -1 do
         if array[i] > array[i+gap] then
            swap array[i] with array[i+gap]
            flag = true;
      done
   done
End
```
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