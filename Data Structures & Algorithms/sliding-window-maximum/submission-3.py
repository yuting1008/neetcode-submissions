class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        res = []
        for l in range(len(nums) - k + 1):
            res.append(max(nums[l:l + k]))
            # if l == 0:
            #     res.append(max(nums[l:l + k]))
            # else:
            #     res.append(max(res[-1], nums[l + k - 1]))
        return res
        