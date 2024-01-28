# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to invert a binary tree iteratively
def invertTree(root: TreeNode) -> TreeNode:
    # Base case: if the root is None, return None
    if root is None:
        return None
    
    # Create a queue and enqueue the root
    queue = [root]

    # Loop until the queue is empty
    while queue:
        # Dequeue the front node
        node = queue.pop(0)

        # Swap the left and right children of the node
        node.left, node.right = node.right, node.left

        # Enqueue the left and right children if they are not None
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    # Return the inverted root
    return root
