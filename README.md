## Python Data Structures and Algorithms

[![GitHub issues](https://img.shields.io/github/issues/strongSoda/gopy?style=flat-square)](https://github.com/strongSoda/gopy/issues)  [![GitHub forks](https://img.shields.io/github/forks/strongSoda/gopy?style=flat-square)](https://github.com/strongSoda/gopy/network) [![GitHub stars](https://img.shields.io/github/stars/strongSoda/gopy?style=flat-square)](https://github.com/strongSoda/gopy/stargazers) [![GitHub license](https://img.shields.io/github/license/strongSoda/gopy?style=flat-square)](https://github.com/strongSoda/gopy/blob/master/LICENSE.txt) [![PayPal](https://img.shields.io/badge/PayPal-Donate-blue)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=P3BP3APA22KEU&source=url)

**One utility** to get all the algorithms fast and ready into your project, analyze their **visualizations** for your specific test case (not nature of increase but actual running time) and **study** their implementation for academic purposes. :+1:

<p align="center">
  <img width="560" height="300" src="https://media.giphy.com/media/ehgT3wyRUxAnylAzXW/giphy.gif">
</p

This library is under active development. :star: Star the repo for updates.

- [Installation](#install)
- [Usage](#usage)
- [Api Docs](#api-docs)
- [For Analysis](#for-analysis)
- [List of Implementations](#list-of-implementations)
- [Contribute](#contribute)
- [Support](#support)

### Api Docs

Read the full doumentation here [API Docs](https://strongsoda.github.io/gopy/)

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

### For Analysis

#### Building awesome visualizations for algorithms

Although on paper one algorithm might prove better than other but it's mostly based on nature of order of increase in 
running time with respect to input size.
However, in practice an algorithm having higher runtime complexity than others may actually have a smaller runtime
for your specific test case.
With gopy, you can test each algorithm's behavior for your specific input and test case and compare actual running times in practice.

eg:

**test for knuth_morris_pratt**

```python
from gopy.profile import profile
from gopy.strings.knuth_morris_pratt import match 
print(profile('match("ABCDAADDABCABAB","A")'))
```
This will make in depth visualizations in your browser for the kmp algorithm.

<p align="center">
  <img width="760" height="400" src="https://media.giphy.com/media/ehgT3wyRUxAnylAzXW/giphy.gif">
</p

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
