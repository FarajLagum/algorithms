# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node:
                children = [node.left, node.right]
                if not any(children):
                    return depth
                for child in children:
                    if child:
                        queue.append((child, depth + 1))
