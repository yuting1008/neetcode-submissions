class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            tmp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * tmp, n * curMin, n)
            res = max(res, curMax)
        return res

'''
[2,4,-3,5]
2, 2
8, 4
-3, -24
5, -120
'''