class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTrees(t1, t2):
    if t1 is None:
        return t2
    queue = [(t1, t2)]
    while queue:
        node1, node2 = queue.pop(0)
        if node1 is None or node2 is None:
            continue
        node1.val += node2.val
        if node1.left is None:
            node1.left = node2.left
        else:
            queue.append((node1.left, node2.left))
        if node1.right is None:
            node1.right = node2.right
        else:
            queue.append((node1.right, node2.right))
    return t1
