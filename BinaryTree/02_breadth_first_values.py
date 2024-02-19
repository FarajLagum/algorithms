'''
Write a function, breadth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in breadth-first order
'''

from BinaryTreeNodeClass import Node


def breadth_first_values(root):
    if not root: 
        return []

    queue = [root]
    values = []

    while queue:
        node = queue.pop(0) # not recommended (n)
        values.append(node.value)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return values




# n = number of nodes
# Time: O(n)
# Space: O(n)
# using deque (double ended queue)
from collections import deque

def breadth_first_values_2(root):
  if not root:
    return []
  
  queue = deque([root])
  values = []
  
  while queue:
    node = queue.popleft()
    
    values.append(node.value)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return values


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    print(breadth_first_values(a))
    print(breadth_first_values_2(a))
