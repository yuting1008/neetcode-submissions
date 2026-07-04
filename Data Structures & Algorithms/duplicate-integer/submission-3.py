class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] > 1:
                return True
        return False