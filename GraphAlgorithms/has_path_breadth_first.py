# breadth first we use queue as data-structure and solve it iterativaly

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}  # directed graph


def has_path(graph, source, destination):
    queue = [source]
    visited_nodes = []

    while len(queue) > 0:
        current_source = queue.pop(0)  # popleft()
        print(current_source)
        if current_source == destination:
            return True
        visited_nodes.append(current_source)
        for neighbor in graph[current_source]:
            queue.append(neighbor)

    return         


if __name__ == '__main__':
    flag = has_path(graph, 'a', "c")
    print(flag)

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
