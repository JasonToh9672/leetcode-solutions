# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time complexity: O(n)
# Space complexity: O(1)
# LeetCode runtime: 22 ms
# Solved directly in one pass.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0] # set the min_price to first price in the list
        max_profit = 0 # initialize the max_profit to zero, so if later can return 0 if no profit is make

        for price in prices:
            if price < min_price: 
                min_price = price # update the min_price to new price value
            elif price - min_price > max_profit: # profit = price - min_price, compare to max_profit, if profit > current max_profit, replace it with this profit
                max_profit = price - min_price  # update the max_profit to new profit if the new profit is larger
        return max_profit

# elif is safe because on a day with a new min_price, selling on the same day gives a profit of 0,
#   which can never be bigger than max_profit (which starts at 0)

# What I learned:
# running minimum: instead of checking every pair of days, remember the lowest price seen so far
# then for each day, the best profit if I sell today is price of the today - min_price 
# slicing like prices[1:] creates a copy, so it would make the space O(n) instead of O(1)