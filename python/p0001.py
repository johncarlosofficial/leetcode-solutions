from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}  # Initialize an empty hash map

        for i, num in enumerate(nums):  # Iterate through the array
            complement = target - num  # Calculate the complement
            if complement in num_idx:  # Check if the complement exists in the hash map
                return [num_idx[complement], i]  # Return the indices if found
            num_idx[num] = i  # Store the current number and its index in the hash map
