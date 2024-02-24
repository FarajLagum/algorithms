def sorted_squares(nums):
    return sorted(num ** 2 for num in nums)

def sortedSquares(A):
    for i in range(len(A)):
        A[i] *= A[i]
    A.sort()
    return A
'''
The time complexity of the solution is O(nlong), where n is the number of elements in the input array.
The space complexity of the solution is O(n).
'''
# Test Case 1
nums = [-4,-1,0,3,10]
assert sorted_squares(nums) == [0,1,9,16,100]
# Test Case 2
nums = [-7,-3,2,3,11]
assert sorted_squares(nums) == [4,9,9,49,121]
