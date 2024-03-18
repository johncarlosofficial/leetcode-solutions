from typing import List


class Solution:

  def evalRPN(self, tokens: List[str]) -> int:
    nums = []

    for i in range(len(tokens)):
      if tokens[i].isdigit() or (tokens[i][0] == '-'
                                 and tokens[i][1:].isdigit()):
        nums.append(int(tokens[i]))

      elif tokens[i] == '+':
        res = nums.pop() + nums.pop()
        nums.append(res)

      elif tokens[i] == '*':
        res = nums.pop() * nums.pop()
        nums.append(res)

      elif tokens[i] == '-':
        res = nums[-2] - nums[-1]
        nums.pop()
        nums.pop()
        nums.append(res)

      elif tokens[i] == '/':
        res = int(nums[-2] / nums[-1])
        nums.pop()
        nums.pop()
        nums.append(res)

    return nums[0]
