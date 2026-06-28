class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        left, right = 0, len(nums) - 1
        vals = []
        while left < right:
            if sortedNums[left] + sortedNums[right] > target:
                right -= 1
            elif sortedNums[left] + sortedNums[right] < target:
                left += 1
            else:
                vals.append(sortedNums[left])
                vals.append(sortedNums[right])
                break
        
        ans = []
        if vals[0] != vals[1]:
            ans.append(nums.index(vals[0]))   
            ans.append(nums.index(vals[1]))   
        else:
            firstIdx = nums.index(vals[0])
            ans.append(firstIdx)
            ans.append(nums[firstIdx + 1:].index(vals[0]) + firstIdx + 1)
        ans.sort()   
        return ans
