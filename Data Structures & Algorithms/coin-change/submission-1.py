class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0

        for currAmount in range(1, amount + 1):
            for coin in coins:
                if currAmount - coin >= 0:
                    dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1