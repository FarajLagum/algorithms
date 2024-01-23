
def missing_number(nums):
    n = len(nums)

    for num in range(n+1):
        #print(num)
        if num not in nums:
            return num 

nums = [3,0,1]

print(missing_number(nums))


'''
Time Complexity:
The range(n+1) creates an iterator of numbers from 0 to n (inclusive). 
This has a time complexity of O(n).

The `for num in range(n+1)` loop iterates over the numbers from 0 to n. 
Inside the loop, the num not in nums check takes O(n) time in the worst case.

The overall time complexity is O(n^2), where n is the length of the nums list. 
This is because, for each number in the range, there is a check if it is in the nums list, 
and this check takes linear time.

Space Complexity:
The space complexity is O(1) because the function uses a constant amount of extra space 
regardless of the input size. The variable n is a single integer, and 
the loop variable num is also a constant amount of space. The algorithm does not use additional data structures that scale with the input size.
'''