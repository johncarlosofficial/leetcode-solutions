from typing import List


class Solution:

  def moveZeroes(self, nums: List[int]) -> None:
    left, right = 0, 1

    while right < len(nums):
      if nums[left] == 0 and nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right += 1
      elif nums[left] == 0 and nums[right] == 0:
        right += 1
      else:
        left += 1
        right += 1
