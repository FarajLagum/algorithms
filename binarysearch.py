import math


def binary_search(array, value):
    """Your code goes here."""
    l = 0
    r = len(array) - 1
    while l <= r:
        m = math.floor((l+r)/2)
        if array[m] < value:
            l = m + 1 
        elif array[m] > value:
            r = m - 1 
        else:
            return m 

    return -1








test_array = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
test_val3 = 1

#print(len(array))
#print(array[6])
print(binary_search(test_array, test_val1))
print(binary_search(test_array, test_val2))
print(binary_search(test_array, test_val3))

