class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(array):
    if not array:
        return None

    # Create the first node
    head = Node(array[0])
    current = head

    # Create the rest of the linked list
    for item in array[1:]:
        current.next = Node(item)
        current = current.next 

    return head





def create_linked_list3(array):

    # dummy first node --- it will not be returned, but we will return the "head.next" 
    # which is the actual first node
    dummy_head = Node(0)  
    current = dummy_head
    for value in array:
        current.next = Node(value)
        current = current.next
    return dummy_head.next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    my_linked_list = create_linked_list(my_list)
    print_linked_list(my_linked_list)
