import bisect
# The time complexity of bisect.bisect_left and bisect.bisect_right is O(log n), 
# These functions use binary search to find the insertion point for a target element in a sorted sequence. 
# The binary search algorithm has a time complexity of O(log n) 



# Example sequence
sequence = [1, 2, 4, 4, 4, 6, 7]

# Using bisect_left
target_left = 4
insert_point_left = bisect.bisect_left(sequence, target_left)
print(f"Insert {target_left} at index {insert_point_left}")

# Using bisect_right
target_right = 4
insert_point_right = bisect.bisect_right(sequence, target_right)
print(f"Insert {target_right} at index {insert_point_right}")

# Output:
#Insert 4 at index 2   # bisect_left returns the leftmost position for 4
#Insert 4 at index 5   # bisect_right returns the rightmost position for 4
