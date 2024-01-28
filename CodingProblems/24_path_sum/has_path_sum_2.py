# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def hasPathSum(root, targetSum):
    if root is None:
        return False
    if root.left is None and root.right is None and root.val == targetSum:
        return True
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

# Test case examples
p = TreeNode(5)
p.left = TreeNode(4)
p.left.left = TreeNode(11)
p.left.left.left = TreeNode(7)
p.left.left.right = TreeNode(2)
p.right = TreeNode(8)
p.right.left = TreeNode(13)
p.right.right = TreeNode(4)
p.right.right.right = TreeNode(1)

print(hasPathSum(p, 22))  # Output: True

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

print(hasPathSum(p, 5))  # Output: False

print(hasPathSum(None, 0))  # Output: False
