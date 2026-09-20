class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDp = set()
            for s in dp:
                nextDp.add(s)
                nextDp.add(s + nums[i])
                if s + nums[i] == target:
                    return True
            dp = nextDp
        return False