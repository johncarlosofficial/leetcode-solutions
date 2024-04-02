from typing import List


class Solution:

  def countNegatives(self, grid: List[List[int]]) -> int:
    ans = 0
    for row in grid:
      left, right = 0, len(row) - 1

      while left <= right:
        mid = (left + right) // 2

        if row[mid] >= 0:
          left = mid + 1
        else:
          right = mid - 1

      if right >= 0 and left < len(row):
        ans += (len(row) - left)
      elif right < 0:
        ans += (len(row))

    return ans
