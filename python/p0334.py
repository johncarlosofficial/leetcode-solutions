from typing import List


class Solution:

  def increasingTriplet(self, nums: List[int]) -> bool:
    first = second = float('inf')

    for i in range(len(nums)):
      if nums[i] <= first:
        first = nums[i]
      elif first < nums[i] <= second:
        second = nums[i]
      else:
        return True

    return False
