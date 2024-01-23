def dijkstra(graph, start_node):
    # Create a dictionary to store the shortest distances
    distances = {node: float('infinity') for node in graph}
    print(distances)
    distances[start_node] = 0

    # Create a set to keep track of visited nodes
    visited = set()

    while len(visited) < len(graph):
        # Find the node with the smallest known distance
        min_node = None
        for node in graph:
            print(node)
            if node not in visited:
                if min_node is None:
                    min_node = node
                elif distances[node] < distances[min_node]:
                    min_node = node

        # Calculate the distances through the current node
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Mark the current node as visited
        # print(min_node)
        visited.add(min_node)

    return distances


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

graph = {
    'A': {'B': 3, 'C': 2, 'D': 5},
    'B': {'A': 3, 'D': 2, 'F': 13},
    'C': {'A': 2, 'D': 2, 'E': 5},
    'D': {'A': 5, 'B': 2, 'C': 2, 'E': 4, 'F': 6, 'G': 3},
    'E': {'C': 5, 'D': 4, 'G': 6},
    'F': {'B': 13, 'D': 6, 'G': 2, 'H': 3},
    'G': {'D': 3, 'E': 6, 'F': 2, 'H': 6},
    'H': {'F': 3, 'G': 6},
}

start_node = 'A'

shortest_distances = dijkstra(graph, start_node)
# print(shortest_distances)

end_node = "H"
print(shortest_distances[end_node])


print("Shortest distances from", start_node, "to",
      end_node, "=", shortest_distances[end_node])


# print(shortest_distances.items())
print("========================================")
print("Shortest distances from", start_node, "to")

for node, distance in shortest_distances.items():
    print(node, "=", distance)
