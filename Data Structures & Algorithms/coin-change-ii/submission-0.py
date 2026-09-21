class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        
        dp = []
        for i in range(n + 1):
            dp.append([0] * (amount + 1))

        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a - coins[i] >= 0:
                    dp[i][a] += dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]
        
        return dp[0][amount]