# stach data structure is the best suties for depth_first
# directed graph
graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def has_path(graph, source, destination):

    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        if current == destination:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)

    return False


if __name__ == '__main__':
    #graph = {}
    flag = has_path(graph, 'a', "c")
    print(flag)

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
