class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        sortedCount = sorted(count, key=count.get, reverse=True)
        return sortedCount[:k]