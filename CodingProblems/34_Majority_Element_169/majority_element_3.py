def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count +=1
        else:
            count -=1 
        #count += (1 if num == candidate else -1)
    return candidate


assert majorityElement([3,2,3]) == 3
assert majorityElement([2,2,1,1,1,2,2]) == 2
assert majorityElement([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9]) == 9