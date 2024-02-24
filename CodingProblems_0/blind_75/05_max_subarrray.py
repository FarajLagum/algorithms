# dynamic programming
'''
53. Maximum Subarray
Medium
Topics
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

def max_subarray_sum(nums):
    max_so_far = float('-inf')  # Initialize max_so_far to negative infinity
    max_ending_here = 0

    for num in nums:
        max_ending_here += num

        max_so_far = max(max_so_far, max_ending_here)
        print(max_so_far)
        # If the current sum becomes negative, resets the sum to 0 and starts a new subarray. 
        if max_ending_here < 0: 
            max_ending_here = 0

    return max_so_far

# Example usage:
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", max_subarray_sum(array))  # Output: 6

array = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum subarray sum:", max_subarray_sum(array))  # Output: 7




def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases
print("Maximum subarray sum:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print("Maximum subarray sum:", max_subarray([1]))  # Output: 1
print("Maximum subarray sum:", max_subarray([5, 4, -1, 7, 8]))  # Output: 23

