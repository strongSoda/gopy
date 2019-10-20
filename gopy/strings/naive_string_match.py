'''
The naïve approach tests all the possible placement of Pattern P [1.......m] relative 
to text T [1......n]. We try shift s = 0, 1.......n-m, successively and for each shifts. 
Compare T [s+1.......s+m] to P [1......m].

The naïve algorithm finds all valid shifts using a loop that checks the condition 
P[1.......m] = T [s+1.......s+m] for each of the n - m +1 possible value of s.

```
NAIVE-STRING-MATCHER (T, P)
 1. n ← length [T]
 2. m ← length [P]
 3. for s ← 0 to n -m
 4. do if P [1.....m] = T [s + 1....s + m]
 5. then print "Pattern occurs with shift" s
```

### Analysis: 

This for loop from 3 to 5 executes for n-m + 1(we need at least m characters at 
the end) times and in iteration we are doing m comparisons. So the total complexity is 
O (n-m+1).
'''
def match(text,pat):
    m = len(text)
    n = len(pat)
    pos = []
    for i in range(m-(n-1)):
        if text[i:i+n] == pat:
            pos.append(i)
    if len(pos):
        return pos
    else:
        return "No Match Found"
