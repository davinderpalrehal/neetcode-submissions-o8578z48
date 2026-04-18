class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = {
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        }

        fresh_oranges = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        
        
        visited = set()

        while q:
            r, c, t = q.popleft()

            if (r, c) in visited:
                continue
            visited.add((r, c))
            time = max(time, t)
            if grid[r][c] == 1:
                fresh_oranges -= 1

            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    q.append((nr, nc, t + 1))


        return -1 if fresh_oranges > 0 else time