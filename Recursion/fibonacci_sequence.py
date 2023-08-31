


def fibonacci_sequence(n):
    if n < 2:
        return  n
    
    return fibonacci_sequence (n-1) + fibonacci_sequence(n-2)
 


    return 


if __name__ == "__main__":
    n= 16

    print(fibonacci_sequence(n))


