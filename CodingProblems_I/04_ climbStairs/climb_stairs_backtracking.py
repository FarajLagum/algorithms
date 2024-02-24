# it's important to note that this approach will be less efficient than the dynamic programming solution. 
# The reason is that backtracking involves exploring all possible paths, which leads to a lot of repeated calculations. 


def climbStairs(n):
    if n == 1 or n == 2:
        return n
    else:
        return climbStairs(n-1) + climbStairs(n-2)


print(climbStairs(3))



'''

**Time complexity analysis:**
The time complexity of the above code is $$O(2^n)$$, where $$n$$ is the input to the function. 
This is because in the worst case, we are making two recursive calls for each call to the function.

**Space complexity analysis:**
The space complexity of the above code is $$O(n)$$, because in the worst case, the maximum depth of the recursion tree can go up to $$n$$. 

Please note that this solution is not efficient for large inputs due to its high time complexity. 
For larger inputs, the dynamic programming approach would be more suitable.
    



'''
