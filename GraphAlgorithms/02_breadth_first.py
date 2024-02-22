# breadth first we use queue as data-structure and solve it iterativaly

from collections import deque

def depth_first(graph, source):
    queue = deque([source])
    visited_nodes = []

    while queue:
        current = queue.popleft()  # popleft() remove from the front (left)
        print(current)
        visited_nodes.append(current) # add to the back (right)
        for neighbor in graph[current]:
            queue.append(neighbor)  # add to the back (right)

    return visited_nodes


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}  # directed graph



if __name__ == '__main__':
    visited_nodes = depth_first(graph, 'a')
    print(visited_nodes)

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
