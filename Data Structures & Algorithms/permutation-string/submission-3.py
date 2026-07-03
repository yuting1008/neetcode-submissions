class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if len(s2) < len(s1):
            return False

        s1_count = [0] * 26
        for i in s1:
            s1_count[ord(i) - ord('a')] += 1
        
        s2_count = [0] * 26
        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord('a')] += 1

        i = 0
        while i + len(s1) - 1 < len(s2):
            if i != 0:
                s2_count[ord(s2[i - 1]) - ord('a')] -= 1
                s2_count[ord(s2[i + len(s1) - 1]) - ord('a')] += 1
            if s1_count == s2_count:
                return True
            i += 1
        return False