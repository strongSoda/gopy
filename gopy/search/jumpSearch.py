"""
Jump search technique also works for ordered lists. It creates a block and 
tries to find the element in that block. If the item is not in the block, 
it shifts the entire block. The block size is based on the size of the list. 
If the size of the list is n then block size will be √n. 

After finding a correct block it finds the item using a linear search technique. The jump 
search lies between linear search and binary search according to its performance.

### The complexity of Jump Search Technique

- Time Complexity: O(√n)

- Space Complexity: O(1)

### Input and Output

```
Input: 

A sorted list of data:
10 13 15 26 28 50 56 88 94 127 159 356 480 567 689 699 780 850 956 995
The search key 356

Output: 

Item found at location: 11
```

### Algorithm

```
jumpSearch(array, size, key)

Input: An sorted array, size of the array and the search key

Output: location of the key (if found), otherwise wrong location.

Begin
   blockSize := √size
   start := 0
   end := blockSize
   while array[end] <= key AND end < size do
      start := end
      end := end + blockSize
      if end > size – 1 then
         end := size
   done
   for i := start to end -1 do
      if array[i] = key then
         return i
   done
   return invalid location
End
```
"""

import math 
  
def search( x , arr ): 
    n = len(arr)
    # Finding block size to be jumped 
    step = int(math.sqrt(n)) 
      
    # Finding the block where element is 
    # present (if it is present) 
    prev = 0
    while arr[int(min(step, n)-1)] < x: 
        prev = step 
        step += int(math.sqrt(n)) 
        if prev >= n: 
            return "Not Found"
      
    # Doing a linear search for x in  
    # block beginning with prev. 
    while arr[int(prev)] < x: 
        prev += 1
          
        # If we reached next block or end  
        # of array, element is not present. 
        if prev == min(step, n): 
            return "Not Found"
      
    # If element is found 
    if arr[int(prev)] == x: 
        return prev 
      
    return "Not Found"