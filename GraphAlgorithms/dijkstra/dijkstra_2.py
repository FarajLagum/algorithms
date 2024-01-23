def dijkstra(graph, start_node, end_node):
    # Initialize data structures
    solved_nodes = set()
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    arcs = {}

    while end_node not in solved_nodes:
        # Find unsolved nodes with minimum distance
        smallest_candidate_distance = float('inf')
        current_node = None
        for node in graph:
            if node not in solved_nodes and distances[node] < smallest_candidate_distance:
                smallest_candidate_distance = distances[node]
                current_node = node

        if current_node is not None:
            # Update solved nodes
            solved_nodes.add(current_node)

            for neighbor, weight in graph[current_node].items():
                if distances[current_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + weight
                    arcs[neighbor] = current_node

        print(current_node)
        print(solved_nodes)

    return distances, arcs


def find_shortest_path(arcs, end_node):
    # backtrack
    path = []
    while end_node:
        path.insert(0, end_node)
        end_node = arcs.get(end_node, None)
        if end_node:
            end_node = end_node[0]
    return path


# Example usage
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
end_node = "H"

shortest_distances, arcs = dijkstra(graph, start_node, end_node)

shortest_path = find_shortest_path(arcs, end_node)
shortest_distance = shortest_distances[end_node]


print(
    f"Shortest distances from {start_node} to {end_node} = {shortest_distance}")
print(f"Shortest path: {' -> '.join(shortest_path)}")

print(arcs)
