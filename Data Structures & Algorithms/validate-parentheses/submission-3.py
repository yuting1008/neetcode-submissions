class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in mapping: # 右括號
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # 左括號
        
        # 左括號還有剩
        if stack:
            return False

        return True

        