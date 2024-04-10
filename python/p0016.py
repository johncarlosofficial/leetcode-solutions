from typing import List


class Solution:

  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums = self.bubbleSort(nums)
    cur_sum = nums[0] + nums[1] + nums[len(nums) - 1]
    ans = cur_sum
    for i in range(len(nums) - 2):
      left = i + 1
      right = len(nums) - 1
      while left < right:
        cur_sum = nums[i] + nums[left] + nums[right]
        if cur_sum > target:
          right -= 1
        elif cur_sum < target:
          left += 1
        else:
          return cur_sum

      if abs(cur_sum - target) < abs(ans - target):
        ans = cur_sum

    return ans

  def bubbleSort(self, nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
      swapped = False
      for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
          nums[j], nums[j + 1] = nums[j + 1], nums[j]
          swapped = True
      if not swapped:
        break

    return nums
