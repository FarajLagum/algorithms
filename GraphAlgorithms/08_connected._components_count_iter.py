def connected_components_count(graph):
    visited = set()
    counter = 0

    for node in graph.keys():
        if node in visited:
            continue
        stack = [node]
        while stack:
            current = stack.pop()
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
        counter += 1
    return counter

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
