def climb_stairs(n: int) -> int:
    if n < 2:
        return n
    ways = [0] * (n +1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]


def climb_stairs_optimized(n: int) -> int:
    if n == 1:
        return 1
    prev_step_count = 1
    curr_step_count = 2
    for _ in range(3, n + 1):
        next_step_count = prev_step_count + curr_step_count
        prev_step_count, curr_step_count  = curr_step_count, next_step_count
        
    return curr_step_count



assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
assert climb_stairs(4) == 5

print(climb_stairs_optimized(4))
