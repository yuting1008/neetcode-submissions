class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return -1
    
'''
target = 3

  0 1 2 3 4 5 
[-1,0,2,4,6,8]
  l   m     r

[-1,0,2,4,6,8]
        l m r

[-1,0,2,4,6,8]
        l
        r
'''