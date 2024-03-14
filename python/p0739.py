from typing import List


class Solution: # Time Complexity: O(nˆ2)

  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    if len(temperatures) == 1:
      return [0]

    ans = []

    for i in range(len(temperatures)):
      warmer = False

      for j in range(i, len(temperatures)):
        if temperatures[j] > temperatures[i]:
          ans.append(j - i)
          warmer = True
          break

      if not warmer:
        ans.append(0)

    return ans
