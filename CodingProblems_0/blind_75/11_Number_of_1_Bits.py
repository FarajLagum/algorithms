
'''
191. Number of 1 Bits
Topics
Companies
Write a function that takes the binary representation of an unsigned integer and 
returns the number of '1' bits it has (also known as the Hamming weight).
'''
def hammingWeight(n):
    count = 0
    while n != 0:
        count += n & 1  # Add LSB to count if it's 1
        n >>= 1        # Shift input number to the right by one bit
    return count

# Example usage:
n1 = 0b00000000000000000000000000001011
print(hammingWeight(n1))  # Output: 3

n2 = 0b00000000000000000000000010000000
print(hammingWeight(n2))  # Output: 1

n3 = 0b11111111111111111111111111111101
print(hammingWeight(n3))  # Output: 31


# If the number is given as a string representing its binary representation
def hammingWeight(n):
    count = 0
    for bit in n:
        if bit == '1':
            count += 1
    return count

# Example usage:
n1 = "00000000000000000000000000001011"
print(hammingWeight(n1))  # Output: 3
