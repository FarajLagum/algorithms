def sorted_squares(nums):
    n = len(nums)
    left, right = 0, n - 1
    result = [0] * n
    for i in range(n - 1, -1, -1):
        #print(i)
        if abs(nums[left]) > abs(nums[right]):
            
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1
    return result

'''
The time complexity of the solution is O(n), where n is the number of elements in the input array.
The space complexity of the solution is O(n).
'''
# Test Case 1
nums = [-4,-1,0,3,10]
assert sorted_squares(nums) == [0,1,9,16,100]
# Test Case 2
nums = [-7,-3,2,3,11]
assert sorted_squares(nums) == [4,9,9,49,121]
