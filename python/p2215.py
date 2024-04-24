class Solution:

  def findDifference(self, nums1: List[int],
                     nums2: List[int]) -> List[List[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)

    ans = [[], []]

    for num in nums1:
      if num not in nums2:
        ans[0].append(num)

    for num in nums2:
      if num not in nums1:
        ans[1].append(num)

    return ans
