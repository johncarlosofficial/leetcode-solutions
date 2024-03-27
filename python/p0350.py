from typing import List


class Solution:

  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hash_map = {}
    ans = []

    for i in range(len(nums1)):
      if nums1[i] in hash_map:
        hash_map[nums1[i]] += 1
      else:
        hash_map[nums1[i]] = 1

    for i in range(len(nums2)):
      if nums2[i] in hash_map:
        ans.append(nums2[i])
        hash_map[nums2[i]] -= 1
        if hash_map[nums2[i]] == 0:
          del hash_map[nums2[i]]

    return ans
