# note the use of the partation_index not the pivot_index

def partition(array, low_index, high_index):
    partition_index = low_index
    pivot = array[high_index]

    for j in range(low_index, high_index):
        if array[j] <= pivot:
            array[partition_index], array[j] =  array[j], array[partition_index]
            partition_index += 1

    array[partition_index], array[high_index] = array[high_index] ,array[partition_index]

    return partition_index


def quick_sort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)

    return array


if __name__=="__main__":
    list = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    quick_sort(list, 0, len(list) - 1)
    print(list)

    list = [3, 9, 2, 1]
    my_list = quick_sort(list, 0, len(list) - 1)
    print(my_list)

