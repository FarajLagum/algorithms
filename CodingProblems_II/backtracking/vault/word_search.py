def is_valid_word(word, k): 
    return k == len(word) - 1

def is_out_of_bounds_or_no_match(board, word, i, j, k): # is not valid state?
    checks = not 0 <= i < len(board) or \
        not 0 <= j < len(board[0]) or \
        board[i][j] != word[k] # is the current cell match the current letter id the word
    return checks

def search(board, word, row_index, col_index, letter_index):
    # Check if the current cell is out of bounds or does not match the current letter of the word
    if is_out_of_bounds_or_no_match(board, word, row_index, col_index, letter_index):
        return False
    # Check if we have found the entire word
    if is_valid_word(word, letter_index):
        return True
    
    # Mark the current cell with '_' as visited and  
    original_letter, board[row_index][col_index] = board[row_index][col_index], '_'

    # try to find the next letter of the word in the neighboring cells
    result = search(board, word, row_index + 1, col_index, letter_index + 1) or \
          search(board, word, row_index - 1, col_index, letter_index + 1) or \
          search(board, word, row_index, col_index + 1, letter_index + 1) or \
          search(board, word, row_index, col_index - 1, letter_index + 1)
    
    # Unmark the current cell and return the result
    board[row_index][col_index] = original_letter

    return result


def is_exist(board, word):
    # Iterate over all cells in the board and try to find the word starting from each cell
    for row_index in range(len(board)):
        for col_index in range(len(board[0])):
            if search(board, word, row_index, col_index, letter_index=0):
                return True
    # If the word is not found, return False
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"
print(is_exist(board, word1))  # Output: True
print(is_exist(board, word2))  # Output: True
print(is_exist(board, word3))  # Output: False
