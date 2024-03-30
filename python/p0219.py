from typing import List


class Solution:

  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    num_indices = {}
    for i in range(len(nums)):
      if (nums[i] in num_indices) and ((i - num_indices[nums[i]]) <= k):
        return True
      num_indices[nums[i]] = i
    return False
