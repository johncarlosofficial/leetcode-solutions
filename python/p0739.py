from typing import List


class Solution:

  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = []
    ans = [0] * len(temperatures)

    for i in range(len(temperatures)):
      if not stack:
        stack.append([i, temperatures[i]])
      else:
        if temperatures[i] <= stack[-1][1]:
          stack.append([i, temperatures[i]])
        else:
          while stack and temperatures[i] > stack[-1][1]:
            prev_idx = stack[-1][0]
            ans[prev_idx] = i - prev_idx
            stack.pop()
          stack.append([i, temperatures[i]])

    return ans
