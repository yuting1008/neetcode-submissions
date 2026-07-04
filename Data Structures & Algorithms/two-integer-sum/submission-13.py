class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(int)
        for i in range(len(nums)):
            indices[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indices and i != indices[diff]:
                return [i, indices[diff]]
                
        
