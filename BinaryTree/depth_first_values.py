'''
Write a function, depth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in depth-first order
'''

from BinaryTreeNodeClass import Node


def depth_first_values(root):
    if root is None or root is []: # if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values




# n = number of nodes
# Time: O(n)
# Space: O(n)
# recursive
def depth_first_values_recursive(root):
  if not root:
    return []
  
  left_values = depth_first_values_recursive(root.left)
  right_values = depth_first_values_recursive(root.right)
  # return [root.val, *left_values, *right_values]
  return [root.value] + left_values + right_values



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

    print(depth_first_values(a))
    print(depth_first_values_recursive(a))
