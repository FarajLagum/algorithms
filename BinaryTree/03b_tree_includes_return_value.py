from BinaryTreeNodeClass import Node



def tree_includes_target(root, target):
    if not root:
        return None

    if root.value == target:
        return target

    return tree_includes_target(root.left, target) or tree_includes_target(root.right, target)



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

print(tree_includes_target(a, "e"))  # --> True
print(tree_includes_target(a, "f"))  # --> True


