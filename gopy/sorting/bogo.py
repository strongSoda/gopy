"""
BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or 
monkey sort is a particularly ineffective algorithm based on generate and test 
paradigm. The algorithm successively generates permutations of its input until 
it finds one that is sorted.

Bogosort simply shuffles a collection randomly until it is sorted.

"Bogosort" is a perversely inefficient algorithm only used as an in-joke.

### Complexity:

Its average run-time is   O(n!)   because the chance that any given shuffle of a set will end up in sorted order is about one in   n   factorial,   and the worst case is infinite since there's no guarantee that a random shuffling will ever produce a sorted sequence.

Its best case is   O(n)   since a single pass through the elements may suffice to order them.


### Pseudocode:

```
while not InOrder(list) do
   Shuffle(list)
done
```
"""
import random
 
def bogosort(l):
    while not in_order(l):
        random.shuffle(l) # throw all elements
    return l
 
"""
For example, if bogosort is used to sort a deck of cards, it would consist of 
checking if the deck were in order, and if it were not, one would throw the 
deck into the air, pick the cards up at random, and repeat the process until 
the deck is sorted.
"""

def in_order(l):
    if not l:
        return True
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True


"""
### Complexity

- Worst case time complexity: O((N+1)!)
- Average case time complexity: O((N+1)!)
- Best case time complexity: O(N)
- Space complexity: O(1)

"""

def sort(array):
    return bogosort(array)
