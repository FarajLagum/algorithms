def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or \
                board[i][col] == num or \
                board[3*(row//3)+i//3][3*(col//3)+i%3] == num:
                return False
        return True

def search(empty):
    if not empty:
        return True
    row, col = empty[-1]
    for num in range(1, 10):
        if is_valid(row, col, str(num)):
            board[row][col] = str(num)
            empty.pop()
            if search(empty):
                return True
            board[row][col] = '.'
            empty.append((row, col))
    return


def solve_sudoku(board):
    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']
    #print(empty)
    search(empty_cells)
    return board

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solve_sudoku(board)
print(board)


'''
[
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'], 
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'], 
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'], 
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'], 
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'], 
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'], 
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'], 
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'], 
    ['3', '4', '5', '2', '8', '6', '1', '7', '9']
]
'''