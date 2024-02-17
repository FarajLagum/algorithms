#  given an array of positive numbers, find the sub-arrays that add up to a given number.
# Sliding Window Technique
def find_subarrays_with_sum(array, target_sum):
    result = []
    current_sum = 0
    start_index = 0

    for end_index in range(len(array)):
        current_sum += array[end_index]

        while current_sum > target_sum:
            current_sum -= array[start_index]
            start_index += 1

        if current_sum == target_sum:
            result.append(array[start_index:end_index + 1])

    return result


# Example usage:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 8, 2]
array = [1, 2, -3, 5, 5, -6, 7, 8, 9, 1, 8, 2]
target_sum = 10

subarrays = find_subarrays_with_sum(array, target_sum)
print("Subarrays with sum", target_sum, "are:", subarrays)
