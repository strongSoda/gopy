'''
Merge sort is a sorting technique based on divide and conquer technique. With worst-case time 
complexity being Ο(n log n), it is one of the most respected algorithms.

Merge sort first divides the array into equal halves and then combines them in a sorted manner.
### Algorithm

Merge sort keeps on dividing the list into equal halves until it can no more be divided. 
By definition, if it is only one element in the list, it is sorted. Then, merge sort 
combines the smaller sorted lists keeping the new list sorted too.

```
Step 1 − if it is only one element in the list it is already sorted, return.
Step 2 − divide the list recursively into two halves until it can no more be divided.
Step 3 − merge the smaller lists into new list in sorted order.
```

### Pseudocode

We shall now see the pseudocodes for merge sort functions. As our algorithms point out 
two main functions − divide & merge.

Merge sort works with recursion and we shall see our implementation in the same way.

```python
procedure mergesort( var a as array )
   if ( n == 1 ) return a

   var l1 as array = a[0] ... a[n/2]
   var l2 as array = a[n/2+1] ... a[n]

   l1 = mergesort( l1 )
   l2 = mergesort( l2 )

   return merge( l1, l2 )
end procedure

procedure merge( var a as array, var b as array )

   var c as array
   while ( a and b have elements )
      if ( a[0] > b[0] )
         add b[0] to the end of c
         remove b[0] from b
      else
         add a[0] to the end of c
         remove a[0] from a
      end if
   end while
   
   while ( a has elements )
      add a[0] to the end of c
      remove a[0] from a
   end while
   
   while ( b has elements )
      add b[0] to the end of c
      remove b[0] from b
   end while
   
   return c
	
end procedure
```
'''
def merge_sort(array, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge_list(array, start, mid, end)
        return array
        
def merge_list(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1

def sort(array):
    return merge_sort(array, 0, len(array))