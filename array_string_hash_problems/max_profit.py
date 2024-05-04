def max_profit(prices):
    if len(prices) <= 1:
        return 0
    cheapest = prices[0]
    maxProfit = float("-inf")
    for price in prices:
        if price < cheapest:
            cheapest = price
        profit = price - cheapest
        maxProfit = max(maxProfit, profit)
    return maxProfit