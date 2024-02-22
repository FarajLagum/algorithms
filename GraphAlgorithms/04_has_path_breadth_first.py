# breadth first we use queue as data-structure and solve it iterativaly

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}  # directed graph

from collections import deque

def has_path(graph, source, destination):
    queue = deque(source)
    visited_nodes = [] # in case we want to return the path

    while queue:
        current = queue.popleft()  # popleft()
        print(current)
        if current == destination:
            return True
        visited_nodes.append(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

    return         


if __name__ == '__main__':
    flag = has_path(graph, 'a', "c")
    print(flag)

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
