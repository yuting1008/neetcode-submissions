class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        # nums = [-1,0,1,2,3]
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])
        # prefix = [1, 1, 2, 8]
        # prefix = [1, 1, 0, 0, 0]

        postfix = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i+1] * nums[i+1]
        # postfix = [48, 24, 6, 1]
        # postfix = [0,0,6, 6, 3, 1]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res
            
        