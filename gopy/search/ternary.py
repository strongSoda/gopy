"""Like linear search and binary search, ternary search is a searching
technique that is used to determine the position of a specific value in an
array. In binary search, the sorted array is divided into two parts while in
ternary search, it is divided into 3 parts and then you determine in which part
the element exists.

Ternary search, like binary search, is a divide-and-conquer algorithm. It is mandatory
for the array (in which you will search for an element) to be sorted before you begin
the search. In this search, after each iteration it neglects ⅓ part of the array and
repeats the same operations on the remaining ⅔.

### Psuedo Code

```
int ternary_search(int l,int r, int x)
{
    if(r>=l)
    {
        int mid1 = l + (r-l)/3;
        int mid2 = r -  (r-l)/3;
        if(ar[mid1] == x)
            return mid1;
        if(ar[mid2] == x)
            return mid2;
        if(x<ar[mid1])
            return ternary_search(l,mid1-1,x);
        else if(x>ar[mid2])
            return ternary_search(mid2+1,r,x);
        else
            return ternary_search(mid1+1,mid2-1,x);

    }
    return -1;
}
```

### Complexity

O(log3N) , where N is the size of the array
"""


def ternary_search(left_index, right_index, search_key, array):
    if left_index <= right_index:
        mid_index1 = left_index + (right_index - left_index)//3
        mid_index2 = right_index - (right_index - left_index)//3
        # print(mid_index2, mid_index1, left_index, right_index)
        if array[mid_index1] == search_key:
            return mid_index1
        if array[mid_index2] == search_key:
            return mid_index2
        if search_key < array[mid_index1]:
            return ternary_search(left_index, mid_index1-1, search_key, array)
        elif search_key > array[mid_index2]:
            return ternary_search(mid_index2+1, right_index, search_key, array)
        else:
            return ternary_search(mid_index1+1, mid_index2-1, search_key, array)
    return "Not Found"

def search(item,array):
    left_index = 0
    right_index = len(array) - 1
    return ternary_search(left_index, right_index, item, array)
