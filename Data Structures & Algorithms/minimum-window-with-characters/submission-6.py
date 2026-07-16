class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        
        have, need = 0, len(t)
        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        
        resLen = float("infinity")
        res = [-1, -1]
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            if window[char] <= countT[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                char = s[l]
                window[char] -= 1
                if window[char] < countT[char]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res != [-1, -1] else ""
        