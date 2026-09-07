class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(
        #   rob(nums[0] + nums[2:n-1])
        #   rob(nums[1:n])
        #)

        def robWithoutCircle(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        n = len(nums)
        sum1 = nums[0] + robWithoutCircle(nums[2:n-1])
        sum2 = robWithoutCircle(nums[1:n])
        return max(sum1, sum2)
