class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: (temp, index)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                res[stack[-1][1]] = (i - stack[-1][1])
                stack.pop()
            stack.append((t, i))
        return res
