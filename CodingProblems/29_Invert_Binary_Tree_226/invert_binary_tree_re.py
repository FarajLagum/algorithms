
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to invert a binary tree
def invertTree(root: TreeNode) -> TreeNode:
    # Base case: if the root is None, return None
    if root is None:
        return None
    
    # Recursively invert the left and right subtrees
    left = invertTree(root.left)
    right = invertTree(root.right)

    # Swap the left and right children of the root
    root.left = right
    root.right = left

    # Return the inverted root
    return root

def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


# Test Case 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

inverted_root = invertTree(root)

assert inverted_root.val == 4
assert inverted_root.left.val == 7
assert inverted_root.right.val == 2
assert inverted_root.left.left.val == 9
assert inverted_root.left.right.val == 6
assert inverted_root.right.left.val == 3
assert inverted_root.right.right.val == 1
