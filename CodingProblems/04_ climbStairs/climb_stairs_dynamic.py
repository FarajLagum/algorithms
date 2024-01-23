def climb_stairs(n):
    if n == 1:
        return 1
    n_ways = [0]*(n+1)
    print(n_ways)
    n_ways[1] = 1
    n_ways[2] = 2
    for i in range(3, n+1):
        n_ways[i] = n_ways[i-1] + n_ways[i-2]
    return n_ways[n]


print(climb_stairs(4))


'''
Time complexity analysis:
The time complexity of the above code is O(n), where n is the input to the function. 
This is because we are simply iterating from 3 to n once.


Space complexity analysis:
The space complexity of the above code is also O(n), 
because we are using a list of size n+1 to store the number of ways to reach each step.

'''