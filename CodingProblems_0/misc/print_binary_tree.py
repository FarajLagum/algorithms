class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printBinaryTree(root):
    if not root:
        return

    queue = [root]

    while queue:
        current_level = []
        next_level = []

        for node in queue:
            if node:
                current_level.append(node.val)
                next_level.extend([node.left, node.right])

        if current_level:
            print(" ".join(map(str, current_level)))

        queue = next_level


# Driver code
if __name__ == "__main__":
    # # Creating a binary tree with three levels
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
    print("Binary tree:")
    printBinaryTree(root)
