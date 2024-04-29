from typing import List


class Solution:

  def equalPairs(self, grid: List[List[int]]) -> int:
    ans = 0
    rows_map = {}

    for i in range(len(grid)):
      if tuple(grid[i]) in rows_map:
        rows_map[tuple(grid[i])].append(i)
      else:
        rows_map[tuple(grid[i])] = [i]

    for i in range(len(grid)):
      temp = []
      for j in range(len(grid[0])):
        temp.append(grid[j][i])

      if tuple(temp) in rows_map:
        ans += len(rows_map[tuple(temp)])

    return ans
