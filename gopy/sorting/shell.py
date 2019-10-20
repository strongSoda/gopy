"""
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. 
This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to 
the far right and has to be moved to the far left.

This algorithm uses insertion sort on a widely spread elements, first to sort them and then 
sorts the less widely spaced elements. This spacing is termed as interval. This interval is 
calculated based on Knuth's formula as −

Knuth's Formula
h = h * 3 + 1
where −
   h is interval with initial value 1

This algorithm is quite efficient for medium-sized data sets as its average and worst-case 
complexity of this algorithm depends on the gap sequence the best known is Ο(n), where n is 
the number of items. And the worst case space complexity is O(n).

### Algorithm

Following is the algorithm for shell sort.

```
Step 1 − Initialize the value of h
Step 2 − Divide the list into smaller sub-list of equal interval h
Step 3 − Sort these sub-lists using insertion sort
Step 3 − Repeat until complete list is sorted
```

### Pseudocode

Following is the pseudocode for shell sort.

```python
procedure shellSort()
   A : array of items 
	
   /* calculate interval*/
   while interval < A.length /3 do:
      interval = interval * 3 + 1	    
   end while
   
   while interval > 0 do:

      for outer = interval; outer < A.length; outer ++ do:

      /* select value to be inserted */
      valueToInsert = A[outer]
      inner = outer;

         /*shift element towards right*/
         while inner > interval -1 && A[inner - interval] >= valueToInsert do:
            A[inner] = A[inner - interval]
            inner = inner - interval
         end while

      /* insert the number at hole position */
      A[inner] = valueToInsert

      end for

   /* calculate interval*/
   interval = (interval -1) /3;	  

   end while
   
end procedure
```
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