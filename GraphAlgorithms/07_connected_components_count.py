'''
connected components count
Write a function, connected_components_count, that takes a graph. 
The function should return the number of connected 
components within the graph.
'''


def connected_components_count(graph):
    visited = set()
    counter = 0

    for node in graph.keys():
        #print(node)
        if explore_nodes(graph, node, visited) == True:
            counter += 1
    return counter



def explore_nodes(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)

    for neighbor in graph[current]:
        explore_nodes(graph, neighbor, visited)

    return True


test1 ={
  '0': ['8', '1', '5'],
  '1': ['0'],
  '5': ['0', '8'],
  '8': ['0', '5'],
  '2': ['3', '4'],
  '3': ['2', '4'],
  '4': ['3', '2']
} # answer=2

test2 ={
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
} # answer=1


test3 = {} # answer=0


test4 = {
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
} # answer -> 5



print(connected_components_count(test4))



# https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=1333s
# https://structy.net/problems/connected-components-count