from collections import deque  # Efficient deque for popping from both ends
from typing import List  # For type hinting

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []  # Stores the max of each window
        max_to_min = deque()  # Deque to keep track of max elements

        left = right = 0  # Window pointers

        # Process the first window
        while right < k:
            while max_to_min and max_to_min[-1] < nums[right]:
                max_to_min.pop()  # Maintain decreasing order in deque
            max_to_min.append(nums[right])
            right += 1

        ans.append(max_to_min[0])  # First window max

        # Process the rest of the windows
        while right < len(nums):
            if max_to_min[0] == nums[left]:
                max_to_min.popleft()  # Remove element leaving the window
            while max_to_min and max_to_min[-1] < nums[right]:
                max_to_min.pop()
            max_to_min.append(nums[right])
            ans.append(max_to_min[0])  # Current window max
            left += 1
            right += 1

        return ans  # Return all window maximums

# Example usage
solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))