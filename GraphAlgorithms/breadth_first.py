# breadth first we use queue as data-structure and solve it iterativaly

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}  # directed graph


def depth_first(graph, source):
    queue = [source]
    visited_nodes = []

    while len(queue) > 0:
        current = queue.pop(0)  # popleft() remove from the front (left)
        print(current)
        visited_nodes.append(current) # add to the back (right)
        for neighbor in graph[current]:
            queue.append(neighbor)  # add to the back (right)

    return visited_nodes


if __name__ == '__main__':
    visited_nodes = depth_first(graph, 'a')
    print(visited_nodes)

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
