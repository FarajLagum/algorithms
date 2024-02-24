def maxProfit(prices):
    # if not prices:
    #     return 0

    buy = prices[0]
    max_profit = 0

    for price in prices:
        if price < buy:
            buy = price
        else:
            max_profit = max(max_profit, price - buy)

    return max_profit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 5
