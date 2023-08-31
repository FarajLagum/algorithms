
def factorial(n):

    if n < 0:
        raise ValueError("No factorial for negative numbers")

    if n == 0:
        return 1
    return n*factorial(n-1)

print(factorial(-2))