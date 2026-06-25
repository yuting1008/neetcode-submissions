class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                height = min(heights[i], heights[j])
                length = j - i
                current_amount = length * height
                maximum = max(maximum, current_amount)
        return maximum