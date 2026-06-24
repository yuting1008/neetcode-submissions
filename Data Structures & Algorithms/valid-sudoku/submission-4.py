class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            row = defaultdict(int)
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row[board[i][j]] += 1
                if row[board[i][j]] > 1:
                    return False

        # column
        for i in range(9):
            column = defaultdict(int)
            for j in range(9):
                if board[j][i] == ".":
                    continue
                column[board[j][i]] += 1
                if column[board[j][i]] > 1:
                    return False

        # square
        square = [0] * 9
        for i in range(9):
            square[i] = defaultdict(int)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                idx = (row // 3) * 3 + (col // 3)
                square[idx][board[row][col]] += 1
                if square[idx][board[row][col]] > 1:
                    return False

        return True
