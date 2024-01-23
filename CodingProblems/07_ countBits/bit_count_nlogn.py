def countOnes(x):
        total = 0
        while x:
            total += x % 2
            x >>= 1
        return total

def countBits(n):
    return [countOnes(i) for i in range(n+1)]


print(countBits(2))


