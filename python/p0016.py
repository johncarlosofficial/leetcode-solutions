from typing import List


class Solution:

  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()

    ans = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
      left = i + 1
      right = len(nums) - 1

      while left < right:
        temp_sum = nums[i] + nums[left] + nums[right]

        if abs(target - temp_sum) < abs(target - ans):
          ans = temp_sum

        if temp_sum == target:
          return temp_sum
        elif temp_sum < target:
          left += 1
        else:
          right -= 1

    return ans