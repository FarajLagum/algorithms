def move_zeroes(nums):
    slow_index = 0
    for fast_index in range(len(nums)):
        print("i = ", slow_index, ";", "j = ", fast_index)
        if nums[fast_index] != 0: # if the current element is not zero, I put it at the index slow_index
            nums[slow_index], nums[fast_index] = nums[fast_index], nums[slow_index]
            slow_index += 1
    return nums

nums = [0,1,0,3,12]
print(move_zeroes(nums)) # Output: [1,3,12,0,0]


''''
def move_zeroes(nums):
    non_zero_index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1

    return nums

# Example usage:
nums = [0, 1, 0, 3, 12]
result = move_zeroes(nums)
print(result)

'''


