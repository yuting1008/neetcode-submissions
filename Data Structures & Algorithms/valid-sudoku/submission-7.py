class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        squares = [defaultdict(int) for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                idx = (row // 3) * 3 + (col // 3)
                rows[row][num] += 1
                cols[col][num] += 1
                squares[idx][num] += 1
                if rows[row][num] > 1 or cols[col][num] > 1 or squares[idx][num] > 1:
                    return False
        return True

