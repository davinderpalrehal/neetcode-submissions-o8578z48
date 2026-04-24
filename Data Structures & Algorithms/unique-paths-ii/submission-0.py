class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0] * COLS for _ in range(ROWS)]

        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0
        res[ROWS - 1][COLS - 1] = 1

        for c in reversed(range(COLS - 1)):
            if obstacleGrid[ROWS - 1][c] == 1:
                res[ROWS - 1][c] = 0
            else:
                res[ROWS - 1][c] = res[ROWS - 1][c + 1]
        
        for r in reversed(range(ROWS - 1)):
            if obstacleGrid[r][COLS - 1] == 1:
                res[r][COLS - 1] = 0
            else:
                res[r][COLS - 1] = res[r + 1][COLS - 1]

        for r in reversed(range(ROWS - 1)):
            for c in reversed(range(COLS - 1)):
                if obstacleGrid[r][c] == 1:
                    res[r][c] = 0
                else:
                    res[r][c] = res[r + 1][c] + res[r][c + 1]
        
        return res[0][0]