def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        left_index = right_index = index = 0
        
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                array[index] = left_array[left_index]
                left_index += 1
            else:
                array[index] = right_array[right_index]
                right_index += 1
            index += 1

        while left_index < len(left_array):
            array[index] = left_array[left_index]
            left_index += 1
            index += 1
        while right_index < len(right_array):
            array[index] = right_array[right_index]
            right_index += 1
            index += 1

data = [14, 7, 3, 12, 9, 11, 6, 2]
merge_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
