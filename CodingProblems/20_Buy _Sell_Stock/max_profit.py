def max_profit(prices: list[int]) -> int:
    left_ptr, profit = 0, 0
    for right_ptr in range(1, len(prices)):
        if prices[left_ptr] < prices[right_ptr]:
            profit = max(profit, prices[right_ptr] - prices[left_ptr])
        else:
            left_ptr = right_ptr
    return profit

def max_profit(prices: list[int]) -> int:
    # buy_ptr is the left pointer
    # sell_ptr is the right pointer
    buy_ptr, profit = 0, 0
    for sell_ptr in range(1, len(prices)):
        if prices[buy_ptr] < prices[sell_ptr]:
            profit = max(profit, prices[sell_ptr] - prices[buy_ptr])
        else:
            buy_ptr = sell_ptr
    return profit

def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


def max_profit(prices):
    profit = 0 # max_profit
    buy_price = prices[0] # min_price
    for sell_price in prices[1:]:
        if sell_price > buy_price:
            profit = max(profit, sell_price - buy_price)
        else:
            buy_price = sell_price
    
    return profit
    

assert max_profit([7,1,5,3,6,4]) == 5
assert max_profit([7,6,4,3,1]) == 0
assert max_profit([1,2,3,4,5]) == 4
assert max_profit([7,1,5,3,6,4,8]) == 7

