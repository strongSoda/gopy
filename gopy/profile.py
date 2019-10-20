"""
### Building awesome visualizations for algorithms

Although on paper one algorithm might prove better than other but it's mostly based on nature of order of increase in 
running time with respect to input size.

However, in practice an algorithm having higher runtime complexity than others may actually have a smaller runtime
for your specific test case.

With gopy, you can test each algorithm's behavior for your specific input and test case and compare actual running times in practice.

eg:

# test for knuth_morris_pratt

```python
from gopy.profile import profile
from gopy.strings.knuth_morris_pratt import match 
print(profile('match("ABCDAADDABCABAB","A")'))
```

This will make in depth visualizations in your browser for the kmp algorithm.
"""

import cProfile
import subprocess

def profile(s):
    cProfile.run(s,'test.profile')
    return subprocess.check_output(['snakeviz', 'test.profile'])