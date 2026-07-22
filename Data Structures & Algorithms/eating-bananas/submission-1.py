class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        res = maxPiles
        l, r = 1, maxPiles

        while l <= r:
            m = l + ((r - l) // 2)
            total = 0
            for p in piles:
                if p % m == 0:
                    total += p // m
                else:
                    total += (p // m + 1)

            if total <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res