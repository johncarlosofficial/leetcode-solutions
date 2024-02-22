from typing import List


class Solution:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Pointer for nums1 array
    pointer_nums1 = m - 1
    # Pointer for nums2 array
    pointer_nums2 = n - 1
    # Pointer for the position to insert the merged elements
    merged_pointer = m + n - 1

    # Loop until both arrays have elements
    while pointer_nums1 >= 0 and pointer_nums2 >= 0:
      # Compare elements at current pointers and place the greater one at the end of nums1
      if nums1[pointer_nums1] > nums2[pointer_nums2]:
        nums1[merged_pointer] = nums1[pointer_nums1]
        pointer_nums1 -= 1
      else:
        nums1[merged_pointer] = nums2[pointer_nums2]
        pointer_nums2 -= 1
      merged_pointer -= 1

    # If nums2 still has elements remaining, add them to nums1
    while pointer_nums2 >= 0:
      nums1[merged_pointer] = nums2[pointer_nums2]
      pointer_nums2 -= 1
      merged_pointer -= 1
