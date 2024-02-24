def maxProfit(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit = max(max_profit, prices[i] - prices[i - 1])
            # max_profit += prices[i] - prices[i - 1] # this give the max accumulated profit

    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 
