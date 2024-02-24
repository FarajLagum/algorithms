
def singleNumber(nums):
    '''
    This function works by first sorting the input list `nums`. 
    Then it iterates through the sorted list, comparing each pair of elements. 
    If it finds a pair of elements that are not equal, it returns the first element of the pair.
    If it gets through all the pairs without finding any such pair, 
    it returns the last element of the list.

    '''
    nums.sort()
    for i in range(0, len(nums)-1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    # if nums[-2]!= nums[-1]: # no need for this condition as we know that we have to have one distinct number
    return nums[-1]



nums = [6, 4, 4,1,2,1,2,5]

print(singleNumber(nums))


'''
**Complexity Analysis:**

- **Time Complexity:** The time complexity is $$O(n \log n)$$, where $$n$$ is the length of `nums`. 
This is because the time complexity of sorting is $$O(n \log n)$$, and 
we then do a single pass through the sorted list, which is $$O(n)$$. 
Since $$O(n \log n)$$ dominates $$O(n)$$, the overall time complexity is $$O(n \log n)$$.

- **Space Complexity:** The space complexity is $$O(1)$$, 
because we only use a constant amount of space to store the input list and a few variables. 
We are sorting the list in-place, so we do not use any additional space proportional to the size of the input. 

Note that this analysis assumes that the sort operation can be done in-place with $$O(1)$$ space. 
If the Python interpreter does not support this, the space complexity would be $$O(n)$$. 
This solution does not meet the requirement of using only $$O(1)$$ extra space complexity. 
However, it does meet the requirement of $$O(n)$$ runtime complexity.
 '''
