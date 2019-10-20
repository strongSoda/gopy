"""
### Longest Common Subsequence

If a set of sequences are given, the longest common subsequence problem is to find a common subsequence of all the sequences that is of maximal length.

The longest common subsequence problem is a classic computer science problem, the basis of data comparison programs such as the diff-utility, and has applications in bioinformatics. It is also widely used by revision control systems, such as SVN and Git, for reconciling multiple changes made to a revision-controlled collection of files.

### Naïve Method

Let X be a sequence of length m and Y a sequence of length n. Check for every subsequence of X whether it is a subsequence of Y, and return the longest common subsequence found.

There are 2m subsequences of X. Testing sequences whether or not it is a subsequence of Y takes O(n) time. Thus, the naïve algorithm would take O(n2m) time.

### Dynamic Programming

Let X = < x1, x2, x3,…, xm > and Y = < y1, y2, y3,…, yn > be the sequences. To compute the length of an element the following algorithm is used.

In this procedure, table C[m, n] is computed in row major order and another table B[m,n] is computed to construct optimal solution.

### Algorithm:

```
LCS-Length-Table-Formulation (X, Y)
m := length(X) 
n := length(Y) 
for i = 1 to m do 
   C[i, 0] := 0 
for j = 1 to n do 
   C[0, j] := 0 
for i = 1 to m do 
   for j = 1 to n do 
      if xi = yj 
         C[i, j] := C[i - 1, j - 1] + 1 
         B[i, j] := ‘D’ 
      else 
         if C[i -1, j] ≥ C[i, j -1] 
            C[i, j] := C[i - 1, j] + 1 
            B[i, j] := ‘U’ 
         else 
         C[i, j] := C[i, j - 1]
         B[i, j] := ‘L’ 
return C and B
```

### Analysis

To populate the table, the outer for loop iterates m times and the inner for loop iterates n times. Hence, the complexity of the algorithm is O(m, n), where m and n are the length of two strings.
"""
def lcs(x,y):
    m= len(x)
    n= len(y)
    # print(m,n)
    k = [[0 for i in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 or y==0:
                # print(i,j)
                k[i][j] = 0
            if x[i-1]==y[j-1]:
                k[i][j] = 1+k[i-1][j-1]
            else:
                k[i][j] = max(k[i-1][j], k[i][j-1])
    
    return k[m-1][n-1]