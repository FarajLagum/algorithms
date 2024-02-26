def coin_change_problem(coins, amount):

    result = [float("inf")]*( amount + 1)
    result[0] = 0

    for coin in coins:

        for value in range(coin, amount +1): 

            # if amount >= coin:
                
            result[value] = min(result[value], 1+ result[value-coin])

    
    if result[amount] <= amount:
        return result[amount] 

    return -1


print(coin_change_problem([1, 2, 5], 4))

print(coin_change_problem([2, 5], 3))






# This code is not solving the problem, but help udertanding it
def total_combinations(coins, amount):

    combinations = [0]*( amount + 1)
    combinations[0] = 1

    for coin in coins:

        for value in range(1, amount +1): 

            if value >= coin:

                combinations[value] += combinations[value-coin]
                print(combinations)


    return combinations[amount] 




print(total_combinations([1, 2, 5], 12))

