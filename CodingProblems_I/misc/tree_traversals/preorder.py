# Python3 program to for tree traversals


# A class that represents an individual node
# in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do preorder tree traversal
def print_preorder(root):

    if root:

        # First print the data of node
        print(root.val, end=" "),

        # Then recur on left child
        print_preorder(root.left)

        # Finally recur on right child
        print_preorder(root.right)


# Driver code
if __name__ == "__main__":
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # Creating a binary tree with four levels
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    # Function call
    print("Preorder traversal of binary tree is")
    print_preorder(root)
    print(end="\n")
