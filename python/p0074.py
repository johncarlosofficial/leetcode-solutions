from typing import List


class Solution:

  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    top = 0
    bottom = len(matrix) - 1

    while top < bottom:
      middle = (top + bottom) // 2

      if matrix[middle][0] == target:
        return True

      elif matrix[middle][0] > target:
        bottom = middle - 1

      elif matrix[middle][-1] < target:
        top = middle + 1

      else:
        top = middle
        bottom = middle

    print(top)

    left = 0
    right = len(matrix[top]) - 1

    while left <= right:
      middle = (left + right) // 2

      if matrix[top][middle] == target:
        return True

      elif matrix[top][middle] > target:
        right = middle - 1

      else:
        left = middle + 1

    return False
