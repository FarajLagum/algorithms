# Python program to print largest contiguous array sum

# Function to find the maximum contiguous subarray
# and print its starting and end index


def maxSubArraySum(array, size):

    max_so_far = float('-inf')
    max_ending_here = 0
    start_index = 0
    end_index = 0
    s = 0

    for i in range(0, size):

        max_ending_here += array[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start_index = s  # Update the starting index
            end_index = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1  # Set the starting index for the next potential subarray

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % start_index)
    print("Ending Index %d" % end_index)


# Driver program to test maxSubArraySum
a = [-2, -3, 4, -1, -2, 1, 5, -3]
a = [1, 2, -3, 5, 5, -6, 7, 8, 9, 1, 8, 2]
maxSubArraySum(a, len(a))


# # Example usage:
# array = [1, 2, -3, 5, 5, -6, 7, 8, 9, 1, 8, 2]
# target_sum = 10

# subarrays = find_subarrays(array, target_sum)
# print("Subarrays with sum", target_sum, "are:", subarrays)
