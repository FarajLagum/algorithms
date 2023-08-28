
test_1 = {
  '0': ['8', '1', '5'],
  '1': ['0'],
  '5': ['0', '8'],
  '8': ['0', '5'],
  '2': ['3', '4'],
  '3': ['2', '4'],
  '4': ['3', '2']
} # ans = 4

def largest_component(graph):
    visited = set()
    longest = 0

    for node in graph.keys():
        #print(node)
        size = explore_size(graph, node, visited)
        if size > longest:
            longest = size
    return longest




def explore_size(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size =1 

    for neighbor in graph[node]:
        s = explore_size(graph, neighbor, visited)
        size = size + s

    return size

print(largest_component(test_1))

# https://youtu.be/tWVWeAqZ0WU?si=CzLSHNfUGZjK4tNk&t=4413
# https://structy.net/problems/largest-component