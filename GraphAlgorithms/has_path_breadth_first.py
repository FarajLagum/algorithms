# breadth first we use queue as data-structure and solve it iterativaly

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}  # directed graph


def depth_first(graph, source, destination):
    queue_list = [source]
    visited_nodes = []

    while len(queue_list) > 0:
        current_source = queue_list.pop(0)  # popleft()
        print(current_source)
        if current_source == destination:
            return True
        visited_nodes.append(current_source)
        for neighbor in graph[current_source]:
            queue_list.append(neighbor)

    return False


if __name__ == '__main__':
    visited_nodes = depth_first(graph, 'a', "c")
    print(visited_nodes)

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
