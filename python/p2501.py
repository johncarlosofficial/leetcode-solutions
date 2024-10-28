from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Step 1: Sort the array in ascending order.
        nums.sort()
        
        # Step 2: Store all numbers in a set for quick lookup.
        num_set = set(nums)
        
        # Step 3: Initialize the variable to store the length of the longest streak.
        longest_streak = 0
        
        # Step 4: Iterate through each number to try forming a square streak.
        for num in nums:
            # For each number, start a new streak if possible
            current_streak = 1
            current_num = num
            
            # Step 5: Try to build a square streak with this starting number
            while (current_num * current_num) in num_set:
                # Move to the next number in the streak
                current_num = current_num * current_num
                current_streak += 1
            
            # Step 6: Check if the current streak is the longest so far.
            if current_streak > 1:  # A valid streak must be at least length 2
                longest_streak = max(longest_streak, current_streak)
        
        # Step 7: Return the longest streak found, or -1 if no valid streak was found.
        return longest_streak if longest_streak > 1 else -1
