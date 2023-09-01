from BinaryTreeNodeClass import Node
from collections import deque

'''
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. 
The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
'''


def tree_min_value_iterative(root):
    min_value = root.value
    queue = deque([root])

    while queue:
        node = queue.popleft()
        # print(node.value)
        if (node.value < min_value):
            min_value = node.value

        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)

    return min_value


def tree_min_value(root):
    if root is None:
        return float("inf")
    smallest_left_value = tree_min_value(root.left)
    smallest_right_value = tree_min_value(root.right)
    return min(root.value, smallest_left_value, smallest_right_value)


def test_00():
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1
    return tree_min_value(a)


if __name__ == "__main__":
    print(test_00())
