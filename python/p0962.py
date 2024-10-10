from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Initialize an empty stack that will store indices in a decreasing order
        monotonic_stack = []

        # First pass: Traverse the array from left to right
        # The goal is to build a decreasing stack of indices
        for i in range(len(nums)):
            # Only append the index if nums[i] is less than the value at the top of the stack
            # This ensures we have a decreasing sequence of values in nums
            if not monotonic_stack or nums[i] < nums[monotonic_stack[-1]]:
                monotonic_stack.append(i)

        # Initialize a variable to keep track of the maximum ramp width found
        max_ramp = 0
        
        # Second pass: Traverse the array from right to left to find the widest valid ramp
        for i in range(len(nums) - 1, -1, -1):
            # While there are elements in the stack and nums[i] is greater than or equal to
            # the value at the index at the top of the stack, calculate ramp width
            while monotonic_stack and nums[i] >= nums[monotonic_stack[-1]]:
                # Update the maximum ramp width if the current one is larger
                max_ramp = max(max_ramp, i - monotonic_stack[-1])
                # Pop the top index from the stack as it has been used in a valid ramp
                monotonic_stack.pop()

        # Return the maximum ramp width found
        return max_ramp
