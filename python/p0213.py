from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        # Edge cases
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Robbing First House (from index 0 to len(nums) - 2)
        previous_house = 0
        two_houses_ago = 0
        current_max = 0

        for i in range(len(nums) - 1):
            current_max = max(previous_house, two_houses_ago + nums[i])
            two_houses_ago = previous_house
            previous_house = current_max

        robbing_first_house_max = previous_house

        # Robbing Second House (from index 1 to len(nums) - 1)
        previous_house = 0
        two_houses_ago = 0
        current_max = 0

        for i in range(1, len(nums)):
            current_max = max(previous_house, two_houses_ago + nums[i])
            two_houses_ago = previous_house
            previous_house = current_max

        robbing_second_house_max = previous_house

        # Return the maximum of robbing the first house or the second house
        return max(robbing_first_house_max, robbing_second_house_max)
