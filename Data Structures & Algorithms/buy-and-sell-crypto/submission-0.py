class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
            
        maxProfit = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                maxProfit = max(maxProfit, prices[j]-prices[i])
        return maxProfit
        