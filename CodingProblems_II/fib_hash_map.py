def fib(n):
    fib_seq={0:0, 1:1, 2:1}
    if n in fib_seq:
        return fib_seq[n]


    for i in range(3, n+1):
        fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
    
    return fib_seq[n]


print(fib(6))
