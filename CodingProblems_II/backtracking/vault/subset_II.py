def subsets(nums):
    nums.sort()
    res = []
    backtrack(nums, [], res, 0)
    return res

def backtrack(nums, temp, res, start):
    res.append(temp.copy())
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:
            return # continue # we can use continue as well 
        temp.append(nums[i])
        backtrack(nums, temp, res, i+1)
        temp.pop()

nums = [1, 2, 2]
print(subsets(nums))

# lst =[1, 2,3]
# test = lst[:]

# lst.append(4)
# print(test)
