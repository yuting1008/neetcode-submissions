class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        leftMost, rightMost = height[l], height[r]
        while l < r:
            if leftMost <= rightMost:
                l += 1
                leftMost = max(leftMost, height[l])
                res += leftMost - height[l]
            else:
                r -= 1
                rightMost = max(rightMost, height[r])
                res += rightMost - height[r]
        return res
            


