from typing import List


class Solution:

  def twoSum(self, nums: List[int], target: int) -> List[int]:
    map = {}
    ans = []

    for i in range(len(nums)):
      complement = target - nums[i]
      if complement in map:
        ans.append(map[complement])
        ans.append(i)
      else:
        map[nums[i]] = i

    return ans
