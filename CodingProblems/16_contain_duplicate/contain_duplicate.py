
# Time Complexity: O(n)
# Space Complexity: O(n)
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Time Complexity:  O(n)
# Space Complexity:  O(n)
def contains_duplicate_elegent(nums):
    return len(nums) != len(set(nums))

# Time Complexity:  O(n)
# Space Complexity:  O(n)
def contains_duplicate_dic(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        num_dict[num] = 1
    return False


# Time Complexity:  O(nlogn)
# Space Complexity:  O(1)
def contains_duplicate_sorting(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


nums_1 =[1, 3, 3, 4]

nums_2 =[1, 2, 3, 4]


print(contains_duplicate(nums_1))
print(contains_duplicate(nums_2))







