def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Example usage:
n1 = 0b00000010100101000001111010011100
print("Input:", bin(n1))
print("Output:", reverse_bits(n1))  # Output: 964176192

n2 = 0b11111111111111111111111111111101
print("Input:", bin(n2))
print("Output:", reverse_bits(n2))  # Output: 3221225471





def reverse_bits(n):
    # Convert the integer to a binary string and remove the '0b' prefix
    binary_str = bin(n)[2:]
    
    # Ensure that the binary string has exactly 32 bits by padding zeros to the left if needed
    binary_str = binary_str.zfill(32)
    
    # Reverse the binary string
    reversed_binary_str = binary_str[::-1]
    
    # Convert the reversed binary string back to an integer
    reversed_int = int(reversed_binary_str, 2)
    
    return reversed_int

# Example usage:
n1 = 0b00000010100101000001111010011100
print("Input:", bin(n1))
print("Output:", reverse_bits(n1))  # Output: 964176192

n2 = 0b11111111111111111111111111111101
print("Input:", bin(n2))
print("Output:", reverse_bits(n2))  # Output: 3221225471

