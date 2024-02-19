'''
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
The function should return the total sum of all values in the tree.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# n = number of nodes
# Time: O(n)
# Space: O(n)
from collections import deque


def tree_sum_depth_first_iterative(root):
    sum = 0
    if not root:
        return sum
    
    
    stack =[root]

    while stack:
        node = stack.pop()
        sum +=node.val
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return sum

def tree_sum_depth_first(root):
    if root is None:
        return 0
    return root.val + tree_sum_depth_first(root.left) + tree_sum_depth_first(root.right)


# breadth first
def tree_sum(root):
    if not root:
        return 0

    queue = deque([root])
    total_sum = 0
    while queue:
        node = queue.popleft()

        total_sum += node.val

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return total_sum




# Creating a binary tree
#        5
#       / \
#      3   8
#     / \   \
#    2   4   10
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(10)

# Using the tree_sum function to find the sum of all values in the tree
print("Total sum of all values in the tree:", tree_sum(root))

print("Total sum of all values in the tree:", tree_sum_depth_first_iterative(root))


