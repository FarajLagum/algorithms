class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Floyd’s cycle-finding algorithm 
def has_cycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    # slow = head
    fast = head.next

    while head != fast:
        if not fast or not fast.next:
            return False
        head = head.next
        fast = fast.next.next

    return True



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

'''
Time complexity: The time complexity is O(n)
In the worst case scenario, we have to traverse all nodes once.


Space complexity: The space complexity is O(1)
, as we only use two pointers regardless of the size of the linked list.
'''