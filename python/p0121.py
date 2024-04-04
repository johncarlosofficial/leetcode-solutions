from typing import List


class Solution:

  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    left, right = 0, 1

    while right < len(prices):
      profit = prices[right] - prices[left]
      max_profit = max(max_profit, profit)
      if prices[left] > prices[right]:
        left = right
      right += 1

    return max_profit
