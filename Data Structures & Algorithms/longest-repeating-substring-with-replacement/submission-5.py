class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        mostFeq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            mostFeq = max(mostFeq, count[s[r]])
            remaining = (r - l + 1) - mostFeq
            while remaining > k:
                count[s[l]] -= 1
                l += 1
                remaining -= 1
            res = max(res, r - l + 1)
        return res