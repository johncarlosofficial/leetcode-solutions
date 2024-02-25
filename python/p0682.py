from typing import List


class Solution:

  def calPoints(self, operations: List[str]) -> int:
    scores = []

    for i in range(len(operations)):
      if operations[i] == '+':
        if len(scores) >= 2:
          scores.append(scores[-1] + scores[-2])
        elif len(scores) == 1:
          scores.append(scores[-1])
        else:
          pass

      elif operations[i] == 'D':
        if len(scores) >= 1:
          scores.append(scores[-1] * 2)
        else:
          pass

      elif operations[i] == 'C':
        if len(scores) >= 1:
          scores.pop()

      else:
        scores.append(int(operations[i]))

    ans = 0

    for score in scores:
      ans += score

    return ans
