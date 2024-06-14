class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Transpose the matrix
        for row in range(n):
            for column in range(row + 1, n):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        
        # Reverse each row
        for row in range(n):
            left = 0
            right = n - 1

            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1
