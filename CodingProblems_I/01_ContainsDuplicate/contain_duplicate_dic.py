def containsDuplicate(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        num_dict[num] = num
    return False


nums = [1, 3, 4,5,6, 1]

print(containsDuplicate(nums))


'''
Complexity Analysis:


Time Complexity: The time complexity is O(n). 
This is because we need to iterate through each element in nums to add it to the dictionary.


Space Complexity: The space complexity is O(n), 
because in the worst case (when all elements are distinct), 
the size of the dictionary will be equal to the size of nums.
'''