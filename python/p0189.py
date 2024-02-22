from typing import List


class Solution:

  def reverse(self, nums, left, right) -> None:
    # Reverses the subarray nums[left:right+1] in-place
    while left < right:
      nums[left], nums[right] = nums[right], nums[left]
      left += 1
      right -= 1

  def rotate(self, nums: List[int], k: int):
    n = len(nums)
    k = k % n  # Adjust k if it's greater than the length of nums

    # Reverse the entire array
    self.reverse(nums, 0, n - 1)
    # Reverse the first k elements
    self.reverse(nums, 0, k - 1)
    # Reverse the remaining elements
    self.reverse(nums, k, n - 1)
