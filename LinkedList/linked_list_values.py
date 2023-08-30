"""
Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
The function should return an array containing all values of the nodes in the linked list.
https://youtu.be/Hj_rA0dhr2I?si=_fD6o-IAH1uN74ig&t=1419
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

# A -> B -> C -> D -> Null

# # iterative
def linked_list_values(current):
    values = []
    while current != None: 
        values.append(current.value)
        current = current.next
        #print(current)

    return values


print(linked_list_values(a))



# recursive

def linked_list_values_recursive(current):
    values = []
    fill_values(current, values)
    return values
     
 
def fill_values(current, values):
    if current == None:
        return    
    values.append(current.value)
    fill_values(current.next, values)

     


print(linked_list_values_recursive(a))