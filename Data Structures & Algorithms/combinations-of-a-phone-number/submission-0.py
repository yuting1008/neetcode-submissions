class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        string = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []
        curr = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(curr))
                return
            
            strings = string[digits[i]]
            for s in strings:
                curr.append(s)
                dfs(i + 1)
                curr.pop()
        dfs(0)
        return res
