class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(list)
        for i in range(len(nums)):
            indices[nums[i]].append(i)

        for i in range(len(nums)):
            if target - nums[i] in indices:
                for j in indices[target - nums[i]]:
                    if j != i:
                        return [i, j]
