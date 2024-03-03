from typing import List


class Solution:

  def searchInsert(self, nums: List[int], target: int) -> int:
    i = 0
    while i < len(nums):
      if nums[i] < target:
        i += 1
      else:
        return i
    return i
