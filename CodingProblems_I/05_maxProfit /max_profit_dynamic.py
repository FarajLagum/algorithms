def maxProfit(prices):
    buy = float('inf') # the minmum price
    max_profit = 0

    for price in prices:
        if price < buy:
            buy = price
        elif price - buy > max_profit:
            max_profit = price - buy

    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 5

'''

 the time complexity is $$O(n)$$, where $$n$$ is the length of the prices list. 
 
 
 The space complexity is $$O(1)$$ because only two variables (`min_price` and `max_profit`) 
 are used, and their usage does not scale with the size of the input list. 

'''