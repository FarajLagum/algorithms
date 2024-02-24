def containsDuplicate(nums):
    return len(nums) != len(set(nums))

nums = [1, 3, 4,5,6, 1]

print(containsDuplicate(nums))

'''

The time complexity is O(n), where n is the number of elements in the `nums` list. 


1. `set(nums)`: Creating a set from a list has a time complexity of O(n).

2. `len(set(nums))`: The time complexity of getting the length of a set is O(1).

3. `len(nums)`: The time complexity of getting the length of a list is also O(1).

4. `len(nums) != len(set(nums))`: This is a simple comparison, which has a time complexity of O(1).

The dominating factor here is the creation of the set, which has a time complexity of O(n). 
Therefore, the overall time complexity of the function is O(n).
'''