class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_updated = ""
        for c in s:
            c_lower = c.lower()
            if ord('a') <= ord(c_lower) <= ord('z') or ord('0') <= ord(c_lower) <= ord('9'):
                s_updated += c_lower
        
        l, r = 0, len(s_updated) - 1
        while l <= r:
            if s_updated[l] != s_updated[r]:
                return False
            l += 1
            r -= 1
        return True

        