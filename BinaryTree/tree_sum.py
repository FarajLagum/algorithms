'''
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
The function should return the total sum of all values in the tree.
'''

# n = number of nodes
# Time: O(n)
# Space: O(n)
from collections import deque


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
