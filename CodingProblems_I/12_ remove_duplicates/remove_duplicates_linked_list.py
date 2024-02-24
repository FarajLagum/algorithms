import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from create_n_print_linked_list import create_linked_list
from create_n_print_linked_list import print_linked_list




# Definition for singly-linked list.
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.value == current.next.value: 
            current.next = current.next.next # Skip 
        else:
            current = current.next
    return head





# Test case 1:
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
head = delete_duplicates(head)
print_linked_list(head) # Expected output: 1 2 3 4 5

# Test case 2:
head = create_linked_list([])
head = delete_duplicates(head)
print_linked_list(head) # Expected output: None

# Test case 3:
head = create_linked_list([7, 7, 7, 7])
head = delete_duplicates(head)
print_linked_list(head)  # Expected output: 7 -> None




# Here's a step-by-step breakdown of the the function  'delete_duplicates(head)' works :

# 1. The function takes `head` as an argument, which is the first node (head) of the linked list.

# 2. It sets `current` to `head`, which means it starts checking the list from the head node.

# 3. The `while` loop continues as long as `current` and `current.next` are not `None`. 
# This ensures that the function doesn't try to access a non-existent next node.

# 4. Inside the loop, it checks if the value of the `current` node is the same as the value of the next node (`current.next.value`). 
# If they are the same, it means there is a duplicate.

# 5. If a duplicate is found, `current.next` is set to `current.next.next`. 
# This effectively skips over the duplicate node and it's no longer part of the list. 
# The duplicate node is not explicitly deleted here, but Python's garbage collection will take care of that.

# 6. If `current.value` is not equal to `current.next.value`, it means there is no duplicate, 
# so it moves on to the next node by setting `current` to `current.next`.

# 7. The function continues this process for all nodes in the list, effectively removing all duplicates.

# 8. Finally, it returns `head`, which is now the head of the modified list with all duplicates removed.


'''
Complexity Analysis:

Time Complexity: O(n), where n is the number of nodes in the list. 
This is because we are processing each node exactly once.

Space Complexity: O(1), as we are not using any extra space proportional to the input size.

'''


