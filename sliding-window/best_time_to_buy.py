def max_profit(prices) -> int:
    # get min prices
    # better day to buy
    # get the max prices
    # better to sell
    # but, index of buy must be lower than index of sell
    # first you need to buy to then sell it

    res = 0
    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
    return print(res)


max_profit([1, 6, 4, 3, 7])
