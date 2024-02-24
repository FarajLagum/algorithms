def missing_number(nums):
    n = len(nums)
    
    # Calculate the expected sum of the series from 0 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the elements in the nums list
    actual_sum = sum(nums)
    
    # The missing number is the difference between the expected and actual sums
    return expected_sum - actual_sum

nums = [3, 0, 1]
print(missing_number(nums))

'''
Time Complexity:
This optimized solution has a time complexity of O(n), where n is the length of the nums list. 
Both the calculation of the expected sum and the summation of the elements in nums 
take linear time.

Space Complexity:
The space complexity is O(1) as the algorithm only uses 
a constant amount of extra space for variables (n, expected_sum, actual_sum).
'''