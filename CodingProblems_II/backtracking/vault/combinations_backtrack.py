result = []

def backtrack(start, curr_comb, n, r):
    if len(curr_comb) == r:
        result.append(curr_comb.copy())
        return
    for i in range(start, n + 1):
        curr_comb.append(i)
        backtrack(i + 1, curr_comb, n, r)
        curr_comb.pop()


def combination(n, r):

    backtrack(1, [], n, r) # start = 1 -> range = [1 --> 5] inclusive
    return result
n = 5
r = 3

result = combination(n, r)
print(result)
n_comb = len(result)


print(f"The number of combinations of {r} items from a set of {n} items is {n_comb}.")
