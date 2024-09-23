class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        two_houses_ago = 0  # Max money robbed up to two houses ago
        previous_house = 0  # Max money robbed up to the last house
        
        for money in nums:
            current_max = max(previous_house, two_houses_ago + money)  # Max money if we rob the current house
            two_houses_ago = previous_house  # Update for the next house
            previous_house = current_max  # Update for the next house
        
        return previous_house
