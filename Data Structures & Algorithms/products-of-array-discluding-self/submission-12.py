class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i - 1] * nums[i - 1])
        
        postfix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i + 1] * nums[i + 1]
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res

        