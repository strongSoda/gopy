"""
Radix sort is a small method that many people intuitively use when alphabetizing a large list 
of names. Specifically, the list of names is first sorted according to the first letter of 
each name, that is, the names are arranged in 26 classes.

Intuitively, one might want to sort numbers on their most significant digit. However, Radix 
sort works counter-intuitively by sorting on the least significant digits first. On the first 
pass, all the numbers are sorted on the least significant digit and combined in an array. 
Then on the second pass, the entire numbers are sorted again on the second least significant 
digits and combined in an array and so on.

### Algorithm: 

```
Radix-Sort (list, n) 
shift = 1 
for loop = 1 to keysize do 
   for entry = 1 to n do 
      bucketnumber = (list[entry].key / shift) mod 10 
      append (bucket[bucketnumber], list[entry]) 
   list = combinebuckets() 
   shift = shift * 10 
```

### Analysis
Each key is looked at once for each digit (or letter if the keys are alphabetic) of the longest 
key. Hence, if the longest key has m digits and there are n keys, radix sort has order O(m.n).

However, if we look at these two values, the size of the keys will be relatively small when 
compared to the number of keys. For example, if we have six-digit keys, we could have a 
million different records.

Here, we see that the size of the keys is not significant, and this algorithm is of linear 
complexity O(n).
"""
def radix_sort(array, base=10):
    if array == []:
        return
 
    def key_factory(digit, base):
        def key(array, index):
            return ((array[index]//(base**digit)) % base)
        return key
    largest = max(array)
    exp = 0
    while base**exp <= largest:
        array = counting_sort(array, base - 1, key_factory(exp, base))
        exp = exp + 1
    return array
 
def counting_sort(array, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(array)):
        c[key(array, i)] = c[key(array, i)] + 1
 
    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(array)
    for i in range(len(array) - 1, -1, -1):
        result[c[key(array, i)]] = array[i]
        c[key(array, i)] = c[key(array, i)] - 1
 
    return result

def sort(array):
    return radix_sort(array)