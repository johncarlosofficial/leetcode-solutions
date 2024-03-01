from typing import List


class Solution:

  def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:  # Edge case: empty array
      return 0

    i = 0  # Pointer for placing unique elements

    for j in range(1, len(nums)):
      if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]  # Update the next position with the unique element

    return i + 1  # Number of unique elements
