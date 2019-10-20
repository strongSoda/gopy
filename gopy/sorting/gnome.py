"""
The simplest sort algorithm is not Bubble Sort..., it is not Insertion Sort..., it's Gnome Sort!

Gnome Sort is based on the technique used by the standard Dutch Garden Gnome (Du.: tuinkabouter). 
Here is how a garden gnome sorts a line of flower pots. 

Basically, he looks at the flower pot 
next to him and the previous one; if they are in the right order he steps one pot forward, 
otherwise he swaps them and steps one pot backwards. Boundary conditions: if there is no 
previous pot, he steps forwards; if there is no pot next to him, he is done.

### Psuedocode
```
void gnomesort(int n, int ar[]) {
	int i = 0;
	
	while (i < n) {
		if (i == 0 || ar[i-1] <= ar[i]) i++;
		else {int tmp = ar[i]; ar[i] = ar[i-1]; ar[--i] = tmp;}
	}
}
```
"""
def gnome_sort(array):
    for pos in range(1, len(array)):
        while (pos != 0 and array[pos] < array[pos - 1]):
            array[pos], array[pos - 1] = array[pos - 1], array[pos]
            pos = pos - 1
    return array
    
def sort(array):
    return gnome_sort(array)