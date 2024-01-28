class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)
    return root1

# Test case examples
p1 = TreeNode(1)
p1.left = TreeNode(3)
p1.left.left = TreeNode(5)
p1.right = TreeNode(2)

p2 = TreeNode(2)
p2.left = TreeNode(1)
p2.right = TreeNode(3)
p2.left.right = TreeNode(4)
p2.right.right = TreeNode(7)

merged_tree = mergeTrees(p1, p2)
print(merged_tree.val)  # Output: 3
print(merged_tree.left.val)  # Output: 4
print(merged_tree.right.val)  # Output: 5
print(merged_tree.left.left.val)  # Output: 5
print(merged_tree.left.right.val)  # Output: 4
print(merged_tree.right.right.val)  # Output: 7

p1 = TreeNode(1)
p2 = TreeNode(1)
p2.right = TreeNode(2)

merged_tree = mergeTrees(p1, p2)
print(merged_tree.val)  # Output: 2
print(merged_tree.right.val)  # Output: 2
