def combination(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r) # nCr = (n-1)C(r-1) + (n-1)C(r) + 

n = 10
r = 3
print(f"The number of combinations of {r} items from a set of {n} items is {combination(n, r)}.")
