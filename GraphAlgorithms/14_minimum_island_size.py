# https://youtu.be/tWVWeAqZ0WU?si=iqH6u68XihX06gfv&t=7145
'''
minimum island
Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.
'''
def explore_size(grid, row, coloumn, visited):
    if is_out_bounds(grid, row, coloumn):
        return 0
    
    if grid[row][coloumn] == 'W':
        return 0
    
    current_pos = (row, coloumn) # f"{row},{coloumn}"
    
    if current_pos in visited:
        return 0
    
    visited.add(current_pos)
    size = 1

    size += explore_size(grid, row - 1, coloumn, visited)
    size += explore_size(grid, row + 1, coloumn, visited)
    size += explore_size(grid, row, coloumn - 1, visited)
    size += explore_size(grid, row, coloumn + 1, visited)
    return size

def is_out_bounds(grid, row, coloumn):
    return row < 0 or row >= len(grid) or coloumn < 0 or coloumn >= len(grid[0])

def minimum_island(grid):
    visited = set()

    min_size = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore_size(grid, row, col, visited)
            if 0 < size < min_size:
                min_size = size

    if min_size == float('inf'):
        return 0  # return 0 if there is no island

    return min_size


grid0 = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

grid1 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]


grid2 = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

grid3=[['W', 'W'],
       ['W', 'W'],
       ['W', 'W']] # Output: 0



grid4=[['W']] # Output: 0


grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W']
] # Output: 0 

print(minimum_island(grid0))  
