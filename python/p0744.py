from typing import List


class Solution:

  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    left, right = 0, len(letters) - 1

    while left <= right:
      mid = (left + right) // 2
      mid_val = letters[mid]

      if mid_val <= target:
        left = mid + 1
      else:
        right = mid - 1

    if left < len(letters):
      return letters[left]
    else:
      return letters[0]
