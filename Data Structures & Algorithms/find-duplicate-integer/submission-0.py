class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] > 1:
                return n
        return None