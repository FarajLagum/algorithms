class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def has_path_sum(root, targetSum):
    if not root:
        return False

    stack = [(root, targetSum - root.val), ]
    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.left:
            stack.append((node.left, curr_sum - node.left.val))
        if node.right:
            stack.append((node.right, curr_sum - node.right.val))
    return False

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
