class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_inorder_non_recursive(root):
    stack = []
    current = root

    while stack or current:
        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Visit the top of the stack (current leftmost node)
        current = stack.pop()
        print(current.val, end=" ")

        # Move to the right subtree
        current = current.right


if __name__ == "__main__":
    # Creating a binary tree with four levels
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
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
    print_inorder_non_recursive(root)
    print(end="\n")
