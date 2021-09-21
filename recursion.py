def factorial(n):
    if n < 0:
        raise TypeError("Only non-negative are allowed")
    elif n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# test
n = 1

# check if the number is negative
if n  < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   print(f"The factorial of {n}  is {factorial(n)}")



def fibonacci(n):
    if n < 0:
          raise TypeError("Only non-negative are allowed")
    
    if n == 0 or n == 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 1)


# test
n = 2

# check if the number is negative
if n  < 0:
   print("Sorry, fibonacci does not exist for negative numbers")
else:
   print(f"The {n} fibonacci number is {fibonacci(n)}")


#fibonacci(-1)
factorial(-1)