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


def depth_first(graph, source):
    stack = [source]

    while len(stack) > 0: # while stack: # works well
        current = stack.pop()
        print(current)
        for neighbor in graph[current]: # graph[current] returns the list of neighbor nodes
            stack.append(neighbor)  # append is a push to the top of the stack


if __name__ == '__main__':
    depth_first(graph, 'a') # out: abdfce


# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
