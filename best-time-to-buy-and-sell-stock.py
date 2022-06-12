# find largest peak following smallest valley, single pass
# time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            lowest = min(prices[i], lowest)
            max_profit = max(max_profit, prices[i] - lowest)
        return max_profit
