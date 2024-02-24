

def countBits(n):
    # Initialize result array with 0's
    ans = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # If i is even, number of set bits = number of set bits in i // 2
        # If i is odd, number of set bits = 1 + number of set bits in i // 2
        ans[i] = ans[i // 2] + (i % 2)
    
    return ans

# Example usage:
n1 = 2
print(countBits(n1))  # Output: [0, 1, 1]

n2 = 5
print(countBits(n2))  # Output: [0, 1, 1, 2, 1, 2]

