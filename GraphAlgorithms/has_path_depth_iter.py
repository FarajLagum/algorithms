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

    while len(stack) > 0:
        current_source = stack.pop()
        print(current_source)
        if current_source == destination:
            return True
        for neighbor in graph[current_source]:
            stack.append(neighbor)

    return False


if __name__ == '__main__':
    #graph = {}
    flag = has_path(graph, 'a', "c")
    print(flag)

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
