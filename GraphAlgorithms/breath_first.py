# stach data structure is the best suties for depth_first
# directed graph
import queue


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def depth_first(graph, source):
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


if __name__ == '__main__':
    depth_first(graph, 'a')
