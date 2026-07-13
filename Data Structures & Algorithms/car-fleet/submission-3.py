class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(list(zip(position, speed)))

        stack = []
        for i in range(len(pair) - 1, -1, -1):
            time = (target - pair[i][0]) / pair[i][1]
            if stack and time > stack[-1]:
                stack.append(time)
            elif i == len(pair) - 1:
                stack.append(time)
        return len(stack)
            