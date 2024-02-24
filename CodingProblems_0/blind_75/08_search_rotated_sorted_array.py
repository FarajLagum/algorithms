'''
33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 
 
'''

# my own solution
def search(nums, target):

    left, right = 0, len(nums)-1

    

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        
        if nums[mid] < nums[right]: # Right half is sorted 
            if nums[mid] < target <= nums[right]:
                left = mid
            else: # explore the left side 
                right = mid -1
        
        else: # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid
            else: # # explore the right side 
                left = mid+1


    
    return -1


print(search([2, 3, 4, 0, 1], 0))



print(search([4,5,6,7,0,1,2], 0))
print(search([4,5,6,7,0,1,2], 3))
print(search([1], 0))
print(search([1], 1))



'''
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''



def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

# Example usage:
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(search(nums1, target1))  # Output: 4

nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(search(nums2, target2))  # Output: -1

nums3 = [1]
target3 = 0
print(search(nums3, target3))  # Output: -1


'''
If the left half of the current range (from left to mid) is sorted, we check if the target falls within the range of this sorted half.
    If it does, we update the right pointer to indicate that we'll search in the left half next.
    If it doesn't, we update the left pointer to indicate that we'll search in the right half next.
If the left half is not sorted, then the right half must be sorted. We follow similar steps as above to decide whether to search in the left or right half next.
'''