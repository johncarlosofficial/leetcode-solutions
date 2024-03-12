from typing import List


class Solution:

  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    ans = []

    left, right = 0, len(numbers) - 1

    while left < right:
      current_sum = numbers[left] + numbers[right]

      if current_sum == target:
        ans.append(left + 1)
        ans.append(right + 1)
        break

      elif current_sum < target:
        left += 1

      else:
        right -= 1

    return ans
