class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l, r = 0, len(row) - 1
            # if row[l] > target or row[r] < target:
            #     continue
            while l <= r:
                m = l + ((r - l) // 2)
                if row[m] == target:
                    return True
                elif row[m] < target:
                    l = m + 1
                elif row[m] > target:
                    r = m - 1
        return False