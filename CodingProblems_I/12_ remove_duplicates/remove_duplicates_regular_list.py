def remove_duplicates(array):
    if not array:
        return []

    deduplicated = [array[0]]

    for item in array[1:]:
        if item != deduplicated[-1]:
            deduplicated.append(item)

    return deduplicated

# Example usage:
input_list = [1, 2, 3, 4, 4, 5, 5, 6]
output_list = remove_duplicates(input_list)

print(output_list)
