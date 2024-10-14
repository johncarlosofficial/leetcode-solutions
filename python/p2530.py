import heapq  # For heap operations
import math  # For math functions like ceil
from typing import List  # For type hinting

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert the list into a negative to simulate max-heap
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)  # Create a heap from the list (O(n))

        score = 0  # Initialize the score

        # Perform k operations
        for _ in range(k):
            largest = -heapq.heappop(nums)  # Get the largest value (O(log n))
            score += largest  # Add to score
            new_value = math.ceil(largest / 3)  # Divide by 3 and round up (O(1))
            heapq.heappush(nums, -new_value)  # Push the new value back into the heap (O(log n))

        return score  # Return the total score

# Time complexity:
# - heapify is O(n), where n is the size of the nums list.
# - Each iteration of the loop performs a pop and push operation, both O(log n).
# - The loop runs k times, so the total time complexity is O(n + k log n).

# Space complexity:
# - O(n), where n is the size of the heap (nums list).
# - Additional space is minimal (only a few variables), so the overall space complexity is O(n).
