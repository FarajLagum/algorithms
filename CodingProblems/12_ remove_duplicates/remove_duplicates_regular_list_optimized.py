def remove_duplicates(array):
    if not array:
        return 0

    index = 1  # Index to track the position where the next unique element should be placed

    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            array[index] = array[i]
            index += 1

    return index

# Example usage:
input_list = [1, 2, 3, 4, 4, 5, 5, 6]
length = remove_duplicates(input_list)

output_list = input_list[:length]

print(output_list)
