def is_valid(row, col, num):
        for index in range(9):
            # validate all the rows
            if board[row][index] == num:
                return False
            # validate columns
            if board[index][col] == num:
                return False
            # validate sub-boxes
            # sub_box_row = 3 * (row // 3) + index//3
            # sub_box_col = 3 * (col//3) + index%3
            # print(sub_box_row, sub_box_col) 
            if board[3 * (row // 3) + index//3][3 * (col//3) + index%3] == num: 
                return False
        return True

def search(remaning):
    if not remaning: #if empty 
        return #True
    (row, col) = remaning[-1]
    for num in range(1, 10):
        if is_valid(row, col, num):
            board[row][col] = num
            remaning.pop() # mark as solved
            search(remaning)
            if not remaning: # if empty 
                return #True
            board[row][col] = '.'
            remaning.append((row, col)) #unmark
    #return


def solve_sudoku(board):
    remaning = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']
    print(remaning)
    search(remaning)
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