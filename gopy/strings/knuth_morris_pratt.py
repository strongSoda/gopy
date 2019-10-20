"""Knuth-Morris and Pratt introduce a linear time algorithm for the string
matching problem. A matching time of O (n) is achieved by avoiding comparison
with an element of 'S' that have previously been involved in comparison with
some element of the pattern 'p' to be matched. i.e., backtracking on the string
'S' never occurs.

### Components of KMP Algorithm:

#### 1. The Prefix Function (Π): 

The Prefix Function, Π for a pattern encapsulates knowledge
about how the pattern matches against the shift of itself. This information can be used
to avoid a useless shift of the pattern 'p.' In other words, this enables avoiding
backtracking of the string 'S.'

#### 2. The KMP Matcher:

With string 'S,' pattern 'p' and prefix function 'Π' as inputs, find
the occurrence of 'p' in 'S' and returns the number of shifts of 'p' after which occurrences
are found.

### The Prefix Function (Π)

Following pseudo code compute the prefix function, Π:

```
COMPUTE- PREFIX- FUNCTION (P)
 1. m ←length [P]               //'p' pattern to be matched
 2. Π [1] ← 0
 3. k ← 0
 4. for q ← 2 to m
 5. do while k > 0 and P [k + 1] ≠ P [q]
 6. do k ← Π [k]
 7. If P [k + 1] = P [q]
 8. then k← k + 1
 9. Π [q] ← k
 10. Return Π
```

### Running Time Analysis:

In the above pseudo code for calculating the prefix function, the for loop from step 4 to step
10  runs 'm' times. Step1 to Step3 take constant time. Hence the running time of computing
prefix function is O (m).

### The KMP Matcher:

The KMP Matcher with the pattern 'p,' the string 'S' and prefix function 'Π' as input, finds a
match of p in S. Following pseudo code compute the matching component of KMP algorithm:

```
KMP-MATCHER (T, P)
 1. n ← length [T]
 2. m ← length [P]
 3. Π← COMPUTE-PREFIX-FUNCTION (P)
 4. q ← 0               // numbers of characters matched
 5. for i ← 1 to n      // scan S from left to right
 6. do while q > 0 and P [q + 1] ≠ T [i]
 7. do q ← Π [q]                // next character does not match
 8. If P [q + 1] = T [i]
 9. then q ← q + 1              // next character matches
 10. If q = m                              // is all of p matched?
 11. then print "Pattern occurs with shift" i - m
 12. q ← Π [q]                          // look for the next match
```

### Running Time Analysis:

The for loop beginning in step 5 runs 'n' times, i.e., as long as the length of the string 'S.'
Since step 1 to step 4 take constant times, the running time is dominated by this for the loop.
Thus running time of the matching function is O (n).
"""

def match(txt, pat): 
    M = len(pat) 
    N = len(txt) 
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
    #Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
    i = 0 # index for txt[] 
    pos = []
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
        if j == M: 
            pos.append(i-j)
            j = lps[j-1] 
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    if len(pos):
        return pos
    else:
        return "No Match Found"

def computeLPSArray(pat, M, lps): 
	len = 0 # length of the previous longest prefix suffix 
	lps[0] # lps[0] is always 0 
	i = 1
	while i < M: 
		if pat[i]== pat[len]: 
			len += 1
			lps[i] = len
			i += 1
		else: 
			if len != 0: 
				len = lps[len-1] 
			else: 
				lps[i] = 0
				i += 1