from typing import List


class Solution:

  def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) < 3:
      return len(nums)

    left = 2

    for right in range(2, len(nums)):
      if nums[right] != nums[left - 2]:
        nums[left] = nums[right]
        left += 1

    return left
