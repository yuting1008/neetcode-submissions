class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        for p in points:
            x, y = p[0], p[1]
            d = ((x ** 2) + (y ** 2)) ** (0.5)
            heapq.heappush(minHeap, [d, p])
        res = []
        while len(res) < k:
            p = heapq.heappop(minHeap)[1]
            res.append(p)
        return res