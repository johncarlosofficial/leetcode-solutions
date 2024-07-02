from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the frequency of each number
        num_freq = {}

        # Count the frequency of each number in the input list
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        # Create a list of empty lists to store numbers by their frequency
        frequencies = [[] for _ in range(len(nums) + 1)]

        # Populate the frequencies list with numbers based on their frequency
        for num, freq in num_freq.items():
            frequencies[freq].append(num)

        ans = []
        counter = 0

        # Iterate from the highest frequency to the lowest
        for i in range(len(frequencies) - 1, -1, -1):
            if not frequencies[i]:
                continue  # Skip empty lists

            # Append numbers with the current frequency to the result list
            for j in range(len(frequencies[i])):
                ans.append(frequencies[i][j])
                counter += 1

                # If we have collected k numbers, return the result
                if counter >= k:
                    return ans

        return ans
