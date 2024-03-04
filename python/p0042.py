from typing import List


class Solution:

  def trap(self, height: List[int]) -> int:
    # Initialize arrays to store maximum heights to the left and right of each bar
    max_left = [None] * len(height)
    max_right = [None] * len(height)

    # Variable to store temporary maximum height
    temp = 0

    # Calculate the maximum height to the left of each bar
    for i in range(len(height)):
      max_left[i] = temp
      if height[i] > temp:
        temp = height[i]

    # Reset temporary maximum height
    temp = 0

    # Calculate the maximum height to the right of each bar
    for i in range(len(height) - 1, -1, -1):
      max_right[i] = temp
      if height[i] > temp:
        temp = height[i]

    # Initialize array to store minimum of max_left and max_right heights for each bar
    min_left_right = [None] * len(height)

    # Calculate the minimum of max_left and max_right for each bar
    for i in range(len(height)):
      min_left_right[i] = min(max_left[i], max_right[i])

    # Initialize array to store trapped water for each bar
    ans = [None] * len(height)

    # Calculate the trapped water for each bar
    for i in range(len(height)):
      if (min_left_right[i] - height[i]) < 0:
        ans[i] = 0
      else:
        ans[i] = min_left_right[i] - height[i]

    # Calculate total trapped water by summing up all values in ans array
    total = 0
    for i in range(len(ans)):
      total += ans[i]

    return total
