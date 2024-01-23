# The solution can be optimized further by reducing the space complexity. 
# We don't need to store the number of ways for all the steps. 
# We only need to keep track of the number of ways for the last two steps at a time. 



def climb_stairs(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

print(climb_stairs(5))

'''
**Time complexity analysis:**
The time complexity is still $$O(n)$$, where $$n$$ is the input to the function. 
This is because we are simply iterating from `3` to `n` once.

**Space complexity analysis:**
The space complexity is now $$O(1)$$, 
because we are using only two variables to store the number of ways to reach the current and the previous step. 

'''