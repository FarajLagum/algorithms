def subsets(nums):
    output = [[]]
    nums_len = len(nums)
    def backtrack(array, i):
        if i >= nums_len:
            return
        output.append(array+[nums[i]])
        # take
        backtrack(array+[nums[i]], i+1)
        # not take
        backtrack(array, i+1)

    backtrack([], 0)
    return output

nums = [1, 2, 3]
print(subsets(nums))