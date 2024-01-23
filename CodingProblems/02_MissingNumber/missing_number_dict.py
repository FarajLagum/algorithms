
def missing_number(nums):
    num_dict = {num: True for num in nums}
    for i in range(len(nums) + 1):
        if i not in num_dict:
            return i


nums = [3,0,1]

print(missing_number(nums))

'''


**Complexity Analysis:**

- **Time Complexity:** The time complexity is $$O(n)$$, where $$n$$ is the length of `nums`. 
This is because we need to iterate through each element in `nums` to add it to the dictionary, 
and then we do another pass through the numbers from `0` to `n` to find the missing number.

- **Space Complexity:** The space complexity is $$O(n)$$, because we create a dictionary with `n` elements. In the worst case (when the missing number is `n`), the size of the dictionary will be equal to the size of `nums`. This solution does not meet the follow-up requirement of using only $$O(1)$$ extra space complexity. However, it does meet the requirement of $$O(n)$$ runtime complexity.


'''