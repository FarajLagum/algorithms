# Without Memoization
    # - time: O(2^n) -- e.g., 2^50 ~= 1.12*10^15
    # - space: O(n)
# With Memoization
    # - time: O(n) 
    # - space: O(n)
from functools import lru_cache 
# lru_cache(): reducing the execution time using memoization technique.


from functools import lru_cache 
import time 

N =35
# Function that computes Fibonacci 
# numbers without lru_cache 
def fib_without_cache(n): 
	if n < 2: 
		return n 
	return fib_without_cache(n-1) + fib_without_cache(n-2) 
	
# Execution start time 
begin = time.time() 
fib_without_cache(N) 

# Execution end time 
end = time.time() 

print("Time taken to execute the function without lru_cache is", end-begin) 

# Function that computes Fibonacci 
# numbers with lru_cache 
@lru_cache(maxsize = 128) 
def fib_with_cache(n): 
	if n < 2: 
		return n 
	return fib_with_cache(n-1) + fib_with_cache(n-2) 
	
begin = time.time() 
fib_with_cache(N) 
end = time.time() 

print("Time taken to execute the function with lru_cache is", end-begin) 
