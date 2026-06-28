class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        res = sorted(count, key=count.get, reverse=True)

        return res[0:k]