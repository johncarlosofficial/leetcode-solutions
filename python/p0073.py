from typing import List


class Solution:

  def setZeroes(self, matrix: List[List[int]]) -> None:
    rows = set()
    columns = set()

    for row in range(len(matrix)):
      for column in range(len(matrix[row])):
        if matrix[row][column] == 0:
          rows.add(row)
          columns.add(column)

    for row in rows:
      for column in range(len(matrix[row])):
        matrix[row][column] = 0

    for column in columns:
      for row in range(len(matrix)):
        matrix[row][column] = 0

    print(matrix)
