class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0
    else:
        left_height = max_depth(root.left)
        right_height = max_depth(root.right)
        return 1+ max(left_height, right_height)

# Test case examples
p = TreeNode(3)
p.left = TreeNode(9)
p.right = TreeNode(20)
p.right.left = TreeNode(15)
p.right.right = TreeNode(7)

print(max_depth(p))  # Output: 3

p = TreeNode(1)
p.right = TreeNode(2)

print(max_depth(p))  # Output: 2

print(max_depth(None))  # Output: 0
