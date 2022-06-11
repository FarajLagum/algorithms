# stach data structure is the best suties for depth_first
# directed graph
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def depth_first(graph, source):
    print(source)
    for neighbor in graph[source]:
        depth_first(graph, neighbor)


if __name__ == '__main__':
    depth_first(graph, 'a')
