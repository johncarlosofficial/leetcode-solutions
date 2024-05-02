from typing import List


class Solution:

  def maxOperations(self, nums: List[int], k: int) -> int:
    ans = 0
    seen = {}

    for i in range(len(nums)):
      if (k - nums[i]) in seen:
        if len(seen[k - nums[i]]) > 1:
          seen[k - nums[i]].pop()
        else:
          del seen[k - nums[i]]
        ans += 1
      else:
        if nums[i] in seen:
          seen[nums[i]].append(i)
        else:
          seen[nums[i]] = [i]

    return ans
