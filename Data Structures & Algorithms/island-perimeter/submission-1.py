class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def traverse(r, c):
            q = deque([(r, c)])
            res = 0
            directions = {
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0)
            }
            seen = set()

            while q:
                cr, cc = q.popleft()
                if (cr, cc) in seen:
                    continue
                seen.add((cr, cc))

                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc

                    if nr < 0 or nr >= ROWS:
                        res += 1
                        continue
                    if nc < 0 or nc >= COLS:
                        res += 1
                        continue
                    if grid[nr][nc] == 0:
                        res += 1
                        continue
                    q.append((nr, nc))
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return traverse(r, c)