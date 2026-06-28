class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i # 如果有重複的值，會記錄到最大的 index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return[i, indices[diff]] # 一定是遞增排列
        return []