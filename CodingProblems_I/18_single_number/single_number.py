# Time Complexity:  O(n)
# Space Complexity:  O(1)
def single_number_xor(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


from collections import Counter

# Time Complexity:  O(n)
# Space Complexity:  O(n)
def single_number_counter(nums):
    count = Counter(nums)
    for num in count:
        if count[num] == 1:
            return num

# Time Complexity:  O(n) -> um(set(nums)) complexity is O(n) + O(n) = O(n).
# Space Complexity:  O(n)
def single_number_set(nums):
    return 2 * sum(set(nums)) - sum(nums)


print(single_number_counter([2,2,1]))  # Output: 1
print(single_number_counter([4,1,2,1,2]))  # Output: 4
print(single_number_counter([1]))  # Output: 1

