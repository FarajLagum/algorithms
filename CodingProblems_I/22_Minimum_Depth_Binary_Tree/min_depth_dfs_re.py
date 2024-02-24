# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(root):
    if root is None:
        return 0
    elif root.left is None:
        return minDepth(root.right) + 1
    elif root.right is None:
        return  minDepth(root.left) + 1
    else:
        return min(minDepth(root.left), minDepth(root.right)) + 1


# Test case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(minDepth(root))  # Output: 2

# Test case 2
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print(minDepth(root))  # Output: 5

