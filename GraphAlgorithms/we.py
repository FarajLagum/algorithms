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

# Initialize an empty list to store edges
edges_with_weights = []

# Iterate through the nodes and their neighbors to extract edges and weights
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        edges_with_weights.append((node, neighbor, weight))

# Print the list of edges with weights
for edge in edges_with_weights:
    print(edge)


# Initialize an empty dictionary to store edges with weights
edges_with_weights = {}

# Iterate through the nodes and their neighbors to extract edges and weights
for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
        edge = (node, neighbor)
        edges_with_weights[edge] = weight

# Print the dictionary of edges with weights
for edge, weight in edges_with_weights.items():
    print(edge, ":", weight)
