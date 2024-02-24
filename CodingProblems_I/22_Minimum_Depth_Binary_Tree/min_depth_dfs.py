class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(root):
    if root is None:
        return 0

    node_stack = [root]
    depth_stack = [1]
    min_depth = float('inf')

    while node_stack:
        node = node_stack.pop()
        print(node.val)
        depth = depth_stack.pop()

        if node:
            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
            else:
                if node.left is not None:
                    node_stack.append(node.left)
                    depth_stack.append(depth + 1)
                if node.right is not None:
                    node_stack.append(node.right)
                    depth_stack.append(depth + 1)

    return min_depth

# Test case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print("min depth:", minDepth(root))  # Output: 2

# Test case 2
root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)


print("min depth:", minDepth(root))  # Output: 5

