# space complexity: O(n)
# time complexity: 3*O(n) -> O(n)

# Define the list and the pivot
lst = [9, 12, 3, 5, 14, 10, 10]
x = 10

# Partition the list into three parts
less = [y for y in lst if y < x] # All elements less than x
equal = [y for y in lst if y == x] # All elements equal to x
greater = [y for y in lst if y > x] # All elements greater than x

# Print the results
print(less)
print(equal)
print(greater)


def list_paration(lst):
    less = []
    equal = []
    greater = []
    for item in lst:
        if item < x:
            less.append(item)
        elif item == x:
            equal.append(item)
        else:
            greater.append(item)
    
    return less, equal, greater

less, equal, getattr = list_paration(lst)
# Print the results
print(less)
print(equal)
print(greater)