class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            curr = [1]
            for j in range(i + 1, len(nums), 1):
                if nums[i] < nums[j]:
                    curr.append(dp[j] + 1)
                elif nums[i] == nums[j]:
                    curr.append(dp[j])
            dp[i] = max(curr)
        
        return max(dp)
            