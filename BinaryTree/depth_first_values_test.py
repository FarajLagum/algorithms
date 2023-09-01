from BinaryTreeNodeClass import Node
from depth_first_values import depth_first_values, depth_first_values_recursive


def test_depth_first_values_empty_tree():
    assert depth_first_values(None) == []
    assert depth_first_values_recursive(None) == []


def test_depth_first_values_single_node():
    root = Node('a')
    assert depth_first_values(root) == ['a']
    assert depth_first_values_recursive(root) == ['a']


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
    assert depth_first_values_recursive(a) == ['a', 'b', 'd', 'e', 'c', 'f']


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

<<<<<<< Updated upstream
    assert depth_first_values(a) == ['a', 'b', 'd', 'e', 'g', 'c', 'f']
    assert depth_first_values_recursive(a) == ['a', 'b', 'd', 'e', 'g', 'c', 'f']
=======
    result = depth_first_values(a)
    assert result == ['a', 'b', 'd', 'e', 'g', 'c', 'f']
    # Optional: Individual node value checks
    assert result[0] == 'a'
    assert result[1] == 'b'
    assert result[2] == 'd'
    assert result[3] == 'e'
    assert result[4] == 'g'
    assert result[5] == 'c'
    assert result[6] == 'f'
>>>>>>> Stashed changes


def test_02():
    a = Node('a')

    assert depth_first_values(a) == ['a']
    assert depth_first_values_recursive(a) == ['a']


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
    assert depth_first_values_recursive(a) == ['a', 'b', 'c', 'd', 'e']
