import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from create_n_print_linked_list import create_linked_list
from create_n_print_linked_list import print_linked_list


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(list_1: ListNode, list_2: ListNode) -> ListNode:
    # create a prehead node
    prehead = ListNode(-1) # dummy node

    current = prehead
    while list_1 and list_2:
        if list_1.value <= list_2.value:
            current.next = list_1
            list_1 = list_1.next
        else:
            current.next = list_2
            list_2 = list_2.next            
        
        current = current.next

    # At least one of l1 and l2 can still have nodes at this point, so connect
    # the non-null list to the end of the merged list.
    
    if list_1 is not None:
        current.next = list_1 
        
    else:
        current.next = list_2

    return prehead.next

list_1 = create_linked_list([1, 3, 4, 5])

list_2 = create_linked_list([1, 2, 5, 7, 9, 11])


megred_list = mergeTwoLists(list_1, list_2)

print_linked_list(megred_list)