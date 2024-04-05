from typing import List


class Solution:

  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    min_sub = len(nums) + 1
    left = right = 0
    prefix_sum = 0

    while right < len(nums):
      prefix_sum += nums[right]

      while prefix_sum >= target:
        min_sub = min(min_sub, right - left + 1)
        prefix_sum -= nums[left]
        left += 1

      right += 1

    if min_sub == len(nums) + 1:
      return 0
    else:
      return min_sub
