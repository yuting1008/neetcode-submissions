class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT = defaultdict(int)
        for i in range(len(t)):
            countT[t[i]] += 1
        
        window = defaultdict(int)
        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = len(s) + 1
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                c = s[l]
                window[c] -= 1
                if c in countT and window[c] < countT[c]:
                    have -= 1
                l += 1
        
        if resLen > len(s):
            return ""
        else:
            l, r = res
            return s[l:r + 1]


            
