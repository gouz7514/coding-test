# 121. Best Time to Buy and Sell Stock
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.
# slower than second one, because of max
class Solution(object):
    def maxProfit(self, prices):
        # profit
        r = 0
        # smallest element
        a = 10001

        for i in range(len(prices)):
            if prices[i] < a:
                a = prices[i]
            else:
              r = max(r, prices[i] - a)
        return r
        
# This is faster....
# but slower than third one because of list indexing, len() and elif
# elif means second condition can be evaluted potentially
class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
    
# much much faster
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit

if __name__ == "__main__":
    solution = Solution()

    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)
    print(result)