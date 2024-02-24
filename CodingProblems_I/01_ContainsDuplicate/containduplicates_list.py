
def containsDuplicate(nums: list[int]) -> bool:

    appeard_before = []
    
    for num in nums:
        if num in appeard_before:
            return True
        appeard_before.append(num)
    return False 

nums = [1, 3, 4,5,6]

print(containsDuplicate(nums))

'''
The complexity of the provided Python code is as follows:

- **Time Complexity:** The time complexity is $$O(n^2)$$, where $$n$$ is the length of `nums`. 
This is because for each element in `nums`, the code checks if it is in the list `appeard_before`. 
In the worst case, this operation can take $$O(n)$$ time, 
and since it is done for each of the $$n$$ elements in `nums`, 
the total time complexity is $$O(n^2)$$.


- **Space Complexity:** The space complexity is $$O(n)$$, 
because in the worst case (when all elements are distinct), 
the size of the list `appeard_before` will be equal to the size of `nums`.

Please note that this code could be optimized by using a set or a dictionary 
instead of a list for `appeard_before`, which would reduce the time complexity to $$O(n)$$, 
as lookup operations in a set or dictionary are $$O(1)$$ on average. 
However, this would slightly increase the space complexity due to the overhead of maintaining a set or dictionary.
'''