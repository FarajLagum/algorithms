def max_profit(prices):
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))  # Output: 5

'''
the time complexity is O(n^2)

The space complexity is O(1) because only one variable (max_profit) is used, and 
its usage does not scale with the size of the input list.

'''