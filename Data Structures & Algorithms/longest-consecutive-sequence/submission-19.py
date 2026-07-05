class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numSet = set(nums)
        sortedNum = sorted(list(numSet))
        res, curr = 1, 1
        for i in range(len(sortedNum) - 1):
            if sortedNum[i] + 1 == sortedNum[i + 1]:
                curr += 1
                res = max(res, curr)
            else:
                curr = 1
        return res
            
