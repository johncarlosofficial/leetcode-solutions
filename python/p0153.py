from typing import List


class Solution:
  def findMin(self, nums: List[int]) -> int:
      left = 0
      right = len(nums) - 1

      while left < right:
          middle = (left + right) // 2

          # If the middle element is greater than the rightmost element,
          # the smallest value must be in the right half
          if nums[middle] > nums[right]:
              left = middle + 1
          else:
              # If the middle element is less than or equal to the rightmost element,
              # the smallest value is in the left half (including middle)
              right = middle

      # After the loop, left == right and it should point to the smallest element
      return nums[left]
