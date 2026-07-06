class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanumeric(char):
            if ord('0') <= ord(char) <= ord('9'):
                return True
            elif ord('a') <= ord(char) <= ord('z'):
                return True
            else:
                return False
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not isalphanumeric(s[l].lower()):
                l += 1
            while r > l and not isalphanumeric(s[r].lower()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


        