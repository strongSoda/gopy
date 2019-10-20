"""
### What is Bucket Sort ?

Bucket sort is a comparison sort algorithm that operates on elements by dividing 
them into different buckets and then sorting these buckets individually. Each 
bucket is sorted individually using a separate sorting algorithm or by applying 
the bucket sort algorithm recursively. Bucket sort is mainly useful when the 
input is uniformly distributed over a range.

#### Assume one has the following problem in front of them:

One has been given a large array of floating point integers lying uniformly 
between the lower and upper bound. This array now needs to be sorted. A simple 
way to solve this problem would be to use another sorting algorithm such as Merge 
sort, Heap Sort or Quick Sort. However, these algorithms guarantee a best case 
time complexity of O(NlogN). However, using bucket sort, the above task can be 
completed in O(N) time.

#### Psuedo Code 

```
void bucketSort(float[] a,int n)
{
    for(each floating integer 'x' in n)
    {
        insert x into bucket[n*x]; 
    }
    for(each bucket)
    {
        sort(bucket);
    }
}
```

### Time Complexity:

If one assumes that insertion in a bucket takes O(1) time, then steps 1 and 2 of the 
above algorithm clearly take O(n) time.

"""
def bucket_sort(array):
    largest = max(array)
    length = len(array)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(array[i]/size)
        if j != length:
            buckets[j].append(array[i])
        else:
            buckets[length - 1].append(array[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp

def sort(array):
    return bucket_sort(array)