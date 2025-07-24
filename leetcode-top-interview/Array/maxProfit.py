# Best Time to Buy and Sell Stock II
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profilt You can achieve
class Solution(object):
  def maxProfit(self, prices):
    k = 0

    for i in range(0, len(prices) - 1):
      if prices[i] < prices[i + 1]:
        k += (prices[i + 1] - prices[i])

    return k
  
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1,2,3,4,5]
    result1 = solution.maxProfit(nums1)
    print(result1)