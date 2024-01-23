
def maxProfit(prices):
    left = 0 #Buy
    right = 1 #Sell
    max_profit = 0
    while right < len(prices):
        current_profit = prices[right] - prices[left] #our current Profit
        if prices[left] < prices[right]:
            max_profit =max(current_profit,max_profit)
        else:
            left = right
        right += 1
    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 5
