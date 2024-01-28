
def majorityElement(nums):
    nums.sort()
    n = len(nums)
    return nums[n//2] # nums[-1]

# The time complexity: O(n log n)
# The space complexity is O(1).

assert majorityElement([3,2,3]) == 3
assert majorityElement([2,2,1,1,1,2,2]) == 2
assert majorityElement([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9]) == 9