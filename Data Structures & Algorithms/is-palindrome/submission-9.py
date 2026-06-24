class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        def is_alphanumeric(char):
            ch = char.lower()
            return ('a' <= ch <= 'z') or ('0' <= ch <= '9')
        
        s_updated = ""
        for char in s:
            if is_alphanumeric(char):
                s_updated = s_updated + char.lower()
            

        left = 0
        right = len(s_updated) - 1
        while left <= right:
            if s_updated[left] != s_updated[right]:
                return False
            left += 1
            right -= 1
        return True