import random

#from functools import lru_cache

def generate_random_list(lower_limit, upper_limit, size):
    # Ensure that x is less than or equal to y
    if lower_limit > upper_limit:
        lower_limit, upper_limit = upper_limit, lower_limit

    # Generate a list of random integers
    random_list = [random.randint(lower_limit, upper_limit) for _ in range(size)]

    return random_list




def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        lesser = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = quicksort(my_list)
print(sorted_list)


# Example usage:
lower_limit = -5
upper_limit = 5
list_size = 10

random_numbers = generate_random_list(lower_limit, upper_limit, list_size)
#print(random_numbers)

sorted_list = quicksort(random_numbers)
print(sorted_list)
