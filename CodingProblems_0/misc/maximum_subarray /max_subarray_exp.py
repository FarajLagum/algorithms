# Kadane's algorithm to solve the Maximum Subarray problem:


def max_subarray_sum(array):
    max_ending_here = max_so_far = float('-Inf')
    for i in range(0, len(array)):
        max_ending_here = max(array[i], max_ending_here + array[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# The `max_subarray_sum` function takes an array of integers as input and return
# the maximum sum of a contiguous subarray within the input array.

# The algorithm works by iterating over the input array and keeping track of the maximum sum
# of a subarray ending at each position.
# The idea behind Kadane's algorithm is to maintain a variable `max_ending_here` that stores
# the maximum sum contiguous subarray ending at the current index and
# a variable `max_so_far` that stores the maximum sum of contiguous subarray found so far.
# Every time there is a positive-sum value in `max_ending_here`,
# we compare it with `max_so_far` and update `max_so_far` if it is greater than `max_so_far`.
# The subarray with negative sum is discarded (by assigning `max_ending_here = arr[i]` in code).
# We carry the subarray till it gives positive sum.

# Here is an example usage of the function:


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(
    f"The maximum sum of a contiguous subarray within {arr} is {max_subarray_sum(arr)}")
# ```

# This will output:

# ```
# The maximum sum of a contiguous subarray within [-2, -3, 4, -1, -2, 1, 5, -3] is 7
# ```
