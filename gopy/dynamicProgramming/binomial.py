"""
Computing binomial coefficients is non optimization problem but can be solved using dynamic programming. 

Binomial coefficients are represented by C(n, k) or (nk) and can be used to represent the coefficients of a binomail:
```
(a + b)n  = C(n, 0)an + ... + C(n, k)an-kbk + ... + C(n, n)bn
```

The recursive relation is defined by the prior power
```
C(n, k) = C(n-1, k-1) + C(n-1, k) for n > k > 0

IC C(n, 0) = C(n, n) = 1
```

### Algorithm Binomial(n, k)

```
for i ← 0 to n do  // fill out the table row wise

for i = 0 to min(i, k) do

if j==0 or j==i then C[i, j] ← 1  // IC

else C[i, j] ← C[i-1, j-1] + C[i-1, j]  // recursive relation

return C[n, k]
```

The cost of the algorithm is filing out the table. Addition is the basic operation. Because k ≤ n, the sum needs to be split into two parts because only the half the table needs to be filled out for i < k and remaining part of the table is filled out across the entire row.


A(n, k) = sum for upper triangle + sum for the lower rectangle

```
= ∑i=1k ∑j=1i-1 1 + ∑i=1n ∑j=1k 1

= ∑i=1k (i-1) + ∑i=1n k

= (k-1)k/2 + k(n-k) ε Θ(nk)
```
"""
def bino(n,k):
    C = [[0 for i in range(k+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j in (0,i):
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j] + C[i-1][j-1]
    return C[n][k]