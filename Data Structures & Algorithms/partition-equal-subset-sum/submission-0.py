class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        currSum = set()
        currSum.add(0)

        for i in range(len(nums) - 1, -1, -1):
            tempSum = []
            for s in currSum:
                tempSum.append(s + nums[i])
                if s + nums[i] == target:
                    return True
            for s in tempSum:
                currSum.add(s)
        return False