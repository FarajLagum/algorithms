# Import the bisect module
import bisect
# The complexity of this solution is O(n log n), where n is the length of the list. 
# This is because sorting the list takes O(n log n) time, 
# note that finding the index and slicing the list take O(log n) and O(n) time respectively.

# Define the list and the pivot
lst = [9, 12, 3, 5, 14, 10, 10]
x = 10

# Sort the list
lst.sort()

# Find the index of the pivot using binary search
index = bisect.bisect_left(lst, x)

# Partition the list into three parts using slicing
less = lst[:index] # All elements less than x
equal = lst[index:index + lst.count(x)] # All elements equal to x
greater = lst[index + lst.count(x):] # All elements greater than x

# Print the results
print(less)
print(equal)
print(greater)
