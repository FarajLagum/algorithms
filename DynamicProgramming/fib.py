import time


def fib(n):
    # Time: O(2^n)
    # Space: O(n)
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_memo(n):
    # Time: O(n)
    # Space: O(n)
    memo = {}
    return _fib(n, memo)


def _fib(n, memo):
    if n == 0 or n == 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]


def tic_tac(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()

    excution_time = end_time - start_time

    print(
        f"Excution Time of {str(func.__name__)} given args {args}:", 1000*excution_time, "ms")


tic_tac(fib, 40)

tic_tac(fib_memo, 40)
