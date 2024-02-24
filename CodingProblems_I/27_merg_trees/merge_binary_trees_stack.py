class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees(root1, root_2):
    if root1 is None:
        return root_2
    stack = [(root1, root_2)]
    while stack:
        root = stack.pop()
        if root[0] is None or root[1] is None:
            continue
        root[0].val += root[1].val
        if root[0].left is None:
            root[0].left = root[1].left
        else:
            stack.append((root[0].left, root[1].left))
        if root[0].right is None:
            root[0].right = root[1].right
        else:
            stack.append((root[0].right, root[1].right))
    return root1
