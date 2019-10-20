"""
Fibonacci series generates the subsequent number by adding two previous numbers. Fibonacci series starts from two numbers − F0 & F1. The initial values of F0 & F1 can be taken 0, 1 or 1, 1 respectively.

Fibonacci series satisfies the following conditions −
```
Fn = Fn-1 + Fn-2
```
Hence, a Fibonacci series can look like this −
```
F8 = 0 1 1 2 3 5 8 13
```
or, this −
```
F8 = 1 1 2 3 5 8 13 21
```
"""
# Fibonacci Series using Dynamic Programming 
def fibonacci(n): 
	
	# Taking 1st two fibonacci nubers as 0 and 1 
	FibArray = [0, 1] 
	
	while len(FibArray) < n + 1: 
		FibArray.append(0) 
	
	if n <= 1: 
		return n 
	else: 
		if FibArray[n - 1] == 0: 
			FibArray[n - 1] = fibonacci(n - 1) 

		if FibArray[n - 2] == 0: 
			FibArray[n - 2] = fibonacci(n - 2) 
			
	FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
	return FibArray[n] 
 
