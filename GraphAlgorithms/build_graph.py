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

if __name__ == "__main__":
     
     edges = [
    ['i', 'j'], 
    ['k', 'i'], 
    ['m', 'k'], 
    ['k', 'l'], 
    ['o', 'n']
    ]

     graph = build_graph(edges)
     print(graph)