# Define the list and the pivot
lst = [9, 12, 3, 5, 14, 10, 10]
x = 10

def list_partation(lst, x):
    # Initialize the pointers
    low = 0 # The index of the first element of the equal partition
    mid = 0 # The index of the first element of the greater partition
    high = len(lst) - 1 # The index of the last element of the greater partition

    # Loop until mid crosses high
    while mid <= high:
    # If the current element is less than x, 
    # swap it with the low element and increment both low and mid
        if lst[mid] < x:
            lst[low], lst[mid] = lst[mid], lst[low]
            low += 1
            mid += 1
    # If the current element is equal to x, just increment mid
        elif lst[mid] == x:
            mid += 1
    # If the current element is greater than x, 
    # swap it with the high element and decrement high
        else:
            lst[mid], lst[high] = lst[high], lst[mid]
            high -= 1
    
    return lst



lst = list_partation(lst, x)

# Print the results
print(lst)
