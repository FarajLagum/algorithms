# Two pointers
def move_zeroes(nums):
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        while right_index >= 0 and nums[right_index] == 0:
            right_index -= 1

        if left_index < right_index and nums[left_index] == 0 and nums[right_index] != 0:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index += 1
            right_index -= 1
        else:
            left_index += 1

    return nums






# Example usage:
nums = [0, 1, 0, 3, 12]
result = move_zeroes(nums)
print(result)


