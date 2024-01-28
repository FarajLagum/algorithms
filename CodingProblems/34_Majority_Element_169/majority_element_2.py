
from collections import defaultdict 

def majorityElement(nums):
    n = len(nums)
    m = defaultdict(int)

    for num in nums:
        m[num] += 1 # increment count each time you see num 
    for key, value in m.items():
        print(key, value)
    n = n // 2
    for key, value in m.items():
        if value > n:
            return key
    
    return 0

assert majorityElement([3,2,3]) == 3
assert majorityElement([2,2,1,1,1,2,2]) == 2
assert majorityElement([1,2,3,4,5,6,7,8,9,9,9,9,9,9,9,9,9,9]) == 9