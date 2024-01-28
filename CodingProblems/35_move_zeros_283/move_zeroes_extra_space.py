def moveZeroes(nums):
    
    non_zero_list = []
    for num in nums:
        if num != 0: # if the current element is not zero, I put it at the index i
            non_zero_list.append(num)
    n_zeroes = len(nums) - len(non_zero_list)
    print(non_zero_list)
    return non_zero_list + [0]*n_zeroes

nums = [0,1,0,3,12]
print(moveZeroes(nums.copy())) # Output: [1,3,12,0,0]
