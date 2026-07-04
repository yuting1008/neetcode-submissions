class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resSet = set()
        for l in range(len(nums) - 2):
            for r in range(l+1, len(nums) - 1):
                diff = -(nums[l] + nums[r])
                if diff in nums[r+1:len(nums)]:
                    triplet = tuple(sorted([nums[l], nums[r], diff]))
                    resSet.add(triplet)
        return [list(triplet) for triplet in resSet]
        