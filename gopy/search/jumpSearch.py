"""Jump Search Implementation
Takes in an item & array & returns the indeitem of match
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