# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
        # Left, root, right
def print_inorder(root):

    if root:

        # First recur on left child
        print_inorder(root.left)  # current node

        # Then print the data of node
        print(root.val, end=" "),  # current node

        # Now recur on right child
        print_inorder(root.right)  # current node


# Driver code
if __name__ == "__main__":
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
    print("Inorder traversal of binary tree is")
    print_inorder(root)
    print(end="\n")
# crete a tree leves tree as a test case


'''


1. **Base Case**: If the current node (`root`) is `None`, the function returns without doing anything. 


2. **Recursive Case**: If the current node is not `None`, the function performs the following steps:
    - First, it makes a recursive call to `print_inorder(root.left)`. 
    This means it will traverse the left subtree of the current node.

    - After the left subtree has been fully traversed, 
      it prints the value of the current node using `print(root.val, end=" ")`.

    - Finally, it makes a recursive call to `print_inorder(root.right)`, 
      which means it will traverse the right subtree of the current node.


'''
