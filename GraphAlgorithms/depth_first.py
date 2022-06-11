# stach data structure is the best suties for depth_first
# directed graph
graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "f": []
}


def depth_first(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


if __name__ == '__main__':
    depth_first(graph, 'a')
