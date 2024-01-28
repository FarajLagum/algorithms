# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)



# Test case 1
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(is_same_tree(p, q))  # Output: True

# Test case 2
p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
q.right = TreeNode(2)

print(is_same_tree(p, q))  # Output: False

# Test case 3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)

q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)

print(is_same_tree(p, q))  # Output: False

