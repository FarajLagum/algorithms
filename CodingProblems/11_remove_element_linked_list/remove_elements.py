import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from create_n_print_linked_list import create_linked_list
from create_n_print_linked_list import print_linked_list

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeElements(head, remove_value):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    while current.next is not None:
        if current.next.value == remove_value:
            current.next = current.next.next # skip
        else:
            current = current.next
    return dummy.next



# Test case 1:
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
head = removeElements(head, 6)

print_linked_list(head) # Expected output: 1 2 3 4 5

# Test case 2:
head = create_linked_list([])
head = removeElements(head, 1)
print_linked_list(head) # Expected output: 

# Test case 3:
head = create_linked_list([7, 7, 7, 7])
head = removeElements(head, 7)
print_linked_list(head)  # Expected output: 



'''
Time complexity: The time complexity is O(n), where n is the number of nodes in the linked list. 
This is because we are traversing the linked list once.

Space complexity: The space complexity is O(1), 
because we are not using any extra space that scales with the size of the input.
'''