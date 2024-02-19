from BinaryTreeNodeClass import Node
from collections import deque

'''
Write a function, tree_includes, that takes in the root of a binary tree and a target value. 
The function should return a boolean indicating whether or not the value is contained in the tree.
'''


def tree_includes_depth_first_iterative(current, target):
    if not current:
        return False

    stack = [current]

    while stack:
        if current.value == target:
            return True

        if current.right: # if current.right is not None
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        current = stack.pop()

    return False


def tree_includes_depth_first_recursive(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    return tree_includes_depth_first_recursive(root.left, target) or tree_includes_depth_first_recursive(root.right, target)


def tree_includes_breadth_first(root, target):
    if not root:
        return False

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.val == target:
            return True

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return False


def test_00():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    return tree_includes_depth_first_iterative(a, "e")  # --> True


if __name__ == "__main__":
    print(test_00())
