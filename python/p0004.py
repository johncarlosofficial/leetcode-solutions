from typing import List


class Solution:

  def findMedianSortedArrays(self, nums1: List[int],
                             nums2: List[int]) -> float:

    # Initialize pointers for both arrays
    pointer1 = 0
    pointer2 = 0

    # Calculate total length and median index
    total_length = len(nums1) + len(nums2)
    median_indices = [total_length // 2] if total_length % 2 else \
                     [total_length // 2 - 1, total_length // 2]

    current_index = -1
    median = 0

    while current_index < median_indices[0]:
      # Check if both pointers are within range
      if pointer1 < len(nums1) and pointer2 < len(nums2):
        if nums1[pointer1] < nums2[pointer2]:
          median = nums1[pointer1]
          pointer1 += 1
        else:
          median = nums2[pointer2]
          pointer2 += 1
      elif pointer1 < len(nums1):
        median = nums1[pointer1]
        pointer1 += 1
      else:
        median = nums2[pointer2]
        pointer2 += 1

      current_index += 1

    # If there's only one median index
    if len(median_indices) == 1:
      return median
    else:
      median1 = median
      if pointer1 < len(nums1) and pointer2 < len(nums2):
        if nums1[pointer1] < nums2[pointer2]:
          median = nums1[pointer1]
        else:
          median = nums2[pointer2]
      elif pointer1 < len(nums1):
        median = nums1[pointer1]
      else:
        median = nums2[pointer2]

      return (median1 + median) / 2
