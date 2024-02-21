from typing import List


class Solution:

  def findMaxAverage(self, nums: List[int], k: int) -> float:

    # First subarray
    my_sum = 0
    for i in range(k):
      my_sum += nums[i]

    average = my_sum / k
    greatest = average

    # Next subarrays
    left = 0
    right = k

    while right < len(nums):
      my_sum -= nums[left]
      my_sum += nums[right]

      average = my_sum / k
      greatest = max(greatest, average)

      left += 1
      right += 1

    return greatest
