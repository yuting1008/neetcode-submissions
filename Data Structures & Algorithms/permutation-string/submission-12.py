class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1, count_s2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if count_s1[i] == count_s2[i]:
                matches += 1
        
        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            if matches == 26:
                return True

            idx = ord(s2[r + 1]) - ord('a')
            if count_s1[idx] == count_s2[idx] + 1:
                matches += 1
            elif count_s1[idx] == count_s2[idx]:
                matches -= 1
            count_s2[idx] += 1
            
            idx = ord(s2[l]) - ord('a')
            if count_s1[idx] == count_s2[idx]:
                matches -= 1
            elif count_s1[idx] == count_s2[idx] - 1:
                matches += 1
            count_s2[idx] -= 1

            r += 1
            l += 1

        return matches == 26
            

