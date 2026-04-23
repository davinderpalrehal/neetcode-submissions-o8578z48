class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        prev = [0] * COLS

        for _ in range(ROWS):
            curr = [0] * COLS
            curr[COLS - 1] = 1
            for c in reversed(range(COLS - 1)):
                curr[c] = prev[c] + curr[c+1]
            prev = curr
        
        return prev[0]