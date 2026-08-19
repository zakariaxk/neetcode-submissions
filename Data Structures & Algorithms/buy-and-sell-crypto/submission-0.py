class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0

        for i in range(len(prices) - 1):
            maxVal = max(prices[i+1:])
            maxprofit = max(maxprofit, maxVal - prices[i])

        return maxprofit



        
        