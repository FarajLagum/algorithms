edges0 = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
] # -> 2

edges1 = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
] # -> 1

edges2 = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
] #  -> 3

edges3 = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
] # -> 2

edges4 = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
] # -> -1

edges5 = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
] # -> 1

edges6 = [
  ['c', 'n'],
  ['c', 'e'],
  ['c', 's'],
  ['c', 'w'],
  ['w', 'e'],
] # -> 2


edges7 = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
] # -> 6

from build_graph import build_graph



def shortest_path(edges, src, dst):
    graph = build_graph(edges)
    visited = {src}
    queue = [(src, 0)] # list of Tuples 
    
    while queue:
        node, distance = queue.pop(0)
        
        if node == dst:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1


if __name__ == "__main__":
    print(shortest_path(edges0, 'w', 'z'))
    print(shortest_path(edges1, 'y', 'x'))
    print(shortest_path(edges2, 'a', 'e'))
    print(shortest_path(edges3, 'e', 'c'))
    print(shortest_path(edges4, 'b', 'g')) # -> -1
    print(shortest_path(edges5, 'w', 'e')) # -> 1
