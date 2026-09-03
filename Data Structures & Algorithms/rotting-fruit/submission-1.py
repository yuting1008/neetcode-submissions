class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        visit = set()
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr not in range(ROWS) or
                    nc not in range(COLS) or
                    (nr, nc) in visit or
                    grid[nr][nc] == 0):
                    continue
                visit.add((nr, nc))
                q.append((nr, nc))

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                if grid[r][c] == 1 or grid[r][c] == 2:
                    count += 1
        
        # all rotten
        if len(visit) == count:
            return 0
        
        minute = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r, c)
            minute += 1
        return -1 if len(visit) != count else minute


