# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def has_path_sum(root, targetSum: int) -> bool:
    if not root:
        return False
    
    if not root.left and not root.right:
        return targetSum == root.val
    
    left_sum = has_path_sum(root.left, targetSum - root.val)
    right_sum = has_path_sum(root.right, targetSum - root.val)
    
    return left_sum or right_sum

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

print(has_path_sum(p, 22))  # Output: True

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

print(has_path_sum(p, 5))  # Output: False

print(has_path_sum(None, 0))  # Output: False