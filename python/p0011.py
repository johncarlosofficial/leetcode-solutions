from typing import List


class Solution:

  def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1

    if len(height) == 1:
      return 0

    max_capacity = 0

    while left < right:
      water = (right - left) * min(height[left], height[right])
      max_capacity = max(max_capacity, water)

      if height[left] < height[right]:
        left += 1
      elif height[right] < height[left]:
        right -= 1
      else:
        left += 1
        right -= 1

    return max_capacity
