from typing import List


class Solution:

  def bubbleSort(self, nums: List[int]):
    for i in range(len(nums) - 1):
      swapped = False

      for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
          nums[j], nums[j + 1] = nums[j + 1], nums[j]
          swapped = True

      if not swapped:
        break

    return nums

  def threeSum(self, nums: List[int]):
    ans = []
    nums = self.bubbleSort(nums)

    for i in range(len(nums)):
      if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
        continue

      left = i + 1
      right = len(nums) - 1

      while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
          ans.append([nums[i], nums[left], nums[right]])

          # Skip duplicate triplets
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1
        elif total < 0:
          left += 1
        else:
          right -= 1

    return ans
