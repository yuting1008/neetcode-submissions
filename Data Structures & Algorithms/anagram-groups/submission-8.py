class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        count = [0] * 26
        for s in strs:
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
            count = [0] * 26
            
        return list(result.values())