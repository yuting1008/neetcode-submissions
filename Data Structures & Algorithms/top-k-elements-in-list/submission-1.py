class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        countList = sorted(count, key=count.get, reverse=True)
        return countList[0:k]
        