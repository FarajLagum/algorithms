"""
Write a function, linked_list_find, that takes in the head of a linked list and a target value. 
The function should return a boolean indicating whether or not the linked list contains the target.
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
  
a.next = b
b.next = c

c.next = d


# iterative 
def linked_list_find(head, traget):

    while head is not None:
        if head.value == traget:
            return True
        
        head = head.next

    return False


print(linked_list_find(a, "G"))




# recursive:
def linked_list_find_recursive(head, traget):

    if head is None:
        return False
    elif head.value == traget:
        return True
  
    return linked_list_find_recursive(head.next, traget)  


print(linked_list_find_recursive(a, "D"))