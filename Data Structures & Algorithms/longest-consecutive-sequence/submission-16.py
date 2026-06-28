class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        sortedNums = sorted(list(set(nums)))
        res = 1
        count = 1
        for i in range(len(sortedNums) - 1):
            if sortedNums[i] + 1 == sortedNums[i + 1]:
                count += 1
                res = max(res, count)
            else:
                count = 1
        return res

