def max_profit(prices):

    max_p = 0

    for  i in range(len(prices)-1):
        print("i:", i)
        if prices[i] < prices[i +1]:
            p_diff = prices[i +1] - prices[i]
            if max_p < p_diff:
                max_p = p_diff
    
    return max_p



prices = [7,1,5,3,6,4]
print(max_profit(prices))  # Output: 5

