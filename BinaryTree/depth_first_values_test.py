from depth_first_values import depth_first_values
from BinaryTreeNodeClass import Node


def test_00():

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
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

    assert depth_first_values(a) == ['a', 'b', 'd', 'e', 'c', 'f']
