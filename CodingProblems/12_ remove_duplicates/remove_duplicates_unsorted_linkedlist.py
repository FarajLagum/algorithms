def delete_duplicates_unsorted(head):
    if head is None:
        return head

    node_set = set([head.val])
    current = head
    while current.next:
        if current.next.val in node_set:
            current.next = current.next.next
        else:
            node_set.add(current.next.val)
            current = current.next
    return head
'''
The time complexity of the function for an unsorted list is not strictly O(n), 
due to the time taken for set operations.

In Python, the average time complexity for checking if an element is in a set (the `in` operation) is O(1). 
However, in the worst-case scenario, it can be O(n). 
Therefore, if we consider the worst-case scenario, 
the time complexity of the function could be O(n^2).

But, in practice, the time complexity is often considered as O(n) 
because the hash table structure of the set in Python usually allows 
for very fast lookup times. 
This is under the assumption of simple uniform hashing, 
which means that every key is equally likely to be placed into each slot in the table, 
making collisions (which cause the slowdown) relatively rare.

So, while it's important to be aware of the worst-case scenario, 
for practical purposes and with large datasets, 
the time complexity is often considered to be O(n).

'''


def delete_duplicates_unsorted(head):
    if head is None:
        return head

    node_dict = {head.val: True}
    current = head
    while current.next:
        if current.next.val in node_dict:
            current.next = current.next.next
        else:
            node_dict[current.next.val] = True
            current = current.next
    return head


'''
The time complexity for this approach is the same as the set-based approach. 
The average case is O(n) due to the average O(1) lookup time for Python dictionaries, 
but the worst-case time complexity could be O(n^2) due to potential hash collisions. 
The space complexity is O(n) for storing the unique elements in the dictionary.
'''