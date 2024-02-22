edges = [
    ['i', 'j'], 
    ['k', 'i'], 
    ['m', 'k'], 
    ['k', 'l'], 
    ['o', 'n']
    ]

def build_graph(edges):
    '''
    convert edges list to adjacency list
    '''
    graph = {}

    for edge in edges:
        a, b  = edge
        #print(a, b)
        
        if a not in graph:
             #print(a, 'not in graph yet')
             graph[a] = []
        if b not in graph:
             graph[b] = []

        graph[a].append(b) # = [b]
        graph[b].append(a)
    
    return graph


graph = build_graph(edges)
#print(graph)


def undirected_path(edges, node_a, node_b):
     graph = build_graph(edges=edges)
     visited = set()
     return has_path(graph, node_a, node_b, visited)


def has_path(graph, source, destination, visited):
    if source == destination:
         return True
    
    if source in visited:
         return False
    visited.add(source)

    for neighbor in graph[source]:
         if has_path(graph, neighbor, destination, visited):
               return True
    return False
          



print(undirected_path(edges, 'j', 'm'))
