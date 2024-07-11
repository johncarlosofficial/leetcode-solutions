from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        
        # Initialize arrays to store the maximum height to the left and right of each bar
        max_lefts = [0] * n
        max_rights = [0] * n

        # Compute maximum heights to the left of each bar
        max_lefts[0] = height[0]
        for i in range(1, n):
            max_lefts[i] = max(max_lefts[i - 1], height[i])

        # Compute maximum heights to the right of each bar
        max_rights[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_rights[i] = max(max_rights[i + 1], height[i])

        # Calculate the water trapped at each bar
        trapped_water = 0
        for i in range(n):
            water = min(max_lefts[i], max_rights[i]) - height[i]
            if water > 0:
                trapped_water += water

        return trapped_water
