class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] == 1:
            return -1
        
        dir = {
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1)
        }

        q = deque()
        q.append((0, 0, 1))
        visited = set()

        while q:
            r, c, d = q.popleft()
            if (r, c) == (N - 1, N - 1):
                return d
            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    q.append((nr, nc, d + 1))
        
        return -1