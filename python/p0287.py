from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize the pointers for cycle detection
        slow = nums[0]
        fast = nums[0]

        # Move slow pointer by one step and fast pointer by two steps until they meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Move one pointer to the start and find the cycle entry point
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
