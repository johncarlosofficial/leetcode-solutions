from typing import List


class Solution:

  def firstMissingPositive(self, nums: List[int]) -> int:
    integers = set()
    greatest = 0

    for num in nums:
      if num > 0 and num < len(nums):
        integers.add(num)
      if num > greatest:
        greatest = num

    if greatest == 0:
      return 1

    for i in range(1, greatest):
      if i not in integers:
        return i

    return greatest + 1
