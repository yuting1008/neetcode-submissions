class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        
        l, r = 0, 1
        chars = set(s[l])
        longest = 1
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                longest = max(longest, len(chars))
            else:
                while l < len(s):
                    if s[l] == s[r]:
                        break
                    chars.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return longest

        