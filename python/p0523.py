from typing import List


class Solution:

  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    remainer_index = {0: -1}
    total_sum = 0
    for i in range(len(nums)):
      total_sum += nums[i]
      remainer = total_sum % k

      if remainer not in remainer_index:
        remainer_index[remainer] = i
      elif i - remainer_index[remainer] >= 2:
        return True
    return False
