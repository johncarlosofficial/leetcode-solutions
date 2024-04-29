from typing import List


class Solution:

  def pivotIndex(self, nums: List[int]) -> int:
    total = 0

    for i in range(len(nums)):
      total += nums[i]

    left = 0
    right = total - nums[0]

    for i in range(len(nums)):
      if left == right:
        return i
      else:
        left += nums[i]
        if i + 1 < len(nums):
          right -= nums[i + 1]
        else:
          right = 0

    return -1
