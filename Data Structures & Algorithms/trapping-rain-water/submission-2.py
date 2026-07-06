class Solution:
    def trap(self, height: List[int]) -> int:
        leftMost = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                leftMost[i] = height[i]
            else:
                leftMost[i] = max(leftMost[i - 1], height[i])

        rightMost = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                rightMost[i] = height[i]
            else:
                rightMost[i] = max(rightMost[i + 1], height[i])

        res = 0
        for i in range(len(height)):
            res += min(leftMost[i], rightMost[i]) - height[i]
        return res


