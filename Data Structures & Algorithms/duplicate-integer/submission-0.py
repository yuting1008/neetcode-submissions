class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = dict()
        for num in nums:
            if num in record:
                record[num] += 1
            else:
                record[num] = 1
            
            if record[num] > 1:
                return True
                
        return False