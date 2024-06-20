from typing import List

class Solution:

  def subarraySum(self, nums: List[int], k: int):
    hash_map = {}
    prefix = 0
    ans = 0

    for i in range(len(nums)):
        prefix += nums[i]

        if prefix == k:
            ans += 1
        
        if prefix - k in hash_map:
            ans += hash_map[prefix-k]

        if prefix in hash_map:
            hash_map[prefix] += 1

        else:
            hash_map[prefix] = 1

    return ans