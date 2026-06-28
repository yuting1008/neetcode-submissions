class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []
        n = len(sortedNums)
        
        for curr in range(n - 2):
            # 去重：如果這個起點跟上一個起點一樣，直接跳過，避免做出重複的組合
            if curr > 0 and sortedNums[curr] == sortedNums[curr - 1]:
                continue
                
            l = curr + 1
            r = n - 1
            
            while l < r:
                three_sum = sortedNums[curr] + sortedNums[l] + sortedNums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # 找到一組解
                    res.append([sortedNums[curr], sortedNums[l], sortedNums[r]])
                    
                    # 關鍵：移動指針，並同時「去重」
                    l += 1
                    r -= 1
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1
                    while l < r and sortedNums[r] == sortedNums[r + 1]:
                        r -= 1
                        
        return res