def climb_stairs(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 1 or n == 2:
        result = n
    else:
        result = climb_stairs(n-1, memo) + climb_stairs(n-2, memo)
    
    memo[n] = result
    return result


print(climb_stairs(4))

'''
a memo dictionary is used to store the results of previously calculated subproblems. 

If the result for a particular n is already in the memo, 
it is directly returned, avoiding redundant computations.

This approach significantly reduces the number of recursive calls and 
improves the time complexity to O(n), making it more efficient for larger values of n. 

The space complexity is O(n) due to the memo dictionary.



'''