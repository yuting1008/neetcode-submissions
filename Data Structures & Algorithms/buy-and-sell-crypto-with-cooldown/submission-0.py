class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        dp = {} # key=(day, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                profit = max(cooldown, buy)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                profit = max(cooldown, sell)
            dp[(i, buying)] = profit
            return dp[(i, buying)]
        
        return dfs(0, True)