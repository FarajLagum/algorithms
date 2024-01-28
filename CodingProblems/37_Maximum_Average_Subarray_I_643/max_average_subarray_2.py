def max_sum_subarray(array, k):
    if k <= 0 or k > len(array):
        return 0

    # Calculate the sum of the first subarray of length k
    current_sum = sum(array[:k])
    max_avge = current_sum

    # Iterate through the array starting from index k
    for i in range(k, len(array)):
        # Update the current sum by adding the next element and subtracting the first element in the previous subarray
        current_sum = current_sum + array[i] - array[i - k]
        max_avge = max(max_avge, current_sum)

    return max_avge / k

# Example usage:
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(max_sum_subarray(nums, k))
