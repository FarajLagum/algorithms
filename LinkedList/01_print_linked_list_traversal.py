class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node("A")
#print(a.value)
b = Node("B")
c = Node("C")
d = Node("D")
 
a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> Null

# iterative: time = O(n); Space = O(1)
def print_linked_list_iterative(head):
    current = head # current is a Node

    while current != None: 
        print(current.value)
        current = current.next
        # print(current)


#print_linked_list_iterative(a)

# recursive: time = O(n); Space = O(n)
def print_linked_list_recursive(current):
    if current == None:
        return  # Terminate recursion
    print(current.value)

    print_linked_list_recursive(current.next)


print_linked_list_recursive(a)

