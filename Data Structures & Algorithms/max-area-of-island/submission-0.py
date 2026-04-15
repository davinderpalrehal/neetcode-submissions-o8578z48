class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def explore(r, c, visited):
            if (r, c) in visited:
                return 0
            
            area = 0
            q = deque()
            q.append((r, c))

            while q:
                cr, cc = q.popleft()
                if (cr, cc) in visited:
                    continue
                visited.add((cr, cc))
                area += 1

                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((nr, nc))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, explore(r, c, visited))

        return res