"""
BogoSort also known as permutation sort, stupid sort, slow sort, shotgun sort or 
monkey sort is a particularly ineffective algorithm based on generate and test 
paradigm. The algorithm successively generates permutations of its input until 
it finds one that is sorted.

For example, if bogosort is used to sort a deck of cards, it would consist of 
checking if the deck were in order, and if it were not, one would throw the 
deck into the air, pick the cards up at random, and repeat the process until 
the deck is sorted.

### Complexity

- Worst case time complexity: O((N+1)!)
- Average case time complexity: O((N+1)!)
- Best case time complexity: O(N)
- Space complexity: O(1)

"""
import random
 
def bogosort(l):
    while not in_order(l):
        random.shuffle(l)
    return l
 
def in_order(l):
    if not l:
        return True
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True

def sort(array):
    return bogosort(array)
