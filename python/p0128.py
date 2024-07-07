from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set from the list
        hash_set = set(nums)
        # Initialize max length
        max_length = 0

        # Iterate through each number in the set
        for num in hash_set:
            # Check if it's the start of a sequence
            if (num - 1) not in hash_set:
                count = 1
                # Check for the next numbers in the sequence
                while (num + 1) in hash_set:
                    count += 1
                    num += 1

                # Update max length if current sequence is longer
                max_length = max(max_length, count)

        return max_length
