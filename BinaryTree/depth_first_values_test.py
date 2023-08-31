from depth_first_values import depth_first_values
from BinaryTreeNodeClass import Node


def test_depth_first_values_empty_tree():
    assert depth_first_values(None) == []


def test_depth_first_values_single_node():
    root = Node('a')
    assert depth_first_values(root) == ['a']


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


def test_01():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    result = depth_first_values(a)
    assert result == ['a', 'b', 'd', 'e', 'g', 'c', 'f']


def test_02():
    a = Node('a')

    assert depth_first_values(a) == ['a']


def test_03():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    a.right = b
    b.left = c
    c.right = d
    d.right = e

    #      a
    #       \
    #        b
    #       /
    #      c
    #       \
    #        d
    #         \
    #          e

    assert depth_first_values(a) == ['a', 'b', 'c', 'd', 'e']
