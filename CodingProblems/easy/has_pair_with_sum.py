
# time complexity of O(n^2)
# space complexity of O(1)
def has_pair_with_sum_bruteforce(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == k:
                return True
    return False


# time complexity of O(n)
# space complexity of O(1)
def has_pair_with_sum(nums, k):
    num_set = set()
    
    for num in nums:
        complement = k - num # The complement represents the number that, when added to num, would give the desired sum k.
        if complement in num_set:
            return True
        num_set.add(num)
    
    return False


if __name__ == "__main__":
    
    numbers = [10, 15, 3, 7]
    k = 17
    result = has_pair_with_sum_bruteforce(numbers, k)
    print(result)  # This will print True since 10 + 7 = 17
    result = has_pair_with_sum(numbers, k)
    print(result)  # This will print True since 10 + 7 = 17
