class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        longest = 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) in num_set:
                continue # num 不是起點
            current_num = num
            current_streak = 1
            while (current_num + 1) in num_set:
                current_streak += 1
                current_num += 1
            longest = max(longest, current_streak)
        return longest
        # 每個元素最多只會被訪問兩次 -> O(n)