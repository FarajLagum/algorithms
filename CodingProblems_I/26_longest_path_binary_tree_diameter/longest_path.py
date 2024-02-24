class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0

    def depth(node):
        nonlocal diameter
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)

        # Update the diameter at each node
        diameter = max(diameter, left_depth + right_depth)

        # Return the depth of the current node
        return 1 + max(left_depth, right_depth)

    depth(root)
    return diameter

# Example usage:
# Construct the binary tree from the given input
# Input: [1, 2, 3, 4, 5]
# Output: 3
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
result = diameterOfBinaryTree(tree)
print(result)
