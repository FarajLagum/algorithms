from collections import deque

def sorted_squares(nums):
    left, right = 0, len(nums) - 1
    result = deque([])
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.appendleft(nums[left] ** 2)
            left += 1
        else:
            result.appendleft(nums[right] ** 2)
            right -= 1
    return result # the array is deque. you can make it a list: list(result)

'''
The time complexity of the solution is O(n), where n is the number of elements in the input array.
The space complexity of the solution is O(n).
'''
# Test Case 1
nums = [-4,-1,0,3,10]
print(sorted_squares(nums))

assert sorted_squares(nums) == deque([0,1,9,16,100])
# Test Case 2
nums = [-7,-3,2,3,11]
print(sorted_squares(nums))
assert sorted_squares(nums) == deque([4,9,9,49,121])
