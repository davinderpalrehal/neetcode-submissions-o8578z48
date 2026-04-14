class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        def explore(r, c, visited):
            if (r, c) in visited:
                return 0
            
            q = deque()
            q.append((r, c))
            
            while q:
                cr, cc = q.popleft()

                if (cr, cc) in visited:
                    continue
                visited.add((cr, cc))

                for dr, dc in dirs:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                        q.append((nr, nc))
            
            return 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += explore(r, c, visited)

        return res