'''
Write a function, reverse_list, that takes in the head of a linked list as an argument. 
The function should reverse the order of the nodes in the linked list in-place and return 
the new head of the reversed linked list.
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d

# iterative
# n = number of nodes
# Time: O(n)
# Space: O(1)
def reverse_list(current):
  previous = None
  while current is not None:
    next = current.next # Catch next before overwrite 
    current.next = previous
    previous = current 
    current = next  
  return previous # return that just before the null (None)


# recursive

def reverse_list_recursive(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list_recursive(next, head)


if __name__ == "__main__":
   def linked_list_values(current):
    values = []
    while current != None: 
        values.append(current.value)
        current = current.next
        #print(current)

    return values

   #print(reverse_list_2(a)) # 'c'
   print(linked_list_values(a))
   print(linked_list_values(reverse_list_recursive(a)))



# recursive







