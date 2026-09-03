class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return

        visit = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque()
            visit.add((row, col))
            q.append((row, col))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        (r, c) not in visit and
                        grid[r][c] == "1"):
                        visit.add((r, c))
                        q.append((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
