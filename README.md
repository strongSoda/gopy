## Python Data Structures and Algorithms

### Install

```bash
pip3 install gopy
```

or

```bash
pip install gopy
```

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
