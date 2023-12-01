# 121. Best Time to Buy and Sell Stock
# Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

#**********************************

#solution will use a nested loop to update a profit variable and then return it

def stock_profit(prices):
    #tracking variable "max_profit" is innitialized at zero, if no positive profits exist we will can still return this value
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i, len(prices)):
            potential_profit = prices[j] - prices[i]
            if potential_profit > max_profit:
                max_profit = potential_profit
    return max_profit

ex_prices = [7,1,5,3,6,4]

print(stock_profit(ex_prices))
# prints 5 (example one correct answer)