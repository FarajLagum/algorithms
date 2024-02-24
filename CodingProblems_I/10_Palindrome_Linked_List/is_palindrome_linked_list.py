class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

def is_palindrome(head):
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values == values[::-1]


def create_linked_list(array):
    head = Node(0) # dummy head
    current = head
    for value in array:
        current.next = Node(value)
        current = current.next
    return head.next # actual head is head.nex

# Test case 1:
head = create_linked_list([1, 2, 2, 1])
print(is_palindrome(head))  # Expected output: True

# Test case 2:
head = create_linked_list([1, 2])
print(is_palindrome(head))  # Expected output: False


# Test case 3:
head = create_linked_list([1, 2, 1])
print(is_palindrome(head))  # Expected output: True



# We can optimize the space complexity to O(1) by using a two-pointer technique 
# to reverse the second half of the linked list in-place and then compare 
# it with the first half
# Source: https://github.com/adityasarvaiya/coding/blob/6869c212c870985ff4ac8bd8c5cade8842d78a6c/Crio/LinkedList/12_Palindrome/Solution.py

