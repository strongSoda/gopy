"""
Linear search is used on a collections of items. It relies on the technique of 
traversing a list from start to end by exploring properties of all the elements 
that are found on the way.

For example, consider an array of integers of size N. You should find and print 
the position of all the elements with value x. Here, the linear search is based 
on the idea of matching each element from the beginning of the list to the end 
of the list with the integer x, and then printing the position of the element 
if the condition is `True`.

### Psuedo Code:

The pseudo code for this example is as follows :

```
for(start to end of array)
{
    if (current_element equals to 5)  
    {
        print (current_index);
    }
}
```

### Time Complexity:

The time complexity of the linear search is 
O(N) because each element in an array is compared only once.

"""

def search(item,array):
	for i in range(len(list(array))):
		if array[i] == item:
			return i
	return "Not Found"