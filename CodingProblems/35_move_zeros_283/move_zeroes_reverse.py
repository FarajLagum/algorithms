
def move_zeroes(nums):
    zero_index = -1

    for i in range(-1, -len(nums)-1, -1):
        print(i)
        if nums[i] == 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index -= 1

    return nums

# Example usage:
nums = [0, 1, 0, 3, 12]
result = move_zeroes(nums)
print(result)



# def move_zeroes(nums):
#     slow_index = 0
#     for fast_index in range(len(nums)):
    
#         if nums[fast_index] != 0: # if the current element is not zero, I put it at the index slow_index
#             nums[slow_index], nums[fast_index] = nums[fast_index], nums[slow_index]
#             slow_index += 1
#     return nums

# nums = [0,1,0,3,12]
# print(move_zeroes(nums)) # Output: [1,3,12,0,0]
