
# Time Complexity:  O(n)
# Space Complexity:  O(1)
def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    array_sum = sum(nums)
    return total_sum - array_sum

# Time Complexity:  O(n)
# Space Complexity:  O(1)
def missing_number_xor(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

# Time Complexity:  O(nlogn)
# Space Complexity:  O(1)
def missing_number_sort(nums):
    nums.sort()
    for i, num in enumerate(nums):
        if i != num:
            return i
    return len(nums)

# Time Complexity:  O(n) -> set(list) requires O(n)
# Space Complexity:  O(n)
def missingNumber(nums):
    return list(set(range(len(nums) + 1)) - set(nums))[0]


print(missing_number([3,0,1]))  # Output: 2
print(missing_number([0,1]))  # Output: 2
print(missing_number([9,6,4,2,3,5,7,0,1]))  # Output: 8

