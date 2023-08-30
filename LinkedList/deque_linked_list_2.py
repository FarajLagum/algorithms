
from collections import deque

linked_list_01 = deque()
# Using append() to add single item at right
linked_list_01.append('Germany')
print(linked_list_01)

# Using appendleft() to add single item at left
linked_list_01.appendleft('Canada')
print(linked_list_01)

# Using extend() to add item at right
linked_list_01.extend(['Spain', 'France'])
print(linked_list_01)

# Using extendleft() to add item at left
linked_list_01.extendleft(['US', 'China'])
print(linked_list_01)

# Insert at index 0 using insert()
linked_list_01.insert(0,'Mexico')

# Insert at last using insert()
linked_list_01.insert(len(linked_list_01),'Egypt')

# Insert at particular position using insert()
linked_list_01.insert(5,'Germany')
print(linked_list_01)

# list the contents of the linked list
print(list(linked_list_01))

# list the contents of a linked list in reverse
print(list(reversed(linked_list_01)))

# return and remove the rightmost item
print(linked_list_01.pop())
print(linked_list_01)


# return and remove the leftmost item
print(linked_list_01.popleft())
print(linked_list_01)

