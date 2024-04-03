from typing import List


class Solution:

  def generate(self, numRows: int) -> List[List[int]]:
    ans = [[1]]

    for _ in range(numRows - 1):
      temp = [0] + ans[-1] + [0]
      new_row = []
      for j in range(len(temp) - 1):
        new_row.append(temp[j] + temp[j + 1])
      ans.append(new_row)

    return ans
