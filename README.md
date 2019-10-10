## Python Data Structures and Algorithms

- [Installation](install)
- [Usage](usage)
- [For Education](for-education)
- [For Analysis](for-analysis)
- [List of Implementations](list-of-implementations)
- [Contribute](contribute)
- [Support](support)

### Install

```bash
pip3 install gopy
```

or

```bash
pip install gopy
```

### Usage

You can test this by making a python file `test.py`

**Example:** Bubble Sort

```python
from gopy.sorting import bubble
print(bubble.sort([5,4,3,2,1]))
```

Output: 

```bash
[1,2,3,4,5]
```

**Example:** Linear Search

```python
from gopy.search import lsearch
print(lsearch.search(3,[5,4,3,2,1]))
```

Output: 

```bash
2
```

**Example:** Binary Search

```python
from gopy.search import bsearch
print(bsearch.search(30,[5,4,3,2,1]))
```

Output: 

```bash
Not Found
```

### For Education

This library can be used for production software as well as for educational purposes.

**Example:** Learn Quick Sort

```python
import gopy.sorting.quick as quick
print(quick.__doc__)
```

Output: 

```markdown
Quick Sort Implementation
Takes in an array & returns the sorted array

## Documentation

**Task**

Sort an array (or list) elements using the   quicksort   algorithm.

The elements must have a   strict weak order   and the index of the array can be of any discrete type.

For languages where this is not possible, sort an array of integers.


Quicksort, also known as   partition-exchange sort,   uses these steps.

  - Choose any element of the array to be the pivot.
  - Divide all other elements (except the pivot) into two partitions.
  - All elements less than the pivot must be in the first partition.
  - All elements greater than the pivot must be in the second partition.
  - Use recursion to sort both partitions.
  - Join the first sorted partition, the pivot, and the second sorted partition.

The best pivot creates partitions of equal length (or lengths differing by   1).

The worst pivot creates an empty partition (for example, if the pivot is the first or last element of a sorted array).

The run-time of Quicksort ranges from   O(n log n)   with the best pivots, to   O(n2)   with the worst pivots, where   n   is the number of elements in the array.


This is a simple quicksort algorithm, adapted from Wikipedia.

function quicksort(array)
    less, equal, greater := three empty arrays
    if length(array) > 1  
        pivot := select any element of array
        for each x in array
            if x < pivot then add x to less
            if x = pivot then add x to equal
            if x > pivot then add x to greater
        quicksort(less)
        quicksort(greater)
        array := concatenate(less, equal, greater)

A better quicksort algorithm works in place, by swapping elements within the array, to avoid the memory allocation of more arrays.


function quicksort(array)
    if length(array) > 1
        pivot := select any element of array
        left := first index of array
        right := last index of array
        while left ≤ right
            while array[left] < pivot
                left := left + 1
            while array[right] > pivot
                right := right - 1
            if left ≤ right
                swap array[left] with array[right]
                left := left + 1
                right := right - 1
        quicksort(array from first index to right)
        quicksort(array from left to last index)

Quicksort has a reputation as the fastest sort. Optimized variants of quicksort are common features of many languages and libraries. One often contrasts quicksort with   merge sort,   because both sorts have an average time of   O(n log n).

"On average, mergesort does fewer comparisons than quicksort, so it may be better when complicated comparison routines are used. Mergesort also takes advantage of pre-existing order, so it would be favored for using sort() to merge several sorted arrays. On the other hand, quicksort is often faster for small arrays, and on arrays of a few distinct values, repeated many times." — http://perldoc.perl.org/sort.html
Quicksort is at one end of the spectrum of divide-and-conquer algorithms, with merge sort at the opposite end.

Quicksort is a conquer-then-divide algorithm, which does most of the work during the partitioning and the recursive calls. The subsequent reassembly of the sorted partitions involves trivial effort.
Merge sort is a divide-then-conquer algorithm. The partioning happens in a trivial way, by splitting the input array in half. Most of the work happens during the recursive calls and the merge phase.

With quicksort, every element in the first partition is less than or equal to every element in the second partition. Therefore, the merge phase of quicksort is so trivial that it needs no mention!
```

### For Analysis

You can see profiling of all algorithms


**Example:** Analyse ternary search

```python
from gopy.search.ternary import *
print(profile())
```

Output: 

```bash
7 function calls (6 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      2/1    0.000    0.000    0.000    0.000 ternary.py:14(ternary_search)
        1    0.000    0.000    0.000    0.000 ternary.py:31(search)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

*Check input data for profiling*

```python
from gopy.search.ternary import *
print(profile.__doc__)
```

Output: 

```bash
profiling input 
    search(10,[0,1,2,3,4,5,6,7,8,9,10])
```

### List of implementations

- [sorting](/gopy/sorting/)
    - [bubble](/gopy/sorting/bubble.py/)
- [searching](/gopy/search/)
    - [linear search](/gopy/search/lsearch.py/)
    - [binary search](/gopy/search/bsearch.py/)


### Contributing

Any form of contribution is welcome :smile:

### Support

If this project helps you, consider supporting


<a href="https://www.patreon.com/bePatron?u=17066721">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

#### OR 

[Paypal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=P3BP3APA22KEU&source=url)
