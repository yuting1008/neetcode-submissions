class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            if i != 0:
                prefix *= nums[i - 1]
            res[i] = prefix
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                postfix *= nums[i + 1]
            res[i] *= postfix

        return res

        