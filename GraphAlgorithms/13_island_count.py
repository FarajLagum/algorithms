# similar to connected components count
'''
island count
Write a function, island_count, that takes in a grid containing Ws and Ls. 
W represents water and L represents land. The function should return the number of islands on the grid. 
An island is a vertically or horizontally connected region of land.
'''

# is_invalid_index
# is_invalid_position
# is_out_range
# is_illegal_position
# is_out_grid_bounds
# is_not_safe_index
# is_invalid_cell
def is_out_bounds(grid, row, coloumn):
    return row < 0 or row >= len(grid) or coloumn < 0 or coloumn >= len(grid[0])


def explore_dfs(grid, row, coloumn, visited):
        if is_out_bounds(grid, row, coloumn):
            return False

        if grid[row][coloumn] == 'W':
            return False

        current_pos = (row, coloumn) # you can present the visited nodes as string as f"{row},{coloumn}"
        
        if current_pos in visited:
            return False
        visited.add(current_pos)

        explore_dfs(grid, row - 1, coloumn, visited)  # Up
        explore_dfs(grid, row + 1, coloumn, visited)  # Down
        explore_dfs(grid, row, coloumn - 1, visited)  # Left
        explore_dfs(grid, row, coloumn + 1, visited)  # Right
        return True

def island_count(grid):
    visited = set()    

    count = 0
    for row in range(len(grid)):
        for coloumn in range(len(grid[0])):
            #print(row, coloumn)
            if explore_dfs(grid, row, coloumn, visited):
                count += 1

    return count



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

print(island_count(grid0))  
#print(len(grid3[1]))
