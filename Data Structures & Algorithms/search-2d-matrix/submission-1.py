class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def int_to_index(n: int, n_rows: int, n_cols: int) -> tuple:
            row = n // n_cols
            column = n % n_cols
            return (row, column)

        n_rows, n_cols = len(matrix), len(matrix[0])
        low, high = 0, n_rows * n_cols - 1

        while low <= high:
            middle = (high + low) // 2
            i, j = int_to_index(middle, n_rows, n_cols)
            if matrix[i][j] < target:
                low = middle + 1
            elif matrix[i][j] > target:
                high = middle - 1
            else:
                return True
        
        return False

        