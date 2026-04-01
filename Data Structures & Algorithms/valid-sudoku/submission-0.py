class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9

        def valid_row(r, n):
            found = False
            for c in range(COLS):
                if board[r][c] == n:
                    if found:
                        return False
                    found = True
            return True
        
        def valid_col(c, n):
            found = False
            for r in range(ROWS):
                if board[r][c] == n:
                    if found:
                        return False
                    found = True
            return True
        
        def valid_square(r, c, n):
            row_range = 9
            if r == 0 or r == 1 or r == 2:
                row_range = 3
            elif r == 3 or r == 4 or r == 5:
                row_range = 6

            col_range = 9
            if c == 0 or c == 1 or c == 2:
                col_range = 3
            elif c == 3 or c == 4 or c == 5:
                col_range = 6

            found = False
            for row in range(row_range - 3, row_range):
                for col in range(col_range - 3, col_range):
                    if board[row][col] == n:
                        if found:
                            return False
                        found = True
            
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != '.':
                    n = board[r][c]
                    if not valid_row(r, n) or not valid_col(c, n) or not valid_square(r, c, n):
                        return False
        
        return True