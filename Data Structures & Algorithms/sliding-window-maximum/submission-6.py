class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque() # indices
        res = []
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if (r + 1) >= k:
                while q[0] < l:
                    q.popleft()
                l += 1
                res.append(nums[q[0]])
        return res




