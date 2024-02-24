def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
        print(result)
    return result


nums = [4,1,2,1,2]
print(single_number(nums))

# XORing a number with itself results in 0, and 
# XORing a number with 0 results in the number itself. 
# Therefore, after XORing all the numbers in nums, 
# the result will be the number that appears only once. 

# This is because every number that appears twice is XORed twice and becomes 0, 
# and the number that appears only once is XORed only once and remains as the result.