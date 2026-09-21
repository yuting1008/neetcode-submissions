class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # P + N = total
        # P - N = target
        # P = (total + target) // 2
        
        if (total + target) % 2 == 1 or total < abs(target):
            return 0
        
        subsetSum = (total + target) // 2

        # dp[i] = number of ways to sum to i
        dp = [0] * (subsetSum + 1)
        dp[0] = 1 # 1 way (empty subset) to sum to 0

        for i in range(len(nums)):
            n = nums[i]
            for j in range(subsetSum, n - 1, -1):
                dp[j] += dp[j - n]
                
        return dp[subsetSum]

