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
    - [bubble](/gopy/sorting/bubble/)
- [searching](/gopy/search/)
    - [linear search](/gopy/search/lsearch/)
    - [binary search](/gopy/search/bsearch/)


### Contributing

Any form of contribution is welcome :smile:

### Support

If this project helps you, consider supporting

<a href="https://www.patreon.com/bePatron?u=17066721" data-patreon-widget-type="become-patron-button">Become a Patron!</a><script async src="https://c6.patreon.com/becomePatronButton.bundle.js"></script>

#### OR 

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick" />
<input type="hidden" name="hosted_button_id" value="P3BP3APA22KEU" />
<input type="image" src="https://www.paypalobjects.com/en_GB/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_IN/i/scr/pixel.gif" width="1" height="1" />
</form>
