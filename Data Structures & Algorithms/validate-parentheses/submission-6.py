class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if stack:
                    openingBracket = stack.pop()
                    if openingBracket == "(" and c != ")":
                        return False
                    elif openingBracket == "[" and c != "]":
                        return False
                    elif openingBracket == "{" and c != "}":
                        return False
                else:
                    return False
        return len(stack) == 0