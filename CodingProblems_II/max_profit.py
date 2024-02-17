def maxProfit(prices):
    j = 1
    i = 0
    max_profit = 0

    while j < len(prices):
        max_profit = max(max_profit, prices[j] - prices[i])
        if prices[j] < prices[i]:
            i = j

        j += 1    
            # max_profit += prices[i] - prices[i - 1] # this give the max accumulated profit

    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 