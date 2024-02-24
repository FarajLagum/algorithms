def single_number(nums):
    '''
    This function works by iterating through the input list nums and adding each element to a dictionary num_dict. 
    If it encounters an element that is already in the dictionary, it removes it. 
    In the end, the only key left in the dictionary is the number that appears only once.
    '''
    num_dict = {}
    for num in nums:
        if num in num_dict:
            del num_dict[num]
        else:
            num_dict[num] = 1
    return list(num_dict.keys())[0]


nums = [4,1,2,1,2]

print(single_number(nums))


'''

**Complexity Analysis:**

- **Time Complexity:** The time complexity is $$O(n)$$, where $$n$$ is the length of `nums`.
This is because we need to iterate through each element in `nums`.

- **Space Complexity:** The space complexity is $$O(n)$$, 
because in the worst case (when all elements are distinct), the size of the dictionary will be equal to the size of `nums`. 
This solution does not meet the requirement of using only $$O(1)$$ extra space complexity.
'''