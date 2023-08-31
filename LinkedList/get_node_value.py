'''
Write a function, get_node_value, that takes in the head of a linked list and an index. 
The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

# iterative
def get_node_value(head, index):
  count = 0

  while head is not None:

    if count == index:
       return head.value
    head = head.next
    count += 1
  
  return None



# recursive
def get_node_value_recursive(head, index, counetr = 0):
    
    if head is None:
       return None
   
    if index == counetr:
        return head.value
  
    return get_node_value_recursive(head.next, index, counetr + 1)







def get_node_value_recursive_2(head, pointer):

    # the first element in the linked list will have decremental pointer = the trager index (pointer = index)
    # We then decrement decremental index untill it reach zeor. If it reach sero, then
    # we are at the target node which we want to retirn its value
    
    if head is None:
       return None
  
    if pointer == 0:
       return head.value
  
    return get_node_value_recursive_2(head.next, pointer - 1)


if __name__ == "__main__":
   print(get_node_value(a, 2)) # 'c'

   print(get_node_value_recursive(a, 2)) # 'c'
   print(get_node_value_recursive_2(a, 2)) # 'c'


   