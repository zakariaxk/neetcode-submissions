class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = prices[-1]
        maxprofit = 0

        for i in range(len(prices) - 2, -1, -1):
            maxprofit = max(maxprofit, maxVal - prices[i])
            maxVal = max(maxVal, prices[i])

        return maxprofit