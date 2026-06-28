class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0, 1, 2
        # 3, 4, 5
        # 6, 7, 8
        # idx = (row // 3) * 3 + (col // 3)

        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        squares = [defaultdict(int) for _ in range(9)]

        # rows[0][1] -> how many 1 in row 0
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                idx = (row // 3) * 3 + (col // 3)
                rows[row][val] += 1
                cols[col][val] += 1
                squares[idx][val] += 1

                if rows[row][val] > 1 or cols[col][val] > 1 or squares[idx][val] > 1:
                    return False
        return True



        