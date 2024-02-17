"""
Write a function, linked_list_values, that takes in the head of a linked list as an argument. 
The function should return an array containing all values of the nodes in the linked list.
https://youtu.be/Hj_rA0dhr2I?si=_fD6o-IAH1uN74ig&t=1419
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

a =  Node(2)
b =  Node(8)
c =  Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

# # iterative
def sum_list(current):
    sum = 0
    while current != None: 
        sum += current.value 
        current = current.next
        #print(current)
    return sum


print(sum_list(a))



# recursive

def sum_list_recursive(current):
    if current is None:
        return 0
    return current.value + sum_list_recursive(current.next)

print(sum_list_recursive(a))

     


 