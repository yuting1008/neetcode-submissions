class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        output = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            output[sortedS].append(s)
        return list(output.values())

        
            
                