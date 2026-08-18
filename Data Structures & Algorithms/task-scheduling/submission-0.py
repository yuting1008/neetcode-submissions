class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque() # pair of count and readyTime
        while maxheap or q:
            time += 1
            
            if not maxheap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxheap) + 1
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        
        return time