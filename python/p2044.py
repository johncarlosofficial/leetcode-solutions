from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        
        for num in nums:
            max_or |= num
        
        def backtrack(i, curr_or):
            if i == len(nums):
                return 1 if curr_or == max_or else 0
            
            return (
                # Include nums[i] in the subset
                backtrack(i + 1, curr_or | nums[i]) +
                # Exclude nums[i] from the subset
                backtrack(i + 1, curr_or)
            )
        
        return backtrack(0, 0)