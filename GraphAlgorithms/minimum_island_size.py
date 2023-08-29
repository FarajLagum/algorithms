# https://youtu.be/tWVWeAqZ0WU?si=iqH6u68XihX06gfv&t=7145

def explore_size(grid, row, coloumn, visited):
    if row < 0 or row >= len(grid) or coloumn < 0 or coloumn >= len(grid[0]):
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

def minimum_island(grid):
    visited = set()

    min_size = float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if 0 < size < min_size:
                min_size = size

    if min_size == float('inf'):
        return -1  # return -1 if there is no island

    return min_size

grid = [
    ['W', 'W'],
    ['W', 'W'],
    ['W', 'W']
] # Output: -1  

print(minimum_island(grid))  
