from typing import List  
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        # Binary search to find the correct row
        while top < bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] < target:
                if matrix[mid][-1] >= target:
                    top = mid
                    bottom = mid
                else:
                    top = mid + 1
            else:
                bottom = mid - 1

        # Binary search within the row to find the target
        left = 0
        right = len(matrix[top]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[top][mid] == target:
                return True
            
            elif matrix[top][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False  # Return False if the target is not found