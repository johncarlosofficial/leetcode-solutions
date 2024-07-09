from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Initialize left and right pointers

        while l < r:
            temp = numbers[l] + numbers[r]  # Sum of the numbers at left and right pointers

            if temp == target:
                return [l + 1, r + 1]  # Return 1-based indices if sum matches target

            elif temp < target:
                l += 1  # Move left pointer to the right if sum is less than target

            else:
                r -= 1  # Move right pointer to the left if sum is greater than target
