def missing_number(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
        print(missing)
    return missing


nums = [3, 0, 1]
print(missing_number(nums))
