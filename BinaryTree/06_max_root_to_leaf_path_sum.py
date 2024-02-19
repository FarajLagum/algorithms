from BinaryTreeNodeClass import Node

'''
Write a function, max_path_sum, that takes in the root of a binary tree 
that contains number values. The function should return the maximum sum 
of any root to leaf path within the tree.

You may assume that the input tree is non-empty.
'''

def max_path_sum(root):
  if root is None:
    return float("-inf")

  if root.left is None and root.right is None:
    return root.value

  return root.value + max(max_path_sum(root.left), max_path_sum(root.right))




def max_path_sum_iterative_dfs(root):
    if root is None:
        return float("-inf")

    max_sum = float("-inf")
    current_sum = root.value
    stack = [(root, current_sum)]

    while stack:
        node, current_sum = stack.pop()
        
        if node.left is None and node.right is None:  # If it's a leaf node
            max_sum = max(max_sum, current_sum)
        
        if node.left:
            stack.append((node.left, current_sum + node.left.value))
        if node.right:
            stack.append((node.right, current_sum + node.right.value))

    return max_sum






from collections import deque


def max_path_sum_iterative_bfs(root):
    if root is None:
        return float("-inf")

    max_sum = float("-inf")
    queue = deque([(root, root.value)])

    while queue:
        node, current_sum = queue.popleft()
        
        if node.left is None and node.right is None:  # If it's a leaf node
            max_sum = max(max_sum, current_sum)
        
        if node.left:
            queue.append((node.left, current_sum + node.left.value))
        if node.right:
            queue.append((node.right, current_sum + node.right.value))

    return max_sum




# Creating a binary tree
#        10
#       / \
#      5   20
#     /   / \
#    2   15  30
#           / \
#          25  40
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.right.left = Node(15)
root.right.right = Node(30)
root.right.right.left = Node(25)
root.right.right.right = Node(40)

# Using the max_path_sum function to find the maximum sum of any root to leaf path
print("Maximum sum of any root to leaf path:", max_path_sum(root))
# Using the max_path_sum_iterative_dfs function to find the maximum sum of any root to leaf path
print("Maximum sum of any root to leaf path (iterative DFS):", max_path_sum_iterative_dfs(root))

# Using the max_path_sum_iterative_bfs function to find the maximum sum of any root to leaf path
print("Maximum sum of any root to leaf path (iterative BFS using deque):", max_path_sum_iterative_bfs(root))