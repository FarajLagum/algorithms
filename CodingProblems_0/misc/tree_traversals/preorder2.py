class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_preorder(root):
    if not root:
        return

    stack = [root]

    while stack:
        current_node = stack.pop()
        print(current_node.val, end=" ")

        # Push the right child first so that it is processed after the left child
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)


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
