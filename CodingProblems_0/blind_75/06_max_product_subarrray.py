# dynamic programming


def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for num in nums[1:]:
        # If num is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result

# Test cases
print(max_product_subarray([2, 3, -2, 4]))  # Output: 6
print(max_product_subarray([-2, 0, -1]))    # Output: 0




def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = 1
    min_product = 1
    max_so_far = nums[0]

    for num in nums:
        # If num is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        max_so_far = max(max_so_far, max_product)

    return max_so_far

# Test cases
print(max_product_subarray([2, 3, -2, 4]))  # Output: 6
print(max_product_subarray([-2, 0, -1]))    # Output: 0

