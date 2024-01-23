class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: ListNode) -> bool:
    nodes = []
    while head:
        if head in nodes:
            return True
        nodes.append(head)
        head = head.next
    return False



# Create nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Connect nodes to form a linked list with a cycle
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates a cycle where the tail connects to the 1st node (0-indexed)



# Test the hasCycle method
print(has_cycle(node1))  # Should print True

''''
In terms of complexity analysis:

Time complexity: The time complexity is O(n^2)
This is because for each node, we check whether it is in the list of visited nodes.

Space complexity: The space complexity is O(n)
we have to store all nodes in the list.
'''