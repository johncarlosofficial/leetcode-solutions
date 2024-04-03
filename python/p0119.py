from typing import List


class Solution:

  def getRow(self, rowIndex: int) -> List[int]:
    if rowIndex == 0:
      return [1]

    triangle = [[1]]

    for _ in range(rowIndex):
      new_row = []
      temp_row = [0] + triangle[-1] + [0]

      for j in range(len(temp_row) - 1):
        new_row.append(temp_row[j] + temp_row[j + 1])

      triangle.append(new_row)

    return triangle[-1]
