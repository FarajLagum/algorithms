# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to invert a binary tree iteratively using a stack
def invertTree(root: TreeNode) -> TreeNode:
    # Base case: if the root is None, return None
    if root is None:
        return None
    
    # Create a stack and push the root node
    stack = [root]

    # Loop until the stack is empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # Swap the left and right children of the node
        node.left, node.right = node.right, node.left

        # Push the left and right children of the node to the stack if they are not None
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    # Return the inverted root
    return root
