class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(left_max[i - 1], height[i])
        
        right_max = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                right_max[i] = height[i]
            else:
                right_max[i] = max(right_max[i + 1], height[i])
        
        res = 0
        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
        
