def euclid_gcd(a, b):
    """
    Implementation of Euclid's algorithm to find the greatest common divisor (GCD)
    of two integers a and b.

    :param a: First integer
    :param b: Second integer
    :return: GCD of a and b

    https://en.wikipedia.org/wiki/Euclidean_algorithm
    """
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
a = 48
b = 18
gcd = euclid_gcd(a, b)
print("GCD of", a, "and", b, "is:", gcd)
