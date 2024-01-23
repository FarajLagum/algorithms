import heapq


def dijkstra(graph, start):
    # Create a dictionary to store the distance to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Create a priority queue to keep track of vertices to visit
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip this iteration if we've already processed this vertex
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If we've found a shorter path to the neighbor, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    print(priority_queue)

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

start_vertex = 'A'

shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from", start_vertex)
for vertex, distance in shortest_distances.items():
    print(vertex, ":", distance)
