def search(left_count, close_count, state, result):
    # If we've used all open and close parentheses, the path is a valid combination.
    if left_count == 0 and close_count == 0:
        result.append(state)
        return
    # If we have not used all open parentheses, we can add an open parenthesis.
    if left_count > 0:  
        state = state + '(' # Mark
        left_count -=1 # decrement 
        search(left_count, close_count, state, result)
        left_count +=1 # increment -- backtrack
        state = state[:-1]  # Unmark -- Remove the last character

    # If we have more close parentheses left than open parentheses, we can add a close parenthesis.
    if close_count > left_count:
        search(left_count, close_count - 1, state + ')', result)

def generateParenthesis(n_pairs):
    result = []
    state = ''
    open_count, close_count = n_pairs, n_pairs 
    # We start the search with n open and close parentheses, and an empty path and result.
    search(open_count, close_count, state, result)
    # We return the result, which contains all combinations of well-formed parentheses.
    return result

# We test the generateParenthesis function with some inputs.
print(generateParenthesis(3))  # Expected output: ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1))  # Expected output: ["()"]