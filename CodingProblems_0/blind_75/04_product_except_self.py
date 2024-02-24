'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
def product_except_self(nums):
    n = len(nums)
    # Initialize arrays to store products of elements to the left and right of current element
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    # Calculate products of elements to the left of each element
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Calculate products of elements to the right of each element
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Multiply the corresponding elements from left_products and right_products to get the result
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result

# Test cases
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]


def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Calculate products of elements to the left of each element and store it in the result array
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]

    # Calculate products of elements to the right of each element and update the result array
    right_product = 1
    for i in range(n - 1, -1, -1): # for i in reversed(range(0, n)): 
        result[i] *= right_product
        right_product *= nums[i]

    return result

# Test cases
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]
