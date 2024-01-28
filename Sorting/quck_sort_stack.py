# note the use of pivot_index not the partation_index
def quicksort(array):
    if len(array) <= 1:
        return array

    stack = [(0, len(array) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(array, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return array

def partition(array, low_index, high_index):
    pivot = array[high_index]
    pivot_index = low_index - 1

    for j in range(low_index, high_index):
        if array[j] <= pivot:
            pivot_index += 1
            array[pivot_index], array[j] = array[j], array[pivot_index]

    array[pivot_index + 1], array[high_index] = array[high_index], array[pivot_index + 1]
    return pivot_index + 1

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quicksort(my_list)
print(my_list)
