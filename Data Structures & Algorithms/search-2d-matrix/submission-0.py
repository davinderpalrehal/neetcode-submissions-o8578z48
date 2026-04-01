class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            lo, hi = 0, len(matrix[r]) - 1

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if matrix[r][mid] == target:
                    return True
                if matrix[r][mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
        
        return False