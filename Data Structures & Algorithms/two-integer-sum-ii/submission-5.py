class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for curr in range(len(numbers) - 1):
            for add in range(curr + 1, len(numbers)):
                if numbers[curr] + numbers[add] == target:
                    return[curr+1, add+1]
        