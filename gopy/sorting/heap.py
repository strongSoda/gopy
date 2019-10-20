"""
Heaps can be used in sorting an array. In max-heaps, maximum element will always be 
at the root. Heap Sort uses this property of heap to sort the array.

Consider an array Arr which is to be sorted using Heap Sort.

- Initially build a max heap of elements in Arr.The root element, that is Arr[1], will 
contain maximum element of Arr. After that, swap this element with the last element of 
- Arr and heapify the max heap excluding the last element which is already in its correct 
position and then decrease the length of heap by one.
- Repeat the step 2, until all the elements are in their correct position.

### Psuedocode:

```
void heap_sort(int Arr[ ])

{
    int heap_size = N;

    build_maxheap(Arr);
    for(int i = N; i >= 2 ; i-- )
    {
        swap|(Arr[ 1 ], Arr[ i ]);
        heap_size = heap_size - 1;
        max_heapify(Arr, 1, heap_size);
    }
}
```

### Complexity:

`max_heapify` has complexity `O(logN)`, `build_maxheap` has complexity `O(N)` and we run `max_heapify` 
`N−1` times in `heap_sort` function, therefore complexity of `heap_sort` function is `O(NlogN)`.
"""
def heapsort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, index=0, size=i)
    return array
    
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(array):
    length = len(array)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(array, index=start, size=length)
        start = start - 1
 
def max_heapify(array, index, size):
    l = left(index)
    r = right(index)
    if (l < size and array[l] > array[index]):
        largest = l
    else:
        largest = index
    if (r < size and array[r] > array[largest]):
        largest = r
    if (largest != index):
        array[largest], array[index] = array[index], array[largest]
        max_heapify(array, largest, size)

def sort(array):
    return heapsort(array)