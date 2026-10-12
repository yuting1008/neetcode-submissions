class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_char = ord(s1[i]) - ord('a')
            s1_count[s1_char] += 1

            s2_char = ord(s2[i]) - ord('a')
            s2_count[s2_char] += 1
        
        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            if s1_count == s2_count:
                return True

            l_char = ord(s2[l]) - ord('a')
            s2_count[l_char] -= 1
            l += 1

            r += 1
            r_char = ord(s2[r]) - ord('a')
            s2_count[r_char] += 1
        
        return s1_count == s2_count


'''
lecabee
l r
'''