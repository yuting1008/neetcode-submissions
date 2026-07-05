class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        feq = [[] for _ in range(len(nums))]
        for num, cnt in count.items():
            feq[cnt - 1].append(num)
        
        res = []
        for i in range(len(feq) - 1, -1, -1):
            for j in range(len(feq[i])):
                if len(res) == k:
                    break
                res.append(feq[i][j])
        return res
            
