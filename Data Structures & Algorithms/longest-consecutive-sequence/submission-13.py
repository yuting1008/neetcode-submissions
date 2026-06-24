class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        sortedNums = sorted(set(nums))
        count = 1
        current = 1
        for i in range(0, len(sortedNums) - 1):
            if sortedNums[i + 1] - sortedNums[i] == 1:
                current += 1
            else:
                if current > count:
                    count = current
                current = 1
        
        if current > count:
            count = current

        return count