from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize variables for the maximum and minimum possible eating speeds (bananas per hour)
        max_eating_speed = max(piles)
        min_eating_speed = 1

        # Initialize the answer with the maximum eating speed
        optimal_speed = max_eating_speed

        # Define the search range for binary search
        left = min_eating_speed
        right = max_eating_speed

        # Perform binary search to find the minimum feasible eating speed
        while left <= right:
            mid = (left + right) // 2  # Calculate the mid-point speed
            total_hours = 0  # Initialize the total hours needed at this speed

            # Calculate the total hours needed to eat all bananas at the current mid-point speed
            for pile in piles:
                if pile % mid:  # If there are leftover bananas when divided by mid
                    total_hours += int(pile / mid) + 1
                else:
                    total_hours += pile / mid

            # Check if the current speed can eat all bananas within the allowed hours
            if total_hours <= h:
                optimal_speed = mid  # Update the optimal speed
                right = mid - 1  # Try to find a lower feasible speed
            else:
                left = mid + 1  # Increase the speed to reduce total hours

        return optimal_speed

s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8))


        