# def maxProfit(prices) -> int:
#     l, r = 0, 1  # left = buy, right = sell
#     maxP = 0

#     while r < len(prices):
#         # is profitable?
#         if prices[l] < prices[r]:
#             profit = prices[r] - prices[l]
#             maxP = max(maxP, profit)
#         else:
#             l = r
#         r += 1
#     return maxP


def maxProfit(prices) -> int:
    min_price = float('inf')
    profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = max(price - min_price, profit)
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
