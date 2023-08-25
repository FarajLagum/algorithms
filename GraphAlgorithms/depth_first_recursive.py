# code to implement depth first algorithm

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


def depth_first(graph, source_node):
    print(source_node) # print the starting node
    for neighbor in graph[source_node]:
        depth_first(graph, neighbor)


if __name__ == '__main__':
    # print all nodes in the graph according to depth first algorithm
    depth_first(graph, 'a')

# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
