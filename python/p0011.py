from typing import List


class Solution:

  def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1  # Left and right pointers
    ans = 0  # Maximum area

    while l < r:
        # Calculate the current water area
        water = (r - l) * min(height[l], height[r])
        # Update the maximum area if current is larger
        ans = max(ans, water)

        # Move the pointer with the shorter line inward
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ans  # Return the maximum area found