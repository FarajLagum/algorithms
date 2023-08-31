#  greatest common factor (GCF) using the Euclidean algorithm
# https://en.wikipedia.org/wiki/Euclidean_algorithm



def gcd_iterative(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def gcd_recursive_0(a, b):
    a, b = b % a, a  # remainder = a % b;    a = b;    b = remainder
    if a == 0:
        # BASE CASE
        return b
    else:
        # RECURSIVE CASE
        return gcd_recursive_0(a, b)


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b) # a % b is the remainder 





if __name__ == "__main__":
      
      print(gcd_iterative(42, 28)) # out: 14
      print(gcd_recursive_0(42, 28))
      print(gcd_iterative(108, 48)) # out: 12

      # Example usage
      num1 = 48 
      num2 = 108
      result = gcd_recursive(num1, num2)
      print(f"The GCF of {num1} and {num2} is {result}")

