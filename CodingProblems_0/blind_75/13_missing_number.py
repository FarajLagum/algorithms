def missing_number(nums):
    # n = len(nums)
    

    actual_sum =0
    upperbound_sum= 0

    for i , num in enumerate(nums):
        actual_sum += num
        upperbound_sum += i
    
    upperbound_sum +=  i +1  # i+1 is n which is  the highest number in the array
    
    # The missing number is the difference between the expected and actual sums
    return upperbound_sum - actual_sum

nums = [3, 0, 1]
print(missing_number(nums))




def missing_number(nums):
    # n = len(nums)
    

    actual_sum =sum (nums)
   
    upperbound_sum= 0
    for i  in range(len(nums)+1):
        upperbound_sum += i
    
    
    # The missing number is the difference between the expected and actual sums
    return upperbound_sum - actual_sum

nums = [3, 0, 1]
print(missing_number(nums))




# def missing_number(nums):
#     n = len(nums)
    
#     # Calculate the expected sum of the series from 0 to n
#     expected_sum = n * (n + 1) // 2
    
#     # Calculate the actual sum of the elements in the nums list
#     actual_sum = sum(nums)
    
#     # The missing number is the difference between the expected and actual sums
#     return expected_sum - actual_sum

# nums = [3, 0, 1]
# print(missing_number(nums))

