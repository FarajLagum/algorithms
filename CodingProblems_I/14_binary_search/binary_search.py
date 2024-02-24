def binary_search(nums, target):
    left= 0
    right = len(nums) - 1 # last element index
    while left <= right:
        mid = left + (right - left) // 2 # floor division
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



nums = [-1,0,3,5,9,12]
# nums.sort()

target = 9
print(binary_search(nums, target))  # Output: 4

target = 2
print(binary_search(nums, target))  # Output: -1


'''
The time complexity is $$O(\log n)$$

The space complexity is $$O(1)$$
'''