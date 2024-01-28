import random

def partition(array, start, stop):
    pivot_index = start
    pivot = array[pivot_index]
    low_index, high_index = start + 1, stop - 1

    while low_index <= high_index:
        while low_index <= high_index and not pivot < array[low_index]:
            low_index += 1
        while low_index <= high_index and pivot < array[high_index]:
            high_index -= 1

        if low_index < high_index:
            array[low_index], array[high_index] = array[high_index], array[low_index]
            low_index += 1
            high_index -= 1

    array[pivot_index], array[high_index] = array[high_index], pivot

    return high_index

def quicksort_recursively(seq, start, stop):
    if start >= stop - 1:
        return

    pivot_index = partition(seq, start, stop)

    quicksort_recursively(seq, start, pivot_index)
    quicksort_recursively(seq, pivot_index + 1, stop)

def quicksort(array):
    # Randomize the sequence first
    for i in range(len(array)):
        j = random.randint(0, len(array) - 1)
        array[i], array[j] = array[j], array[i]

    quicksort_recursively(array, 0, len(array))

    return array

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted = quicksort(my_list.copy())
print("Sorted List:", sorted)
