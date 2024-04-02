from typing import List


class Solution:

  def jump(self, nums: List[int]) -> int:
    jumps = 0
    left, right = 0, 0
    longest = 0

    while right < len(nums) - 1:
      # Iterate over the elements within the current jump range
      for i in range(left, right + 1):
        # Maximum jump
        jump = i + nums[i]
        longest = max(longest, jump)

      # Update the boundaries for the next jump
      left = right + 1
      right = longest

      # Increment the number of jumps
      jumps += 1

    # Return the total number of jumps required to reach the end
    return jumps
