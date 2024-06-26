from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      answer = []
      nums.sort()  # Sort the array

      for i in range(len(nums) - 2):
          if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate numbers
              continue

          left, right = i + 1, len(nums) - 1

          while left < right:
              sum_ = nums[i] + nums[left] + nums[right]

              if sum_ == 0:
                  answer.append([nums[i], nums[left], nums[right]])
                  # Move left pointer to the right, skipping duplicates
                  while left < right and nums[left] == nums[left + 1]:
                      left += 1
                  left += 1
                  # Move right pointer to the left, skipping duplicates
                  while left < right and nums[right] == nums[right - 1]:
                      right -= 1
                  right -= 1
              elif sum_ < 0:
                  left += 1  # Increase the sum by moving the left pointer to the right
              else:
                  right -= 1  # Decrease the sum by moving the right pointer to the left

      return answer


        